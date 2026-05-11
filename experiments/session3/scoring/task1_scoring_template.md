# Session 3 Task 1 Scoring Template

**Task:** checkout + coupons (`tasks/session3_task_1/`)  
**Scorer:** [NAME]  
**Date:** [DATE]

## Seeded Issue Scoring

### Bug 1: Invalid quantity silently coerced instead of rejected (`checkout.js`)
- **Expected:** Falsy quantities such as `0` / `undefined` should not be silently coerced to `1`
- **Identified:** [ ] YES / [ ] NO
- **Fix Correct:** [ ] YES / [ ] NO
- **Points:** ___ / 100

### Bug 2: Fixed discount not capped at eligible subtotal (`checkout.js`)
- **Expected:** Clamp fixed discount to the eligible base
- **Identified:** [ ] YES / [ ] NO
- **Fix Correct:** [ ] YES / [ ] NO
- **Points:** ___ / 100

### Bug 3: Tax computed on pre-discount taxable subtotal (`checkout.js`)
- **Expected:** Compute tax from post-discount taxable merchandise
- **Identified:** [ ] YES / [ ] NO
- **Fix Correct:** [ ] YES / [ ] NO
- **Points:** ___ / 125

### Bug 4: Free shipping checked against pre-discount subtotal (`checkout.js`)
- **Expected:** Compare the correct post-discount subtotal to the free-shipping threshold
- **Identified:** [ ] YES / [ ] NO
- **Fix Correct:** [ ] YES / [ ] NO
- **Points:** ___ / 100

### Bug 5: Fixed-discount allocation can divide by zero (`coupon_utils.js`)
- **Expected:** Guard against `base <= 0` before allocation math
- **Identified:** [ ] YES / [ ] NO
- **Fix Correct:** [ ] YES / [ ] NO
- **Points:** ___ / 100

## Bonus / Higher-Order Credit

### Interaction Effects (+25)
- **Clearly documented at least one meaningful interaction:** [ ] YES / [ ] NO
- **Notes:** ___

### Test Design (+25)
- **Proposed discriminating cross-file tests:** [ ] YES / [ ] NO
- **Notes:** ___

### Ambiguity Credit (+0 to +25 discretionary)
- **Real ambiguity identified and clearly distinguished from definite defects:** ___ / 25
- **Notes:** ___

### False-Positive Deduction (-0 to -50)
- **Unsupported bug claims or misclassified non-bugs:** ___ / 50 deduction
- **Notes:** ___

## Totals

| Category | Points |
|----------|--------|
| Bug 1 | ___ / 100 |
| Bug 2 | ___ / 100 |
| Bug 3 | ___ / 125 |
| Bug 4 | ___ / 100 |
| Bug 5 | ___ / 100 |
| Interaction Bonus | ___ / 25 |
| Test Bonus | ___ / 25 |
| **Base + Standard Bonus** | ___ / 575 |
| Ambiguity Credit | ___ / 25 |
| False-Positive Deduction | -___ / 50 |
| **TOTAL** | ___ / 575 reporting max (+ up to 25 ambiguity credit) |

## Notes
[Additional scoring observations]
