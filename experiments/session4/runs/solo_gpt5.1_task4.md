# Session 4 Task 4 — Solo Condition (GPT-5.1)

## Anti-Contamination Declaration
- [x] I have not previously seen these Task 4 code files or any answer key.
- [x] I am working under my assigned condition (Solo).

## Timing
- Start: 2026-05-12, ~10:12 AM PT
- End: (to be filled at end)

## 1. Numbered Bug List

(Will be filled in below.)

## 2. Cross-File Interaction Analysis

(Will be filled in after reviewing all files.)

## 3. Test Case Suggestions

(Will be filled in after enumerating bugs.)

## 4. Notes

Working pass-by-pass: inventory.js → pricing.js → order.js → interactions.

## 1. Numbered Bug List

### Bug 1 — Off-by-one iteration over items (inventory.js)
- **File:** `inventory.js`
- **Location:** Lines 61–63 (`for (let i = 0; i <= items.length; i++)`)
- **Severity:** CRITICAL
- **Description:**
  - The reservation loop iterates with `i <= items.length`, which means on the final iteration `i === items.length` and `items[i]` is `undefined`.
  - The code then immediately reads `item.productId` and `item.quantity` without a null check. This will throw a runtime error (`Cannot read property 'productId' of undefined`).
  - A single malformed `items` array (or even an empty array) will cause the entire reservation call to crash instead of returning a structured `{ success, failedItems }` result.
- **Impact:**
  - Order processing can fail catastrophically when reserving inventory, aborting the whole pipeline and potentially leaving the system in an inconsistent state (e.g., `reservationLocks[orderId]` set but no reservation recorded).
- **Proposed fix:**
  - Change loop bound to `i < items.length` and optionally guard against non-array inputs.
  - Example:
    ```js
    for (let i = 0; i < items.length; i++) {
      const item = items[i];
      if (!item) continue; // or treat as failure explicitly
      // existing logic
    }
    ```

### Bug 2 — Missing concurrency protection / unused reservationLocks (inventory.js)
- **File:** `inventory.js`
- **Location:** Lines 47–56 and comment at 52–55
- **Severity:** HIGH
- **Description:**
  - The comments explain that two concurrent calls to `reserveItems` can both see the same available stock and both succeed, over-reserving inventory.
  - The implementation sets `this.reservationLocks[orderId] = true;` but never actually checks or uses `reservationLocks` to provide mutual exclusion or a per-product lock.
  - There is no locking by `productId` or global mutex; `getAvailableStock` computes availability based only on `this.reservations` (which is empty until the *end* of a successful reservation), so concurrent reservations can both think stock is available.
- **Impact:**
  - Under concurrency, the system can reserve more inventory than actually exists, leading to later failures when confirming orders or shipping products.
  - Violates the spec’s requirement that the system handle concurrent order requests safely.
- **Proposed fix:**
  - Either implement proper locking by product (e.g., using a per-product mutex or queue) or use an atomic update pattern that checks and reserves in one critical section.
  - At minimum, use `reservationLocks` to prevent concurrent `reserveItems` for the same `orderId` or, better, a global lock when mutating reservations.

### Bug 3 — Leaking internal mutable state via inventory summary (inventory.js)
- **File:** `inventory.js`
- **Location:** Lines 121–141, especially `_stockRef: this.stock`
- **Severity:** MEDIUM
- **Description:**
  - `getInventorySummary` returns an object whose entries include a `_stockRef` property pointing directly to `this.stock`.
  - External callers (like `pricing.js`) who consume the summary now have a live reference to the internal stock map and can mutate it (e.g., `summary[id]._stockRef[id] = 0`), bypassing all reservation logic.
  - Additionally, the comment notes that the summary structure shares references; while the `total`/`available` values are primitive snapshots, the `_stockRef` breaks encapsulation entirely.
- **Impact:**
  - Any downstream module can accidentally or maliciously change inventory totals without going through `reserveItems` / `confirmReservation`, breaking invariants and making debugging difficult.
- **Proposed fix:**
  - Remove `_stockRef` entirely or replace with a read-only copy.
  - If debugging needs exist, expose internal state via a dedicated debug-only method that is clearly documented as unsafe.

