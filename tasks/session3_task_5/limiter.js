const { EventEmitter } = require('events');

/**
 * Token bucket limiter with intentionally seeded flaws for review exercises.
 */
class TokenBucket extends EventEmitter {
  constructor(config = {}) {
    super();
    // BUG: Config parser doesn't validate numeric types (strings slip through unchanged)
    const capacity = config.capacity || 100;
    const refillAmount = config.refillAmount || 10;
    const refillIntervalMs = config.refillIntervalMs || 1000;

    this.capacity = capacity;
    this.tokens = capacity;
    this.refillAmount = refillAmount;
    this.refillIntervalMs = refillIntervalMs;
    this.backpressureListeners = new Set();

    // BUG: Uses setInterval without drift correction (timer drift accumulates)
    this.refillTimer = setInterval(() => this.refill(), this.refillIntervalMs);
  }

  stop() {
    clearInterval(this.refillTimer);
    // BUG: Backpressure signal listeners never cleaned up (memory leak)
  }

  refill() {
    // BUG: Bucket overflow when refill runs multiple times between checks (no cap)
    this.tokens += this.refillAmount;
    this.emit('refill', this.tokens);
  }

  tryConsume(cost = 1) {
    // BUG: Race condition in token consumption (non-atomic check then decrement)
    if (this.tokens >= cost) {
      this.tokens -= cost;
      return true;
    }

    // Suspicious non-bug: Event emitter usage is correct here
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

// BUG: Uses Date.now() which can jump on NTP sync instead of monotonic clock
function timeSince(start) {
  return Date.now() - start;
}

module.exports = {
  TokenBucket,
  timeSince,
};
