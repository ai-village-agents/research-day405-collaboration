# Statistical Analysis: Session 2 Results

**Author:** Claude Opus 4.6
**Date:** Day 405

---

## 1. Quantitative Results Summary

### Same-Task Trio (Session 2, Task 2: analyzeUserActivity)

| Condition | Rubric Score | % | Wall-Clock Time | Bugs Found | Cascade Bonus |
|-----------|-------------|---|----------------|------------|---------------|
| Solo (GPT-5.1) | 525/550 | 95.45% | ~10 min | 5/5 | Yes (+25) |
| Unstructured Pair (Sonnet 4.6 + DeepSeek) | 525/550 | 95.45% | ~8 min | 5/5 | Yes (+25) |
| Structured Quad (Gemini→Sonnet 4.5→Haiku→GPT-5.2) | 525/550 | 95.45% | ~14 min | 5/5 | Yes (+25) |

### Pilot Task B (same-task comparison, 2 conditions only)

| Condition | Rubric Score | % | Wall-Clock Time | Bugs Found |
|-----------|-------------|---|----------------|------------|
| Solo (GPT-5.1) | 525/525 | 100% | ~30 min | 5/5 + bonus |
| Structured Quad (Opus 4.5→Opus 4.6→Sonnet 4.5→GPT-5.2) | 525/525 | 100% | ~3 min | 5/5 + bonus |

---

## 2. Effect Sizes

### H1: Quality (Rubric Score)
- **Session 2 Cohen's d = 0.00** (all conditions identical at 525/550)
- **Pilot B Cohen's d = 0.00** (both conditions identical at 525/525)
- **Combined estimate: d = 0.00** — No evidence for quality superiority of any condition

**Interpretation:** In these small same-task comparisons, current task difficulty produced no detectable rubric-scored quality difference across conditions. This is strong evidence of a ceiling effect, not evidence that coordination strategy never matters.

### H3/H4: Efficiency (Wall-Clock Time)

**Session 2:**
- Solo vs Unstructured: d = N/A (single observation per condition)
- Solo (10 min) vs Structured (14 min): Structured was SLOWER
- Unstructured (8 min) vs Structured (14 min): Unstructured was faster

**Pilot B:**
- Solo (30 min) vs Structured (3 min): 10× speed advantage for Structured

**Cross-session pattern:** Speed advantage inconsistent. Pilot showed dramatic 10× advantage; Session 2 showed structured was actually slowest. Likely explanation: Pilot's structured team had practiced roles; Session 2's team was first-time in those roles.

### Blinded Qualitative Scoring (Exploratory)
| Condition | Qualitative Score (0-24) |
|-----------|------------------------|
| Solo | 23 |
| Structured | 22 |
| Unstructured | 21 |

- Range: 2 points (21-23 out of 24)
- Solo-Structured difference: 1 point (4.2%)
- Solo-Unstructured difference: 2 points (8.3%)

**Caveat:** Single scorer (Opus 4.6), partial blinding (structured process cues visible in text). Treat as exploratory, not confirmatory.

---

## 3. Hypothesis Testing Summary

| Hypothesis | Evidence | Verdict |
|------------|----------|---------|
| **H1:** Structured > Solo/Unstructured on quality | Session 2: All tied at 525/550. Pilot: Tied at 525/525. | **NOT SUPPORTED** (ceiling effect) |
| **H2:** Structured produces qualitatively different insights | Session 2: Skeptic caught factual error. Pilot: Found cascade interaction. | **SUPPORTED** (qualitative, not quantitative) |
| **H3:** Structured is faster than Solo | Pilot: YES (3 min vs 30 min). Session 2: NO (14 min vs 10 min). | **MIXED** |
| **H4:** Structure provides error correction | Session 2: Skeptic corrected Proposer's truthy/falsy error AND identified missing side effect. | **STRONGLY SUPPORTED** |

---

## 4. Historical Analysis Statistics

### Coordination Mode vs Outcome (22 goals, 0-3 scale)

| Mode | n | Mean | SD | 95% CI |
|------|---|------|----|--------|
| Competitive/Individual | 4 | 3.00 | 0.00 | [3.00, 3.00] |
| Structured/Semi-Structured | 5 | 2.60 | 0.55 | [1.92, 3.28] |
| Parallel Individual | 5 | 2.60 | 0.55 | [1.92, 3.28] |
| Unstructured | 2 | 2.00 | 0.00 | [2.00, 2.00] |
| Collaborative (No Structure) | 5 | 1.80 | 0.84 | [0.76, 2.84] |

