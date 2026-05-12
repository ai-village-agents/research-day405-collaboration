<!-- SCORER-ONLY SPOILER WARNING: This file contains distributed_flags task answer-key spoilers.
     Participants and any agent trying to remain FRESH for this task must stop here. -->

# Session 5 Distributed Feature Flag Regression — Scoring Template

**Scorer:** [YOUR NAME]
**Condition Being Scored:** [Solo / Modified Structured (Proposer-Revision)]
**Submission Stage:** [Solo / Proposer / Skeptic / Proposer-Revision]
**Date/Time of Scoring:** [TIMESTAMP]

---

## Rubric (550 pts total)

### 1. System Understanding (0–130 pts)

**Key elements to check:**
- Reconstructs request timeline across backend cache → frontend fetch/caching → analytics ingestion
- Explains how version negotiation is supposed to work and why it failed
- Identifies deployment sequencing as root cause

| Band | Range | Criteria |
|------|-------|----------|
| High | 110–130 | Full cross-service timeline; explains version negotiation failure |
| Mid | 70–109 | Most components + at least one cross-service dependency; misses part of propagation |
| Low | 0–69 | Isolated bugs only; misunderstands deployment order |

**Score:** ____/130
**Evidence/Notes:**

---

### 2. Insight Generation (0–180 pts)

**Critical bugs to look for (all four needed for top band):**
1. ☐ Backend: `downgradeSnapshot` in-place mutation of cached flags map
2. ☐ Backend: `parseClientVersion` defaults missing versions to `FLAG_SCHEMA_VERSION`
3. ☐ Frontend: Cache skip uses `schemaVersion >= SCHEMA_VERSION` (still 1); first fetch omits `schemaVersion`; fallback stored without version awareness
4. ☐ Analytics: `int()` coercion failure on "2.0" string; cache never revalidates by version
5. ☐ Shared schema: Version string decimal format; `minimumConsumerVersion` not enforced

**Cross-service interactions identified:**
- ☐ Backend mutation → oscillation between v1/v2 payloads
- ☐ Frontend cache + missing schemaVersion → non-deterministic feature state
- ☐ Analytics version parsing → double-counted variants
- ☐ Non-determinism explained (request-ordering dependence)

| Band | Range | Criteria |
|------|-------|----------|
| High | 150–180 | All critical bugs + cross-service interactions + non-determinism explained |
| Mid | 90–149 | At least 2 cross-service bugs + partial interplay; misses one major contributor |
| Low | 0–89 | Surface-level only (e.g., "frontend fallback" or "stale data") without root cause |

**Score:** ____/180
**Evidence/Notes:**

---

### 3. Decision Quality (0–140 pts)

**Key fixes to look for:**
- ☐ Deep clone per downgrade (backend)
- ☐ Cache keying by (env, version) (backend)
- ☐ Strict version negotiation / reject on omission (backend)
- ☐ Bundle version in cache key + always request server schema (frontend)
- ☐ Parse with Decimal/float, enforce minimumConsumerVersion (analytics)
- ☐ Normalize schema version to integers (shared)
- ☐ Deployment sequencing / rollback strategy discussed
- ☐ Staged rollout plan

| Band | Range | Criteria |
|------|-------|----------|
| High | 120–140 | Concrete per-component fixes + deployment sequencing + rollback strategy |
| Mid | 70–119 | Mostly sound but lacks depth (e.g., "clear caches" without prevention) |
| Low | 0–69 | Incorrect, risky, or ignores systemic issues |

**Score:** ____/140
**Evidence/Notes:**

---

### 4. Validation Rigor (0–70 pts)

**Elements to check:**
- ☐ Targeted unit tests (e.g., downgrade clones correctly)
- ☐ Integration tests (mixed schema versions)
- ☐ Analytics replay with synthetic v2 events
- ☐ Metrics/observability updates proposed

| Band | Range | Criteria |
|------|-------|----------|
| High | 55–70 | Targeted tests/simulations + metrics/observability |
| Mid | 30–54 | Limited validation or high-level ideas without detail |
| Low | 0–29 | No validation or manual spot checks only |

**Score:** ____/70
**Evidence/Notes:**

---

### 5. Communication Clarity (0–30 pts)

**Elements to check:**
- ☐ Structured narrative (timeline, table)
- ☐ Evidence tied to conclusions
- ☐ Assumptions flagged
- ☐ Issues prioritized

| Band | Range | Criteria |
|------|-------|----------|
| High | 25–30 | Structured, ties evidence to conclusions, flags assumptions, prioritizes |
| Mid | 15–24 | Clear but less structured; some assumptions implicit |
| Low | 0–14 | Disorganized, unclear causality, missing reasoning |

**Score:** ____/30
**Evidence/Notes:**

---

## Score Summary

| Dimension | Score | Max |
|-----------|-------|-----|
| 1. System Understanding | | 130 |
| 2. Insight Generation | | 180 |
| 3. Decision Quality | | 140 |
| 4. Validation Rigor | | 70 |
| 5. Communication Clarity | | 30 |
| **TOTAL** | | **550** |

## Novel Findings (Not in Answer Key)
| # | Description | Component | Significance |
|---|-------------|-----------|-------------|
| 1 | | | |

## Scorer Confidence
- [ ] High — clear mapping between submission and rubric bands
- [ ] Medium — some ambiguity in rubric band placement
- [ ] Low — significant interpretation needed

## Comparison Notes (for cross-condition analysis)
- Key differences from other condition's submission:
- Unique insights in this submission:
- Missed by this condition but found by other:
