# Session 5 — Proposer (Modified Structured) Instructions
## Agent: Gemini 2.5 Pro
## Task: Distributed Feature Flag Regression

### Pre-Start Checklist
- [ ] Confirm: "I have NOT viewed any files in `tasks/session4_distributed_flags/`"
- [ ] Confirm: "I have NOT seen any scoring rubrics for this task"
- [ ] Confirm FRESH status in chat

### Your Role: PROPOSER (Stage 1 of 3)
You produce the **initial analysis**. After the Skeptic reviews your work, you will **revise your own analysis** (Stage 3) — you are BOTH Proposer AND final author.

### Stage 1 Time Limit: 15 minutes

### Stage 1 Instructions (Initial Analysis)
1. When the coordinator says "EXPERIMENT START", navigate to `tasks/session4_distributed_flags/`
2. Read the task description and examine all provided code files
3. Analyze the system for bugs, design issues, and failure modes
4. Focus on:
   - **System Understanding:** How the components interact
   - **Insight Generation:** Root causes of failures
   - **Decision Quality:** Actionable recommendations
   - **Validation Rigor:** How to verify your findings
5. Write your initial analysis

### Stage 1 Submission
- Save to: `experiments/session5/runs/proposer/GEMINI25_proposer_submission.md`
- Git add, commit: "Session 5: Proposer initial submission (Gemini 2.5 Pro)"
- Git push
- Post in chat: "Proposer Stage 1 submission committed"

### Stage 3 Instructions (Proposer Revision — after Skeptic review)
**Wait for coordinator to say "PROPOSER REVISION STAGE BEGIN"**
1. Read the Skeptic's review at: `experiments/session5/runs/skeptic/DEEPSEEK_skeptic_submission.md`
2. Integrate the Skeptic's feedback into your analysis
3. Fix any issues the Skeptic identified
4. Add any new findings suggested by the Skeptic
5. Produce your final revised analysis

### Stage 3 Submission
- Save to: `experiments/session5/runs/proposer_revision/GEMINI25_revision_submission.md`
- Git add, commit: "Session 5: Proposer revision submission (Gemini 2.5 Pro)"
- Git push
- Post in chat: "Proposer Revision (Stage 3) committed"

### Stage 3 Time Limit: 15 minutes

### Anti-Contamination Rules
- ❌ Do NOT share any findings in chat
- ❌ Do NOT read Solo participant's submission
- ✅ Only submit via git commit to your designated paths
- ✅ Announce completion in chat (without details)

### Submission Format (use for BOTH Stage 1 and Stage 3)
```markdown
# Proposer [Initial/Revised] Analysis — Session 5 Distributed Feature Flags
## Agent: Gemini 2.5 Pro
## Stage: [1 Initial / 3 Revision]
## Start Time: [fill in]
## End Time: [fill in]
## TASK_ID_VERIFIED: session4_distributed_flags

## 1. System Understanding
[Your analysis of how components interact]

## 2. Insights & Root Causes
[Your identified bugs/issues with evidence]

## 3. Recommendations
[Your actionable fixes]

## 4. Validation Approach
[How to verify each finding]

## 5. [Stage 3 only] Changes from Skeptic Feedback
[What you changed based on Skeptic review, and why]
```
