# Output B

## Task family
Seeded bug inspection.

## Final output

### Seeded bugs
1. **Line 6:** `run.completed = true` inside `filter` mutates input and makes the filter always truthy.
   - **Fix:** `run.completed === true` or `run.completed`.
2. **Line 11:** `run.condition.toLowerCase` is missing `()` and uses a function reference as the key, collapsing all conditions into one bucket.
   - **Fix:** `run.condition.toLowerCase()`.
3. **Line 27:** `Math.round(x, 2)` ignores the precision argument and returns an integer.
   - **Fix:** `Number((x).toFixed(2))` or `Math.round(x * 100) / 100`.
4. **Line 28:** `completion_rate` divides by all runs rather than the per-condition count.
   - **Fix:** `item.completed / item.count`.
5. **Line 32:** The `sort` comparator returns a boolean instead of a signed numeric difference.
   - **Fix:** `(a, b) => a.mean_duration - b.mean_duration`.

### Additional observation
- `totalDuration / completedRuns.length` mixes an all-run numerator with a completed-only denominator; if the intended metric is mean duration of completed runs, the numerator should also be restricted.

### Additional insight
- The bugs on lines 6, 11, and 28 can mask each other in demo output: mutation makes all runs appear completed, grouping collapses into one bucket, and the wrong denominator can coincidentally yield a plausible completion rate.
