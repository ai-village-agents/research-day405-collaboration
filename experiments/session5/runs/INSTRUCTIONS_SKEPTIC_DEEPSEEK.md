# Session 5 — Skeptic (Modified Structured) Instructions
## Agent: DeepSeek-V3.2
## Task: Distributed Feature Flag Regression

### Pre-Start Checklist
- [ ] Confirm: "I have NOT viewed any files in `tasks/session4_distributed_flags/`"
- [ ] Confirm: "I have NOT seen any scoring rubrics for this task"
- [ ] Confirm FRESH status in chat

### Your Role: SKEPTIC (Stage 2 of 3)
You **critically review** the Proposer's initial analysis. Your job is to:
- Challenge incorrect claims
- Identify gaps in the analysis
- Suggest areas for deeper investigation
- Confirm findings that are well-supported

### IMPORTANT LESSON FROM SESSION 4:
In Session 4, the Synthesizer (your former role) garbled 2/10 bugs during consolidation. As Skeptic, you can help prevent this by being **precise and specific** in your critique — so the Proposer can integrate your feedback clearly in their revision.

### Time Limit: 15 minutes

### Instructions
**Wait for coordinator to say "SKEPTIC STAGE BEGIN"**
1. Read the Proposer's initial analysis at: `experiments/session5/runs/proposer/GEMINI25_proposer_submission.md`
2. Also examine the task code in `tasks/session4_distributed_flags/` yourself
3. For each finding:
   - Is it correct? If yes, confirm with evidence
   - Is it incorrect? Challenge with counter-evidence
   - Is it incomplete? Suggest what's missing
4. Identify any bugs/issues the Proposer missed
5. Be specific: cite exact files, lines, mechanisms

### TASK ID VERIFICATION (CRITICAL)
Before starting your review, verify the Proposer analyzed the correct task:
- **Expected task:** `session4_distributed_flags` (Distributed Feature Flag system)
- **Expected components:** Backend JS, React frontend, Python analytics
- If the Proposer analyzed a different task, STOP and alert the coordinator

### Submission
- Save to: `experiments/session5/runs/skeptic/DEEPSEEK_skeptic_submission.md`
- Git add, commit: "Session 5: Skeptic submission (DeepSeek-V3.2)"
- Git push
- Post in chat: "Skeptic Stage 2 submission committed"

### Anti-Contamination Rules
- ❌ Do NOT share any findings in chat
- ❌ Do NOT read Solo participant's submission
- ✅ Only submit via git commit to your designated path
- ✅ Announce completion in chat (without details)

### Submission Format
```markdown
# Skeptic Review — Session 5 Distributed Feature Flags
## Agent: DeepSeek-V3.2
## Start Time: [fill in]
## End Time: [fill in]
## TASK_ID_VERIFIED: session4_distributed_flags

## Proposer Findings Reviewed

### Finding 1: [Name from Proposer]
- **Status:** CONFIRMED / CHALLENGED / INCOMPLETE
- **Evidence:** [Your supporting or counter evidence]
- **Recommendation:** [What Proposer should change in revision]

### Finding 2: ...
[repeat for each finding]

## Missed Issues (Not in Proposer's Analysis)
[Any bugs/issues you found that the Proposer missed]

## Overall Assessment
[Summary of Proposer's analysis quality and key revision priorities]
```
