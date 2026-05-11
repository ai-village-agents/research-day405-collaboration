# Session 3 Task 1 — Answer Key

**Task files:**
- `tasks/session3_task_1/checkout.js`
- `tasks/session3_task_1/coupon_utils.js`
- `tasks/session3_task_1/spec.md`

## Seeded Issues (5 total)

### Bug 1: Invalid quantity is silently coerced instead of rejected
- **Location:** `checkout.js`
- **Code:** `quantity: item.quantity || 1` and `lineSubtotalCents: item.unitPriceCents * (item.quantity || 1)`
- **Issue:** Violates spec rule 1. Invalid values such as `0`, `undefined`, or other falsy quantities are silently converted to `1` instead of throwing.
- **Severity:** HIGH
- **Impact:** Bad input can produce plausible-but-wrong totals, masking upstream data errors.
- **Fix:** Validate `quantity` explicitly and throw for non-positive / non-integer values.
- **Points:** 75 (find) + 25 (fix)

### Bug 2: Fixed discounts are not capped at the eligible subtotal
- **Location:** `checkout.js`
- **Code:** `discountCents = coupon.amountOffCents;`
- **Issue:** Violates spec rule 6. A fixed coupon can exceed the eligible base and drive totals below zero.
- **Severity:** HIGH
- **Impact:** Over-discounting, negative totals, and inconsistent downstream allocations.
- **Fix:** Clamp to `Math.min(coupon.amountOffCents, eligibleBase)`.
- **Points:** 75 (find) + 25 (fix)

### Bug 3: Tax is computed on the pre-discount taxable subtotal
- **Location:** `checkout.js`
- **Code:** taxable subtotal is derived from `items`, not `discountedItems`
- **Issue:** Violates spec rule 4. Tax should be computed on post-discount taxable merchandise.
- **Severity:** CRITICAL
- **Impact:** Tax is overstated whenever a taxable item receives a discount.
- **Fix:** Compute taxable subtotal from discounted per-item amounts, e.g. `lineSubtotalCents - allocatedDiscountCents` for taxable items.
- **Points:** 100 (find) + 25 (fix)

### Bug 4: Free shipping is checked against pre-discount subtotal instead of post-discount subtotal
- **Location:** `checkout.js`
- **Code:** `const shippingCents = subtotalCents >= config.freeShippingThresholdCents ? 0 : config.shippingCents;`
- **Issue:** Violates spec rule 5.
- **Severity:** MEDIUM
- **Impact:** Orders can receive free shipping when discounts should have dropped them below threshold.
- **Fix:** Compare `subtotalCents - discountCents` (or another correctly defined post-discount merchandise subtotal) to the threshold.
- **Points:** 75 (find) + 25 (fix)

### Bug 5: Fixed-discount allocation can divide by zero when the coupon has no eligible items
- **Location:** `coupon_utils.js`
- **Code:** `const share = Math.round((item.lineSubtotalCents / base) * discountCents);`
- **Issue:** If `base === 0`, the allocator computes invalid shares.
- **Severity:** HIGH
- **Impact:** `NaN` / `Infinity` propagation or nonsensical allocations when a coupon is present but no item is eligible.
- **Fix:** Short-circuit when `base <= 0`, or validate coupon applicability earlier and return zero allocation.
- **Points:** 75 (find) + 25 (fix)

## Bonus / Higher-Order Credit

### Interaction bonus (+25)
Award if the participant clearly explains at least one meaningful interaction, such as:
- Bug 2 + Bug 3: uncapped discount plus pre-discount tax can produce simultaneously negative or implausible totals and overstated tax.
- Bug 2 + Bug 4: an oversized fixed coupon can create free-shipping decisions inconsistent with the spec if threshold logic is based on the wrong subtotal.
- Bug 5 + Bug 3: failed allocation logic can make any tax-after-discount computation impossible or corrupted.

### Test-design bonus (+25)
Award if the participant proposes discriminating tests that would catch cross-file failures, not just local syntax issues.

### Ambiguity credit (+0 to +25 discretionary)
There is room for thoughtful discussion about rounding/allocation policy across line items. This should **not** replace identifying the seeded bugs, but it can earn extra credit if the participant clearly distinguishes a real ambiguity from a definite defect.

## False-Positive Guidance

This task intentionally includes some lines that may look suspicious but are not seeded defects on their own.
Examples of **non-bugs by themselves**:
- `scope: "nonFood"` applying to `book` items (the spec defines `nonFood` as “not food,” so books remain eligible)
- returning dollar-denominated outputs via `Number((value / 100).toFixed(2))`

Participants should not receive extra credit for inventing unsupported problems.

## Scoring Summary

| Component | Max |
|-----------|-----|
| 5 seeded issues | 500 |
| Interaction bonus | 25 |
| Test-design bonus | 25 |
| Ambiguity credit | 25 |
| False-positive deduction budget | -50 |
| **Recommended reporting max** | **550 + up to 25 discretionary ambiguity credit** |
