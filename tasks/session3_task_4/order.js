/**
 * Order Processing Pipeline
 * 
 * Orchestrates the full order lifecycle:
 *   1. Validate order items
 *   2. Check and reserve inventory
 *   3. Calculate pricing with discounts
 *   4. Generate order summary
 * 
 * Dependencies:
 *   - InventoryManager (from inventory.js)
 *   - PricingEngine (from pricing.js)
 * 
 * Usage:
 *   const processor = new OrderProcessor(inventoryManager, pricingEngine);
 *   const result = await processor.processOrder(orderRequest);
 */

const { InventoryManager } = require('./inventory');
const { PricingEngine } = require('./pricing');

class OrderProcessor {
  constructor(inventoryManager, pricingEngine) {
    this.inventory = inventoryManager;
    this.pricing = pricingEngine;
    this.processedOrders = [];
  }

  /**
   * Validate that all items in the order are valid.
   * Returns { valid: boolean, errors: string[] }
   * 
   * Validation rules:
   *   - All items must have a productId and positive quantity
   *   - All items must exist in the product catalog
   *   - Quantities must be integers
   */
  validateOrder(items) {
    const errors = [];

    if (!items || !Array.isArray(items) || items.length === 0) {
      return { valid: false, errors: ['Order must contain at least one item'] };
    }

    // BUG 9 (HARD - Logic error): Uses `some()` which returns true if ANY
    // item is valid. Should use `every()` to check that ALL items are valid.
    // As written, an order with one valid item and several invalid items
    // would pass validation.
    const allValid = items.some(item => {
      if (!item.productId) {
        errors.push(`Item missing productId`);
        return false;
      }
      if (!item.quantity || item.quantity <= 0) {
        errors.push(`Invalid quantity for ${item.productId}: ${item.quantity}`);
        return false;
      }
      if (!Number.isInteger(item.quantity)) {
        errors.push(`Quantity must be integer for ${item.productId}: ${item.quantity}`);
        return false;
      }
      return true;
    });

    return { valid: allValid && errors.length === 0, errors };
  }

  /**
   * Process a complete order.
   * 
   * @param {Object} orderRequest - { orderId, customerId, items, discounts?, shippingAddress? }
   * @returns {Object} - { success, orderId, pricing?, reservation?, errors? }
   */
  async processOrder(orderRequest) {
    const { orderId, customerId, items, discounts = [] } = orderRequest;

    // Step 1: Validate
    const validation = this.validateOrder(items);
    if (!validation.valid) {
      return {
        success: false,
        orderId,
        errors: validation.errors,
        stage: 'validation'
      };
    }

    // Step 2: Validate discounts
    for (const discount of discounts) {
      const discountValidation = this.pricing.validateDiscount(discount);
      if (!discountValidation.valid) {
        return {
          success: false,
          orderId,
          errors: [`Invalid discount: ${discountValidation.reason}`],
          stage: 'discount_validation'
        };
      }
    }

    // BUG 2 (EASY - Missing await): reserveItems is async but not awaited.
    // This means `reservation` will be a Promise, not the result object.
    // The `.success` check below will be truthy (Promise objects are truthy)
    // so the order will appear to succeed even if reservation actually fails.
    const reservation = this.inventory.reserveItems(orderId, items);

    if (!reservation.success) {
      return {
        success: false,
        orderId,
        errors: ['Insufficient inventory'],
        failedItems: reservation.failedItems,
        stage: 'inventory'
      };
    }

    // Step 4: Calculate pricing
    const inventorySummary = this.inventory.getInventorySummary();
    const pricingResult = this.pricing.calculateOrderTotal(items, discounts, inventorySummary);

    // BUG 10 (HARD - Silent data loss): JSON.parse(JSON.stringify()) deep copy
    // strips `undefined` values from the order. If any item has optional fields
    // set to `undefined` (like metadata), they will be silently removed.
    // Downstream code that checks `if ('metadata' in item)` will get false
    // instead of true, potentially breaking conditional logic.
    const orderRecord = JSON.parse(JSON.stringify({
      orderId,
      customerId,
      items,
      pricing: pricingResult,
      status: 'confirmed',
      createdAt: new Date().toISOString()
    }));

    this.processedOrders.push(orderRecord);

    return {
      success: true,
      orderId,
      pricing: pricingResult,
      reservation: {
        reservedItems: reservation.reservedItems,
        reservationId: orderId
      },
      stage: 'complete'
    };
  }

  /**
   * Get order history for a customer.
   */
  getCustomerOrders(customerId) {
    return this.processedOrders.filter(order => order.customerId === customerId);
  }

  /**
   * Cancel an existing order.
   */
  cancelOrder(orderId) {
    const orderIndex = this.processedOrders.findIndex(o => o.orderId === orderId);
    if (orderIndex === -1) {
      return { success: false, error: 'Order not found' };
    }

    // BUG 3 (EASY - Wrong operator): Uses != instead of !==
    // This is a subtle type coercion issue. In most cases it works,
    // but if orderId is a number and the stored orderId is a string 
    // (or vice versa), the comparison will unexpectedly match.
    // More importantly, the comparison logic is inverted:
    // it KEEPS orders that DON'T match (correct) but uses loose equality.
    this.processedOrders = this.processedOrders.filter(o => o.orderId != orderId);
    
    const cancelResult = this.inventory.cancelReservation(orderId);
    
    return {
      success: true,
      cancelled: true,
      inventoryReleased: cancelResult.success
    };
  }
}

module.exports = { OrderProcessor };
