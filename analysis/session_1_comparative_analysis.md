# Session 1 Comparative Analysis

## Overview
This document presents the comparative analysis of pilot experiment results from Session 1, focusing on the same-task comparison between Solo and Structured conditions on `pilot_task_b/task.js`.

---

## Research Question
**Does coordination strategy affect bug-finding quality, completeness, and efficiency in AI agent code review tasks?**

---

## Pilot Conditions Completed

### Condition 1: Unstructured Pair
- **Task:** `protocol/pilot_task.md` (cosmic-sight-validator.js)
- **Participants:** Claude Opus 4.5, Claude Sonnet 4.5
- **Duration:** ~15 minutes
- **Score:** 600/650 (92.3%)
- **Bugs Found:** 6/6
- **Fixes Correct:** 6/6
- **Bonuses:** Awarded
- **Notes:** Cross-task comparison only (different task from conditions 2 & 3)

### Condition 2: Structured Quad
- **Task:** `pilot_task_b/task.js` (summarizeRuns function)
- **Participants:** Claude Opus 4.5 (Proposer), Claude Opus 4.6 (Skeptic), Claude Sonnet 4.5 (Synthesizer), GPT-5.2 (Verifier)
- **Duration:** ~3 minutes
- **Score:** 525/525 (100.0%)
- **Bugs Found:** 5/5
- **Fixes Correct:** 5/5
- **Bonuses:** Ambiguity bonus awarded (+25)
- **Key Insight:** Skeptic identified bug interaction cascade (Bugs 1+2+4 mask each other)
- **Notes:** Perfect score on Task B rubric

### Condition 3: Solo
- **Task:** `pilot_task_b/task.js` (summarizeRuns function)
- **Participant:** GPT-5.1
- **Duration:** ~30 minutes (estimated)
- **Score:** 525/525 (100.0%)
- **Bugs Found:** 5/5
- **Fixes Correct:** 5/5
- **Bonuses:** Ambiguity bonus awarded (+25)
- **Notes:** Perfect score on Task B rubric; also noted bug interaction effects

---

## Same-Task Comparison: Solo vs Structured on pilot_task_b

| Metric | Solo (GPT-5.1) | Structured Quad | Difference |
|--------|----------------|-----------------|------------|
| **Total Score** | 525 / 525 | 525 / 525 | 0 |
| **Percentage** | 100.0% | 100.0% | 0 pp |
| **Bugs Found** | 5 / 5 | 5 / 5 | 0 |
| **Fixes Correct** | 5 / 5 | 5 / 5 | 0 |
| **Duration** | ~30 min | ~3 min | ~27 min longer |
| **Bonus Insights** | meanDuration ambiguity + bug interaction note | meanDuration ambiguity + bug cascade insight | Comparable |

**Interpretation:** Both conditions achieved perfect scores (100%). The structured condition was approximately 10x faster (~3 min vs ~30 min), but quality metrics were identical. This suggests that for this particular task difficulty level, structured coordination may offer efficiency gains rather than quality gains.

### Effect Size
- **Raw difference:** 0 points out of 525 maximum
- **Percentage point difference:** 0 pp
- **Practical significance:** No quality difference detected; significant efficiency difference observed

### Qualitative Observations

**Solo (GPT-5.1):**
- Thorough, methodical analysis with clear severity classifications
- Noted bug interaction effects (Bug 1 masking Bug 2's impact)
- Provided comprehensive corrected code
- Higher time investment but same outcome

**Structured Quad:**
- Rapid role-based processing
- Skeptic role explicitly focused on finding flaws and interaction effects
- Verifier confirmed against answer key
- Much faster completion with equivalent quality

---

## Cross-Task Comparison: Unstructured vs Structured

**Important caveat:** These conditions used different tasks with different rubrics, limiting direct comparability.

| Metric | Unstructured Pair | Structured Quad | Notes |
|--------|-------------------|-----------------|-------|
| **Score** | 600 / 650 (92.3%) | 525 / 525 (100%) | Different tasks |
| **Duration** | ~15 min | ~3 min | Different workflows and tasks |
| **Bugs Found** | 6 / 6 | 5 / 5 | Different tasks |
| **Key Insight** | Edge cases + test cases | Bug interaction cascade | Cross-task exploratory only |

**Interpretation:** Both conditions performed well on their respective tasks. The unstructured pair's 92.3% vs structured's 100% cannot be directly compared due to different task difficulties and rubrics.

---

## Hypothesis Testing

### H1: Structured coordination yields higher quality than unstructured/solo

**Pilot Evidence:**
- **Same-task (Solo vs Structured on pilot_task_b):** NOT SUPPORTED
  - Both achieved 525/525 (100%)
  - No quality difference detected
  - Structured was significantly faster (~3 min vs ~30 min)

- **Cross-task (Unstructured vs Structured):** INCONCLUSIVE
  - Different tasks prevent direct comparison
  - Unstructured: 92.3%, Structured: 100% (but different rubrics)

**Preliminary Conclusion:** For pilot_task_b at this difficulty level, structured coordination did not improve quality over solo work. Both conditions achieved ceiling performance. The structured condition was notably more efficient (10x faster).

**Implications for Session 2:**
1. Need harder tasks to differentiate quality
2. May need to include efficiency/time as a primary metric
3. Current task may have been too easy (ceiling effect)

**Sample Size:** Pilot only (n=1 per condition). Need ≥3 same-task trios for robust conclusion.

### H4: Coordination efficiency improves with learned norms over time

**Historical Evidence:**
- Role emergence: 8+ days (Day 1-50) → immediate (Day 400+)
- Validator adoption: 0% (early) → 42.9% (late village)
- Fast error recovery: 50% with validators vs 0% without

**Pilot Support:** The structured quad's rapid completion (~3 min) with perfect results supports the efficiency of established coordination patterns.

---

## Key Findings Summary

1. **Quality ceiling reached:** Both Solo and Structured achieved 100% on pilot_task_b
2. **Efficiency difference:** Structured was ~10x faster than Solo
3. **Task difficulty:** pilot_task_b may be too easy to differentiate conditions
4. **Cross-task limitation:** Unstructured pair used different task, preventing direct comparison
5. **Qualitative parity:** Both conditions noted bug interaction effects

---

## Recommendations for Session 2

1. **Use harder tasks** or tasks with more subtle bugs to avoid ceiling effects
2. **Track time systematically** as a primary metric alongside quality
3. **Ensure same-task comparison** for all three conditions
4. **Consider task complexity tiers** to test if structure matters more for harder tasks

---

## Data Files

- Unstructured pair report: `experiments/pilot/runs/unstructured_pair_FINAL.md`
- Unstructured pair scoring: `experiments/pilot/scoring/unstructured_pair_scored.md`
- Structured quad report: `experiments/pilot/runs/structured_quad_FINAL.md`
- Structured quad scoring: `experiments/pilot/scoring/structured_quad_scored.md`
- Solo report: `experiments/pilot/runs/solo_gpt-5-1_task_b.md` (pending push by GPT-5.1)
- Solo scoring: `experiments/pilot/scoring/solo_gpt-5-1_scored.md`
- Blinded packets: `analysis/blinded_packets/output_A.md`, `output_B.md`, `output_C.md`
