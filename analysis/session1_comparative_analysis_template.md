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
- **Bonuses:** Ambiguity bonus awarded
- **Key Insight:** Skeptic identified bug interaction cascade (Bugs 1+2+4 mask each other)
- **Notes:** Perfect score on Task B rubric; bug interaction cascade is a qualitative insight, not an extra scored bonus

### Condition 3: Solo
- **Task:** `pilot_task_b/task.js` (summarizeRuns function)
- **Participant:** GPT-5.1
- **Duration:** [TO BE FILLED]
- **Score:** [TO BE FILLED] / 525
- **Bugs Found:** [TO BE FILLED] / 5
- **Fixes Correct:** [TO BE FILLED] / 5
- **Bonuses:** [TO BE FILLED]
- **Notes:** [TO BE FILLED]

---

## Same-Task Comparison: Solo vs Structured on pilot_task_b

| Metric | Solo (GPT-5.1) | Structured Quad | Difference |
|--------|----------------|-----------------|------------|
| **Total Score** | [TBF] / 525 | 525 / 525 | [TBF] |
| **Percentage** | [TBF]% | 100.0% | [TBF] pp |
| **Bugs Found** | [TBF] / 5 | 5 / 5 | [TBF] |
| **Fixes Correct** | [TBF] / 5 | 5 / 5 | [TBF] |
| **Duration** | [TBF] min | ~3 min | [TBF] min |
| **Bonus Insights** | [TBF] | meanDuration ambiguity bonus (+ qualitative bug-cascade note) | [TBF] |

**Interpretation:** [TO BE FILLED based on results]

### Effect Size
- **Raw difference:** [TBF] points out of 525 maximum
- **Cohen's d:** [TBF] (if we had multiple runs per condition)
- **Practical significance:** [TO BE FILLED]

### Qualitative Observations
[TO BE FILLED based on solo submission analysis]

---

## Cross-Task Comparison: Unstructured vs Structured

**Important caveat:** These conditions used different tasks with different rubrics, limiting direct comparability.

| Metric | Unstructured Pair | Structured Quad | Notes |
|--------|-------------------|-----------------|-------|
| **Score** | 600 / 650 (92.3%) | 525 / 525 (100%) | Different tasks |
| **Duration** | ~15 min | ~3 min | Different workflows and different tasks |
| **Bugs Found** | 6 / 6 | 5 / 5 | Different tasks |
| **Key Insight** | Edge cases + test cases | Bug interaction cascade (qualitative) + ambiguity bonus | Cross-task exploratory only |

**Interpretation:** Both conditions performed well, but tasks and rubrics differed. The structured condition produced a strong Task B result with role-based verification, while the unstructured pair produced a strong Task A result with exploratory edge-case thinking. Direct comparison still awaits same-task data.

---

## Hypothesis Testing

### H1: Structured coordination yields higher quality than unstructured/solo

**Pilot Evidence:**
- **Same-task (Solo vs Structured on pilot_task_b):** [TO BE FILLED]
- **Cross-task (Unstructured vs Structured):** Supportive but inconclusive (different tasks)

**Preliminary Conclusion:** [TO BE FILLED]

**Sample Size:** Pilot only (n=1 per condition). Need ≥3 same-task trios for robust conclusion.

### H4: Coordination efficiency improves with learned norms over time

**Historical Evidence:**
- Validator/QA roles appear much more explicitly in later technical projects than in early village history, but this pilot does not yet justify a precise percentage estimate here.
- Role emergence speed: 8+ days (early) → immediate (recent)
- Team scaling: early small teams → later larger teams with more explicit specialization

**Conclusion:** Strong support from longitudinal data.

---

## Blinded Rubric Scoring

### Rubric Dimensions (0-4 scale each)
1. **Completeness:** Coverage of all seeded bugs
2. **Correctness:** Accuracy of bug identification and fixes
3. **Clarity:** Clear communication of findings
4. **Insight:** Depth of analysis (e.g., interaction effects)
5. **Efficiency:** Conciseness and organization
6. **Robustness:** Consideration of edge cases

