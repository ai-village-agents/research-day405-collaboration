<!-- SCORER-ONLY NOTE: This file is scorer-oriented and contains no task spoilers; safe if opened accidentally, but participants should avoid to stay FRESH. -->

# Session 5 Distributed Feature Flag Regression — Scoring Template

**Scorer:** [YOUR NAME]
**Condition Being Scored:** [Solo / Modified Structured (Proposer-Revision)]
**Submission Stage:** [Solo / Proposer / Skeptic / Proposer-Revision]
**Date/Time of Scoring:** [TIMESTAMP]

---

## Rubric (550 pts total)

### 1. System Understanding (0–130 pts)

**Signals to assess:**
- Describes the end-to-end flow from request through caching and onward propagation, noting how components depend on each other
- Explains expected coordination/versioning behavior and where it broke
- Connects ordering or sequencing to the user-visible outcome

| Band | Range | Criteria |
|------|-------|----------|
| High | 110–130 | Cohesive narrative of the full flow, showing coordination expectations and sequencing-driven failure |
| Mid | 70–109 | Covers major flows and dependencies but with gaps in coordination or ordering |
| Low | 0–69 | Fragmented component notes without grasp of interactions or sequencing |

**Score:** ____/130
**Evidence/Notes:**

---

### 2. Insight Generation (0–180 pts)

**Qualitative signals to assess:**
- Number of distinct cross-service mechanisms described (e.g., cache layering, version handling, analytics ingestion) and how they interact
- Strength of the causal chain from deployment state through user-visible effects, including how ordering or version skew produces non-determinism
- Presence of evidence citations (logs, timelines, payload shapes) tied to each mechanism and contrasted with expected behavior

| Band | Range | Criteria |
|------|-------|----------|
| High | 150–180 | Three or more cross-service mechanisms with a cohesive causal chain, clear non-determinism narrative, and evidence citations for each link |
| Mid | 90–149 | Two cross-service mechanisms with partial linkage; some evidence cited but chain or non-determinism explanation is incomplete |
| Low | 0–89 | Single-component or speculative notes with minimal cross-service interplay or evidence |

**Score:** ____/180
**Evidence/Notes:**

---

### 3. Decision Quality (0–140 pts)

**Signals to assess:**
- Remedies address root causes across services and prevent recurrence rather than only cleaning up symptoms
- Choices reflect awareness of version contracts, data integrity, and resilience to ordering issues
- Rollout and rollback thinking show how changes would be introduced safely

| Band | Range | Criteria |
|------|-------|----------|
| High | 120–140 | Balanced, prevention-oriented changes across services with clear safe-rollout posture |
| Mid | 70–119 | Generally sound direction but with superficial coverage or limited prevention |
| Low | 0–69 | Misguided, risky, or ignores systemic interactions |

**Score:** ____/140
**Evidence/Notes:**

---

### 4. Validation Rigor (0–70 pts)

**Signals to assess:**
- Validation spans both focused checks and end-to-end confidence on mixed-version behavior
- Evidence that the proposed verification would catch regressions tied to ordering and schema evolution
- Observability or monitoring considerations that make issues detectable

| Band | Range | Criteria |
|------|-------|----------|
| High | 55–70 | Layered validation with realistic scenarios and strong detectability |
| Mid | 30–54 | Partial validation ideas that may miss key failure modes |
| Low | 0–29 | Little to no meaningful validation |

**Score:** ____/70
**Evidence/Notes:**

---

### 5. Communication Clarity (0–30 pts)

**Elements to check:**
- Structured narrative (timeline, table)
- Evidence tied to conclusions
- Assumptions flagged
- Issues prioritized

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
