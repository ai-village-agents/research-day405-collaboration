# Session 3 — Distributed Feature Flag Regression (Answer Key)

## Incident Synthesis
- **Backend schema bump without deep clone:** `backend/flag_service.js` serves the new v2 shape (with `state.rollout`) but downgrades legacy consumers in-place. `downgradeSnapshot` spreads the top-level snapshot yet leaves `flags` as the same object reference, so mutating `downgraded.flags[flagKey]` rewrites the cached v2 snapshot. Once any legacy client (schema v1) requests flags, the cache now holds the v1 shape for everyone until the cache expires, erasing rollout instructions.
- **Version auto-assumption lets old clients see v2:** `parseClientVersion` coerces missing/invalid versions to `FLAG_SCHEMA_VERSION`. Fresh React sessions (no cache hint) omit `schemaVersion`, so the backend assumes they understand v2 and responds with the new structure. Older bundles cannot parse it and fall back to their local defaults, causing "feature off" experiences despite new rollout rules.
- **Frontend cache pins stale interpretation:** `frontend/FeatureGate.jsx` short-circuits the network when cached `schemaVersion >= SCHEMA_VERSION`. Because the bundle constant is still `1`, any v1 snapshot (including legacy cache predating the deploy) is treated as "fresh enough" and re-used for 30 seconds. First-time sessions fetch without `schemaVersion`, receive v2, fail to parse, and cache the `fallback=false`. Returning sessions that held a `true` value from before the deploy keep the feature enabled. This mix created the non-deterministic on/off reports.
- **Analytics rejects "future" snapshots forever:** `analytics/event_processor.py` tries to coerce the shared schema version with `int(...)`. The new JSON ships "2.0" (string with decimal formatting), triggering the `ValueError` path and reverting to legacy version `1`. Any incoming snapshot with `version > 1` is logged as "future" and replaced with `LEGACY_DEFAULTS`, then cached per env without a version guard. Analytics therefore double-counted variants (control from fallback + treatment from infrequent v2 events).
- **Shared schema leak:** `shared/flag_schema.json` publishes "2.0" and `minimumConsumerVersion: 2`, but neither client enforces it. The value is not normalized, so consumers must trim/parse carefully. Because the frontend reuses cached schema hints and the analytics job truncates to int, both miss the breaking change signal.

### Interaction Timeline
1. Backend deploys first, switching snapshots to the v2 rollout shape.
2. Fresh web sessions (no cache hint) hit `/flags/prod`; backend assumes schema parity and returns v2. React bundle (still on v1) fails to read `flags.discover_feed.state`, falls back to `false`, caches the fallback with `schemaVersion: 1`.
3. Returning sessions with cached `enabled: true` skip the fetch entirely (`schemaVersion >= SCHEMA_VERSION` check), so they keep the feature on even though rollout logic moved server-side.
4. Mobile analytics jobs stream events with `flag_snapshot.version = 2`. The worker cannot parse "2.0", drops to legacy defaults, and caches the downgraded payload, so downstream reports stay on the old shape.
5. When any v1 consumer eventually sends `schemaVersion=1`, `downgradeSnapshot` mutates the cached snapshot into the legacy shape, wiping rollout metadata for the next 15 seconds. Depending on request ordering, later v2-capable clients either see the full rollout or the downgraded control.

## Key Bugs & Fixes

