# Session 3 Task 5 - API Rate Limiter Answer Key

**WARNING: EXPOSURE RISK** - Do not read this file if you intend to participate as a FRESH agent.

## Task Summary
Multi-file API rate limiter with token bucket algorithm, Express middleware, and configuration system.

## Scoring Frame
- `BASE_MAX = 650`
- `BONUS_MAX = 50`
- `RECOMMENDED_REPORTING_MAX = 700`
- `FALSE_POSITIVE_DEDUCTION = 50` per incorrect bug claim

## Bug Catalog

1. `limiter.js`: setInterval drift / no elapsed-time correction — **50**
2. `limiter.js`: numeric config values not validated/coerced — **50**
3. `limiter.js`: refill can exceed capacity — **75**
4. `limiter.js`: non-atomic token consumption / race-prone check-then-decrement — **100**
5. `limiter.js`: listener cleanup / backpressure memory leak — **75**
6. `limiter.js`: `Date.now()` non-monotonic timing source — **75**
7. `middleware.js`: missing `Retry-After` header on 429 — **50**
8. `middleware.js`: nonpositive request cost can bypass limiting — **75**
9. `config.js`: shallow merge drops nested override fields — **50**
10. `config.js`: null override values can wipe out defaults silently — **50**

**Base total:** 650

## Bonus (+50 max)
- Interaction analysis: **+25**
- Test design quality: **+25**
