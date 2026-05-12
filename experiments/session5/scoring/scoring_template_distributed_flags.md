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
- Reconstructs the cross-service timeline from request handling through downstream consumption
- Explains how version/schema negotiation is intended to work and why the observed rollout failed
- Identifies deployment/update ordering as part of the causal story rather than treating symptoms in isolation

| Band | Range | Criteria |
|------|-------|----------|
| High | 110–130 | Full cross-service timeline; explains version/schema negotiation failure and deployment-order contribution |
| Mid | 70–109 | Most components + at least one cross-service dependency; misses part of propagation or sequencing |
| Low | 0–69 | Isolated issue list only; weak or incorrect causal model of propagation/deployment |

**Score:** ____/130
**Evidence/Notes:**

---

### 2. Insight Generation (0–180 pts)

**Major issue clusters to look for (top-band submissions should cover all or nearly all of these):**
1. ☐ Backend/state-management contribution to the regression
2. ☐ Backend/version-negotiation or default-handling contribution
3. ☐ Frontend caching/fallback/version-awareness contribution
4. ☐ Analytics parsing/cache/aggregation contribution
5. ☐ Shared schema/contract mismatch or compatibility-policy contribution

**Cross-service interactions identified:**
- ☐ Explains how multiple components interact to create the failure rather than treating them as independent defects
- ☐ Explains why different clients or request orders can see different states
- ☐ Connects local implementation details to system-level non-determinism or inconsistent rollout behavior
- ☐ Distinguishes primary causal contributors from secondary symptoms

| Band | Range | Criteria |
|------|-------|----------|
| High | 150–180 | Covers all or nearly all major issue clusters, explains cross-service interactions, and accounts for non-deterministic behavior |
| Mid | 90–149 | Identifies multiple substantive contributors with partial interplay; misses at least one major contributor or causal connection |
| Low | 0–89 | Surface-level only (e.g., generic stale data or cache comments) without a persuasive root-cause account |

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
