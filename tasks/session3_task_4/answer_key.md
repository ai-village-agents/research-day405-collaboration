# Task 4: Answer Key (SCORERS ONLY — DO NOT SHARE WITH PARTICIPANTS)

## Bug Summary Table

| # | File | Bug | Tier | Points | Category |
|---|------|-----|------|--------|----------|
| 1 | inventory.js | Off-by-one in reserveItems loop | Easy | 50 | Logic |
| 2 | order.js | Missing `await` on reserveItems | Easy | 50 | Async |
| 3 | order.js | Loose equality in cancelOrder filter | Easy | 50 | Type Safety |
| 4 | inventory.js | Race condition in reserveItems (no real locking) | Hard | 100 | Concurrency |
| 5 | pricing.js | Discount stacking order violates spec (% before flat) | Medium | 75 | Spec Violation |
| 6 | pricing.js | Floating-point arithmetic without rounding | Medium | 75 | Numerical |
| 7 | pricing.js | Tax calculated on pre-discount amount | Medium | 75 | Logic |
| 8 | inventory.js | getInventorySummary leaks internal state reference | Hard | 100 | Data Integrity |
| 9 | order.js | validateOrder uses some() instead of every() | Hard | 75 | Logic |
| 10 | order.js | JSON deep copy strips undefined values | Hard | 75 | Data Loss |

**Base Total: 725 points**
**Bonuses: Up to 100 points (cross-file interaction +50, test cases +50)**
**False Positive Penalty: -25 each**
**Maximum Score: 825 points** (but target is 800; overshoot possible)

NOTE: Adjusted scoring - max reported as 800 in spec. Score = min(sum_of_found_bugs + bonuses - penalties, 800).

---

## Detailed Bug Descriptions

### Bug 1: Off-by-one in reserveItems loop (EASY, 50 pts)
**File:** `inventory.js`, line ~68
**Code:** `for (let i = 0; i <= items.length; i++)`
**Issue:** Uses `<=` instead of `<`. On the last iteration, `items[items.length]` is `undefined`, causing `item.productId` to throw TypeError.
**Fix:** `for (let i = 0; i < items.length; i++)`
**Impact:** Function crashes when called with any non-empty items array.

