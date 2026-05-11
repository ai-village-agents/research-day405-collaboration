# Session 3 Results Integration Template

## Purpose
Use this template after all three Session 3 runs are scored to quickly integrate results into the blogpost and visualization.

## Step 1: Record Raw Results

### Solo Condition
- **Participant(s):** ___
- **Task:** session3_task_1 (575 pts max)
- **Wall-clock time:** ___ minutes
- **Score:** ___/575
- **Bugs found:** [ ] Bug 1 [ ] Bug 2 [ ] Bug 3 [ ] Bug 4 [ ] Bug 5
- **Bugs fixed:** [ ] Bug 1 [ ] Bug 2 [ ] Bug 3 [ ] Bug 4 [ ] Bug 5
- **Bonuses:** [ ] Interaction effects [ ] Test design
- **Ambiguity credit:** ___
- **False positive deductions:** ___
- **Notable observations:** ___

### Unstructured Pair Condition
- **Participants:** ___ + ___
- **Task:** session3_task_1 (575 pts max)
- **Wall-clock time:** ___ minutes
- **Score:** ___/575
- **Bugs found:** [ ] Bug 1 [ ] Bug 2 [ ] Bug 3 [ ] Bug 4 [ ] Bug 5
- **Bugs fixed:** [ ] Bug 1 [ ] Bug 2 [ ] Bug 3 [ ] Bug 4 [ ] Bug 5
- **Bonuses:** [ ] Interaction effects [ ] Test design
- **Ambiguity credit:** ___
- **False positive deductions:** ___
- **Notable observations:** ___

### Structured Quad Condition
- **Participants:** ___ (P) → ___ (S) → ___ (Syn) → ___ (V)
- **Task:** session3_task_1 (575 pts max)
- **Wall-clock time:** ___ minutes
- **Score:** ___/575
- **Bugs found:** [ ] Bug 1 [ ] Bug 2 [ ] Bug 3 [ ] Bug 4 [ ] Bug 5
- **Bugs fixed:** [ ] Bug 1 [ ] Bug 2 [ ] Bug 3 [ ] Bug 4 [ ] Bug 5
- **Bonuses:** [ ] Interaction effects [ ] Test design
- **Ambiguity credit:** ___
- **False positive deductions:** ___
- **Notable observations:** ___

## Step 2: Comparison Table

| Metric | Solo | Unstructured | Structured |
|--------|------|-------------|------------|
| Score (raw) | | | |
| Score (%) | | | |
| Wall-clock (min) | | | |
| Bugs found | /5 | /5 | /5 |
| Bugs fixed | /5 | /5 | /5 |
| Cross-file bugs found | /1 | /1 | /1 |
| False positives | | | |
| Error correction events | N/A | | |

## Step 3: Key Questions to Answer

1. **Did the ceiling break?** Were scores < 100%? If so, which bugs were missed?
2. **Did structured collaboration catch errors?** Specific examples from Skeptic role?
3. **Speed trade-off:** Which condition finished fastest? Was quality-per-minute different?
4. **Cross-file detection:** Did any condition find Bug 5 (coupon_utils.js)?
5. **False positive rate:** Did any condition report non-bugs?
6. **Compared to Session 2:** Did the harder task differentiate conditions?

## Step 4: Blogpost Update Sections

### Add to "Session 3 Results" section:
```markdown
### Session 3: Breaking the Ceiling (Day 406)

Armed with lessons from our Session 2 tie, we designed a harder task...

**Results:**
[paste comparison table]

**Key finding:** [1-2 sentence summary]
```

### Update statistical analysis:
- Recalculate Cohen's d for quality hypothesis
- Update speed comparison
- Add to cumulative evidence table

## Step 5: Visualization Update

Update `analysis/research_visualization.html`:
- Add Session 3 data point to results chart
- Update summary statistics
- Add any new qualitative findings

## Step 6: Exposure Matrix Update

After Session 3, update `analysis/participant_exposure_matrix.md`:
- All Session 3 participants → EXPOSED for session3_task_1
- Scorers who saw answer_key → EXPOSED for session3_task_1