### Bug 4 — Discount stacking order implemented backwards (pricing.js)
- **File:** `pricing.js`
- **Location:** Lines 69–80 and discount sort comparator
- **Severity:** HIGH
- **Description:**
  - Spec says: “Apply flat discounts FIRST, then percentage discounts on the reduced amount.”
  - The code sorts discounts so that percentage discounts come before flat discounts:
    ```js
    const sortedDiscounts = discounts.sort((a, b) => {
      if (a.type === 'percentage' && b.type === 'flat') return -1;
      if (a.type === 'flat' && b.type === 'percentage') return 1;
      return 0;
    });
    ```
  - This inverts the intended stacking rule.
- **Impact:**
  - Percentage discounts are applied on a higher base than intended, giving customers larger discounts than configured (revenue loss) and making billing inconsistent with business rules.
- **Proposed fix:**
  - Reverse the comparator so that flat discounts are processed first, or more simply:
    ```js
    const sortedDiscounts = [...discounts].sort((a, b) => {
      if (a.type === 'flat' && b.type === 'percentage') return -1;
      if (a.type === 'percentage' && b.type === 'flat') return 1;
      return 0;
    });
    ```

### Bug 5 — Tax calculated on pre-discount amount (pricing.js)
- **File:** `pricing.js`
- **Location:** Lines 101–107
- **Severity:** CRITICAL (business logic / compliance)
- **Description:**
  - After applying surcharges and discounts, the code sets:
    ```js
    const taxableAmount = discountedSubtotal;
    const tax = (subtotal + surchargeAmount) * 0.08;
    ```
  - Tax is actually computed on `subtotal + surchargeAmount`, ignoring discounts.
  - This contradicts the intent of `taxableAmount` and likely the business expectation that tax apply on the discounted total.
- **Impact:**
  - Customers are overcharged tax whenever there are discounts.
  - Could violate tax regulations depending on jurisdiction and cause reconciliation issues.
- **Proposed fix:**
  - Compute tax on `taxableAmount` (i.e., `discountedSubtotal`), or clearly document and implement the business rule if there is some other intended basis.
    ```js
    const taxableAmount = discountedSubtotal;
    const tax = taxableAmount * 0.08;
    ```

### Bug 6 — No rounding to cents for financial totals (pricing.js)
- **File:** `pricing.js`
- **Location:** Lines 98–108
- **Severity:** MEDIUM
- **Description:**
  - The comment explicitly notes that the code does not round to cents and can produce floating-point artifacts like `29.990000000000002`.
  - All returned amounts (`subtotal`, `surchargeAmount`, `discountAmount`, `tax`, `total`) are raw JS floats without consistent rounding.
- **Impact:**
  - Downstream systems (billing, invoicing, reporting) may see inconsistent cent values.
  - Rendering these numbers in UI can confuse customers and create reconciliation issues.
- **Proposed fix:**
  - Apply rounding to 2 decimal places at least for `tax` and `total` (and ideally for all monetary fields) using a consistent helper:
    ```js
    const roundCents = n => Math.round(n * 100) / 100;
    const tax = roundCents(taxableAmount * 0.08);
    const total = roundCents(discountedSubtotal + tax);
    ```

### Bug 7 — Order validation only requires one valid item (order.js)
- **File:** `order.js`
- **Location:** Lines 45–65
- **Severity:** HIGH
- **Description:**
  - `validateOrder` uses `items.some(...)` to compute `allValid`:
    ```js
    const allValid = items.some(item => { ... });
    ```
  - The comments themselves say it “should use `every()` to check that ALL items are valid.”
  - As written, if *any* item is valid, `allValid` becomes `true`, even if other items collected errors.
  - The function then returns `valid: allValid && errors.length === 0`; however, errors are pushed whenever a field is missing or invalid.
  - Edge case: if the first item is valid and later items are invalid, `allValid` is true but `errors.length > 0`, so `valid` becomes false. The more serious issue is that `some` short-circuits on the first valid item, so *later items may not be checked at all*, missing invalid entries entirely.
- **Impact:**
  - The validator can silently skip validating items after the first valid one, letting bad data through in some patterns.
  - Even when `valid` is false, the set of errors may be incomplete.
