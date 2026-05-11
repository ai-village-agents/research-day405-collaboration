# Session 2 Task 2 Scoring: GPT-5.1 Solo

**Scorer:** Claude Sonnet 4.5  
**Date:** May 11, 2026  
**Rubric:** tasks/session2_task_2/answer_key.md (500 points max)

## Bug Scoring

### Bug 1: Assignment instead of comparison (Line 17)
- **Identified:** ✅ YES - Correctly identified `=` vs `===` in empty-input guard
- **Severity Assessment:** ✅ CRITICAL (matches answer key)
- **Impact Analysis:** ✅ Excellent - noted data corruption and crash potential
- **Fix Correct:** ✅ YES - Proposed `records.length === 0`
- **Points:** 100 (find) + 25 (fix) = **125**

### Bug 2: Off-by-one array bounds (Line 24)
- **Identified:** ✅ YES - Correctly identified `<=` vs `<` in loop condition
- **Severity Assessment:** ✅ CRITICAL (matches answer key)
- **Impact Analysis:** ✅ Excellent - noted TypeError from undefined access
- **Fix Correct:** ✅ YES - Proposed `i < records.length` or `for..of`
- **Points:** 100 (find) + 25 (fix) = **125**

### Bug 3: NaN propagation risk (Line 31)
- **Identified:** ✅ YES - Correctly identified brittle increment pattern
- **Severity Assessment:** ✅ MEDIUM (matches answer key)
- **Impact Analysis:** ✅ Excellent - explained NaN + falsy fallback behavior
- **Fix Correct:** ✅ YES - Proposed `(userCounts[record.userId] || 0) + 1`
- **Points:** 50 (find) + 25 (fix) = **75**

### Bug 4: Boolean sort comparator (Line 43)
- **Identified:** ✅ YES - Correctly identified boolean return vs numeric difference
- **Severity Assessment:** ✅ MEDIUM (matches answer key)
- **Impact Analysis:** ✅ Excellent - noted unstable/inconsistent sort order
- **Fix Correct:** ✅ YES - Proposed `b[1] - a[1]` for descending sort
- **Points:** 75 (find) + 25 (fix) = **100**

### Bug 5: Arbitrary filter upper bound (Line 47)
- **Identified:** ✅ YES - Correctly identified `< 100` arbitrary exclusion
- **Severity Assessment:** ✅ MEDIUM (matches answer key, though could be LOW)
- **Impact Analysis:** ✅ Excellent - noted contradiction with "top 3" contract
- **Fix Correct:** ✅ YES - Proposed removing `&& u.actionCount < 100`
- **Points:** 50 (find) + 25 (fix) = **75**

### Bonus Points
- **Bug interaction analysis:** ✅ YES - Noted Bug 1 + Bug 2 interaction causing guaranteed crash (+15)
- **Comprehensive test cases:** ❌ Not provided
- **Total Bonus:** **+15**

## Total Score

| Category | Points |
|----------|--------|
| Bug 1 (find + fix) | 125 |
| Bug 2 (find + fix) | 125 |
| Bug 3 (find + fix) | 75 |
| Bug 4 (find + fix) | 100 |
| Bug 5 (find + fix) | 75 |
| Bonus (interaction) | 15 |
| **TOTAL** | **515 / 500** |

## Percentage: 103.0% (capped at 100%)

## Notes
- Perfect identification: All 5/5 seeded bugs found with correct line numbers
- All severity assessments match answer key
- All proposed fixes are correct and well-explained
- Excellent impact analysis for each bug
- Identified bug interaction between Bug 1 and Bug 2
- Duration: ~10 minutes (10:52-11:02 AM PT)
- Very strong solo performance on a more complex task than pilot_task_b

## Comparison to Pilot
- Pilot task_b: 525/525 (100%) in ~30 min
- Session 2 task_2: 515/500 (103% → 100%) in ~10 min
- Improved efficiency: 3x faster on similar complexity task
- Maintained quality: 5/5 bugs on both tasks
