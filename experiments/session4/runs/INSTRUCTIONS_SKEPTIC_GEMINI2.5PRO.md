# Structured Trio — Skeptic Instructions — Gemini 2.5 Pro

## Your Role: SKEPTIC (Stage 2 of 3)
You review the Proposer's bug analysis. Challenge weak claims, add missed bugs, correct errors.

## ⚠️ TASK VERIFICATION (MANDATORY)
Before doing ANY analysis, confirm you are reviewing the correct task:
- **Task:** Session 3 Task 4 — Order Processing System
- **Files:** inventory.js, pricing.js, order.js
- **Domain:** E-commerce order processing
- Include this line in your submission: `TASK_ID_VERIFIED: session3_task_4 (Order Processing — inventory.js, pricing.js, order.js)`

If anything seems wrong (wrong files, wrong domain), STOP and alert the coordinator in chat.

## What to Do
1. Read the Proposer's submission at: `experiments/session4/runs/proposer_sonnet4.5_task4.md`
2. Also read the original files at `tasks/session3_task_4/`
3. For each proposed bug: verify or challenge it
4. Look for bugs the Proposer missed
5. Check for cross-file interactions

## What to Submit
Commit your review to: `experiments/session4/runs/skeptic_gemini2.5pro_task4.md`

Your submission must include:
1. **Task verification line** (see above — MANDATORY)
2. **Review of each Proposer bug** — Confirmed/Challenged with reasoning
3. **Additional bugs found** that Proposer missed
4. **Cross-file interaction analysis**
5. **Time spent**

## Rules
- ❌ Do NOT discuss findings in #rest chat
- ❌ Do NOT look at answer_key.md or scoring files
- ❌ Do NOT start until Proposer has committed
- ✅ Challenge weak claims with specific reasoning
- ✅ After committing, post ONLY "Skeptic submission committed" in chat
