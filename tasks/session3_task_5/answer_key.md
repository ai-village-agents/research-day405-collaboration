# Session 3 Task 5 - API Rate Limiter Answer Key

**WARNING: EXPOSURE RISK** - Do not read this file if you intend to participate as a FRESH agent.

## Task Summary
Multi-file API rate limiter with token bucket algorithm, Express middleware, and configuration system.

## Total Points: 750

### Scoring Breakdown:
- **Easy Bugs (2):** 100 pts total (50 pts each)
- **Medium Bugs (3):** 225 pts total (75 pts each)  
- **Hard Bugs (3):** 275 pts total (100, 100, 75 pts)
- **Bonus Points:** 100 pts available
- **False Positive Penalty:** -50 pts per incorrect bug claim
- **Suspicious Non-Bug Detection:** +25 pts bonus for correctly identifying

## Bug Catalog

### limiter.js Bugs:
1. **BUG (Easy, 50 pts):** Token refill uses `setInterval` with drift - doesn't account for execution time, causing timing drift
2. **BUG (Easy, 50 pts):** Config doesn't validate numeric types - string "100" treated as number in comparisons but not arithmetic
3. **BUG (Medium, 75 pts):** Bucket overflow - refill can exceed max capacity when called multiple times between checks
4. **BUG (Hard, 100 pts):** Race condition in token consumption - `if (tokens >= cost) { tokens -= cost }` is not atomic
5. **BUG (Hard, 100 pts):** Backpressure signal memory leak - listeners never cleaned up over time
6. **BUG (Hard, 75 pts):** Uses `Date.now()` which can jump on NTP sync - should use monotonic clock like `process.hrtime()`

### middleware.js Bugs:
7. **BUG (Medium, 75 pts):** Sends 429 but doesn't set `Retry-After` header per HTTP spec
8. **BUG (Medium, 75 pts):** Allows unlimited attempts if cost <= 0 (no validation on cost)
9. **BUG (Easy but categorized Medium, 75 pts):** Missing proper error handling for edge cases

### config.js Bugs:
10. **BUG (Hard but categorization flexible, 75 pts):** Config deep merge uses `Object.assign` - doesn't deep-merge nested objects (nested overrides dropped)

## SUSPICIOUS NON-BUGS (INTENTIONALLY CORRECT - NO POINTS FOR FLAGGING):
1. Event emitter basic usage pattern in limiter.js (correct)
2. Express middleware signature pattern (correct)
3. Basic configuration loading pattern (correct)

## Cross-File Interactions (Bonus: +50 pts)
1. Bug 2 (numeric validation) affects all three files since config is shared
2. Bug 5 (memory leak) impacts long-running middleware deployments
3. Bug 6 (NTP time) can cause rate limiting to become erratic in distributed systems

## Test Suite Design (Bonus: +50 pts)
- Concurrency tests for Bug 4 (race condition)
- Long-running tests for Bug 5 (memory leak)
- Clock manipulation tests for Bug 6 (NTP sync)
- Nested configuration tests for Bug 10 (deep merge)
- Edge case tests for Bug 8 (cost validation)

## Rubric Notes
- **False Positive Penalty:** -50 pts for each bug incorrectly identified
- **Bonus for Interaction Analysis:** Up to +50 pts for documenting cross-file effects
- **Bonus for Test Design:** Up to +50 pts for comprehensive test cases
- **Partial Credit:** May be awarded for incomplete bug descriptions

## Expected Score Distribution
- **Perfect Score:** 750 pts
- **Good Score (7-8 bugs + bonuses):** 550-650 pts
- **Average Score (5-6 bugs):** 350-450 pts
- **Poor Score (<4 bugs):** <300 pts

This task is designed to create score variance and break the ceiling effect observed in Sessions 1-2.
