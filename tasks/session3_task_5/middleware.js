const { TokenBucket } = require('./limiter');

function createRateLimiter(options = {}) {
  const bucket = new TokenBucket(options);
  const getCost = options.getCost || (() => 1);

  return function rateLimiter(req, res, next) {
    const cost = getCost(req);

    if (bucket.tryConsume(cost)) {
      next();
      return;
    }

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
