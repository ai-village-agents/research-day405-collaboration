# Statistical Analysis Plan

## Purpose
Define the statistical tests and analyses we'll use to evaluate H1-H4 hypotheses once we have sufficient pilot data.

---

## Primary Hypotheses

### H1: Structured coordination yields higher quality than unstructured/solo
**Test:** Paired/repeated measures comparison of quality scores across conditions
**Data:** Task-specific scores (%) + blinded rubric scores (0-4 on 6 dimensions)
**Requirements:** At least 3 same-task comparisons (Solo vs Unstructured vs Structured)

### H2: Agents develop persistent collaboration preferences over time  
**Test:** Longitudinal preference survey + behavioral analysis from historical data
**Data:** Agent-reported preferences + actual coordination mode choices over 405 days
**Requirements:** Survey data + historical participation patterns

### H3: Different task types benefit from different strategies
**Test:** Task type × Coordination mode interaction analysis
**Data:** Quality scores grouped by task family (code review, creative, infrastructure, etc.)
**Requirements:** Multiple task types × multiple conditions

### H4: Coordination efficiency improves with learned norms over time
**Test:** Time series analysis of coordination metrics over 405 days
**Data:** Historical data on role emergence time, error recovery speed, validator adoption
**Status:** Strong quantitative evidence already collected (Days 1-100 vs 301-405)

---

## Statistical Tests Planned

### 1. Pilot Experiment: Within-Task Comparison
**Design:** Solo vs Unstructured vs Structured on same task
**Test:** Friedman test (non-parametric repeated measures) or one-way ANOVA if n≥5
**Effect size:** Cohen's d for pairwise comparisons
**Current status:** Need ≥1 complete same-task trio for meaningful test

### 2. Cross-Task Rubric Scoring  
**Design:** Blinded judges score outputs A/B/C on 6 dimensions (0-4 scale)
**Test:** Mixed-effects model with judge as random effect, condition as fixed effect
**Inter-rater reliability:** Krippendorff's alpha or ICC
**Current status:** Blinded packets prepared, awaiting solo submission

### 3. Historical Validator Impact
**Design:** Goals WITH validators vs WITHOUT validators
**Metrics:** Error recovery speed (categorical: fast/slow/none), outcome quality (0-3)
**Test:** Mann-Whitney U test (non-parametric, small n)
**Effect size:** Rank-biserial correlation
**Current status:** Data collected (6 validator goals, 16 non-validator goals)

### 4. Historical Role Emergence Speed
**Design:** Early era (Days 1-100) vs Late era (Days 301-405)
**Metric:** Days until explicit roles emerge
**Test:** Two-sample t-test or Mann-Whitney U
**Current status:** Qualitative evidence strong (8+ days → immediate), needs quantification

### 5. Historical Coordination Mode Outcomes
**Design:** 5 coordination modes × 22 goals
**Metric:** Outcome quality (0-3 scale)
**Test:** Kruskal-Wallis test (non-parametric one-way ANOVA)
**Post-hoc:** Dunn's test with Bonferroni correction
**Current status:** Data coded in coordination_modes_analysis.txt

---

## Sample Size Requirements

### Current State
- **Pilot:** 2 complete runs (unstructured on task A, structured on task B), 1 pending (solo on task B)
- **Historical:** 22 goals with coded coordination modes
- **Validator analysis:** 6 WITH, 16 WITHOUT

### Minimum for Publication
- **Pilot:** ≥3 complete same-task trios (9 runs total) for within-subjects comparison
- **Cross-task:** ≥2 blinded judges scoring ≥5 outputs per condition
- **Historical:** Current n=22 sufficient for exploratory analysis, note limitations

### Target for Session 2
- Complete 1-2 same-task trios using session2_task_1 and session2_task_2
- Run with fresh participants (no contamination)
- Total new runs: 6 (2 tasks × 3 conditions)

---

## Effect Sizes & Interpretation

Using Cohen's (1988) conventions:
- **Small:** d=0.2, η²=0.01, r=0.1
- **Medium:** d=0.5, η²=0.06, r=0.3  
- **Large:** d=0.8, η²=0.14, r=0.5

Given our small sample, we focus on **effect size estimation** rather than p-value significance testing. Report:
1. Point estimate with confidence interval
2. Effect size with interpretation
3. Practical significance (e.g., "Structured caught 20% more bugs")

---

## Data Quality Checks

### Pilot Experiment
- [ ] Contamination check: No participant saw same task twice
- [ ] Timing recorded: Start/end timestamps for all runs
- [ ] Output preserved: Full transcripts in experiments/pilot/runs/
- [ ] Scoring blinded: Scorer doesn't know condition until after rating

### Historical Data
- [ ] Coding reliability: Second coder reviews ≥20% of goals
- [ ] Operational definitions: Clear criteria for "validator", "role emergence", etc.
- [ ] Missing data: Document incomplete goals or ambiguous cases
- [ ] Temporal confounds: Control for agent count increase over time

---

## Planned Visualizations

### Figure 1: Pilot Results - Same-Task Comparison
Box plots or violin plots: Solo | Unstructured | Structured on same task

### Figure 2: Historical Validator Effect  
Bar chart: Error recovery speed (fast/slow/none) by validator presence

### Figure 3: Historical Role Emergence Timeline
Line graph: Days to role emergence vs village day (showing acceleration)

### Figure 4: Coordination Mode Outcomes
Grouped bar chart: Average outcome quality by coordination mode (with error bars)

### Figure 5: Rubric Dimension Radar
Radar chart: 6 rubric dimensions by condition (from blinded scoring)

---

## Limitations to Address

1. **Small pilot n:** Results exploratory, needs replication
2. **Different tasks across conditions:** Limits direct comparison (until same-task data)
3. **Non-independence:** Some agents participated in multiple conditions
4. **Task selection:** Tasks chosen for bug-finding, may not generalize to creative/social tasks
5. **LLM-only sample:** Results may not apply to human teams or human-AI teams
6. **Observational historical data:** Causal claims limited by confounds
7. **No pre-registration:** Hypotheses refined during analysis (exploratory)

---

## Next Steps

1. **Await GPT-5.1 solo results** - Complete first same-task comparison
2. **Blinded scoring** - 2 judges score outputs A/B/C under rubric.md
3. **Session 2 execution** - Collect 1-2 complete same-task trios
4. **Historical coding validation** - Second coder reviews sample
5. **Run planned tests** - Execute statistical analysis with complete data
6. **Draft results section** - Report effect sizes, visualizations, limitations

---

**Status:** Analysis plan ready, awaiting data completion for execution.
