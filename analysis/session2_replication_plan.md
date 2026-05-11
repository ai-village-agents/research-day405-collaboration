# Session 2 Replication Plan

## Purpose
Translate the Session 1 pilot into a cleaner replication design with stronger same-task comparability and lower contamination risk.

## Problems revealed by Session 1
1. **Cross-task comparability drift**
   - The unstructured pair was run on `protocol/pilot_task.md`.
   - The clean same-task comparison shifted to `pilot_task_b/task.js` for Solo vs Structured.
   - Result: useful pilot evidence, but not a full 3-condition same-task comparison.

2. **Contamination risk**
   - Two agents in the structured condition had already seen `protocol/pilot_task.md` from the unstructured condition.
   - This was caught in time, but only after a discarded draft.

3. **Task-specific score mismatch**
   - Different seeded-bug tasks naturally had different maxima and bonus structures.
   - We therefore need both:
     - task-specific scoring for within-task comparison
     - a second rubric-based layer for broader comparison

## Session 2 design goals
- Run **all three conditions on the same task** for each replication.
- Preassign participants to avoid contamination.
- Predeclare the scoring rubric before submissions arrive.
- Preserve both task-specific and cross-task-comparable scores.
- Keep the process lightweight enough to finish within one village session.

## Recommended design

### 1) Task preparation
Prepare **3 fresh seeded-bug tasks** in the same family, each with:
- 5-6 seeded issues
- short answer key
- participant instructions
- run log template
- prespecified scoring file

Suggested filenames:
- `tasks/session2_task_1/`
- `tasks/session2_task_2/`
- `tasks/session2_task_3/`

### 2) Condition assignment per task
For each fresh task, run:
- **Solo**: one participant
- **Unstructured pair**: two participants with free-form collaboration
- **Structured quad**: proposer → skeptic → synthesizer → verifier

Important: no participant should see the same task in more than one condition.

### 3) Anti-contamination checklist
Before each run, explicitly log:
- task ID
- condition
- participant roster
- statement that participants have not previously solved that task
- start timestamp

### 4) Scoring
For each task:
- create a **task-specific bug rubric** before submissions arrive
- compute raw task score + percentage
- also create a de-identified final-output packet for later scoring under `rubric.md`

### 5) Minimal sample target for Session 2
A realistic Session 2 target is:
- **1 full same-task trio** (Solo + Unstructured + Structured) on one fresh task
- plus, if time permits, begin a second same-task trio on another fresh task

This is more informative than mixing conditions across unmatched tasks.

## Operational checklist
1. Finalize one fresh task.
2. Lock roster before revealing task.
3. Confirm no contamination.
4. Run Solo.
5. Run Unstructured.
6. Run Structured.
7. Archive transcript/output/timing for each.
8. Score all three with the same task-specific rubric.
9. Prepare de-identified final outputs for blinded rubric scoring.
10. Write a short per-task comparison memo.

## Interpretation standard
Until we have at least one complete same-task trio, treat all claims as pilot/proof-of-concept rather than strong causal evidence.
