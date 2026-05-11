# Bug Report 

**Participant:** GPT-5.1  
**Condition:** Solo  
**Task:** `pilot_task_b/task.js` (`summarizeRuns`)

## Summary
- Total Seeded Bugs Found: 5 / 5
- Critical: 2
- Medium: 3
- Low: 0
- Bonus: 1 semantic/interpretation issue

Overall, the function attempts to compute per-condition summary statistics for an array of run records, but several logic errors corrupt the data, collapse conditions together, or misreport aggregates.

---

## Bug 1 – Assignment in filter instead of comparison (data corruption)

- **Location:** `const completedRuns = runs.filter((run) => run.completed = true);`
- **Severity:** Critical

### What is wrong
The `filter` predicate uses **assignment** (`=`) instead of a boolean test (`===` or just the property value). This line both mutates each `run` and always returns `true` for the callback, so **every** element passes the filter.

### Impact
1. **Data mutation:** Every run in the original `runs` array is modified so that `run.completed` becomes `true`, destroying any distinction between completed and incomplete runs.
2. **Completed set is wrong:** `completedRuns` ends up containing all runs instead of only completed ones.
3. **Downstream metrics are misleading:** `completed_runs` in the returned object is always `runs.length`. Any later logic that depends on an accurate `completed` flag operates on corrupted data.

### Proposed fix
```js
const completedRuns = runs.filter((run) => run.completed === true);
```

---

## Bug 2 – `toLowerCase` used without calling it (grouping collapses)

- **Location:** `const key = run.condition.toLowerCase;`
- **Severity:** Critical

### What is wrong
`String.prototype.toLowerCase` is a function, but here it is **referenced, not invoked**. `key` becomes a reference to the `toLowerCase` function object rather than a lowercased string.

### Impact
1. **All runs share the same key:** The function reference is stringified, so every run maps into the **same** bucket.
2. **Loss of per-condition statistics:** Instead of separate entries for each condition, there is effectively a single aggregate row.
3. **Makes other bugs harder to see:** With only one bucket, completion rates and mean durations may look superficially plausible.

### Proposed fix
```js
const key = run.condition.toLowerCase();
```

---

## Bug 3 – Incorrect rounding: `Math.round` ignores precision argument

- **Location:** `mean_duration: Math.round(item.duration / item.count, 2),`
- **Severity:** Medium

### What is wrong
`Math.round` in JavaScript accepts **one argument**. The second argument (`2`) is silently ignored. This rounds to the nearest integer rather than to two decimal places.

### Proposed fix
```js
mean_duration: Number((item.duration / item.count).toFixed(2)),
```

---

## Bug 4 – Completion rate uses global denominator instead of per-condition count

- **Location:** `completion_rate: item.completed / runs.length,`
- **Severity:** Medium

### What is wrong
`completion_rate` divides completed runs **for this condition** by the **total number of runs across all conditions**.

### Proposed fix
```js
completion_rate: item.count === 0 ? 0 : item.completed / item.count,
```

---

## Bug 5 – Sort comparator returns boolean instead of numeric difference

- **Location:** `rows.sort((a, b) => a.mean_duration > b.mean_duration);`
- **Severity:** Medium

### What is wrong
`Array.prototype.sort` expects a **negative/zero/positive** number. The comparator returns a boolean, which never returns negative, so items are not reliably ordered.

### Proposed fix
```js
rows.sort((a, b) => a.mean_duration - b.mean_duration);
```

---

## Bonus Observation – Ambiguity in overall `meanDuration`

- **Location:** `totalDuration` sums all runs, `meanDuration` divides by `completedRuns.length`
- **Severity:** Semantic/requirements issue

### Description
`totalDuration` sums **all** run durations regardless of completion status, while the divisor is intended to be completed runs only. Bug 1 currently hides this because it forces all runs into `completedRuns`.

### Suggested fix
Clarify intent and align numerator/denominator.
