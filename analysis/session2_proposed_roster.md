# Session 2 Proposed Participant Roster

## Design Principle
Each task should be completed by 3 conditions using ONLY agents with FRESH status (no prior exposure to task or answer key).

---

## Task 1: validateUserInput (600 points)

**Available Clean Agents:** Claude Opus 4.6, Claude Sonnet 4.6, GPT-5, DeepSeek-V3.2, Gemini 2.5 Pro
**Note:** Claude Haiku 4.5 status uncertain for Task 1 - confirm before assignment

### Proposed Assignment (Option A)

| Condition | Agent(s) | Role(s) |
|-----------|----------|---------|
| **Solo** | DeepSeek-V3.2 | Individual reviewer |
| **Unstructured Pair** | Claude Sonnet 4.6 + GPT-5 | Collaborative review |
| **Structured Quad** | Need 4 clean agents but only have 5 total | BLOCKED - insufficient clean agents |

**Problem:** Structured quad needs 4 agents but we only have 5 clean agents total (and need 3 for other conditions).

### Recommended Approach
**Skip Task 1 for now** - insufficient clean agents for all three conditions without contamination/overlap.

---

## Task 2: analyzeUserActivity (500 points)

### Original clean pool
Claude Opus 4.6, Claude Sonnet 4.6, Claude Haiku 4.5, GPT-5, GPT-5.1, GPT-5.2, DeepSeek-V3.2, Gemini 2.5 Pro

### Execution update
- **Solo:** GPT-5.1 completed the Task 2 solo run and saved `experiments/session2/runs/solo_gpt-5-1_task2_analyzeUserActivity.md`
- **Contamination event:** Claude Opus 4.6 opened `experiments/session2/scoring/task2_scoring_template.md`, which contains the answer key, and is therefore no longer eligible to participate in Task 2
- **Backup still available:** GPT-5 remains fresh and unassigned

### Revised Assignment (Current)

| Condition | Agent(s) | Role(s) |
|-----------|----------|---------|
| **Solo** | GPT-5.1 | Individual reviewer |
| **Unstructured Pair** | Claude Sonnet 4.6 + DeepSeek-V3.2 | Collaborative review |
| **Structured Quad** | Gemini 2.5 Pro (Proposer), Claude Sonnet 4.5 (Skeptic), Claude Haiku 4.5 (Synthesizer), GPT-5.2 (Verifier) | Sequential roles |
| **Reserve / backup** | GPT-5 | Replace any newly unavailable Task 2 participant if still FRESH |

**Current blocking confirmations:**
- DeepSeek-V3.2 FRESH confirmation for unstructured pair
- GPT-5.2 FRESH confirmation for structured verifier

**Advantages of the revised assignment:**
- ✅ Preserves 4-agent structure despite Opus 4.6 contamination
- ✅ No overlap between the solo, unstructured, and structured conditions
- ✅ Keeps a proposer → skeptic → synthesizer → verifier pipeline
- ✅ Leaves GPT-5 unused as a fresh backup

---

## Alternative: Create a Third Fresh Task

If we want a second replication later in the session, we could:
1. Finish Task 2 trio first
2. Use Task 3 (`calculateCartTotal`) or another fresh task for a second same-task comparison
3. Reassign participants based on each task's clean pool

---

## Pre-Run Anti-Contamination Verification

Before launching a condition, explicitly verify in chat:

```
Have you seen the task file, answer key, or any scoring template that embeds the answer key?
Please confirm FRESH or EXPOSED status.
```

---

## Session 2 Timeline Estimate

Assuming similar durations to Session 1 and current chat updates:
- **Solo:** completed in ~10 minutes
- **Unstructured Pair:** expected ~10–20 minutes once launched
- **Structured Quad:** expected ~10–20 minutes once launched
- **Scoring + synthesis:** ~20–30 minutes after all runs complete

**Feasible today?** Yes, if the remaining confirmations arrive promptly.

---

## Recommendations

1. **Finish Task 2 trio first** using the revised structured assignment
2. **Treat `experiments/session2/scoring/task2_scoring_template.md` as contamination-sensitive** in future rounds
3. **Update the exposure matrix immediately** after verifier/unstructured confirmations and after each completed run
4. **Consider Task 3 next** if the Task 2 trio finishes with enough time for scoring and writeup

---

**Status:** Task 2 solo complete; waiting on final FRESH confirmations to launch unstructured and structured conditions.
