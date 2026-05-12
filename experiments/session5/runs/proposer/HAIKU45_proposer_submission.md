# Session 5 Proposer Stage 1: Distributed Feature Flag Analysis
**Submission Time:** 12:17 PM PT | **Task ID:** session4_distributed_flags | **Deadline:** 12:25 PM PT

## Executive Summary
The incident stems from **three synchronized version skew failures** across backend→frontend→analytics pipelines. The backend shipped schema v2.0, but the frontend remained frozen at v1, and the analytics processor contains a critical **string-to-integer coercion bug** that causes v2.0 to default to v1 then immediately trigger a legacy fallback. This creates a **non-deterministic state divergence** amplified by caching without schema-aware invalidation.

---

## Bug 1: Backend Schema Version Bump Without Coordination
**Component:** `flag_service.js`  
**Root Cause:** Backend loaded schema v2.0 (`flag_schema.json`), sets `FLAG_SCHEMA_VERSION = Number(schema.version)` where `schema.version = "2.0"` (string).

**Mechanism:**
```javascript
const FLAG_SCHEMA_VERSION = Number(schema.version);  // "2.0" → NaN or 2?
```

When `schema.version = "2.0"` (semver string), `Number("2.0")` = `2`, so FLAG_SCHEMA_VERSION becomes `2`. However, the **shape of data** changed: v2 uses `state.rollout[]` with geo targeting metadata, while v1 used a simpler boolean `enabled` field.

**Impact on Clients:**
- Clients not redeployed (like frontend v1) request old format but receive new format
- parseClientVersion() defaults to FLAG_SCHEMA_VERSION (2) if client doesn't specify version hint
- This causes older clients to receive data they can't parse

---

## Bug 2: Frontend Hardcoded to Schema v1, Not Redeployed
**Component:** `FeatureGate.jsx`  
**Root Cause:** Frontend has `SCHEMA_VERSION = 1` hardcoded and was not redeployed when backend bumped to v2.

**Mechanism:**
```javascript
const SCHEMA_VERSION = 1;  // Frozen, while backend is at 2
```

**Fetch behavior:**
- Initial fetch: `schemaHint = undefined`, so no `schemaVersion` query param sent
- Backend's `parseClientVersion(undefined)` returns `FLAG_SCHEMA_VERSION = 2`
- Backend sends v2 data structure with `state.rollout[]` array

**coerceFlagState() Mismatch:**
```javascript
if (typeof flagBlock.enabled === 'boolean') {  // v2 doesn't have this
  return flagBlock.enabled;  // Never matches, falls through
}
if (flagBlock.state && flagBlock.state.defaultVariant) {  // v2 has state but NO defaultVariant
  // ...
}
return fallback;  // Returns fallback=false!
```

In v2, the data structure is:
```javascript
discover_feed: {
  state: { defaultTreatment: 'control', rollout: [...] },  // No defaultVariant
  metadata: {...}
}
```

So `flagBlock.state.defaultVariant` is undefined, and the function returns `fallback=false`.

**Non-determinism via Cache:**
- `readCached()` returns previous value if cache still valid (30s TTL)
- Some sessions hit cache with v1 data (enabled), others hit fresh fetch with v2 (fallback)
- After hard refresh, cache expires, forcing fetch, returning fallback=false
- **Result:** Inconsistent flag state across sessions and hard refreshes

---

## Bug 3: Analytics Schema Version Parser Type Coercion Failure
**Component:** `event_processor.py`  
**Root Cause:** Schema JSON has `"version": "2.0"` (string), but processor tries to parse as int without proper fallback.

**Mechanism:**
```python
SCHEMA_VERSION = int(RAW_SCHEMA.get('version', 1))  # int("2.0") raises ValueError
```

The catch block triggers:
```python
except (TypeError, ValueError):
    logger.warning('Failed to parse schema version %r, defaulting to legacy version 1', ...)
    SCHEMA_VERSION = 1  # Coerces to 1
```

So `self._schema_version = 1` in the processor.

**Event Processing Chain:**
- Mobile sends event with `flag_snapshot` in v2 format (because it got v2 from backend)
- `incoming_version = snapshot.get('version', 1)` = "2.0" (string)
- `if incoming_version > self._schema_version:` → `if "2.0" > 1:` **Python compares string vs int, evaluates to True**
- Triggers legacy fallback: `self._legacy_snapshot(flag_key)` returns:
```python
{
  'version': 1,  # Now marked as v1
  'flags': {'discover_feed': {'enabled': True, 'variant': 'treatment'}}  # From legacyFallback
}
```

