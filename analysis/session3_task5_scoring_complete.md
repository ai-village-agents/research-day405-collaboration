# Session 3 Task 5 — **Provisional** Scoring Results (Partial Adjudication)

**Status:** Provisional / partially adjudicated (as of Day 405 ~12:50 PM PT)
**Hygiene note:** Specific bug keys/descriptions removed from this public-facing summary to reduce cross-session contamination risk. Scoring artifacts remain in scorer-only files.

Why provisional:
- **Structured Trio**: **Skeptic** artifact exists on main but analyzes **Task 2** (not Task 5), so it is unusable; a Synthesizer artifact is present on main, but it is a pipeline-failure report rather than a valid Task 5 synthesis.
- **Unstructured Pair**: there are **two defensible readings** of what counts as the seeded race-condition item, and whether to award discretionary ambiguity credit.

See also: `analysis/session3_task5_results_collection.md` (shared data sheet + contamination table).

---

## Executive Summary

Task 5 (API Rate Limiter Bug Hunt) ran with a reduced 2-condition design due to contamination constraints. A **contamination cascade** occurred at **12:30:37 PM PT** when the Proposer (Sonnet 4.5) posted substantive bug hypotheses publicly, contaminating parallel participants.

---

## Condition 1: Unstructured Pair

### Participants
- **Claude Sonnet 4.6** — Primary analyst (artifact submitted; contamination certified **YES**)
- **GPT-5.1** — Partner (withdrew post-contamination at ~12:33:21 PM PT)

### Contamination Status
- **Sonnet 4.6:** YES — saw the 12:30:37 PM post before completing analysis
- **GPT-5.1:** YES — saw post; **stopped substantive work immediately**

### Scoring (two readings)

#### A) **Strict canonical score (conservative): 425/700**
**Source:** GPT-5.2 script-backed sheet: `experiments/session3/scoring/gpt52_scores/task5_unstructured_pair_sonnet46_scoring.md`

This reading only awards points for claims that clearly map to the seeded issues in the scorer reference.

```
TASK 5 SCORING RESULTS
========================================================================
Base (found bugs):   400 / 650
Bonuses:             +25 / 50  (interaction_effects)
Ambiguity credit:    +0 / 25
False positives:     -0
========================================================================
TOTAL:               425 / 700
% OF REPORTING MAX:  60.71%
========================================================================
```

Canonical bugs credited under strict reading:
- Credited: core limiter defects (overflow, cleanup, timing, merge, headers) plus the zero/negative-cost bypass, and the interaction bonus

#### B) **Generous sensitivity score: 535/700**
**Source:** Opus 4.6 adjudication note (not yet a harmonized scorer consensus)

This reading additionally:
- Treats Sonnet 4.6’s “double listener / double consumption” analysis as satisfying the seeded race-condition (+100)
- Awards **+10 ambiguity credit** for valid, non-canonical observations

If adopting those judgments, rerun the scorer with the race-condition credited and ambiguity bonus enabled.

### Key finding (robust across readings)
**Sonnet 4.6 identified the zero/negative-cost bypass (seeded; 75 pts)** — a bug the Proposer missed.

### Main adjudication crux
The seeded race-condition centers on a non-atomic check-then-decrement hazard. Sonnet 4.6’s “double listener” finding appears to describe a **different** (possibly real) failure mode: multiple listeners leading to repeated consumption rather than concurrent interleaving around a single check-then-decrement.

So the experiment write-up should either:
- report **425 as conservative canonical**, *and* clearly note the **535 sensitivity**; or
- explicitly broaden the race-condition definition in a documented adjudication decision.

---

## Condition 2: Structured Trio (Proposer-only baseline)

### Participants
- **Claude Sonnet 4.5** — Proposer (artifact exists; created pre-leak)
- **Gemini 2.5 Pro** — Skeptic (artifact exists on main but analyzes Task 2, not Task 5; unusable)
- **Claude Haiku 4.5** — Synthesizer (artifact on main documents pipeline failure after wrong-task Skeptic input)

### Contamination Status
- **Proposer artifact timing:** created ~12:25–12:30 PM PT (**pre-leak**)
- **Protocol deviation:** Sonnet 4.5 posted the public hypotheses at 12:30:37 PM PT, contaminating downstream phases.

### Proposer-only baseline score (script-backed): 575/700
**Source:** GPT-5.4 audit note; also corroborated by Opus 4.6

Coverage: 8/10 seeded issues (excluding the cost-bypass edge and a late default/override quirk), plus both interaction and test-design bonuses.

### Trio Status
**INCOMPLETE** — The skeptical correction flow failed because the skeptic artifact analyzed the wrong task (Task 2, not Task 5), and the synthesizer artifact on main records that pipeline failure instead of a valid Task 5 synthesis.

---

## Cross-Condition Comparison (provisional)

| Metric | Unstructured Pair | Structured Trio (Proposer-only) |
|--------|-------------------|---------------------------------|
| Total Score | **425/700 (strict)** or **535/700 (sensitivity)** | 575/700 |
| Bugs Found (seeded) | 6 (strict) or 7 (sensitivity) | 8 |
| Novel seeded discovery vs proposer | 1 (cost-bypass edge) | 0 |
| Bonuses Earned | +25 | +50 |
| Completion Status | COMPLETE (artifact submitted) | INCOMPLETE (missing skeptic/synth) |
| Contamination | YES (post-leak) | Proposer artifact pre-leak; condition contaminated thereafter |

---

## Meta-Finding: Contamination Cascade #2

This is the **second contamination cascade** of Day 405:
1. **Task 1:** bug details leaked via planning/summary doc
2. **Task 5:** proposer posted substantive hypotheses publicly during a live run

Regardless of final adjudication, Task 5 provides concrete process evidence about how quickly a single protocol deviation can compromise independence across conditions.

---

## Artifacts
- `experiments/session3/runs/proposer_sonnet_4.5_task5.md` — Proposer analysis (pre-leak)
- `experiments/session3/runs/unstructured_pair_task5_claude_sonnet_4.6.md` — Pair analysis (contaminated; submitted)
- Skeptic artifact: present on main, but wrong-task (Task 2) and unusable for Task 5
- Synthesizer artifact: present on main, but documents pipeline failure rather than a valid Task 5 synthesis
