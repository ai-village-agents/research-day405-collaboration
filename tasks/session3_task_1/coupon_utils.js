function selectCouponBase(items, coupon) {
  if (!coupon) return 0;

  if (coupon.scope === "all") {
    return items.reduce((sum, item) => sum + item.lineSubtotalCents, 0);
  }

  if (coupon.scope === "nonFood") {
    return items
      .filter((item) => item.category !== "food")
      .reduce((sum, item) => sum + item.lineSubtotalCents, 0);
  }

  return 0;
}

function allocateFixedDiscount(items, discountCents, coupon) {
  const base = selectCouponBase(items, coupon);

  return items.map((item) => {
    const eligible = coupon.scope === "all" || item.category !== "food";
    if (!eligible) {
      return { ...item, allocatedDiscountCents: 0 };
    }

    const share = Math.round((item.lineSubtotalCents / base) * discountCents);
    return { ...item, allocatedDiscountCents: share };
  });
}

module.exports = { selectCouponBase, allocateFixedDiscount };
