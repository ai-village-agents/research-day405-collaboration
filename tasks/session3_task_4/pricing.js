/**
 * Pricing and Discount Engine
 * 
 * Calculates order totals with support for:
 * - Percentage discounts
 * - Flat (fixed amount) discounts
 * - Discount stacking (multiple discounts on one order)
 * - Low-stock surge pricing
 * 
 * Discount stacking rule (per specification):
 *   "Apply flat discounts FIRST, then percentage discounts on the reduced amount."
 * 
 * Usage:
 *   const pricing = new PricingEngine(productCatalog);
 *   const total = pricing.calculateOrderTotal(cartItems, discounts, inventorySummary);
 */

class PricingEngine {
  constructor(catalog = {}) {
    this.catalog = catalog;  // { productId: { name, basePrice, category } }
  }

  /**
   * Calculate the total for an order.
   * 
   * @param {Array} cartItems - [{ productId, quantity }]
   * @param {Array} discounts - [{ type: 'percentage'|'flat', value: number, minOrderValue?: number }]
   * @param {Object} inventorySummary - from InventoryManager.getInventorySummary()
   * @returns {{ subtotal, discountAmount, surchargeAmount, tax, total, breakdown }}
   */
  calculateOrderTotal(cartItems, discounts = [], inventorySummary = null) {
    // Step 1: Calculate subtotal
    let subtotal = 0;
    const breakdown = [];

    for (const item of cartItems) {
      const product = this.catalog[item.productId];
      if (!product) {
        breakdown.push({ productId: item.productId, error: 'Product not found' });
        continue;
      }

      const lineTotal = product.basePrice * item.quantity;
      subtotal += lineTotal;
      breakdown.push({
        productId: item.productId,
        name: product.name,
        unitPrice: product.basePrice,
        quantity: item.quantity,
        lineTotal
      });
    }

    // Step 2: Apply surge pricing for low-stock items
    let surchargeAmount = 0;
    if (inventorySummary) {
      for (const item of cartItems) {
        const stockInfo = inventorySummary[item.productId];
        if (stockInfo && stockInfo.available <= 3) {
          // 15% surge on low-stock items
          const product = this.catalog[item.productId];
          if (product) {
            surchargeAmount += product.basePrice * item.quantity * 0.15;
          }
        }
      }
    }

    // Step 3: Apply discounts
    // Apply discounts in sequence
    // but specification says "Apply flat discounts FIRST, then percentage."
    let discountAmount = 0;
    let discountedSubtotal = subtotal + surchargeAmount;

    // Sort discounts by type for processing
    const sortedDiscounts = discounts.sort((a, b) => {
      if (a.type === 'percentage' && b.type === 'flat') return -1;
      if (a.type === 'flat' && b.type === 'percentage') return 1;
      return 0;
    });

    for (const discount of sortedDiscounts) {
      // Check minimum order value (uses original subtotal, not discounted)
      if (discount.minOrderValue && subtotal < discount.minOrderValue) {
        continue;
      }

      if (discount.type === 'percentage') {
        const amount = discountedSubtotal * (discount.value / 100);
        discountAmount += amount;
        discountedSubtotal -= amount;
      } else if (discount.type === 'flat') {
        discountAmount += discount.value;
        discountedSubtotal -= discount.value;
      }
    }

    // Calculate running total
    // without rounding. Can produce values like 29.990000000000002
    // instead of 29.99. Financial calculations should round to cents.
    const taxableAmount = discountedSubtotal;
    
    // Apply tax
    // NOT on the discounted amount. Uses `subtotal + surchargeAmount`
    // instead of `discountedSubtotal` (which already has discounts applied).
    const tax = (subtotal + surchargeAmount) * 0.08;

    const total = discountedSubtotal + tax;

    return {
      subtotal,
      surchargeAmount,
      discountAmount,
      tax,
      total,
      breakdown,
      appliedDiscounts: sortedDiscounts.filter(d => {
        return !(d.minOrderValue && subtotal < d.minOrderValue);
      })
    };
  }

  /**
   * Check if a discount code is valid.
   * This is a simplified validator.
   */
  validateDiscount(discount) {
    if (!discount || !discount.type || discount.value === undefined) {
      return { valid: false, reason: 'Missing required fields' };
    }
    if (discount.type !== 'percentage' && discount.type !== 'flat') {
      return { valid: false, reason: 'Invalid discount type' };
    }
    if (discount.type === 'percentage' && (discount.value < 0 || discount.value > 100)) {
      return { valid: false, reason: 'Percentage must be 0-100' };
    }
    if (discount.type === 'flat' && discount.value < 0) {
      return { valid: false, reason: 'Flat discount cannot be negative' };
    }
    return { valid: true };
  }
}

module.exports = { PricingEngine };
