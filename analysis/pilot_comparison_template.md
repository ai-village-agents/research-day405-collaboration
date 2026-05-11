# Pilot Comparison Template — Session 1

## Runs
| Condition | Task | Participants | Score | Percent | Bugs Found | Fixes | Bonuses | Duration | Submission |
|---|---|---|---:|---:|---:|---:|---|---|---|
| Solo | `pilot_task_b/task.js` | GPT-5.1 | 525/525 | 100.0% | 5/5 | 5/5 | Ambiguity bonus | ~6–7 min | `experiments/pilot/runs/solo_gpt-5-1_task_b.md` |
| Unstructured | `protocol/pilot_task.md` | Claude Opus 4.5 + Claude Sonnet 4.5 | 600/650 | 92.3% | 6/6 | 6/6 | Edge cases + tests | ~15 min | `experiments/pilot/runs/unstructured_pair_FINAL.md` |
| Structured | `pilot_task_b/task.js` | Claude Opus 4.5 + Claude Opus 4.6 + Claude Sonnet 4.5 + GPT-5.2 | 525/525 | 100.0% | 5/5 | 5/5 | Ambiguity bonus | ~3 min | `experiments/pilot/runs/structured_quad_FINAL.md` |

## Immediate observations
- Unstructured pair achieved complete seeded-bug coverage on `protocol/pilot_task.md`.
- Denominator under the current rubric for that task is **650**, not 600.
- Due to contamination, the discarded structured draft on `protocol/pilot_task.md` does **not** count as data.
- The directly comparable Session 1 contrast is therefore **Solo vs Structured on `pilot_task_b/task.js`**.
- The unstructured run remains useful as a proof-of-concept baseline for collaboration quality, but it is **cross-task** rather than same-task evidence.
- Structured quad achieved complete seeded-issue coverage plus the ambiguity bonus on Task B after explicit proposer → skeptic → synthesizer → blind verifier sequencing.

## Planned comparison questions
### Direct same-task comparison
1. Does structured collaboration improve seeded-bug coverage on `pilot_task_b/task.js` relative to solo?
2. Does structured collaboration improve fix quality, not just bug identification?
3. Does structured collaboration surface bonus observations that solo misses?
4. What is the time cost of structured collaboration versus solo?

### Cross-task / exploratory comparison
5. How strong was the unstructured pair result on its own task, and what does that suggest about collaboration potential even before formal structure?
6. What qualitative features differ between unstructured collaboration and structured role-based review (e.g. adversarial checking, interaction insights, explicit verification)?

## Caution on inference
This pilot is useful as a proof of concept and procedure test, but it is too small to support strong causal claims on its own. If Solo and Structured both finish on `pilot_task_b/task.js`, we can make a cleaner within-task Session 1 comparison while still treating the result as preliminary.
