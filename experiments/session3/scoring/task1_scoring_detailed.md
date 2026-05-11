# Session 3 Task 1 — Detailed Scoring Template (with Qualitative Notes)

**Scorer:** ________________________
**Date:** ________________________
**Condition:** [ ] Solo / [ ] Unstructured Pair / [ ] Structured Quad
**Participant(s):** ________________________
**Wall-clock Time:** ________ minutes

---

## Bug Detection (500 pts max)

### Bug 1: Invalid quantity silently coerced to 1 (checkout.js)
- [ ] **Found** (75 pts): Identified that `quantity || 1` allows invalid/falsy values
- [ ] **Fixed** (+25 pts): Proposed explicit validation + throw for non-positive/non-integer
- **Notes:** ________________________
- **Subtotal:** ___/100

### Bug 2: Fixed discounts not capped at eligible subtotal (checkout.js)
- [ ] **Found** (75 pts): Identified uncapped `discountCents = coupon.amountOffCents`
- [ ] **Fixed** (+25 pts): Proposed `Math.min(coupon.amountOffCents, eligibleBase)` or equivalent
- **Notes:** ________________________
- **Subtotal:** ___/100

### Bug 3: Tax computed on pre-discount subtotal (checkout.js) - CRITICAL
- [ ] **Found** (100 pts): Identified tax uses pre-discount taxable amount
- [ ] **Fixed** (+25 pts): Proposed computing taxable from discounted per-item amounts
- **Notes:** ________________________
- **Subtotal:** ___/125

### Bug 4: Free shipping uses wrong subtotal (checkout.js)
- [ ] **Found** (75 pts): Identified threshold comparison uses pre-discount subtotal
- [ ] **Fixed** (+25 pts): Proposed comparing post-discount subtotal to threshold
- **Notes:** ________________________
- **Subtotal:** ___/100

### Bug 5: Divide-by-zero in allocation (coupon_utils.js)
- [ ] **Found** (75 pts): Identified division when `base === 0` in allocation
- [ ] **Fixed** (+25 pts): Proposed short-circuit or validation when no eligible items
- **Notes:** ________________________
- **Subtotal:** ___/100

**Bug Detection Total:** ___/500

---

## Bonuses (75 pts max + 25 discretionary)

### Interaction Bonus (+25 pts)
- [ ] **Awarded**: Clearly explained meaningful bug interaction(s)
- Examples that qualify:
  - Bug 2 + Bug 3: uncapped discount + pre-discount tax = negative/implausible totals
  - Bug 2 + Bug 4: oversized coupon + wrong threshold = inconsistent shipping
  - Bug 5 + Bug 3: failed allocation corrupts tax computation
- **Interaction(s) identified:** ________________________
- **Subtotal:** ___/25

### Test-Design Bonus (+25 pts)
- [ ] **Awarded**: Proposed discriminating tests for cross-file failures
- **Test approach described:** ________________________
- **Subtotal:** ___/25

### Ambiguity Credit (+0-25 discretionary)
- [ ] **Awarded**: Thoughtfully discussed genuine ambiguity (e.g., rounding policy)
- Must distinguish real ambiguity from seeded defects
- **Ambiguity discussed:** ________________________
- **Subtotal:** ___/25

**Bonus Total:** ___/75 (+___/25 discretionary)

---

## False Positives (up to -50 pts)

**Non-bugs (do NOT deduct for these):**
- `scope: "nonFood"` applying to books (spec defines nonFood as "not food")
- Dollar-denominated outputs via `Number((value / 100).toFixed(2))`

| False Positive Claimed | Deduction (-25 each, max -50) |
|------------------------|-------------------------------|
| 1. ________________________ | _____ |
| 2. ________________________ | _____ |

**False Positive Total:** ___/-50

---

## Final Score Calculation

| Component | Points |
|-----------|--------|
| Bug Detection | ___/500 |
| Bonuses | ___/75 |
| Ambiguity (discretionary) | ___/25 |
| False Positives | ___/-50 |
| **TOTAL** | **___/575** |

---

## Qualitative Notes

### Strengths observed:
________________________

### Weaknesses observed:
________________________

### Collaboration quality (for Pair/Quad only):
________________________

### Error correction events (for Structured only):
________________________

---

**Scoring complete:** [ ] Yes
**Scorer signature:** ________________________
