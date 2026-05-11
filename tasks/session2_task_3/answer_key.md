# Session 2 Task 3 — Answer Key

**Task:** `tasks/session2_task_3/task.js` (calculateCartTotal function)

## Seeded Issues (5 total)

### Bug 1: Loose equality (Line 12)
- **Location:** `if (!items || items.length == 0)`
- **Issue:** Uses `==` instead of `===`
- **Severity:** LOW
- **Impact:** Type coercion could cause unexpected behavior
- **Fix:** Change `==` to `===`
- **Points:** 50 (find) + 25 (correct fix)

### Bug 2: Assignment instead of comparison (Line 29)
- **Location:** `else if (config.discountCode = "HALFOFF")`
- **Issue:** Uses `=` (assignment) instead of `===` (comparison)
- **Severity:** CRITICAL
- **Impact:** Always applies 50% discount, mutates config object
- **Fix:** Change `=` to `===`
- **Points:** 100 (find) + 25 (correct fix)

### Bug 3: Off-by-one array bounds (Line 36)
- **Location:** `for (let i = 0; i <= items.length; i++)`
- **Issue:** Uses `<=` instead of `<`
- **Severity:** CRITICAL
- **Impact:** TypeError accessing undefined item
- **Fix:** Change `<=` to `<`
- **Points:** 100 (find) + 25 (correct fix)

### Bug 4: Incorrect threshold comparison (Line 43)
- **Location:** `if (discountedSubtotal > config.freeShippingThreshold)`
- **Issue:** Uses `>` instead of `>=`
- **Severity:** MEDIUM
- **Impact:** Edge case: exact threshold amount doesn't get free shipping
- **Fix:** Change `>` to `>=`
- **Points:** 75 (find) + 25 (correct fix)

### Bug 5: Inconsistent rounding (Line 50)
- **Location:** `discount: discountAmount,` (not rounded)
- **Issue:** discount not rounded while other values are
- **Severity:** LOW
- **Impact:** Inconsistent decimal places in output
- **Fix:** `discount: Math.round(discountAmount * 100) / 100,`
- **Points:** 50 (find) + 25 (correct fix)

## Scoring

| Bug | Find | Fix | Total |
|-----|------|-----|-------|
| Bug 1 (loose equality) | 50 | 25 | 75 |
| Bug 2 (assignment) | 100 | 25 | 125 |
| Bug 3 (off-by-one) | 100 | 25 | 125 |
| Bug 4 (threshold) | 75 | 25 | 100 |
| Bug 5 (rounding) | 50 | 25 | 75 |
| **Total** | **375** | **125** | **500** |

### Bonus Points (up to 50)
- +25: Bug interaction effects (bugs 2+3 cascade)
- +25: Comprehensive test suggestions
