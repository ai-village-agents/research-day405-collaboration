# Checkout System Spec (Session 3 Task 1)

## Inputs
- `cart.items`: array of `{ name, category, quantity, unitPriceCents }`
- `config`: `{ taxRate, shippingCents, freeShippingThresholdCents }`
- `coupon` (optional):
  - `{ type: "percent", percentOff, scope: "all" | "nonFood" }`
  - `{ type: "fixed", amountOffCents, scope: "all" | "nonFood" }`

## Rules
1. `quantity` must be a positive integer. Invalid input should **throw**, not silently coerce.
2. Categories `food` and `book` are non-taxable. All other categories are taxable.
3. `scope: "nonFood"` means the coupon applies to any item whose category is **not** `food`.
4. Tax is computed on the **post-discount taxable subtotal**.
5. Free shipping applies when the **post-discount merchandise subtotal** is **greater than or equal to** `freeShippingThresholdCents`.
6. Fixed discounts may not reduce the eligible subtotal below zero.
7. Output fields should be returned in dollars rounded to 2 decimals.

## Notes
- You may discuss possible rounding edge cases if relevant.
- If you believe the spec itself leaves something important underspecified, explain that explicitly rather than forcing certainty.