**Non-determinism via Cache:**
- First event for a flag caches the resolved value
- Subsequent events for same (env, flag_key) return cached value
- If first event is v2, cache stores legacy snapshot forever (15s TTL or longer in practice)
- If events arrive in different order or from different clients, analytics diverges

---

## Bug 4: Cache Invalidation Not Schema-Aware
**Component:** Backend `snapshotCache`, Frontend local storage, Analytics `_flag_cache`  
**Root Cause:** Caches store resolved values without schema version tagging, making them unreliable across version boundaries.

**Scenario:**
1. Frontend v1 client hits cache expiry, fetches from backend
2. Backend returns v2 data (because frontend didn't send schemaVersion hint)
3. Frontend cache stores `{ value: <v2 data>, schemaVersion: undefined }`
4. Next request within TTL uses cached v2 data, coerceFlagState() fails, returns fallback
5. Cache expired, fresh fetch retrieves v2 again, same failure

**Backend Cache Issue:**
```javascript
snapshotCache.set(env, { value: base, expiresAt: Date.now() + 15_000 });
// Later: getSnapshot() returns base (original object reference)
// If base is mutated or schema version changes, cache serves stale data
```

---

## Bug 5: Schema Version Hint Propagation Broken
**Component:** Cross-service version negotiation  
**Root Cause:** No canonical version agreement mechanism.

**Propagation path:**
1. Frontend sends `schemaVersion=1` (if cached) or `undefined` (first request)
2. Backend ignores schema hint if undefined, assumes latest version (2)
3. Backend returns v2 data
4. Frontend can't parse v2 data, falls back to false
5. Analytics receives v2 data, string "2.0" > int 1 comparison, falls back to legacy

**No feedback loop:** Frontend never learns backend upgraded; backend never constrains to v1.

---

## Summary of Observable Failures

| Symptom | Root Cause |
|---------|-----------|
| "Some web sessions received new rules, others stayed on defaults even after hard refresh" | Cache inconsistency + schema version mismatch; some cached v1 data, some fetch v2 data that fails to parse |
| "Mobile traffic sent events saying flag disabled, contradicting backend dashboards" | Frontend returns fallback=false due to v2 schema mismatch; events capture v2 data that analytics coerces to legacy |
| "A/B test reports showed duplicate variants" | Analytics cache caches legacy fallback; some events arrive as v2 (treated as future), others as v1 (cached), creating false duplicates |

---

## Recommended Fixes

1. **Schema Versioning:**
   - Change `flag_schema.json` version from `"2.0"` (string) to `2` (integer)
   - Add `minimumRequiredConsumerVersion` field
   - Reject clients < minimum version with explicit 400 error, not silent downgrade

2. **Version Negotiation:**
   - Frontend *always* sends `schemaVersion` query param (initial: 1, after successful fetch: received version)
   - Backend uses client version hint to shape response; if client < MIN_VERSION, return 400 + upgrade instructions

3. **Cache Invalidation:**
   - Tag caches with schema version: `{ value, schemaVersion, expiresAt }`
   - Invalidate cache on schema version mismatch
   - Add cross-service schema compatibility check before deployment

4. **Deployment Sequencing:**
   - Deploy consumers (frontend, analytics) *before* producer (backend) upgrades schema
   - Use feature flags to gate schema v2 rollout; verify consumer readiness before enabling

5. **Analytics Robustness:**
   - Parse version as int with explicit error handling: `int(str(schema.get('version')).split('.')[0])`
   - Log schema version mismatches with event context (env, flag_key, incoming_version vs processor_version)
   - Test string vs int comparison edge cases

---

## Depth-Weighted Evidence
- **System Understanding:** End-to-end causal flow from backend v2 bump → frontend v1 client receiving v2 data → failed parsing → analytics coercion → cache divergence
- **Cross-Service Interaction:** Version negotiation, cache coherence, schema format evolution
- **Issue Clusters:** (1) Schema version encoding, (2) Version hint propagation, (3) Cache invalidation, (4) Type coercion in analytics, (5) Deployment coordination
- **Validation Approach:** Test v1 client against v2 backend; test v2 event arriving at v1 analytics processor; verify cache expiry + hard refresh behavior

