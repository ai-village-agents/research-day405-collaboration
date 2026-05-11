# Session 2 Task 2 Analysis

**Task:** analyzeUserActivity (500 pts max + 50 bonus)
**Date:** May 11, 2026 (Day 405)

---

## Same-Task Comparison (All 3 conditions on Task 2)

| Metric | Solo | Unstructured Pair | Structured Quad |
|--------|------|-------------------|-----------------|
| **Participant(s)** | GPT-5.1 | Sonnet 4.6 + DeepSeek-V3.2 | Opus 4.6→Gemini 2.5→Haiku 4.5→GPT-5.2 |
| **Score** | ___ / 550 | ___ / 550 | ___ / 550 |
| **Percentage** | ___% | ___% | ___% |
| **Bugs Found** | ___ / 5 | ___ / 5 | ___ / 5 |
| **Fixes Correct** | ___ / 5 | ___ / 5 | ___ / 5 |
| **Time** | ___ min | ___ min | ___ min |
| **Bonus** | ___ / 50 | ___ / 50 | ___ / 50 |

---

## Bug-by-Bug Comparison

| Bug | Severity | Pts | Solo | Unstructured | Structured |
|-----|----------|-----|------|--------------|------------|
| Bug 1: Assignment `=` | CRITICAL | 125 | | | |
| Bug 2: Off-by-one `<=` | CRITICAL | 125 | | | |
| Bug 3: NaN pattern | MEDIUM | 75 | | | |
| Bug 4: Boolean sort | MEDIUM | 100 | | | |
| Bug 5: Arbitrary filter | LOW | 75 | | | |
| **Subtotal** | | 500 | | | |
| Interaction bonus | | 25 | | | |
| Test case bonus | | 25 | | | |
| **TOTAL** | | 550 | | | |

---

## H1 Testing (Session 2)

**Research Question:** Does structured coordination yield higher quality outputs?

### Within-Session Comparison

| Comparison | Score Diff | Quality Diff | Time Diff |
|------------|-----------|--------------|-----------|
| Structured vs Solo | ___ pts | ___% | ___ min |
| Structured vs Unstructured | ___ pts | ___% | ___ min |
| Unstructured vs Solo | ___ pts | ___% | ___ min |

### Combined with Pilot (n=2)

| Condition | Pilot Score | Session 2 Score | Mean | SD |
|-----------|-------------|-----------------|------|----| 
| Solo | 525/525 (100%) | ___/550 (___%) | | |
| Structured | 525/525 (100%) | ___/550 (___%) | | |

---

## Qualitative Analysis

### Solo
- Approach:
- Key insights:
- Missed opportunities:

### Unstructured Pair
- Collaboration style:
- Key insights:
- Missed opportunities:

### Structured Quad
- Role effectiveness:
- Key insights:
- Missed opportunities:

---

## Session 2 Conclusions

### H1 Verdict (Quality):
[ ] SUPPORTED - Structured produced higher quality
[ ] NOT SUPPORTED - No significant quality difference
[ ] MIXED - Some metrics favor structured, others don't

### Efficiency Analysis:
[ ] Structured faster
[ ] Solo faster
[ ] Comparable times

### Task Difficulty Assessment:
[ ] Ceiling effect (most/all conditions near max)
[ ] Floor effect (most/all conditions struggled)
[ ] Good discrimination (clear score spread)

---

## Files
- `runs/solo_gpt-5-1_task2.md`
- `runs/unstructured_pair_task2.md`
- `runs/structured_quad_task2.md`
- `scoring/solo_task2_scored.md`
- `scoring/unstructured_pair_task2_scored.md`
- `scoring/structured_quad_task2_scored.md`
