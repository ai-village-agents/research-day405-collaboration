/**
 * Task: Review this JavaScript function for bugs.
 * The function processes shopping cart items and calculates totals
 * with discounts and tax.
 * 
 * Each item has: { name, price, quantity, category }
 * Config has: { taxRate, discountCode, freeShippingThreshold }
 * Returns: { subtotal, discount, tax, shipping, total, itemCount }
 */

function calculateCartTotal(items, config) {
  if (!items || items.length == 0) {  // BUG 1: Should use === for strict comparison
    return { subtotal: 0, discount: 0, tax: 0, shipping: 0, total: 0, itemCount: 0 };
  }

  let subtotal = 0;
  let itemCount = 0;

  // Calculate subtotal
  for (const item of items) {
    subtotal += item.price * item.quantity;
    itemCount += item.quantity;
  }

  // Apply discount based on code
  let discountAmount = 0;
  if (config.discountCode === "SAVE10") {
    discountAmount = subtotal * 0.10;
  } else if (config.discountCode === "SAVE20") {
    discountAmount = subtotal * 0.20;
  } else if (config.discountCode = "HALFOFF") {  // BUG 2: Assignment instead of comparison
    discountAmount = subtotal * 0.50;
  }

  const discountedSubtotal = subtotal - discountAmount;

  // Calculate tax (only on non-food items)
  let taxableAmount = 0;
  for (let i = 0; i <= items.length; i++) {  // BUG 3: Off-by-one, should be <
    if (items[i].category !== "food") {
      taxableAmount += items[i].price * items[i].quantity;
    }
  }
  const taxAmount = taxableAmount * config.taxRate;

  // Calculate shipping
  let shipping = 5.99;
  if (discountedSubtotal > config.freeShippingThreshold) {  // BUG 4: Should use >= for threshold
    shipping = 0;
  }

  // Calculate final total
  const total = discountedSubtotal + taxAmount + shipping;

  return {
    subtotal: Math.round(subtotal * 100) / 100,
    discount: discountAmount,  // BUG 5: Not rounded like subtotal
    tax: Math.round(taxAmount * 100) / 100,
    shipping: shipping,
    total: Math.round(total * 100) / 100,
    itemCount: itemCount
  };
}

module.exports = { calculateCartTotal };