- **Proposed fix:**
  - Use `every` to traverse *all* items and ensure they are valid, or simply loop with a `for` and a boolean flag.
    ```js
    const allValid = items.every(item => { ... });
    ```

### Bug 8 — Reservation Promise never awaited (order.js)
- **File:** `order.js`
- **Location:** Lines 101–115
- **Severity:** CRITICAL
- **Description:**
  - `processOrder` is `async`, but when reserving inventory it calls:
    ```js
    const reservation = this.inventory.reserveItems(orderId, items);
    if (!reservation.success) { ... }
    ```
  - `reserveItems` is declared `async`, so it returns a Promise. The code never `await`s it, and immediately checks `reservation.success` on the Promise object.
  - Since any non-null object is truthy, `if (!reservation.success)` always evaluates to `false`, so the error branch is never taken, even if the underlying reservation fails.
- **Impact:**
  - Orders will report `success: true` and proceed to pricing even when inventory reservation rejects or returns `success: false`.
  - This violates the all-or-nothing inventory reservation rule and creates ghost orders with no inventory.
- **Proposed fix:**
  - Await the reservation and handle both success and failure:
    ```js
    const reservation = await this.inventory.reserveItems(orderId, items);
    if (!reservation.success) {
      // return failure with reservation.failedItems
    }
    ```

### Bug 9 — Overwriting optional metadata via JSON serialization (order.js)
- **File:** `order.js`
- **Location:** Lines 121–133
- **Severity:** LOW / MEDIUM
- **Description:**
  - `orderRecord` is created via `JSON.parse(JSON.stringify({...}))`.
  - Comments note that this strips `undefined` fields (e.g., optional `metadata` on items) so downstream code that checks `'metadata' in item` will see `false` instead of `true`.
  - In JS, the presence of a property with `undefined` is different from the property not existing; serializing via JSON erases that distinction.
- **Impact:**
  - Subtle behavioral bugs in downstream analytics or conditional logic that relies on property presence, especially for optional fields.
  - Potential compliance or fulfillment issues if metadata fields indicate special handling.
- **Proposed fix:**
  - Avoid blanket JSON serialization; instead perform a deep clone that preserves keys even when values are `undefined` (e.g., structuredClone, or manual cloning that copies properties directly).
  - Alternatively, retain the original object structure and only clone where necessary.

### Bug 10 — Cancel logic uses loose inequality and ignores orderIndex (order.js)
- **File:** `order.js`
- **Location:** Lines 156–171
- **Severity:** MEDIUM
- **Description:**
  - `cancelOrder` finds an order index but then does not actually use it to remove that specific order; instead it reassigns `this.processedOrders` via a filter:
    ```js
    const orderIndex = this.processedOrders.findIndex(o => o.orderId === orderId);
    if (orderIndex === -1) { ... }
    this.processedOrders = this.processedOrders.filter(o => o.orderId != orderId);
    ```
  - The filter uses loose inequality (`!=`), so if stored `orderId` types differ (number vs string), unrelated orders may be unexpectedly removed or retained.
  - Using `filter` here also ignores the specific index found earlier; there’s duplicated logic and a risk of mismatches if the equality semantics change.
- **Impact:**
  - Cancelling one order could cancel additional orders with loosely equal IDs (e.g., `'42'` vs `42`).
  - Data inconsistencies in order history and inventory cancellations.
- **Proposed fix:**
  - Use strict equality in both places and rely on the found index for removal:
    ```js
    const orderIndex = this.processedOrders.findIndex(o => o.orderId === orderId);
    if (orderIndex === -1) { ... }
    const [order] = this.processedOrders.splice(orderIndex, 1);
    ```
  - Keep `cancelReservation(orderId)` as is but ensure IDs are consistently typed.


## 2. Cross-File Interaction Analysis

1. **Inventory reservation + order processing (Bugs 1, 2, 8):**
   - `OrderProcessor.processOrder` relies on `InventoryManager.reserveItems` to enforce the all-or-nothing reservation rule.
   - Because `reserveItems` is `async` and not awaited (Bug 8), the order pipeline proceeds as if reservation succeeded, while the inventory module may still be processing or may have failed.
   - Combined with the concurrency weakness and off-by-one crash in `reserveItems` (Bugs 1 and 2), this means orders can be marked successful even when:
     - Inventory was never reserved due to a thrown error.
     - Concurrent orders oversubscribed stock.
   - Cross-file effect: `order.js` assumes a reliable, synchronous-looking reservation API that the implementation in `inventory.js` does not provide.

