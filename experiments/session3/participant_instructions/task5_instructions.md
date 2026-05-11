# Session 3 — Task 5: API Rate Limiter — Participant Instructions

## What you do
- Review a three-file API rate limiter (token bucket core, Express middleware, config loader) plus the accompanying spec.
- Find real bugs, incorrect behavior, and cross-file interaction issues; avoid speculative or unsubstantiated claims.
- Keep this participant-safe: do not seek out answer keys or scoring scripts.

## Collaboration conditions
- **Solo:** Work independently. Capture notes and decisions in your run file.
- **Unstructured Pair:** Two participants collaborate freely (voice/text OK). Make sure both review all three files and align on the final bug list before submitting.
- **Structured Quad:** Four participants with roles — Proposer → Skeptic → Synthesizer → Verifier. Proposer surfaces candidate issues, Skeptic challenges/validates, Synthesizer records agreed items, Verifier sanity-checks and looks for omissions. Rotate roles only if agreed in advance; keep the pipeline tight and time-boxed.

## Timing protocol (wall clock)
- Record the **start time (PT)** the moment you begin examining the task materials.
- Record the **end time (PT)** when the final report is complete.
- Note total wall-clock duration and any interruptions or tool failures in the metadata section.

## Deliverable
- Make a copy of `experiments/session3/runs/task5_run_template.md` into `experiments/session3/runs/task5_[condition]_[participants].md` and fill it out.
- Include binding FRESH/EXPOSED confirmations, condition, team roster, and any assigned roles.
- Bug report format (see template Sections A–C):
  - For each bug: what it is, why it violates the spec/invariant/edge case, minimal repro if applicable, and risk/severity.
  - For each fix: file/function, the concrete change, why it is correct, and side effects or new tests needed.
  - Tests/verification plan: unit/property/concurrency checks you would run.
- Keep the report participant-safe; do not include spoilers or references to scoring logic.

## Contamination control reminders
- Do **not** open or reference answer keys, scoring scripts, or prior solutions.
- Confirm you have not previously completed this task and are only using the provided repository materials.
- If anything feels familiar or contaminated, stop and flag it before proceeding.
