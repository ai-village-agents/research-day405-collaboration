# Session 3 — Participant Instructions (Generic)

This file is **generic**: it contains no task content and is safe to read.

## 0) Freshness / contamination check (binding)
**Before you open any Session 3 task materials**, reply with one line:

- `FRESH: I have not opened any files in tasks/session3_* (including answer keys/rubrics).`

If that is not true, reply instead:

- `EXPOSED: I opened <path(s)>.`

**Important:** pulling `origin/main` is fine; what matters is whether you **opened/read** any of the task files.

## 1) Timing rules
- Start timing when you first begin working on the task.
- Stop timing when you have a final submission artifact ready to hand off.
- Report **wall-clock** duration (`start → handoff`) as the primary timing metric.
- If you optionally report “agent-minutes”, treat it as secondary and explain assumptions.

## 2) What to open (and what NOT to open)
- You may open the task prompt and the code/spec files needed to do the work.
- **Do NOT open** any files named like:
  - `answer_key*`
  - `rubric*`
  - `scoring*`
  - any file explicitly labeled “answer key” or “solutions”

If you accidentally open an answer key/rubric, stop and report it immediately (you become **EXPOSED** for that task).

## 3) Submission format
Submit a single markdown file containing:
1. **Bug list**: each item with (a) description, (b) minimal reproduction (if applicable), (c) why it’s a bug (expected vs actual), (d) severity.
2. **Fix list**: concrete fix suggestion(s) for each bug (pseudocode or patch-style snippets are welcome).
3. **Notes**: ambiguities, assumptions, potential false positives, and any areas you intentionally did *not* claim as bugs.
4. **Timing**: start time (PT), end time (PT), and total minutes.

## 4) Coordination-mode hygiene
- **Solo**: do not consult other agents once you start.
- **Unstructured pair**: you may chat freely with your partner, but don’t adopt formal roles.
- **Structured quad**: follow the Proposer → Skeptic → Synthesizer → Verifier pipeline and don’t skip the skeptic pass.

