# Output C — Pilot Experiment

**Task:** pilot_task_b/task.js (summarizeRuns function)  
**Condition:** [BLINDED]  
**Participant(s):** [BLINDED]

---

## Bug Report Summary

| Bug | Location | Severity | Identified | Fix Correct |
|-----|----------|----------|------------|-------------|
| 1 | filter predicate | Critical | ✅ | ✅ |
| 2 | toLowerCase reference | Critical | ✅ | ✅ |
| 3 | Math.round precision | Medium | ✅ | ✅ |
| 4 | completion_rate denominator | Medium | ✅ | ✅ |
| 5 | sort comparator | Medium | ✅ | ✅ |
| Bonus | meanDuration ambiguity | N/A | ✅ | ✅ |

## Bugs Found: 5/5 + bonus
## Fixes Correct: 5/5 + bonus

---

## Bug Details

### Bug 1: Assignment in filter
- Identified assignment (`=`) instead of comparison (`===`) in filter predicate
- Noted data mutation and downstream corruption effects
- Fix: `run.completed === true` or `run.completed`

### Bug 2: toLowerCase not invoked
- Identified function reference instead of function call
- Noted all runs collapse to single bucket
- Fix: `run.condition.toLowerCase()`

### Bug 3: Math.round precision
- Identified that Math.round ignores second argument in JS
- Noted loss of sub-minute precision
- Fix: `.toFixed(2)` or multiply/divide by 100

### Bug 4: Wrong denominator
- Identified `runs.length` should be `item.count` for per-condition rate
- Noted systematic distortion across conditions
- Fix: `item.completed / item.count`

### Bug 5: Boolean sort comparator
- Identified boolean return instead of numeric difference
- Noted unstable/engine-dependent ordering
- Fix: `a.mean_duration - b.mean_duration`

### Bonus: meanDuration ambiguity
- Explicitly explained numerator/denominator mismatch
- Noted Bug 1 masks this issue by making denominators equal
- Provided two alternative fixes depending on intended semantics

---

## Additional Notes
- Provided comprehensive corrected code
- Clear severity classifications
- Noted bug interaction effects
