# Solo Analysis — Session 5 Distributed Feature Flags
## Agent: GPT-5.1
## Start Time: 12:10 PM PT
## End Time: 12:27 PM PT
## TASK_ID_VERIFIED: session4_distributed_flags

## 1. System Understanding

### 1.1 Shared schema

- `tasks/session4_distributed_flags/shared/flag_schema.json` defines a shared schema for feature flags.
- Top-level fields:
  - `version`: string, currently `"2.0"`.
  - `minimumConsumerVersion`: `2`.
  - `flags`: map from flag key to definition. For `discover_feed`:
    - `state`: rollout configuration (defaultTreatment, rollout rules, stickyBy).
    - `metadata`: owner, checksum, playbook, etc.
    - `legacyFallback`: `{ enabled, variant }` for older consumers.

This JSON is read by both the backend service (Node) and the analytics processor (Python).

### 1.2 Backend flag service (`backend/flag_service.js`)

- Express app exporting a `/flags/:env` endpoint.
- On startup it:
  - Requires the shared schema JSON.
  - Computes:
    - `FLAG_SCHEMA_VERSION = Number(schema.version)` → with `"2.0"` becomes numeric `2`.
    - `MIN_CONSUMER_VERSION = schema.minimumConsumerVersion || FLAG_SCHEMA_VERSION` → `2`.
  - Seeds an in-memory `flagStore` with a `prod` snapshot:
    - `version: FLAG_SCHEMA_VERSION`.
    - `generatedAt` timestamp.
    - `flags.discover_feed.state` matching the v2 schema (defaultTreatment `control`, rollout rule for US/CA → treatment, stickyBy `user_id`).

- Caching:
  - `snapshotCache = new Map()` keyed by environment.
  - `getSnapshot(env)`:
    - If there is a cached entry and `expiresAt > Date.now()`, returns `cached.value`.
    - Else reads from `flagStore[env]` and stores `{ value: base, expiresAt: Date.now() + 15_000 }`.
    - **Important:** `value` is the original object from `flagStore` (no cloning), so the cache and the store share the same reference.

- Request handling:
  - `app.get('/flags/:env', ...)`:
    - Parses `schemaVersion` from `req.query` via `parseClientVersion(raw)`.
      - If `raw` missing or falsy → returns `FLAG_SCHEMA_VERSION` (2).
      - If `raw` present but NaN → also falls back to 2.
    - Calls `getSnapshot(env)`.
    - If no snapshot → 404.
    - Otherwise calls `shapeForClient(snapshot, clientVersion)` and `res.json(...)`.

