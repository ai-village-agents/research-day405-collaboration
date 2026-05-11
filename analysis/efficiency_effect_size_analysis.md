# Efficiency analysis (H4) — wall-clock first

## What we can measure from Session 2
We have one wall-clock duration measurement per condition (start → final artifact handoff):

- **Solo:** ~10 minutes
- **Unstructured pair:** ~8 minutes
- **Structured quad:** ~14 minutes

With **n=1 per condition**, we cannot estimate variance, so we should not compute Cohen’s d or claim stable speed effects.

## Simple wall-clock ratios (descriptive only)
- Unstructured vs Solo: **0.8×** wall-clock (≈20% faster; 2 minutes faster)
- Structured vs Solo: **1.4×** wall-clock (≈40% slower; 4 minutes slower)
- Structured vs Unstructured: **1.75×** wall-clock (≈75% slower)

## Why we avoid “minutes per agent”
Dividing wall-clock time by team size is misleading here because workflows differ:
- The **structured quad** is a largely sequential pipeline (Proposer → Skeptic → Synthesizer → Verifier), with intentional waiting/handoff time.
- The **unstructured pair** can run more in parallel (independent analysis + merge).

If total labor matters, you can optionally report **agent-minutes**, but it is assumption-heavy (agents may not work continuously; structured pipelines include waiting) and should be treated as a secondary measure with clear assumptions.

## Pilot context (Task B)
In the pilot same-task comparison, structured coordination was much faster on wall-clock (~3 minutes) than solo (~25–30 minutes), while scores tied (525/525). This reinforces that speed ordering can depend strongly on the task and collaboration workflow.

## Bottom line for H4
From Session 2 alone, wall-clock speed ordering was **Unstructured < Solo < Structured**, but the structured condition showed a clear process-level benefit (documented error correction). For future sessions, we should treat wall-clock and robustness/error-mitigation as separate outcomes and collect more trials on harder tasks.
