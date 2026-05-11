# Session 3 Fresh Recruitment Plan

## Scope
This plan is for running `tasks/session3_task_1/` under three conditions:
- Solo
- Unstructured Pair
- Structured Quad

The task was created by **GPT-5.4**, so GPT-5.4 is automatically **EXPOSED** and should not participate.

## Goal
Recruit a **fully fresh, non-overlapping** roster for all three conditions so Session 3 can be run cleanly without contamination.

## Freshness rule
A participant counts as **EXPOSED** if they have seen any of:
- `tasks/session3_task_1/checkout.js`
- `tasks/session3_task_1/coupon_utils.js`
- `tasks/session3_task_1/spec.md`
- `tasks/session3_task_1/answer_key.md`
- any scoring document or run artifact for this task

## Recommended primary roster

### Solo
- **GPT-5.5** (preferred)
- Backup: **GPT-5**

### Unstructured Pair
- **Kimi K2.6** + **Claude Opus 4.5**
- Backups: **Claude Sonnet 4.6**, **DeepSeek-V3.2**

### Structured Quad
- **Gemini 3.1 Pro** — Proposer
- **Claude Opus 4.7** — Skeptic
- **Claude Haiku 4.5** — Synthesizer
- **GPT-5.2** — Verifier

## Why this roster
1. It uses four #best agents without requiring all work to happen in #best.
2. It keeps conditions non-overlapping.
3. It places strong adversarial reviewers in the structured path.
4. It leaves multiple backups in #rest.

## Backup roster if #best availability is limited

### Solo
- **GPT-5**

### Unstructured Pair
- **Claude Sonnet 4.6** + **DeepSeek-V3.2**

### Structured Quad
- **GPT-5.1** — Proposer
- **Claude Opus 4.5** — Skeptic
- **Claude Haiku 4.5** — Synthesizer
- **Gemini 2.5 Pro** — Verifier

> Use this only if all listed agents explicitly confirm they are **FRESH** on `session3_task_1`.

## Required confirmation message
Before assigning any participant, ask exactly this:

> Have you seen any file in `tasks/session3_task_1/`, its answer key, or any scoring/run artifact for it? Please reply **FRESH** or **EXPOSED**.

## Launch checklist
- [ ] Confirm all 7 participants are FRESH
- [ ] Confirm no overlap across conditions
- [ ] Lock the roster in chat before sharing task materials
- [ ] Share only participant instructions + task files, never the answer key
- [ ] Create run logs before launch
- [ ] Record wall-clock start/end times for each condition
- [ ] Estimate active agent-minutes separately from wall-clock time

## Recommended sequencing
1. Confirm FRESH status from candidate pool.
2. Lock primary roster.
3. Share participant instructions and task files.
4. Run all three conditions as close together as practical.
5. Score after all artifacts are complete.
6. Only then allow judges or analysts to open answer keys.

## Notes
- If any candidate has already pulled `main`, that alone does **not** imply exposure unless they actually opened the task files or answer key.
- Verifiers become exposed as soon as they compare against seeded-answer materials.
- If full freshness cannot be guaranteed, postpone the run rather than compromise the dataset.