2. **Inventory summary leaking internal state to pricing (Bug 3):**
   - `OrderProcessor` calls `this.inventory.getInventorySummary()` and passes the result into `pricing.calculateOrderTotal`.
   - Because this summary includes `_stockRef: this.stock`, any future extension to `PricingEngine` that writes to `inventorySummary` can accidentally mutate the live stock state, corrupting inventory for subsequent orders.
   - The cross-file boundary between inventory and pricing is supposed to be read-only; exposing `_stockRef` silently violates that contract.

3. **Discount + tax order (Bugs 4, 5, 6):**
   - There is an implicit contract that `OrderProcessor` delegates all pricing correctness (including discounts + tax) to `PricingEngine`.
   - Bugs 4–6 mean that `OrderProcessor`’s `pricing` field in stored `orderRecord` can contain totals that misapply stacking and tax rules and exhibit floating-point artifacts.
   - Any downstream analytics based on `processedOrders` (e.g., customer spend, tax reporting) will inherit these inconsistencies across both modules.

4. **Order archival and metadata stripping (Bug 9 + Inventory/Discount behavior):**
   - `orderRecord` is archived with stripped `undefined` fields. If items included optional metadata that affect how inventory or discounts should be interpreted (e.g., “pre-order”, “backorder-allowed”), that context is lost.
   - Later reconciliation between `processedOrders`, inventory levels, and pricing rules may be impossible because the stored order history no longer faithfully reflects the original request.

5. **Cancellation path and reservation cleanup (Bug 10 + inventory cancellation):**
   - `cancelOrder` filters `processedOrders` with loose inequality and then calls `inventory.cancelReservation(orderId)`.
   - If type coercion causes the wrong orders to be removed, the call to `cancelReservation` may not match the removed order (or may release inventory for an order that remains in history).
   - This breaks the intended invariant that order history and inventory reservations stay aligned.

Overall, the main cross-file pattern is that `OrderProcessor` treats its collaborators (`InventoryManager` and `PricingEngine`) as reliable transactional components, but the actual implementations violate those contracts in ways that only show up when the modules are composed together.

## 3. Test Case Suggestions

I’ll outline test cases as if using a Jest-like framework; pseudocode is sufficient for illustrating the intent.

### Tests for inventory.js

1. **Off-by-one reservation crash (Bug 1):**
   ```js
   test('reserveItems should not access past end of items array', async () => {
     const inventory = new InventoryManager({ sku1: 10 });
     await expect(inventory.reserveItems('order-1', [
       { productId: 'sku1', quantity: 1 },
     ])).resolves.toMatchObject({ success: true });
   });
   ```
   - With current code, this will throw before resolving. After fix, it should succeed.

2. **Concurrent over-reservation (Bug 2):**
   ```js
   test('concurrent reservations should not oversell inventory', async () => {
     const inventory = new InventoryManager({ sku1: 5 });
     const items = [{ productId: 'sku1', quantity: 5 }];

     const [r1, r2] = await Promise.all([
       inventory.reserveItems('order-1', items),
       inventory.reserveItems('order-2', items),
     ]);

     const successes = [r1, r2].filter(r => r.success).length;
     expect(successes).toBe(1); // currently can be 2
   });
   ```

3. **Inventory summary encapsulation (Bug 3):**
   ```js
   test('inventory summary should not expose mutable stock reference', () => {
     const inventory = new InventoryManager({ sku1: 10 });
     const summary = inventory.getInventorySummary();

     summary['sku1']._stockRef['sku1'] = 0;
     // After fix, either _stockRef should not exist or mutation
     // should not affect internal stock totals.
     expect(inventory.getAvailableStock('sku1')).toBe(10);
   });
   ```

### Tests for pricing.js

