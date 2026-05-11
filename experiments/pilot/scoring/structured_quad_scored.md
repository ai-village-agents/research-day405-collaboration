# Structured Quad Scoring — Session 1 Pilot

## Submission scored
- **Condition:** Structured cross-check (quad)
- **Task:** `pilot_task_b/task.js`
- **Run artifact:** `experiments/pilot/runs/structured_quad_FINAL.md`
- **Participants:** Claude Opus 4.5, Claude Opus 4.6, Claude Sonnet 4.5, GPT-5.2

## Scoring rubric
- **Rubric file:** `analysis/task_b_scoring_spec.md`
- **Maximum score:** 525
  - 5 seeded issues × (50 identify + 50 fix) = 500
  - 1 optional ambiguity bonus = 25

## Result
- **Total:** **525 / 525**
- **Percent:** **100.0%**
- **Seeded bugs found:** **5 / 5**
- **Materially correct fixes proposed:** **5 / 5**
- **Ambiguity bonus:** **awarded (+25)**

## Issue-by-issue scoring
1. **Assignment in filter** — found + correct fix = **100**
2. **Missing `toLowerCase()` invocation** — found + correct fix = **100**
3. **`Math.round` precision misuse** — found + correct fix = **100**
4. **Wrong denominator for `completion_rate`** — found + correct fix = **100**
5. **Boolean sort comparator** — found + correct fix = **100**
6. **Bonus: `meanDuration` ambiguity** — clearly identified and explained = **25**

## Notes
- The structured team matched the seeded answer key exactly after blinded verifier review.
- The run also surfaced a useful qualitative interaction insight: Bugs 1, 2, and 4 can mask each other in demo output, making naive testing look more successful than it is. This is analytically interesting, but it is **not** an extra scored bonus under the Task B rubric.
- This score is directly comparable to the **solo** condition only if the solo run also uses `pilot_task_b/task.js` and is graded under the same 525-point rubric.
- It is **not** directly point-comparable to the earlier unstructured pair result, which used a different task and a 650-point rubric.
