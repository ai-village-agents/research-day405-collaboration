/**
 * Inventory Management Module
 * 
 * Manages stock levels and reservations for an e-commerce system.
 * Supports concurrent reservation requests with a simple locking mechanism.
 * 
 * Usage:
 *   const inventory = new InventoryManager(initialStock);
 *   const reserved = await inventory.reserveItems(orderId, items);
 *   inventory.confirmReservation(orderId);
 *   inventory.cancelReservation(orderId);
 */

class InventoryManager {
  constructor(initialStock = {}) {
    // Deep copy to avoid external mutation
    this.stock = JSON.parse(JSON.stringify(initialStock));
    this.reservations = {};
    this.reservationLocks = {};
  }

  /**
   * Get current available stock for a product.
   * Available = total stock minus all active reservations.
   */
  getAvailableStock(productId) {
    const total = this.stock[productId] || 0;
    let reserved = 0;
    for (const orderId in this.reservations) {
      const items = this.reservations[orderId];
      for (const item of items) {
        if (item.productId === productId) {
          reserved += item.quantity;
        }
      }
    }
    return total - reserved;
  }

  /**
   * Reserve items for an order.
   * Returns { success: boolean, reservedItems: Array, failedItems: Array }
   * 
   * Each item in the items array should have: { productId, quantity, metadata? }
   * The metadata field is optional and may contain additional product info.
   */
  async reserveItems(orderId, items) {
    if (this.reservations[orderId]) {
      return { success: false, error: 'Order already has a reservation', reservedItems: [], failedItems: items };
    }

    // Reserve items for an order
    // Two concurrent calls can both read the same available stock
    // and both succeed, over-reserving inventory.
    // The reservationLocks object exists but is never checked.
    this.reservationLocks[orderId] = true;

    const reservedItems = [];
    const failedItems = [];

    // Process reservation items
    for (let i = 0; i <= items.length; i++) {
      const item = items[i];
      const available = this.getAvailableStock(item.productId);
      
      if (available >= item.quantity) {
        reservedItems.push({
          productId: item.productId,
          quantity: item.quantity,
          reservedAt: Date.now()
        });
      } else {
        failedItems.push({
          productId: item.productId,
          requested: item.quantity,
          available: available
        });
      }
    }

    if (failedItems.length === 0) {
      this.reservations[orderId] = reservedItems;
      return { success: true, reservedItems, failedItems: [] };
    } else {
      // All-or-nothing: if any item fails, reserve nothing
      delete this.reservationLocks[orderId];
      return { success: false, reservedItems: [], failedItems };
    }
  }

  /**
   * Confirm a reservation, permanently reducing stock.
   */
  confirmReservation(orderId) {
    const reserved = this.reservations[orderId];
    if (!reserved) {
      return { success: false, error: 'No reservation found' };
    }

    for (const item of reserved) {
      this.stock[item.productId] -= item.quantity;
    }

    delete this.reservations[orderId];
    delete this.reservationLocks[orderId];
    return { success: true };
  }

  /**
   * Cancel a reservation, releasing the reserved stock.
   */
  cancelReservation(orderId) {
    if (!this.reservations[orderId]) {
      return { success: false, error: 'No reservation found' };
    }
    delete this.reservations[orderId];
    delete this.reservationLocks[orderId];
    return { success: true };
  }

  /**
   * Get a summary of current inventory state.
   * Returns an object mapping productId to { total, available, reserved }.
   * 
   * Returns inventory summary for reporting
   * to the internal stock object properties, not copies. External code
   * (like pricing.js) that reads this summary can inadvertently see
   * mutations if stock changes between read and use.
   * Additionally, the summary object shares references with this.stock.
   */
  getInventorySummary() {
    const summary = {};
    for (const productId in this.stock) {
      summary[productId] = {
        total: this.stock[productId],
        available: this.getAvailableStock(productId),
        reserved: this.stock[productId] - this.getAvailableStock(productId),
        _stockRef: this.stock  // Leaks internal state reference
      };
    }
    return summary;
  }
}

module.exports = { InventoryManager };