### Bug 2: Missing await on reserveItems (EASY, 50 pts)
**File:** `order.js`, line ~99
**Code:** `const reservation = this.inventory.reserveItems(orderId, items);`
**Issue:** `reserveItems` is `async` but the call doesn't use `await`. `reservation` will be a Promise object, which is always truthy. The `!reservation.success` check evaluates `!undefined` which is `true`, so orders will always fail at the inventory stage (counterintuitively, because `reservation.success` is `undefined`, not `false`).
**Fix:** `const reservation = await this.inventory.reserveItems(orderId, items);`
**Impact:** All orders fail at inventory stage because `reservation.success` is undefined (Promise doesn't have a `.success` property).

**INTERACTION NOTE:** Bug 2 actually MASKS Bug 1. Since reservation is a Promise (not awaited), the code never actually executes the loop in `reserveItems` synchronously before checking the result. If Bug 2 is fixed but Bug 1 is not, the function will crash. If Bug 1 is fixed but Bug 2 is not, orders still fail.

### Bug 3: Loose equality in cancelOrder (EASY, 50 pts)
**File:** `order.js`, line ~149
**Code:** `this.processedOrders.filter(o => o.orderId != orderId)`
**Issue:** Uses `!=` (loose inequality) instead of `!==` (strict inequality). With loose equality, `"123" != 123` is `false`, meaning string and number orderIds will be treated as equal. This can cause unexpected cancellations if orderId types are inconsistent between creation and cancellation.
**Fix:** `this.processedOrders.filter(o => o.orderId !== orderId)`
**Impact:** Potential for incorrect order cancellation when orderId types are mixed (string vs number). In practice, if orderIds are always the same type, this bug is silent.

### Bug 4: Race condition in reserveItems (HARD, 100 pts)
**File:** `inventory.js`, lines ~62-67
**Code:** `reservationLocks` object is set but never checked. No mutex or semaphore.
**Issue:** Two concurrent calls to `reserveItems` can both read available stock as sufficient, both succeed, and collectively over-reserve beyond actual stock. The `reservationLocks` object exists as a red herring — it's populated but never used as a gate.
**Fix:** Implement actual locking:
```javascript
async reserveItems(orderId, items) {
  if (this.reservationLocks[orderId]) {
    return { success: false, error: 'Reservation in progress' };
  }
  this.reservationLocks[orderId] = true;
  try {
    // ... existing logic with await-based atomic check-and-reserve
  } finally {
    delete this.reservationLocks[orderId];
  }
}
```
Or use a proper mutex library for concurrent access.
**Impact:** Inventory can be over-sold in concurrent scenarios.

### Bug 5: Discount stacking order violates spec (MEDIUM, 75 pts)
**File:** `pricing.js`, lines ~78-82
**Code:** Sort puts percentage first, then flat.
**Issue:** Specification says "Apply flat discounts FIRST, then percentage discounts on the reduced amount." But the sort comparator places percentage discounts before flat discounts (returns -1 when a is percentage and b is flat).
**Fix:** Reverse the sort:
```javascript
const sortedDiscounts = discounts.sort((a, b) => {
  if (a.type === 'flat' && b.type === 'percentage') return -1;
  if (a.type === 'percentage' && b.type === 'flat') return 1;
  return 0;
});
```
**Impact:** Customers get a different (usually smaller) discount than specified. Example: On a $100 order with $10 flat + 20% off:
- Correct (flat first): $100 - $10 = $90, then 20% off = $72
- Buggy (% first): $100 * 0.8 = $80, then - $10 = $70

### Bug 6: Floating-point arithmetic (MEDIUM, 75 pts)
**File:** `pricing.js`, throughout calculateOrderTotal
**Issue:** Financial calculations use raw floating-point arithmetic without rounding. Example: `0.1 + 0.2 = 0.30000000000000004` in JavaScript.
**Fix:** Round to cents at each calculation step:
```javascript
const roundToCents = (n) => Math.round(n * 100) / 100;
// Apply throughout: lineTotal = roundToCents(product.basePrice * item.quantity);
```
**Impact:** Order totals may have tiny floating-point errors that accumulate, causing display issues and accounting discrepancies.

### Bug 7: Tax on pre-discount amount (MEDIUM, 75 pts)
**File:** `pricing.js`, line ~102
**Code:** `const tax = (subtotal + surchargeAmount) * 0.08;`
**Issue:** Tax is calculated on the pre-discount subtotal + surcharge, not on the final discounted amount. The variable `discountedSubtotal` exists and should be used instead.
**Fix:** `const tax = discountedSubtotal * 0.08;`
**Impact:** Customers are overcharged on tax. The tax should apply to what they actually pay, not the original price before discounts.

### Bug 8: Internal state leak via getInventorySummary (HARD, 100 pts)
**File:** `inventory.js`, line ~129
**Code:** `_stockRef: this.stock` in the summary object
**Issue:** The summary object includes a direct reference to the internal `this.stock` object. Any code that receives the summary can mutate `_stockRef` and directly modify the inventory's internal state. This is a cross-file concern: `pricing.js` receives this summary and could inadvertently (or maliciously) modify inventory data.
**Fix:** Remove the `_stockRef` field entirely, or deep-copy the stock:
```javascript
// Remove this line:
_stockRef: this.stock
```
**Impact:** External code can bypass the inventory API and directly modify stock levels. In the current codebase, `pricing.js` reads the summary for surge pricing, creating a potential cross-file mutation path.

### Bug 9: validateOrder uses some() instead of every() (HARD, 75 pts)
**File:** `order.js`, line ~51
**Code:** `const allValid = items.some(item => { ... });`
**Issue:** `Array.some()` returns true if ANY callback returns true. For validation, we need `Array.every()` which returns true only if ALL callbacks return true. As written, an order with 1 valid item and 5 invalid items passes validation.
**Fix:** `const allValid = items.every(item => { ... });`
**Impact:** Invalid orders can pass validation if at least one item is valid. Combined with the errors array check (`errors.length === 0`), this partially mitigates the issue since errors ARE accumulated, but the `allValid` variable is misleadingly named and logically wrong.

**SUBTLETY:** The `&& errors.length === 0` secondary check partially masks this bug. If some() returns true (at least one valid item) AND some invalid items pushed errors, then `allValid && errors.length === 0` = `true && false` = `false`, correctly rejecting. But if there's exactly one valid item and no invalid items trigger error pushes (e.g., items with valid productId and quantity but non-integer quantity that the check misses), the bug manifests.

### Bug 10: JSON deep copy strips undefined values (HARD, 75 pts)
**File:** `order.js`, line ~115
**Code:** `JSON.parse(JSON.stringify({ ... items, ... }))`
**Issue:** `JSON.stringify()` silently drops properties with `undefined` values. If any cart item has `metadata: undefined` (explicitly set), the property disappears from the stored order record. Code that later checks `if ('metadata' in item)` will get `false` instead of `true`.
**Fix:** Use a deep copy method that preserves undefined:
```javascript
const orderRecord = structuredClone({ orderId, customerId, items, ... });
```
Or use a custom deep copy function.
**Impact:** Silent data loss. Optional fields set to `undefined` are stripped from order records, potentially breaking downstream logic that distinguishes "field absent" from "field present but undefined."

---

## Cross-File Interaction Effects (Bonus: +50 pts)

### Interaction 1: Bug 2 masks Bug 1
Missing await (Bug 2) prevents the loop in reserveItems from executing before the result is checked. If Bug 2 is fixed, Bug 1 immediately causes a crash.

### Interaction 2: Bug 8 enables cross-file state mutation
The `_stockRef` leak (Bug 8) means any code receiving the inventory summary (including pricing.js) can modify internal inventory state. Combined with surge pricing logic in pricing.js, this creates a pathway for unintended inventory modifications.

### Interaction 3: Bug 5 + Bug 7 compound overcharging
Discount stacking order (Bug 5) changes the discounted subtotal, and tax on pre-discount amount (Bug 7) ignores discounts entirely. Together, customers are hit twice: wrong discount calculation AND tax on the wrong base.

### Interaction 4: Bug 9 + Bug 2 = silent order corruption
If validation passes invalid items (Bug 9) and reservation isn't awaited (Bug 2), the order proceeds to pricing with invalid items, producing an order record with nonsensical pricing for items that don't exist in the catalog.

---

## Scoring Guide

### Full Credit Requirements
- Bug identified with correct location
- Severity correctly classified
- Impact accurately described
- Fix is correct and doesn't introduce new issues

### Partial Credit (50%)
- Bug identified but impact or fix is wrong/incomplete

### Bonus Criteria
- **Cross-file interaction (+50):** Must identify at least 2 interaction effects with clear explanation of the causal chain
- **Test cases (+50):** Must provide executable test cases that demonstrate at least 5 bugs

### False Positive Deduction (-25 each)
- Reporting something as a bug that is actually correct behavior
- Reporting a code style issue as a bug (unless it causes incorrect behavior)