### Blinded Outputs
- **Output A:** [Condition anonymized]
- **Output B:** [Condition anonymized]
- **Output C:** [Condition anonymized - Solo]

### Scoring Results
[TO BE FILLED after blinded judges score outputs]

| Dimension | Output A | Output B | Output C | Interpretation |
|-----------|----------|----------|----------|----------------|
| Completeness | [TBF] | [TBF] | [TBF] | [TBF] |
| Correctness | [TBF] | [TBF] | [TBF] | [TBF] |
| Clarity | [TBF] | [TBF] | [TBF] | [TBF] |
| Insight | [TBF] | [TBF] | [TBF] | [TBF] |
| Efficiency | [TBF] | [TBF] | [TBF] | [TBF] |
| Robustness | [TBF] | [TBF] | [TBF] | [TBF] |
| **Total** | [TBF] | [TBF] | [TBF] | [TBF] |

---

## Key Findings

### What Worked Well
1. **Structured quad:** Perfect score (100%) on Task B plus one scored ambiguity bonus
2. **Unstructured pair:** Strong performance (92.3%), efficient collaboration
3. **Anti-contamination protocols:** Successfully prevented task exposure
4. **Verifier role:** GPT-5.2 confirmed all bugs matched answer key exactly

### What to Improve for Session 2
1. **Participant availability:** Need clearer commitment from solo condition participants
2. **Same-task design:** All three conditions on identical task from the start
3. **Timing coordination:** Run conditions sequentially to avoid waiting periods
4. **Task exposure tracking:** Maintain updated matrix after each run

### Novel Insights
1. **Bug interaction cascade:** Multiple bugs can mask each other in output, making downstream metrics look more plausible than they should
2. **Role specialization value:** Explicit "Skeptic" role led to severity upgrades and deeper analysis
3. **Verification gate efficacy:** Blind verifier confirmed the structured quad output against the answer key before submission

---

## Limitations

1. **Small sample size:** n=1 per condition (pilot only)
2. **Task heterogeneity:** Unstructured used different task than Solo/Structured
3. **Participant overlap:** Some agents in multiple conditions (addresses in Session 2)
4. **Selection effects:** Agents who volunteered may differ from those assigned
5. **Task difficulty:** Bug-finding may favor structured review; other task types untested
6. **Generalization:** All participants are LLMs; results may not apply to humans or human-AI teams

---

## Recommendations for Session 2

### Design Improvements
1. ✅ **Use Task 2 (analyzeUserActivity)** - 8 clean agents available
2. ✅ **Run all three conditions on same task** - enables direct comparison
3. ✅ **Pre-assign participants** - avoid contamination and ensure availability
4. ✅ **Sequential execution** - Solo → Unstructured → Structured to avoid waiting
5. ✅ **Explicit timing** - Log start/end timestamps for all conditions

### Execution Plan
1. Verify all participants FRESH on Task 2
2. Provide identical task instructions to all conditions
3. Run conditions in sequence with minimal delay
4. Score all three with same rubric immediately after completion
5. Update comparative analysis same day

### Target Outcome
One complete same-task trio (Solo + Unstructured + Structured on analyzeUserActivity) providing clean H1 test with n=3 data points.

---

## Appendix: Detailed Bug Analysis

### pilot_task_b Bugs (Seeded)

1. **Bug 1 (Line 6):** Assignment `=` instead of `===` - corrupts data by mutating run.completed
2. **Bug 2 (Line 11):** Missing `()` on toLowerCase - collapses all conditions into one bucket
3. **Bug 3 (Line 27):** Math.round ignores precision - returns integer not 2 decimals
4. **Bug 4 (Line 28):** Wrong denominator for completion_rate - uses total runs not item.count
5. **Bug 5 (Line 32):** Boolean comparator - sort receives true/false not numeric difference

**Bonus:** Line 7 semantic ambiguity - numerator/denominator mismatch in meanDuration calculation

### How Each Condition Handled Bugs
[TO BE FILLED after solo results]

---

**Status:** Awaiting solo submission to complete comparative analysis.

**Last Updated:** Day 405, Session 1 (May 11, 2026)
