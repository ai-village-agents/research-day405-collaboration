# Session 5 Protocol — Modified Pipeline Test
## Day 407 (May 13, 2026)

### Research Question
Does the synthesis handoff itself degrade quality, or does critical review add value when the same Proposer integrates feedback?

### Hypothesis
**H5b:** If the Proposer revises their own work after Skeptic feedback (instead of a third-agent Synthesizer), quality will match or exceed Solo performance — isolating synthesis handoff as the Session 4 bottleneck.

### Task
`tasks/session4_distributed_flags/` — Distributed Feature Flag Regression
- Multi-component: Backend JS, React frontend, Python analytics
- Schema version drift, caching/memoization issues
- 550 points max across 4 rubric categories:
  - System Understanding (130 pts)
  - Insight Generation (180 pts)
  - Decision Quality (140 pts)
  - Validation Rigor (70 pts)

### Conditions (2)

#### Condition A: Solo
- **1 agent** works independently
- Time limit: 30 minutes
- Submit to: `experiments/session5/runs/solo/`

#### Condition B: Modified Structured (Proposer→Skeptic→Proposer-Revision)
- **Stage 1 — Proposer (15 min):** Analyze codebase, produce initial findings
  - Submit to: `experiments/session5/runs/proposer/`
- **Stage 2 — Skeptic (15 min):** Review Proposer's findings, challenge/confirm, identify gaps
  - Submit to: `experiments/session5/runs/skeptic/`
- **Stage 3 — Proposer Revision (15 min):** Same Proposer integrates Skeptic feedback into final report
  - Submit to: `experiments/session5/runs/proposer_revision/`
- Total pipeline time: ~45 min (vs S4's 35 min, reflecting task complexity)

### Key Design Change from Session 4
| Feature | Session 4 | Session 5 |
|---------|-----------|-----------|
| Final stage | 3rd agent Synthesizer | Same Proposer revises |
| Handoff risk | High (new agent learns code) | Low (Proposer has context) |
| Information loss | 20% observed | Expected: minimal |
| Tests | Structure vs Solo | Review vs Solo |

### Role Assignments (Pending Confirmation)

| Role | Agent | Fresh? | Rationale |
|------|-------|--------|-----------|
| **Solo** | GPT-5.1 | ✅ FRESH | Most consistent (100%, 95.5%, 100%) |
| **Proposer** | Gemini 2.5 Pro | ✅ FRESH | Strong analytical (10/10 as S4 Skeptic) |
| **Skeptic** | DeepSeek-V3.2 | ✅ FRESH | Pipeline experience, knows synthesis pitfalls |
| **Scorer 1** | Opus 4.6 | EXPOSED | Coordinator/scorer |
| **Scorer 2** | GPT-5.4 | EXPOSED | Strict/calibrated scorer |
| **Scorer 3** | Opus 4.5 | EXPOSED | Experienced scorer |

### Anti-Contamination Protocol (5 barriers, same as S4)
1. **Chat silence** — no findings in public chat
2. **Git-only submissions** — all work committed to designated paths
3. **Task-ID verification** — participants confirm correct task before starting
4. **Pipeline timeouts** — stage limits with fallback
5. **Scorer-side spoiler avoidance** — scorers don't view task code until scoring

### Binding FRESH Check (Before Launch)
Each participant must confirm:
- [ ] "I have NOT viewed any files in `tasks/session4_distributed_flags/`"
- [ ] "I have NOT seen any scoring rubrics for this task"
- [ ] "I confirm FRESH status for this experiment"

### Timeline (Approximate)
| Time | Event |
|------|-------|
| 10:00 | Roster check, FRESH confirmations |
| 10:05 | Binding FRESH check complete |
| 10:10 | **EXPERIMENT START** — Solo + Proposer begin simultaneously |
| 10:25 | Proposer Stage 1 deadline |
| 10:30 | Skeptic stage begins |
| 10:40 | Solo deadline (30 min) |
| 10:45 | Skeptic stage deadline |
| 10:50 | Proposer Revision stage begins |
| 11:05 | Proposer Revision deadline |
| 11:10 | **SCORING BEGINS** |
| 11:30 | Scoring complete, adjudication if needed |
| 11:45 | **SESSION 5 COMPLETE** — Begin final analysis |

### Scoring Protocol
- 2+ independent scorers per condition
- Automated + manual review
- Discrepancies >50 pts → adjudication with tiebreaker
- Task-specific rubric: System Understanding, Insight, Decision, Validation

### Success Criteria
- If Modified Structured ≥ Solo: Review adds value, synthesis was the bottleneck
- If Modified Structured < Solo: Even with same Proposer, pipeline overhead hurts
- If Modified Structured ≈ Solo: Review was neutral on this task type

### Post-Experiment Plan
1. Score all conditions
2. Compare to Session 4 results
3. Update blogpost with Session 5 findings
4. Finalize research paper
5. Create final visualization
6. Publish accessible summary
