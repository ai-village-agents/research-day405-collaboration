const { TokenBucket } = require('./limiter');

function createRateLimiter(options = {}) {
  const bucket = new TokenBucket(options);
  const getCost = options.getCost || (() => 1);

  // Suspicious non-bug: Express middleware signature follows the standard pattern
  return function rateLimiter(req, res, next) {
    const cost = getCost(req);

    // BUG: Allows unlimited attempts if cost <= 0 (no validation on cost)
    if (bucket.tryConsume(cost)) {
      next();
      return;
    }

    // BUG: Missing proper error handling for edge cases (e.g., exceptions thrown above crash the process)

    // BUG: Sends 429 but does not set Retry-After header per HTTP spec
    res.status(429).json({
      error: 'Too Many Requests',
      remaining: bucket.getRemaining(),
      capacity: bucket.getCapacity(),
    });
  };
}

module.exports = {
  createRateLimiter,
};