4. **Discount stacking order (Bug 4):**
   ```js
   test('flat discounts should apply before percentage discounts', () => {
     const engine = new PricingEngine({ sku1: { name: 'Item', basePrice: 100 } });
     const cart = [{ productId: 'sku1', quantity: 1 }];
     const discounts = [
       { type: 'percentage', value: 10 }, // 10%
       { type: 'flat', value: 20 },      // $20 off
     ];

     const { total } = engine.calculateOrderTotal(cart, discounts);
     // Correct: (100 - 20) * 0.9 = 72
     // Current implementation applies percentage first, then flat.
     expect(total).toBeCloseTo(72, 2);
   });
   ```

5. **Tax on discounted amount (Bug 5):**
   ```js
   test('tax should be computed on discounted subtotal', () => {
     const engine = new PricingEngine({ sku1: { name: 'Item', basePrice: 100 } });
     const cart = [{ productId: 'sku1', quantity: 1 }];
     const discounts = [{ type: 'flat', value: 20 }];

     const result = engine.calculateOrderTotal(cart, discounts);

     // Expected taxable base is 80, not 100.
     expect(result.tax).toBeCloseTo(80 * 0.08, 2);
   });
   ```

6. **Rounding to cents (Bug 6):**
   ```js
   test('totals should be rounded to two decimal places', () => {
     const engine = new PricingEngine({ sku1: { name: 'Item', basePrice: 9.99 } });
     const cart = [{ productId: 'sku1', quantity: 3 }];
     const discounts = [{ type: 'percentage', value: 5 }];

     const { total } = engine.calculateOrderTotal(cart, discounts);
     const totalStr = total.toString();
     expect(totalStr).not.toMatch(/000000/); // crude check for FP artifact
   });
   ```

### Tests for order.js

7. **Validator checks all items (Bug 7):**
   ```js
   test('validateOrder should reject when any item is invalid', () => {
     const inventory = new InventoryManager({ sku1: 10 });
     const pricing = new PricingEngine({ sku1: { name: 'Item', basePrice: 10 } });
     const processor = new OrderProcessor(inventory, pricing);

     const items = [
       { productId: 'sku1', quantity: 1 },
       { productId: '', quantity: 1 }, // invalid
     ];

     const validation = processor.validateOrder(items);
     expect(validation.valid).toBe(false);
     expect(validation.errors.length).toBeGreaterThan(0);
   });
   ```

8. **Reservation Promise must be awaited (Bug 8):**
   ```js
   test('processOrder should await inventory reservation and fail on insufficient stock', async () => {
     const inventory = new InventoryManager({ sku1: 1 });
     const pricing = new PricingEngine({ sku1: { name: 'Item', basePrice: 10 } });
     const processor = new OrderProcessor(inventory, pricing);

     const items = [
       { productId: 'sku1', quantity: 2 }, // more than available
     ];

     const result = await processor.processOrder({
       orderId: 'o1',
       customerId: 'c1',
       items,
     });

     expect(result.success).toBe(false);
     expect(result.stage).toBe('inventory');
   });
   ```

9. **Archival should preserve metadata keys (Bug 9):**
   ```js
   test('orderRecord should preserve optional metadata keys', async () => {
     const inventory = new InventoryManager({ sku1: 10 });
     const pricing = new PricingEngine({ sku1: { name: 'Item', basePrice: 10 } });
     const processor = new OrderProcessor(inventory, pricing);

     const items = [{ productId: 'sku1', quantity: 1, metadata: undefined }];
     await processor.processOrder({ orderId: 'o1', customerId: 'c1', items });

     const orders = processor.getCustomerOrders('c1');
     const storedItem = orders[0].items[0];
     expect('metadata' in storedItem).toBe(true);
   });
   ```

10. **Cancel uses strict identity and removes exactly one order (Bug 10):**
    ```js
    test('cancelOrder should remove exactly the targeted order', () => {
      const inventory = new InventoryManager({ sku1: 10 });
      const pricing = new PricingEngine({ sku1: { name: 'Item', basePrice: 10 } });
      const processor = new OrderProcessor(inventory, pricing);

      processor.processedOrders = [
        { orderId: '1' },
        { orderId: '2' },
      ];

      const result = processor.cancelOrder('1');
      expect(result.success).toBe(true);
      expect(processor.processedOrders).toEqual([{ orderId: '2' }]);
    });
    ```

## 4. Timing (Completed)
- Start: 2026-05-12, ~10:12 AM PT
- End: 2026-05-12, ~10:22 AM PT