- Version shaping:
  - `shapeForClient(snapshot, clientVersion)`:
    - If `clientVersion >= MIN_CONSUMER_VERSION` (≥2) → returns `decorateForTransport(snapshot, FLAG_SCHEMA_VERSION)`.
    - Else → `downgradeSnapshot(snapshot, clientVersion)`.

  - `decorateForTransport(snapshot, version)` returns:

    ```js
    {
      version,
      generatedAt: snapshot.generatedAt,
      flags: snapshot.flags
    }
    ```

  - `downgradeSnapshot(snapshot, clientVersion)`:
    - `const downgraded = { ...snapshot };` (shallow clone).
    - Sets `downgraded.version = clientVersion`.
    - Iterates `Object.keys(downgraded.flags)` and for each flag:
      - Calls `transformToLegacyShape(downgraded.flags[flagKey])`.
      - Assigns the result back into `downgraded.flags[flagKey]`.
    - Preserves `generatedAt` from original snapshot.
    - Returns `decorateForTransport(downgraded, clientVersion)`.

  - `transformToLegacyShape(flagDefinition)`:
    - If missing `flagDefinition` or `flagDefinition.state` → returns `{ enabled: false, variant: 'control' }`.
    - Else uses:
      - `defaultVariant = state.defaultTreatment || 'control'`.
      - `rollout = state.rollout || []`.
      - `enabled` true if there is at least one rollout entry, otherwise `defaultVariant !== 'control'`.
      - `variant` set to the first rollout`s treatment if present, else `defaultVariant`.
    - So the legacy shape is `{ enabled: boolean, variant: string }`.

Net: backend can serve both v2 (rich `state`/`metadata`) and downgraded legacy snapshots with `{enabled, variant}` depending on perceived client version.

### 1.3 Frontend React client (`frontend/FeatureGate.jsx`)

- Component `FeatureGate` wraps children and only renders them when a feature flag is considered enabled.
- Constants:
  - `FLAG_ENDPOINT = '/api/flags/prod'` (assumed to proxy to backend `/flags/prod`).
  - `CACHE_TTL_MS = 30_000` (30s cache in `sessionStorage`).
  - `SCHEMA_VERSION = 1` with a comment that backend has already bumped to `2.0`.

- State:
  - `enabled` (initially `fallback`, default false).
  - `ready` (initially false).

- Effect on mount / when `flagKey` or `fallback` changes:
  - Reads `cached = readCached(flagKey)` from `sessionStorage`.
  - If `cached` exists:
    - Immediately sets `enabled` to `cached.value`.
    - If `cached.schemaVersion >= SCHEMA_VERSION` **and** `cached.expiresAt > Date.now()`:
      - Marks component as ready and **returns early without hitting the network**.
  - Computes `schemaHint = cached ? cached.schemaVersion : undefined`.
  - Calls `fetchSnapshot(flagKey, schemaHint)`:
    - Builds URL with `flag` query parameter.
    - If `schemaHint` is defined, adds `schemaVersion` query param.
    - Fetches JSON, throwing if `!res.ok`.
  - On success:
    - `next = coerceFlagState(snapshot, flagKey, fallback)`.
    - Updates `enabled`, marks `ready` true.
    - Caches via `writeCached(flagKey, next, { schemaVersion: schemaHint ?? SCHEMA_VERSION, expiresAt: now + TTL })`.
  - On error: sets `enabled = fallback`, `ready = true`.

- `coerceFlagState(snapshot, flagKey, fallback)` interprets the snapshot:
  - Reads `flagBlock = snapshot?.flags?.[flagKey]`.
  - If missing → returns `fallback`.
  - If `typeof flagBlock.enabled === 'boolean'` → returns that (legacy v1 shape).
  - If `flagBlock.state && flagBlock.state.defaultVariant`:
    - Reads `defaultVariant` and `rollout`.
    - If there is at least one rollout entry, treats the flag as enabled.
    - Else enables iff `defaultVariant !== 'control'`.
  - Else → returns `fallback`.

- Caching helpers:
  - `readCached` / `writeCached` store `{ value, schemaVersion, expiresAt }` under `sessionStorage` key `flag:${flagKey}`.
  - There is no awareness of the backend’s actual snapshot `version` field; the cache stores a local `schemaVersion` meta that is driven by the React constant / previous requests, not the server’s response.

### 1.4 Analytics event processor (`analytics/event_processor.py`)

- Imports the same shared `flag_schema.json` from `shared/`.
- On import it reads the JSON into `RAW_SCHEMA` and attempts to compute `SCHEMA_VERSION`:

  ```python
  try:
      SCHEMA_VERSION = int(RAW_SCHEMA.get('version', 1))
  except (TypeError, ValueError):
      logger.warning('Failed to parse schema version %r, defaulting to legacy version 1', RAW_SCHEMA.get('version'))
      SCHEMA_VERSION = 1
  ```

  - With `version` set to `"2.0"`, `int("2.0")` raises `ValueError`, so the code logs a warning and ends up with `SCHEMA_VERSION = 1`.
  - This means analytics treats the current schema as **legacy version 1**, even though the shared JSON describes `2.0`.

- Precomputes `LEGACY_DEFAULTS` from the schema:

  ```python
  LEGACY_DEFAULTS = {
      flag: {
          'enabled': definition.get('legacyFallback', {}).get('enabled', False),
          'variant': definition.get('legacyFallback', {}).get('variant', 'control')
      }
      for flag, definition in RAW_SCHEMA.get('flags', {}).items()
  }
  ```

  - For `discover_feed` this uses the `legacyFallback` block (enabled/treatment) as the canonical legacy representation.

- `EventProcessor`:
  - Holds `_flag_cache: Dict[env][flag_key]` (no TTL, process-lifetime cache).
  - Holds `_schema_version` set from `SCHEMA_VERSION` (currently 1).

- `process_event(event)`:
  - Reads `env`, `flag_snapshot`, and `flag_key` from the event.
  - If no `flag_key`, returns the event unchanged.
  - Otherwise calls `_resolve_flag(env, flag_key, snapshot)` and:
    - Sets `event['flag_snapshot'] = resolved`.
    - Sets `event['flag_version'] = resolved.get('version', 1)`.

- `_resolve_flag(env, flag_key, snapshot)`:
  - Looks up `cache_for_env = self._flag_cache.setdefault(env, {})`.
  - If there is an existing cached entry for the flag → returns it immediately.
  - Otherwise:
    - Reads `incoming_version = snapshot.get('version', 1)`.
    - If `incoming_version > self._schema_version` (i.e., >1 under the current configuration):
      - Logs that the flag uses a "future" version and falls back to `_legacy_snapshot(flag_key)`.
    - Else:
      - Uses the incoming `snapshot` as-is.
    - Caches the chosen representation under `_flag_cache[env][flag_key]` and returns it.

- `_legacy_snapshot(flag_key)`:
  - Looks up `legacy = LEGACY_DEFAULTS.get(flag_key, { 'enabled': False, 'variant': 'control' })`.
  - Returns a snapshot of the form:

    ```python
    {
        'version': self._schema_version,
        'flags': {flag_key: legacy},
    }
    ```

Net: analytics views any snapshot with `version > 1` as a future schema and rewrites it back to version `1` with `legacyFallback` semantics, then caches that choice indefinitely per (env, flag).

### 1.5 Cross-service flow

Putting this together for `discover_feed`:

1. Backend reads schema (2.0) and seeds `flagStore.prod` with v2-shaped flag definitions.
2. A web client mounts `FeatureGate` for `discover_feed`:
   - It may have or lack cached state in `sessionStorage`.
   - It calls `/api/flags/prod?flag=discover_feed[&schemaVersion=...]` and receives either a v2 snapshot or a downgraded legacy snapshot, depending on what `schemaVersion` the server infers.
3. The React client interprets the snapshot with `coerceFlagState` and caches a **boolean** `enabled` value plus local `schemaVersion` metadata for 30 seconds.
4. A mobile or web client sends analytics events including some `flag_snapshot` payloads.
   - `EventProcessor` rewrites them, either accepting them as-is (for version ≤1) or falling back to a synthetic legacy snapshot derived from `flag_schema.json`.
   - The first event for a given `(env, flag)` pair determines what is cached and thus what all subsequent events report.

## 2. Insights & Root Causes

### 2.1 Version negotiation mismatch between services

**Backend vs frontend**

- Backend assumes that a missing or malformed `schemaVersion` query param means the client is running at **current schema parity** (`FLAG_SCHEMA_VERSION`, i.e. 2):

  ```js
  if (!raw) {
    return FLAG_SCHEMA_VERSION;
  }
  ```

- The React client’s `SCHEMA_VERSION` constant is still `1`, and it only includes `schemaVersion` in the request if there is already cache metadata available:

  ```js
  const schemaHint = cached ? cached.schemaVersion : undefined;
  if (schemaHint !== undefined) {
    url.searchParams.set('schemaVersion', schemaHint);
  }
  ```

  - On a **cold page load with no cache**, the client sends **no** `schemaVersion` hint → backend treats it as version `2` and serves a v2 snapshot even though the frontend still labels itself as schema 1.
  - After the first response, the frontend caches `schemaVersion: schemaHint ?? SCHEMA_VERSION`, which is `1` (because `schemaHint` was `undefined` even though the server responded with `version: 2`).
  - When the cache expires, the next network request will send `schemaVersion=1`, causing the backend to attempt a downgrade on the *same* underlying snapshot.

This misalignment (backend assuming 2, frontend thinking 1) amplifies differences in behavior across sessions depending on whether they fetched during the “no hint” phase or the “hint=1” phase.

**Backend vs analytics**

- Backend uses `Number(schema.version)` and ends up with `FLAG_SCHEMA_VERSION = 2`.
- Analytics fails to parse `"2.0"` as an integer and falls back to `SCHEMA_VERSION = 1`.
- As a result, any incoming `flag_snapshot` with `version > 1` triggers the “future version” path in `_resolve_flag` and is **downgraded** to a synthetic legacy snapshot based on `legacyFallback`.

Together, this means we have three different notions of schema versioning in play:

1. Backend: `2`.
2. Frontend: `1` but sometimes treated as `2` due to missing hints.
3. Analytics: `1` with an explicit bias to treat `>1` as future and collapse back to defaults.

This is a structural explanation for why analytics tables and dashboards can diverge from live backend behavior.

### 2.2 Shared mutable snapshots and downgrade side effects (backend)

`getSnapshot` stores the **original** snapshot object from `flagStore` by reference in `snapshotCache`:

```js
snapshotCache.set(env, {
  value: base,
  expiresAt: Date.now() + 15_000
});
return base;
```

`downgradeSnapshot` then performs a *shallow* copy of the snapshot:

```js
const downgraded = { ...snapshot };
const flagKeys = Object.keys(downgraded.flags);
flagKeys.forEach((flagKey) => {
  const nextState = transformToLegacyShape(downgraded.flags[flagKey]);
  downgraded.flags[flagKey] = nextState;
});
```

- `downgraded` is a new object, but `downgraded.flags` still points to the **same object** as `snapshot.flags` because the copy is shallow.
- Mutating `downgraded.flags[flagKey]` thus mutates the original `snapshot.flags[flagKey]` in-place.
- Because `snapshot` itself is also the same object as `flagStore[env]` and as the `value` stored in `snapshotCache`, this one downgrade call permanently rewrites the backend’s internal representation of that flag for that environment from rich v2 shape to legacy `{enabled, variant}` shape.

Implications:

- After the first downgrade for a given environment and flag, *all subsequent* requests— including those from modern clients that should receive v2—will see a mutated flags object that no longer contains `state`, `metadata`, or `legacyFallback`.
- `decorateForTransport(snapshot, FLAG_SCHEMA_VERSION)` reuses `snapshot.flags` by reference, so even v2 responses now carry legacy-shaped flag entries.
- Newer clients that expect access to targeting metadata (e.g. `state.rollout`) will see a mixture of shapes depending on whether a downgrade happened earlier in the cache lifetime.

This directly creates non-deterministic behavior across sessions depending on the **ordering** of downgrade vs non-downgrade requests within the snapshot cache TTL window.

### 2.3 Client and server cache interaction creates sticky, inconsistent web sessions

- Backend snapshot cache TTL: 15s.
- React `FeatureGate` cache TTL in `sessionStorage`: 30s.

Key behaviors:

1. A user session that first loads the page when the backend snapshot is still pristine (no downgrade yet) and has no cache:
   - Makes a request **without `schemaVersion`**.
   - Backend treats this as version 2 and returns a v2 snapshot.
   - React computes `enabled` from the v2 shape and caches `{ value: enabled, schemaVersion: 1, expiresAt: now + 30s }`.
   - For 30 seconds, subsequent renders will return early from the effect and never re-fetch, even if the backend later mutates its internal representation due to other clients triggering downgrades.

2. A different user (or the same user after the 30s TTL) who triggers a request with `schemaHint = 1`:
   - Sends `schemaVersion=1`.
   - Backend calls `downgradeSnapshot`, mutating both the downgraded copy and the shared underlying `flags` object.
   - Now any subsequent v2 responses for that environment also carry legacy-shaped flags.

3. Hard refreshes do not necessarily clear `sessionStorage`, so a user can remain on outdated state even after a full reload, as long as the browser process remains alive.

These interactions explain the reported symptom:

> "Some web sessions received the new targeting rules, others stayed on the old defaults even after hard refreshes."

Different sessions end up bound to different combinations of:

- Whether they fetched before or after a downgrade mutated the backend snapshot.
- Whether they hit the early-return cache path in the React effect.
- Whether their first network request sent a schema hint or not.

### 2.4 Analytics caching and schema handling amplify divergence

In analytics:

- Any snapshot with `version > 1` is treated as a future schema and replaced by `_legacy_snapshot(flag_key)`, which is derived from `legacyFallback` in `flag_schema.json` and stamped with `version: self._schema_version` (1).
- Snapshots with `version <= 1` are passed through as-is.
- `_flag_cache` stores the chosen representation for each `(env, flag)` **without any TTL or invalidation**.

Consequences:

1. The *first* event for a given `(env, flag)` determines the analytics view for that entire process lifetime:
   - If the first event includes a v2 snapshot, analytics will lock in the synthetic legacy snapshot for that env/flag and never reconsider, even as live traffic and backend dashboards move to the new rollout rules.
   - If the first event uses a downgraded v1 snapshot (e.g., from backend downgrade or legacy clients), analytics will anchor to that view instead.

2. Because some events are rewritten to a legacy snapshot and others are not, downstream A/B pipelines can see **two distinct payload shapes** for the same `discover_feed` experiment:
   - Legacy-shaped `{ version: 1, flags: { discover_feed: { enabled, variant } } }` from `_legacy_snapshot` or downgraded snapshots.
   - Potentially richer shapes if any v1 or un-downgraded snapshots slip through.

This behavior matches the observation:

> "A/B test reports showed duplicate `discover_feed` variants because downstream jobs treated some payloads as schema v1 and others as v2."

The duplication arises because schema version and payload shape are not normalized before analysis; the same underlying experiment appears under multiple version/shape combinations.

3. Analytics can contradict backend dashboards because:
   - Dashboards likely read from backend snapshots (which, in the happy path, reflect the intended rollout).
   - Analytics, however, may be locked into a fallback view driven by `legacyFallback`, regardless of the actual live config.

Combined with mobile or legacy clients that supply different snapshots, this explains why some analytics views can show `discover_feed` disabled while backend dashboards indicate the opposite.

### 2.5 Summary of main issue clusters

1. **Version misalignment and implicit defaults**
   - Backend treats missing `schemaVersion` as the latest schema.
   - Frontend’s `SCHEMA_VERSION` constant is stale and only sometimes sent.
   - Analytics effectively pins schema to 1 by failing to parse `"2.0"`.

2. **Mutable shared state in downgrade path**
   - Downgrade logic mutates the canonical snapshot/store through shallow copying.
   - Once a downgrade is triggered, all clients may receive legacy-shaped flags regardless of their capabilities.

3. **Cache layering without a consistent invalidation story**
   - Backend 15s cache, frontend 30s session cache, analytics unbounded cache.
   - Each layer makes independent assumptions about version and freshness.
   - Ordering of requests across these caches produces non-deterministic behavior.

4. **Analytics normalization gaps**
   - Future-version snapshots are collapsed into synthetic legacy snapshots.
   - Mixed-schema events aren’t normalized before A/B analysis, yielding duplicate variants and inconsistent aggregates.

## 3. Recommendations

I would focus on changes that reduce version ambiguity, eliminate shared mutable state, and make caches explicitly aware of schema versions.

### 3.1 Make schema versioning explicit and consistent

1. **Adopt a shared version representation**
   - Define a single, canonical representation for the schema version (e.g., integer `2` or structured semver) and ensure both Node and Python interpret it consistently.
   - For example:
     - Store `version: 2` in `flag_schema.json` instead of `"2.0"`, or
     - In Python, parse via something like `int(str(version).split('.')[0])` to coerce major version.

2. **Require explicit client version hints**
   - Change `parseClientVersion` so that missing `schemaVersion` does **not** default to the latest version.
   - Instead, treat missing/invalid hints as oldest-supported (e.g. `1`) and respond with a downgraded/legacy shape.
   - Log metrics for how many requests arrive without hints to encourage upgrading clients over time.

3. **Update and propagate client schema version**
   - Bump `SCHEMA_VERSION` in the React client to match the backend’s major version and always send it:

     ```js
     url.searchParams.set('schemaVersion', SCHEMA_VERSION);
     ```

   - Cache the **actual** snapshot version alongside the client schema version for diagnostics.
   - On receiving a snapshot whose `version` is higher than the client’s supported version, treat this as an error path (or at least as a signal to fall back with logging), not as a silent success.

4. **Align analytics with shared schema**
   - Fix `SCHEMA_VERSION` computation in `event_processor.py` to correctly interpret the shared schema’s version.
   - Replace the current “> schema_version → treat as future and fallback” approach with a more explicit compatibility matrix, e.g.:
     - If `incoming_version == SCHEMA_VERSION` → accept.
     - If `incoming_version < SCHEMA_VERSION` → treat as legacy and normalize.
     - If `incoming_version > SCHEMA_VERSION` → log and either drop or mark as unknown, rather than silently rewriting.

### 3.2 Remove shared mutable state from backend downgrade logic

1. **Avoid shallow copies for snapshots**
   - Ensure that `downgradeSnapshot` produces a **deep copy** before mutation:

     - Either deep-clone the snapshot (e.g., `structuredClone(snapshot)` / `JSON.parse(JSON.stringify(snapshot))`), or
     - At least deep-clone the `flags` object: `downgraded.flags = { ...snapshot.flags }` and deep-clone each flag definition before mutating.

2. **Treat downgrade as a pure projection**
   - Adjust `transformToLegacyShape` so that it operates on a copy of the flag definition and never mutates any object that might be shared with the store.
   - Add tests asserting that after calling `downgradeSnapshot`, `flagStore[env]` and previous snapshots are byte-for-byte unchanged.

3. **Consider separating canonical storage from transport shapes**
   - Maintain a canonical, immutable config object for each environment.
   - Generate transport shapes (v1, v2, etc.) on the fly from the canonical config, without caching the transport objects themselves.
   - If caching is needed, cache **per (env, version)** with deep copies and short TTLs.

### 3.3 Rework caching strategy for determinism

1. **Frontend caching**
   - Tie cache entries to both `flagKey` and `schemaVersion` (e.g. `flag:${schemaVersion}:${flagKey}`).
   - When the app bumps its supported schema version, old cache entries will naturally miss and trigger fresh network fetches.
   - Use the snapshot’s `generatedAt` and `version` to detect obviously stale or mismatched entries.
   - Consider reducing TTL or aligning it with server TTL to minimize windows where clients depend on stale data.

2. **Backend caching**
   - If downgrades remain necessary, cache them per `(env, clientVersion)` instead of mutating the base snapshot.
   - Alternatively, keep `snapshotCache` for canonical snapshots only and compute downgraded shapes per request without caching them.

3. **Analytics caching**
   - Either remove `_flag_cache` or introduce:
     - A TTL.
     - A cache key that includes both `version` and maybe a checksum of the snapshot.
   - The event processor should be willing to reconsider its view when it encounters a snapshot with a different version or checksum.

### 3.4 Normalize analytics payloads before A/B analysis

1. **Introduce a normalization layer**
   - Before analytics events reach downstream A/B jobs, normalize all `flag_snapshot` payloads into a single, stable representation:
     - E.g. a schema with `{ experiment: "discover_feed", variant: "control" | "treatment", source_version: 1|2, downgraded: bool }`.
   - Attach metadata such as `source_schema_version` and `is_downgraded` rather than letting mixed payload shapes compete.

2. **Deduplicate variants by logical meaning, not raw payload**
   - A/B reporting should consider the semantic variant (“control” vs “treatment”) and treat legacy vs v2 payloads as the same variant when they are semantically equivalent.

3. **Surface version skew as a first-class metric**
   - Track and alert on events where `source_schema_version` differs from the expected production schema version.
   - This becomes an operational guardrail: if analytics starts seeing too many downgraded or legacy events, the rollout can be slowed or paused.

### 3.5 Deployment and operational safeguards

1. **Version gate using `minimumConsumerVersion`**
   - Use `minimumConsumerVersion` as an actual guardrail: don’t raise it to 2 until all major consumers (web, mobile, analytics) have shipped compatible versions.
   - Provide a runbook where any schema bump must include confirmation that each consumer has been upgraded and integration-tested.

2. **Pre-deployment integration tests**
   - Before rolling out a schema/version bump:
     - Run a test harness that:
       - Calls the backend with each supported `schemaVersion`.
       - Passes each resulting snapshot through the React `coerceFlagState` logic (via unit tests) and through `EventProcessor`.
       - Verifies that all combinations produce consistent, expected flag states and that no path falls back incorrectly.

3. **Canarying and monitoring**
   - During rollout, route a small fraction of traffic through the new schema and monitor:
     - Percentage of analytics events using downgraded vs native schema.
     - Divergence between backend dashboards and analytics aggregates.
   - Automatically halt the rollout if divergence exceeds a threshold.

## 4. Validation Approach

Here is how I would validate that the above fixes actually resolve the incident and prevent regressions.

### 4.1 Unit tests

**Backend (`flag_service.js`)**

1. **Snapshot immutability tests**
   - Construct a test snapshot with v2 shape and deep-clone it.
   - Call `downgradeSnapshot` for a clientVersion=1.
   - Assert that the original snapshot (and `flagStore`) remain unchanged (including nested `state` and `metadata`).

2. **Version negotiation tests**
   - Test `parseClientVersion` with:
     - Missing `schemaVersion`.
     - Non-numeric values.
     - Explicit `1`, `2`.
   - Ensure behavior matches the intended contract (likely: missing/invalid → old/lowest supported version, not latest).

3. **Shape tests**
   - Verify that `decorateForTransport` and `downgradeSnapshot` produce the correct shape for v2 and v1 clients, including `version` field, and that downgraded shapes only use `{enabled, variant}`.

**Frontend (`FeatureGate.jsx`)**

1. **Caching and invalidation tests**
   - Mock `sessionStorage` and `fetch`.
   - Ensure that when `SCHEMA_VERSION` increases, stale cache entries (with lower schemaVersion) are ignored and a network fetch occurs.
   - Verify that the client always sends `schemaVersion` in the query and that errors in version negotiation (e.g., higher server version) lead to a safe fallback with logging.

2. **Snapshot interpretation tests**
   - Feed `coerceFlagState` with:
     - Pure legacy snapshots (`{enabled, variant}`).
     - Rich v2 snapshots (`{state: { defaultTreatment, rollout }, ... }`).
   - Confirm it returns correct `enabled` booleans in all combinations.

**Analytics (`event_processor.py`)**

1. **Schema version parsing**
   - Test that the current shared schema version is parsed correctly (e.g., `2`), and that the system does not silently downcast to legacy when the version string contains minor components.

2. **Compatibility behavior**
   - Provide snapshots at versions `<`, `==`, and `>` the processor’s version.
   - Assert that only unsupported future versions trigger a clearly-marked fallback or drop, and that the result is explicitly distinguishable (e.g., via flags like `downgraded: True`).

3. **Cache behavior**
   - Ensure `_flag_cache` respects TTL or version changes if caching remains.
   - Include tests where successive events carry different `version` values and validate that the cache invalidates or updates as expected.

### 4.2 Integration and end-to-end tests

1. **Simulated rollout window**
   - Spin up the backend, a headless browser environment for the React client, and an in-process `EventProcessor`.
   - Simulate the following sequence:
     - Old clients sending `schemaVersion=1`.
     - New clients sending `schemaVersion=2`.
     - Clients initially sending no schema hint, then sending explicit hints after an upgrade.
   - Capture:
     - Snapshots returned to each client.
     - The boolean flag states as interpreted by `FeatureGate`.
     - The final `flag_snapshot` / `flag_version` fields produced by analytics.
   - Assert that for each simulated user, the observed flag state and analytics representation agree and match the intended rollout configuration.

2. **Cross-service consistency checks**
   - For a given environment and moment in time, gather:
     - Backend snapshot.
     - Frontend interpretation.
     - Analytics-transformed snapshot.
   - Verify an invariant such as: “For any user session, the flag state recorded in analytics matches the state that gated the feature in the UI.”

### 4.3 Observability and ongoing monitoring

1. **Version skew metrics**
   - Emit counters for:
     - Requests by `schemaVersion` at the backend.
     - Events by `flag_version` at the analytics layer.
   - Alert when the distribution of versions diverges significantly between backend and analytics.

2. **Downgrade and fallback metrics**
   - Track how often downgrade paths are used both in the backend (`downgradeSnapshot` calls) and in analytics (legacy fallbacks).
   - Use these metrics to decide when it is safe to deprecate legacy support or to catch misconfigured rollouts early.

3. **Playbook verification**
   - Incorporate automatic checks into the `discover_feed` rollout playbook that:
     - Confirm version alignment across services.
     - Validate that analytics and backend dashboards agree on exposure and variant split before ramping the rollout further.

Taken together, these changes would make the distributed feature flag system much more resilient to version skew. The key is to make version negotiation explicit, keep snapshots immutable across downgrade paths, tie caches to versioned keys, and normalize analytics payloads before A/B analysis so that schema transitions do not manifest as duplicate or contradictory experiment results.
