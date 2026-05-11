# Session 2 Task 2 Scoring Template

**Task:** analyzeUserActivity (500 pts max + 50 bonus)
**Scorer:** [NAME]
**Date:** May 11, 2026

## Bug Scoring

### Bug 1: Assignment instead of comparison (Line 17)
- **Expected:** `records.length = 0` should be `records.length === 0`
- **Identified:** [ ] YES / [ ] NO
- **Fix Correct:** [ ] YES / [ ] NO  
- **Points:** ___ / 125

### Bug 2: Off-by-one array bounds (Line 24)
- **Expected:** `i <= records.length` should be `i < records.length`
- **Identified:** [ ] YES / [ ] NO
- **Fix Correct:** [ ] YES / [ ] NO
- **Points:** ___ / 125

### Bug 3: NaN propagation risk (Line 31)
- **Expected:** `userCounts[x] + 1 || 1` → `(userCounts[x] || 0) + 1`
- **Identified:** [ ] YES / [ ] NO (accept partial credit if noted as fragile)
- **Fix Correct:** [ ] YES / [ ] NO
- **Points:** ___ / 75

### Bug 4: Boolean sort comparator (Line 43)
- **Expected:** `a[1] > b[1]` should return numeric difference
- **Identified:** [ ] YES / [ ] NO
- **Fix Correct:** [ ] YES / [ ] NO
- **Points:** ___ / 100

### Bug 5: Arbitrary filter excludes power users (Line 47)
- **Expected:** Remove `&& u.actionCount < 100` or justify keeping it
- **Identified:** [ ] YES / [ ] NO
- **Fix Correct:** [ ] YES / [ ] NO
- **Points:** ___ / 75

## Bonus Points

### Interaction Effects (+25)
- **Identified bug interactions:** [ ] YES / [ ] NO
- **Description:** ___

### Test Cases (+25)
- **Suggested comprehensive tests:** [ ] YES / [ ] NO
- **Description:** ___

## Total Score

| Category | Points |
|----------|--------|
| Bug 1 | ___ / 125 |
| Bug 2 | ___ / 125 |
| Bug 3 | ___ / 75 |
| Bug 4 | ___ / 100 |
| Bug 5 | ___ / 75 |
| Bonus | ___ / 50 |
| **TOTAL** | ___ / 550 |

## Notes
[Additional observations about the submission]
