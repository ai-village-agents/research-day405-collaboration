# Pilot Task B Answer Key

Seeded issues intentionally included in `task.js`:

1. `run.completed = true` inside `filter`
   - Assignment instead of comparison mutates every run and makes filter always truthy.
   - Expected fix: `run.completed === true` or simply `run.completed`.

2. `run.condition.toLowerCase`
   - Missing invocation; stores function reference, not lowercase string.
   - Expected fix: `run.condition.toLowerCase()`.

3. `Math.round(item.duration / item.count, 2)`
   - `Math.round` ignores precision argument in JS.
   - Expected fix: e.g. `Number((item.duration / item.count).toFixed(2))`.

4. `completion_rate: item.completed / runs.length`
   - Denominator should be condition-specific run count, not all runs.
   - Expected fix: `item.completed / item.count`.

5. `rows.sort((a, b) => a.mean_duration > b.mean_duration)`
   - Comparator returns boolean, not signed numeric difference.
   - Expected fix: `a.mean_duration - b.mean_duration` (or reverse if desired).

Possible additional note judges may accept if well-argued:
6. `meanDuration = totalDuration / completedRuns.length`
   - Ambiguous metric: numerator includes all runs, denominator completed only; if intention is mean duration of completed runs, numerator should be restricted.
   - Count as a valid bonus observation if participant explicitly explains the ambiguity.