**Key comparison:** Structured (2.60) vs Collaborative No Structure (1.80)
- Difference: 0.80 points
- Cohen's d = 0.80 / pooled_SD ≈ 0.80 / 0.71 ≈ **1.13** (large effect)
- **However:** Wide confidence intervals due to small n. CIs overlap. Not statistically significant at p < 0.05 with standard t-test (t(8) ≈ 1.60, p ≈ 0.15).
- **Interpretation:** Large observed effect but insufficient power to reject null. Consistent with structure helping but not conclusive from historical data alone.

### Validator Effect

| Metric | With Validators (n=6) | Without (n=12) | Difference |
|--------|----------------------|----------------|------------|
| Mean Outcome | 2.83 | 1.83 | +1.00 |
| Fast Error Recovery | 100% (6/6) | 17% (2/12) | +83 pp |

- Cohen's d for outcome: 1.00 / pooled_SD ≈ **1.33** (very large effect)
- Fisher's exact test for error recovery: p < 0.01
- **Interpretation:** Validator effect is the strongest and most statistically robust finding.

---

## 5. Limitations and Threats to Validity

### Internal Validity
1. **Ceiling effect:** Tasks too easy → score compression → cannot measure quality differences
2. **Single-task n:** Only n=1 per condition per task (no within-condition variance)
3. **Non-random assignment:** Agents assigned based on availability and freshness, not randomized
4. **Contamination risk:** Multiple agents exposed to answer keys; self-reporting may be incomplete
5. **Single scorer for blinded evaluation:** Potential for systematic bias

### External Validity
1. **Task domain:** All tasks are JavaScript code review; may not generalize to other domains
2. **Agent population:** All frontier LLMs; results may differ for smaller models
3. **Institutional context:** Village agents have 400+ days of shared history; new teams might differ
4. **Structured protocol specificity:** Our Proposer→Skeptic→Synthesizer→Verifier pipeline is one possible structure

### Construct Validity
1. **Rubric measures bug-counting, not reasoning quality:** Identical scores masked real process differences
2. **Time measurement is approximate:** Based on chat timestamps, not precise instrumentation
3. **"Unstructured" still had some structure:** Agents knew they were being compared and were motivated

---

## 6. Power Analysis for Future Sessions

To detect a medium effect size (d = 0.5) between conditions:
- With n=2 per condition: Power ≈ 0.09 (very underpowered)
- With n=5 per condition: Power ≈ 0.26 (still underpowered)
- With n=20 per condition: Power ≈ 0.69 (approaching adequate)

**Reality check:** We cannot run 20 trials per condition. Our strategy should be:
1. **Increase task difficulty** to break ceiling and increase variance
2. **Use multi-dimensional scoring** (blinded qualitative) to capture richer signal
3. **Focus on large effect sizes** (d > 0.8) which need smaller samples
4. **Combine historical + experimental evidence** for triangulation

If harder tasks produce d > 1.0 differences (as our historical data suggests), then n=3-5 per condition could be sufficient.

---

## 7. Integrated Evidence Summary

Our strongest findings combine historical and experimental evidence:

| Finding | Historical Support | Experimental Support | Combined Strength |
|---------|-------------------|---------------------|-------------------|
| Validators improve outcomes | Very strong (d ≈ 1.33) | Strong (Skeptic error correction) | **Very Strong** |
| Structure > No Structure | Moderate (d ≈ 1.13, p=0.15) | Weak (ceiling effect masks it) | **Moderate** |
| Process quality differs by condition | N/A (not measured historically) | Moderate (blinded scoring, single scorer) | **Moderate** |
| Ceiling effect at current difficulty | N/A | Strong (3 ties across 2 tasks) | **Strong** |
| Role emergence accelerates with experience | Very strong (2000× over 400 days) | N/A (not tested experimentally) | **Strong (historical only)** |

**Overall narrative:** Structure's value lies in ERROR CORRECTION (catching mistakes through adversarial review), not in producing higher baseline quality. This is most visible when tasks are hard enough for initial errors to occur. At current task difficulty, all agents perform near ceiling regardless of structure.

---

**Status:** Complete for Session 2 data. Will be updated after Sessions 3-5 with harder tasks.
