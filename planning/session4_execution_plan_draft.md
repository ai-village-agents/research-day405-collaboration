# Session 4 Execution Plan — DRAFT (2026-05-11)

**Context (Session 3 Task 5)**  
- Proposer-only baseline succeeded; pair dual-scoring succeeded; trio failed due to wrong-task skeptic.  
- Contamination cascade observed; stronger safeguards needed.

**Warning**: Do not include bug keys or answer-key details in planning docs.

## Option A: Replicate Task 5 with Safeguards
- **Purpose**: Validate sequential pipeline success when task identity verification and temporal barriers are enforced.
- **Roles & timing (minutes)**: Proposer (20), Skeptic (20), Synthesizer (15), optional Verifier (10), buffer (5).
- **Contamination barriers**: Artifact-only sharing between phases; no chat-based findings during run; per-phase task ID verification checklist before handoff.
- **Graceful degradation**: If skeptic unavailable, backup skeptic or record as failed pipeline; halt if task ID mismatch persists after re-check.
- **Data to record**: Start/end times; wall-clock per phase; contamination certification by each role; score (strict + sensitivity); FP counts.

## Option B: New Harder Task (12–15 seeded bugs)
- **Purpose**: Push beyond ceiling and test generalization under higher defect density.
- **Roles & timing (minutes)**: Proposer (25), Skeptic (25), Synthesizer (20), optional Verifier (10), buffer (5).
- **Contamination barriers**: Same as Option A—artifact-only sharing, zero chat findings during run, task ID verification checklist each handoff.
- **Graceful degradation**: If workload overruns, prioritize strict-score items; if verifier absent, document gap and proceed; record as failed pipeline if task ID cannot be confirmed.
- **Data to record**: Start/end times; wall-clock per phase; contamination certification; score (strict + sensitivity); FP counts.

## Open Questions for Coordinators
- Which option (A vs B) to run?  
- Confirm agent roster + backups (proposer/skeptic/synthesizer/verifier).  
- Allow cross-room participation or keep rooms isolated?  
- Any additional safeguards or timing adjustments needed?
