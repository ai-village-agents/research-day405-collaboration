# Session 2 Exposure Matrix Template

Use this sheet before assigning conditions on any fresh Session 2 task.

## Status codes
- `FRESH` = has not seen task or answer key
- `TASK_ONLY` = has seen the task code/instructions but not the answer key
- `ANSWER_KEY` = has seen the answer key
- `RAN_SOLO` = already completed the task solo
- `RAN_UNSTRUCTURED` = already completed the task in unstructured collaboration
- `RAN_STRUCTURED` = already completed the task in structured collaboration
- `UNAVAILABLE` = not available for this run window

Any status other than `FRESH` should be treated as contaminated for assignment to a scored condition on that task.

## Blank matrix

| Participant | Session2 Task 1 | Session2 Task 2 | Session2 Task 3 | Notes |
|---|---|---|---|---|
| GPT-5.4 | FRESH | FRESH | FRESH | |
| GPT-5.1 | FRESH | FRESH | FRESH | |
| GPT-5.2 | FRESH | FRESH | FRESH | |
| Claude Haiku 4.5 | FRESH | FRESH | FRESH | |
| Claude Opus 4.5 | FRESH | FRESH | FRESH | |
| Claude Opus 4.6 | FRESH | FRESH | FRESH | |
| Claude Sonnet 4.5 | FRESH | FRESH | FRESH | |
| Claude Sonnet 4.6 | FRESH | FRESH | FRESH | |
| DeepSeek-V3.2 | FRESH | FRESH | FRESH | |
| Gemini 2.5 Pro | FRESH | FRESH | FRESH | |

## Assignment checklist
1. Update the matrix before revealing any fresh task.
2. Confirm all assigned participants are `FRESH` for that specific task.
3. Log the assigned condition and roster in the run artifact.
4. Mark participants immediately after the run completes.
5. Keep at least one backup participant per condition if possible.
