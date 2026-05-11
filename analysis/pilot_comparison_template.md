# Pilot Comparison Template — Session 1

## Runs
| Condition | Participants | Score | Percent | Bugs Found | Fixes | Bonuses | Duration | Submission |
|---|---|---:|---:|---:|---:|---|---|---|
| Solo | GPT-5.1 | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| Unstructured | Claude Opus 4.5 + Claude Sonnet 4.5 | 600/650 | 92.3% | 6/6 | 6/6 | Edge cases + tests | ~15 min | `experiments/pilot/runs/unstructured_pair_FINAL.md` |
| Structured | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Immediate observations
- Unstructured pair achieved complete seeded-bug coverage.
- Denominator under current rubric is 650, not 600.
- We cannot yet evaluate H1 from this pilot because the solo baseline has not been scored and the structured condition has not yet run.

## Planned comparison questions
1. Does collaboration improve seeded-bug coverage relative to solo?
2. Does collaboration improve quality of fixes, not just bug identification?
3. Does collaboration increase bonus edge-case/test-case generation?
4. What is the time cost of collaboration?
5. How much of the unstructured pair's success came from division of labor versus simple redundancy?

## Caution on inference
This pilot is useful as a proof of concept and procedure test, but it is too small to support strong causal claims on its own.
