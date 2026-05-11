const { selectCouponBase, allocateFixedDiscount } = require('./coupon_utils');

function buildCheckoutSummary(cart, config, coupon) {
  if (!cart || !Array.isArray(cart.items) || cart.items.length === 0) {
    return {
      subtotal: 0,
      discount: 0,
      tax: 0,
      shipping: 0,
      total: 0,
      itemCount: 0,
    };
  }

  const items = cart.items.map((item) => ({
    name: item.name,
    category: item.category || 'general',
    quantity: item.quantity || 1,
    unitPriceCents: item.unitPriceCents,
    taxable: item.category !== 'food' && item.category !== 'book',
    lineSubtotalCents: item.unitPriceCents * (item.quantity || 1),
  }));

  const subtotalCents = items.reduce((sum, item) => sum + item.lineSubtotalCents, 0);
  const itemCount = items.reduce((sum, item) => sum + item.quantity, 0);

  let discountCents = 0;
  let discountedItems = items.map((item) => ({ ...item, allocatedDiscountCents: 0 }));

  if (coupon) {
    const eligibleBase = selectCouponBase(items, coupon);

    if (coupon.type === 'percent') {
      discountCents = Math.round(eligibleBase * coupon.percentOff);
      discountedItems = items.map((item) => {
        const eligible = coupon.scope === 'all' || item.category !== 'food';
        if (!eligible) return { ...item, allocatedDiscountCents: 0 };

        return {
          ...item,
          allocatedDiscountCents: Math.round(item.lineSubtotalCents * coupon.percentOff),
        };
      });
    } else if (coupon.type === 'fixed') {
      discountCents = coupon.amountOffCents;
      discountedItems = allocateFixedDiscount(items, discountCents, coupon);
    }
  }

  const taxableSubtotalCents = items
    .filter((item) => item.taxable)
    .reduce((sum, item) => sum + item.lineSubtotalCents, 0);

  const taxCents = Math.round(taxableSubtotalCents * config.taxRate);

  const shippingCents = subtotalCents >= config.freeShippingThresholdCents
    ? 0
    : config.shippingCents;

  const totalCents = subtotalCents - discountCents + taxCents + shippingCents;

  return {
    subtotal: Number((subtotalCents / 100).toFixed(2)),
    discount: Number((discountCents / 100).toFixed(2)),
    tax: Number((taxCents / 100).toFixed(2)),
    shipping: Number((shippingCents / 100).toFixed(2)),
    total: Number((totalCents / 100).toFixed(2)),
    itemCount,
  };
}

module.exports = { buildCheckoutSummary };
