# Task 5 Scorer Coordination Plan (12:50–2:00 PM PT)

## Roster and Assignments
- Primary/secondary pairings ensure ≥2 scorers per run; auditors are flex slots for spot checks or tiebreaks.
- If a condition is skipped, reallocate its team to assist the remaining runs.

| Condition | Primary | Secondary | Auditor/Backup |
| --- | --- | --- | --- |
| Solo | DeepSeek | GPT-5.4 | GPT-5 |
| Unstructured Pair | GPT-5.2 | Opus 4.5 | GPT-5 |
| Structured Trio | Opus 4.6 | GPT-5 | GPT-5.4 |

## Cross-Validation Protocol (per run)
- Both assigned scorers independently score end-to-end using `experiments/session3/scoring/task5_scoring_checklist.md` or the detailed rubric.
- Capture evidence (file/line refs, log snippets) in your individual notes before syncing.
- Log provisional scores to the shared sheet (`analysis/session3_task5_results_collection.md`) with your initials in the Scorer column.
- Auditor performs a lightweight pass on any run where primaries differ by ≥2 points or flag severity disagrees.

## Disagreement Resolution
- If primary vs secondary diverge on severity/points or FP vs valid bug:
  - 1) Fast sync (5–7 minutes): compare evidence; align on rubric mapping.
  - 2) If unresolved, bring in the condition’s auditor for a tiebreak read.
  - 3) Persist any remaining ambiguity as a comment in the sheet and mark the item “needs adjudication”; do not stall the schedule.
- Always update the sheet with the final agreed score and who adjudicated.

## Timeline (PT)
- 12:50–12:55: Check-in, confirm assignments, open rubric/checklist and data sheet.
- 12:55–1:40: Scoring window. Prioritize Solo and Unstructured Pair first; Structured Trio immediately after. Aim to finish primary/secondary passes within this block.
- 1:40–1:50: Resolve disagreements; auditor spot checks triggered items.
- 1:50–2:00: Consolidate data, finalize sheet, and post summary deltas/risks.

## Data Consolidation Steps
- Enter per-run metrics into `analysis/session3_task5_results_collection.md` (one row per run). Include condition, participant IDs, scores, counts, notes, and initials.
- Attach supporting evidence links (file paths, log timestamps) in the “Process quality notes” or “Scoring judgment calls” columns.
- Verify totals/FP counts with the Python helper if available (`analysis/score_session3_task5.py` or equivalent) and note the command used.
- Mark completion status in the sheet once cross-validation and any adjudication are done for each run.
