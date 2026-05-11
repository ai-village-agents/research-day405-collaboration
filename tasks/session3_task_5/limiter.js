const { EventEmitter } = require('events');

/**
 * Token bucket limiter implementation.
 */
class TokenBucket extends EventEmitter {
  constructor(config = {}) {
    super();
    const capacity = config.capacity || 100;
    const refillAmount = config.refillAmount || 10;
    const refillIntervalMs = config.refillIntervalMs || 1000;

    this.capacity = capacity;
    this.tokens = capacity;
    this.refillAmount = refillAmount;
    this.refillIntervalMs = refillIntervalMs;
    this.backpressureListeners = new Set();

    this.refillTimer = setInterval(() => this.refill(), this.refillIntervalMs);
  }

  stop() {
    clearInterval(this.refillTimer);
  }

  refill() {
    this.tokens += this.refillAmount;
    this.emit('refill', this.tokens);
  }

  tryConsume(cost = 1) {
    if (this.tokens >= cost) {
      this.tokens -= cost;
      return true;
    }

    const listener = () => {
      if (this.tokens >= cost) {
        this.tokens -= cost;
        this.removeListener('refill', listener);
        this.backpressureListeners.delete(listener);
      }
    };
    this.backpressureListeners.add(listener);
    this.on('refill', listener);
    return false;
  }

  waitForTokens(cost = 1) {
    return new Promise((resolve) => {
      if (this.tryConsume(cost)) {
        resolve(true);
        return;
      }

      const listener = () => {
        if (this.tryConsume(cost)) {
          this.removeListener('refill', listener);
          this.backpressureListeners.delete(listener);
          resolve(true);
        }
      };

      this.backpressureListeners.add(listener);
      this.on('refill', listener);
    });
  }

  getRemaining() {
    return this.tokens;
  }

  getCapacity() {
    return this.capacity;
  }
}

function timeSince(start) {
  return Date.now() - start;
}

module.exports = {
  TokenBucket,
  timeSince,
};
