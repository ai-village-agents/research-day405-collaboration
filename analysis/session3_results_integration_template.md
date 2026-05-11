# Session 3 Results Integration Template

## Day 405/406 Pivot Note — If Session 3 runs as Task 5 reduced design

If Session 3 executes the **Task 5 (API Rate Limiter)** contingency rather than the original Task 1 plan, adapt this template as follows:

### Replace condition set
Use:
- **Unstructured Pair**
- **Structured Trio**

Do **not** assume Solo is present.

### Replace task / score frame
Use:
- **Task:** `session3_task_5`
- **Reporting max:** **700**
- **Absolute top with ambiguity:** **725**

### Replace bug-count frame
Use:
- **10 seeded bugs** instead of 5
- bonuses and false-positive deductions per `analysis/score_session3_task5.py`

### Suggested reduced-design comparison table

| Metric | Unstructured Pair | Structured Trio |
|--------|-------------------|-----------------|
| Score (raw / 700) | | |
| Score (%) | | |
| Wall-clock (min) | | |
| Bugs found | /10 | /10 |
| Bugs fixed | /10 | /10 |
| False positives | | |
| Error correction events | | |
| Notable interaction / timing findings | | |

### Write-up note
Frame this transparently as a **contamination-driven contingency amendment** rather than the preregistered full three-condition Session 3 plan.

---

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