| Component | Bug | Impact | Suggested Fix |
|-----------|-----|--------|---------------|
| `backend/flag_service.js` | `downgradeSnapshot` mutates the cached `flags` map; `parseClientVersion` defaults missing versions to `FLAG_SCHEMA_VERSION`. | Non-deterministically serves v1 or v2 payloads; strips rollout rules for everyone once downgraded. | Deep clone per downgrade, store cache by `(env, version)`, and reject/force downgrade when clientVersion < `minimumConsumerVersion`. Require explicit version negotiation (400 on omission). |
| `frontend/FeatureGate.jsx` | Cache skip uses `schemaVersion >= SCHEMA_VERSION` (still `1`); first fetch omits `schemaVersion`; fallback stored without version awareness. | Sessions oscillate between stale v1 values and fallback false, ignoring backend rollout. | Include bundle build version in cache key, always request server schema version, and re-fetch when server reports newer version. Consider short TTL while migration completes. |
| `analytics/event_processor.py` | `int(RAW_SCHEMA['version'])` fails on "2.0", forcing legacy mode; cache never revalidates by version. | Drops v2 segments, double-counts variants, pollutes A/B reports. | Parse with `Decimal`/`float`, enforce `minimumConsumerVersion`, and attach `version` to cache key. Ingest future versions via quarantine instead of silent downgrade. |
| `shared/flag_schema.json` | Version string encodes decimals; `minimumConsumerVersion` not enforced anywhere. | Allows silent mismatches; consumers misinterpret version gate. | Publish normalized integers (e.g., `"2"`), add explicit negotiation contract, and document breaking-change process. |

## Rubric (550 pts total)
The rubric mirrors the depth-weighted categories introduced in the design strategy while scaling to 550 points.

### 1. System Understanding (0–130 pts)
Evaluate how well the solver maps inter-service data flow and deployment sequencing.
- **110–130:** Reconstructs request timeline across backend cache, frontend fetch/caching, and analytics ingestion. Explains how version negotiation is supposed to work and why it failed.
- **70–109:** Identifies most components and highlights at least one cross-service dependency (e.g., backend downgrade mutating cache or frontend omitting schemaVersion) but misses part of the propagation story.
- **0–69:** Focuses on isolated bugs without connecting services or misunderstands the deployment order.

### 2. Insight Generation (0–180 pts)
Reward detection of subtle, interaction-driven defects.
- **150–180:** Surfaces all critical bugs: backend in-place downgrade + permissive version default, frontend cache skip + initial request missing schemaVersion, analytics `int()` coercion failure, and schema version normalization gap. Explains the non-determinism and conflicting analytics counts.
- **90–149:** Spots at least two of the cross-service bugs and articulates partial interplay (e.g., backend mutation causes oscillation) but misses one major contributor.
- **0–89:** Only reports surface-level mismatches (e.g., "frontend fallback" or "analytics stale data") without tracing root cause.

### 3. Decision Quality (0–140 pts)
Assesses the quality of recommended fixes and trade-off awareness.
- **120–140:** Proposes concrete code or process fixes per component (deep clone, cache keying, strict version negotiation, schema normalization, staged rollout plan). Discusses deployment sequencing and rollback strategy.
- **70–119:** Recommendations mostly sound but lack depth (e.g., "clear caches" without preventing recurrence).
- **0–69:** Suggestions are incorrect, risky, or ignore systemic issues (e.g., "disable caching everywhere" or "ship frontend immediately" without addressing negotiation).

### 4. Validation Rigor (0–70 pts)
Credit plans/tests that would prove the fixes.
- **55–70:** Designs targeted tests or simulations (e.g., unit tests ensuring downgrade clones, integration test covering mixed schema versions, replay of analytics queue with synthetic v2 events). Includes metrics/observability updates.
- **30–54:** Provides limited validation (single unit test mention) or high-level ideas without detail.
- **0–29:** No validation or relies on manual spot checks only.

### 5. Communication Clarity (0–30 pts)
Measures how well findings are organized and justified.
- **25–30:** Presents structured narrative (timeline, table) tying evidence to conclusions, flags assumptions, and prioritizes issues.
- **15–24:** Clear but less structured; some assumptions implicit.
- **0–14:** Disorganized notes, unclear causality, or missing reasoning steps.

## Additional Review Prompts
- Confirm downstream consumers (mobile, batch jobs) respect `minimumConsumerVersion` before enabling schema auto-upgrades.
- Consider checksum-based cache busting so the frontend never reuses stale snapshots when backend payload changes.
- Evaluate feature-flag rollout process: require synchronized schema deploys, publish migration guides, and enforce compatibility checks during CI.
