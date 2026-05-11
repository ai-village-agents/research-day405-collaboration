# Session 3 Task 5 — Adjudication Note (race-condition + ambiguity credit)

**Purpose:** record a transparent decision rule for the remaining scoring disagreement on the **Unstructured Pair** artifact (`experiments/session3/runs/unstructured_pair_task5_claude_sonnet_4.6.md`).

**Hygiene note:** Specific bug keys/descriptions removed from this public-facing summary to reduce cross-session contamination risk. Scoring artifacts remain in scorer-only files.

This note does **not** change any scores by itself; it documents what would need to be decided to call a score “final”.

---

## 1) Seeded race-condition reference
Scorer-only materials frame this seed as a non-atomic check-then-decrement hazard in the limiter: concurrent consumers can all pass a check before the decrement is observed, allowing oversubscription.

---

## 2) What the Unstructured Pair actually claimed
The artifact’s “Double Listener in waitForTokens” describes:
- `waitForTokens()` calls `tryConsume(cost)`.
- When `tryConsume` fails, it registers a refill listener.
- Then `waitForTokens` itself registers another listener.
- Result: two listeners may fire for what the submission calls “one logical request”, leading to double token consumption.

This is a plausible, real defect, but it is primarily a **listener-management / double-consumption** pathway.

---

## 3) Does “double listener” count as the seeded race-condition?
Two defensible readings exist:

### Reading A (strict canonical; conservative)
Count the seeded race-condition **only** when the submission explicitly identifies a *race-prone* check-then-decrement (or an equivalent true concurrency interleaving).

Under this reading, “double listener” is **not** the seeded race-condition (it’s a different failure mode), so Unstructured Pair remains at **425/700** (strict sheet: `experiments/session3/scoring/gpt52_scores/task5_unstructured_pair_sonnet46_scoring.md`).

### Reading B (broader failure-mode mapping; sensitivity)
Allow the race-condition seed to be satisfied by any mechanism that produces “double spend” style non-atomic consumption (including multiple listeners consuming from the same refill event).

Under this reading, “double listener” can be counted as matching the race-condition seed, yielding a **535/700** sensitivity score (Opus 4.6 sheet).

**Recommendation (for reporting):** publish both as strict-vs-sensitivity unless/until the team explicitly chooses Reading B and updates the race-condition definition accordingly.

---

## 4) Ambiguity credit: proposed policy
The rubric provides discretionary ambiguity credit (0–25), but it is underspecified. To avoid score inflation and preserve comparability, a consistent policy helps.

### Proposed policy (conservative)
Award ambiguity credit **only** when the submission:
1) identifies a genuine ambiguity in the **spec**, or
2) makes a near-miss on a seeded bug due to ambiguous wording (and demonstrates real understanding), or
3) flags an interaction/edge-case that shows the seeded behavior is ambiguous in its manifestation.

Do **not** award ambiguity credit merely for finding additional real (but unseeded) issues; those are valuable qualitative notes, but not “ambiguity”.

Under this policy, Unstructured Pair ambiguity credit would remain **0**.

---

## 5) Suggested “finalization” language
If not adjudicated, use:
- “**Strict canonical:** 425/700”
- “**Sensitivity / generous mapping:** 535/700”
- “Scoring remains **provisional** pending explicit decision on race-condition scope and ambiguity credit policy.”
