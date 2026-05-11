# Session 2 Task 2 — Answer Key

**Task:** `tasks/session2_task_2/task.js` (analyzeUserActivity function)

## Seeded Issues (5 total)

### Bug 1: Assignment instead of comparison (Line 17)
- **Location:** `if (!records || records.length = 0)`
- **Issue:** Uses `=` (assignment) instead of `===` (comparison)
- **Severity:** CRITICAL
- **Impact:** Mutates records.length to 0, always returns empty result
- **Fix:** Change `=` to `===`
- **Points:** 100 (find) + 25 (correct fix)

### Bug 2: Off-by-one array bounds (Line 24)
- **Location:** `for (let i = 0; i <= records.length; i++)`
- **Issue:** Uses `<=` instead of `<`, accessing undefined element
- **Severity:** CRITICAL  
- **Impact:** Causes TypeError when accessing record.userId on undefined
- **Fix:** Change `<=` to `<`
- **Points:** 100 (find) + 25 (correct fix)

### Bug 3: NaN propagation risk (Line 31)
- **Location:** `userCounts[record.userId] = userCounts[record.userId] + 1 || 1`
- **Issue:** `undefined + 1` = NaN, relies on || 1 fallback
- **Severity:** MEDIUM
- **Impact:** Works but fragile pattern
- **Better pattern:** `(userCounts[record.userId] || 0) + 1`
- **Points:** 50 (find) + 25 (correct fix)

### Bug 4: Boolean sort comparator (Line 43)
- **Location:** `.sort((a, b) => a[1] > b[1])`
- **Issue:** Returns boolean instead of numeric difference
- **Severity:** MEDIUM
- **Impact:** Inconsistent sort order
- **Fix:** Change to `(a, b) => b[1] - a[1]`
- **Points:** 75 (find) + 25 (correct fix)

### Bug 5: Arbitrary filter excludes valid users (Line 47)
- **Location:** `u.actionCount > 5 && u.actionCount < 100`
- **Issue:** Upper bound arbitrarily excludes power users
- **Severity:** LOW
- **Impact:** Top users with 100+ actions filtered out
- **Fix:** Remove `&& u.actionCount < 100`
- **Points:** 50 (find) + 25 (correct fix)

## Scoring

| Bug | Find | Fix | Total |
|-----|------|-----|-------|
| Bug 1 (assignment) | 100 | 25 | 125 |
| Bug 2 (off-by-one) | 100 | 25 | 125 |
| Bug 3 (NaN pattern) | 50 | 25 | 75 |
| Bug 4 (boolean sort) | 75 | 25 | 100 |
| Bug 5 (arbitrary filter) | 50 | 25 | 75 |
| **Total** | **375** | **125** | **500** |

### Bonus Points (up to 50)
- +25: Identifying interaction effects between bugs
- +25: Suggesting comprehensive test cases
