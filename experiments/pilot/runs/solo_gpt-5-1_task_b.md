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
3. **Downstream metrics are misleading:**
   - `completed_runs` in the returned object is always `runs.length`.
   - Any later logic that depends on an accurate `completed` flag (e.g., completion-rate calculations per condition) operates on corrupted data.

Because this line rewrites the input array and mislabels completion for all runs, it compromises essentially all downstream statistics. That’s why I rate it as **critical**.

### Proposed fix
Use a pure boolean predicate without assignment, for example:

```js
const completedRuns = runs.filter((run) => run.completed === true);
// or simply
// const completedRuns = runs.filter((run) => run.completed);
```

---

## Bug 2 – `toLowerCase` used without calling it (grouping collapses)

- **Location:** `const key = run.condition.toLowerCase;`
- **Severity:** Critical

### What is wrong
`String.prototype.toLowerCase` is a function, but here it is **referenced, not invoked**. `key` becomes a reference to the `toLowerCase` function object rather than a lowercased string like `'solo'` or `'unstructured'`.

### Impact
1. **All runs share the same key:** When used as a property name on the `conditions` object, this function reference is stringified (e.g. `'function toLowerCase() { [native code] }'`), so every run maps into the **same** bucket.
2. **Loss of per-condition statistics:** Instead of separate entries for `'Solo'`, `'Structured_Cross_Check'`, and `'Unstructured'`, there is effectively a single aggregate row for “everything”.
3. **Makes other bugs harder to see:** With only one bucket, completion rates and mean durations may look superficially plausible, masking logic issues elsewhere.

Because this destroys the entire per-condition breakdown that the function is supposed to compute, I consider this a **critical** defect.

### Proposed fix
Call `toLowerCase()` and consider normalizing whitespace as well:

```js
const key = run.condition.toLowerCase();
// optionally: .trim() if inputs may include stray spaces
```

---

## Bug 3 – Incorrect rounding: `Math.round` ignores precision argument

- **Location:** `mean_duration: Math.round(item.duration / item.count, 2),`
- **Severity:** Medium

### What is wrong
`Math.round` in JavaScript accepts **one argument**. The second argument (`2`) is silently ignored. As written, this rounds to the nearest integer minute rather than to two decimal places as the caller likely intended.

### Impact
- Reported `mean_duration` values lose sub-minute precision and may differ significantly from the true average when durations vary.
- The presence of the unused `2` strongly suggests the author expected two decimal places, so this is a clear logic mismatch, not just a formatting choice.

### Proposed fix
Explicitly round to two decimal places, for example:

```js
const mean = item.duration / item.count;
const mean_duration = Number(mean.toFixed(2));
```

and then in the returned object:

```js
mean_duration,
```

or equivalently:

```js
mean_duration: Math.round((item.duration / item.count) * 100) / 100,
```

---

## Bug 4 – Completion rate uses global denominator instead of per-condition count

- **Location:** `completion_rate: item.completed / runs.length,`
- **Severity:** Medium

### What is wrong
`completion_rate` is computed by dividing the number of completed runs **for this condition** by the **total number of runs across all conditions**.

If there are multiple conditions with different sample sizes, this yields misleading values—for example, a condition with 2/2 completions and one with 1/10 completions will both be normalized by `runs.length`, not their own counts.

### Impact
- Per-condition completion rates are systematically distorted, especially when conditions have unequal numbers of runs.
- In extreme cases (many conditions, each with few runs) most completion rates will appear artificially small.

### Proposed fix
Use the condition’s own count as the denominator:

```js
completion_rate: item.count === 0 ? 0 : item.completed / item.count,
```

This correctly reports, for each condition, the fraction of its runs that completed.

---

## Bug 5 – Sort comparator returns boolean instead of numeric difference

- **Location:** `rows.sort((a, b) => a.mean_duration > b.mean_duration);`
- **Severity:** Medium

### What is wrong
`Array.prototype.sort` expects the comparator to return a **negative number**, **zero**, or a **positive number** to indicate ordering. Here, the comparator returns a boolean (`true` or `false`), which is coerced to `1` or `0`.

This produces a comparator that never returns a negative value, so items are not reliably ordered from smallest to largest `mean_duration`. The resulting order is unstable and engine-dependent.

### Impact
- The `rows` array will not be reliably sorted by `mean_duration`, defeating the intent of the sort.
- In some engines the output may appear “almost sorted” in simple cases, which could hide the bug during casual testing.

### Proposed fix
Return the numeric difference between the two means:

```js
rows.sort((a, b) => a.mean_duration - b.mean_duration);
```

This sorts rows in ascending order of mean duration.

---

## Bonus Observation – Ambiguity in overall `meanDuration`

- **Location:**
  - `const totalDuration = runs.reduce((sum, run) => sum + run.duration_min, 0);`
  - `const meanDuration = totalDuration / completedRuns.length;`
- **Severity:** Not scored as a core bug; semantic/requirements issue

### Description
`totalDuration` sums **all** run durations, regardless of completion status, while the divisor `completedRuns.length` is intended to be the number of completed runs. If the goal is "average duration of completed runs", the numerator should also be restricted to completed runs. If the goal is "average duration of all runs", the denominator should be `runs.length`.

Complicating this further, Bug 1 currently forces `completedRuns` to contain all runs, which hides this inconsistency in the demo data (the two denominators become equal). Once Bug 1 is fixed, the tension between the numerator and denominator becomes visible.

### Suggested clarification/fix
Clarify the intended definition and adjust both numerator and denominator to match. For example, if the intention is to average over completed runs only:

```js
const completedRuns = runs.filter((run) => run.completed);
const totalCompletedDuration = completedRuns.reduce(
  (sum, run) => sum + run.duration_min,
  0
);
const meanDuration =
  completedRuns.length === 0 ? 0 : totalCompletedDuration / completedRuns.length;
```

Alternatively, if the statistic should cover all runs, both numerator and denominator should use all runs:

```js
const meanDuration = runs.length === 0 ? 0 : totalDuration / runs.length;
```

---

## Summary of Proposed Fixed Shape

After addressing the issues above, a corrected version of the core logic could look like:

```js
function summarizeRuns(runs) {
  const completedRuns = runs.filter((run) => run.completed);
  const totalCompletedDuration = completedRuns.reduce(
    (sum, run) => sum + run.duration_min,
    0
  );
  const meanDuration =
    completedRuns.length === 0 ? 0 : totalCompletedDuration / completedRuns.length;

  const conditions = {};
  for (const run of runs) {
    const key = run.condition.toLowerCase();
    if (!conditions[key]) {
      conditions[key] = { count: 0, duration: 0, completed: 0 };
    }
    conditions[key].count += 1;
    conditions[key].duration += run.duration_min;
    if (run.completed) {
      conditions[key].completed += 1;
    }
  }

  const rows = Object.keys(conditions).map((key) => {
    const item = conditions[key];
    const mean = item.count === 0 ? 0 : item.duration / item.count;
    return {
      condition: key,
      runs: item.count,
      mean_duration: Number(mean.toFixed(2)),
      completion_rate: item.count === 0 ? 0 : item.completed / item.count,
    };
  });

  rows.sort((a, b) => a.mean_duration - b.mean_duration);

  return {
    total_runs: runs.length,
    completed_runs: completedRuns.length,
    mean_duration: meanDuration,
    rows,
  };
}
```

This keeps the original structure but ensures completed flags are not corrupted, conditions are grouped correctly, per-condition statistics are accurate, and the output is sorted as intended.
