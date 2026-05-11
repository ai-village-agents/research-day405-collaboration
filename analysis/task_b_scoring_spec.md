# Task B Scoring Specification (Session 1, Same-Task)

This document is the prespecified Session 1 same-task scoring rubric for `pilot_task_b/task.js`.

## Scope and basis

Scoring is anchored to the seeded answer key. The canonical seeded issues are:

1. Assignment in filter
2. Missing `toLowerCase()` invocation
3. `Math.round` precision misuse
4. Wrong denominator for `completion_rate`
5. Boolean sort comparator

## Base scoring rules

For each of the five canonical seeded issues:

- Award **50 points** for correctly identifying the bug.
- Award **50 points** for proposing a materially correct fix.

This yields a base maximum of **500 points**.

## Optional bonus

- **+25 points** optional bonus for explicitly recognizing and clearly explaining the `meanDuration` numerator/denominator ambiguity.

## Maximum score

- `MAX_SCORE = 525`

## Notes

Task B does not ask for edge-case generation or test-case generation. Therefore, there are no extra bonuses beyond the ambiguity note above.
