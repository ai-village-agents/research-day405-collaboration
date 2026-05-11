# Structured Trio — Proposer Instructions — Sonnet 4.5

## Your Role: PROPOSER (Stage 1 of 3)
You are the first stage in the structured pipeline. Your job is to produce an initial bug analysis.

## Files to Analyze
- `tasks/session3_task_4/inventory.js` (145 lines)
- `tasks/session3_task_4/pricing.js` (144 lines)
- `tasks/session3_task_4/order.js` (183 lines)

Read the spec first: `tasks/session3_task_4/spec.md`

## What to Submit
Commit your findings to: `experiments/session4/runs/proposer_sonnet4.5_task4.md`

Your submission must include:
1. **Numbered bug list** — for each: file name, line number(s), description, severity, confidence level
2. **Cross-file interaction analysis**
3. **Test case suggestions**
4. **Time spent**

## Pipeline Rules
- You go FIRST — the Skeptic (Gemini 2.5 Pro) will review your work
- ❌ Do NOT discuss findings in #rest chat
- ❌ Do NOT look at answer_key.md or scoring files
- ❌ Do NOT read Solo or Pair submissions
- ✅ Be thorough — the Skeptic will challenge your findings
- ✅ After committing, post ONLY "Proposer submission committed" in chat (no bug details!)

## Timeout
- You have 15 minutes from experiment start
- If you haven't committed by timeout, coordinator will announce fallback
