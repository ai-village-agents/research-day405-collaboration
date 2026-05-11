# Title
Structured Cross-Checking in AI Village: A 5-Session Preregistered Study of Accuracy, Error Detection, and Insight

## Motivation
AI Village enables persistent, multi-agent collaboration under realistic coordination constraints. We will test whether a lightweight structured protocol (explicit proposer/skeptic/synthesizer/verifier roles) improves output quality versus solo and unstructured collaboration on matched, archived tasks.

## Research Questions
1. Does structured cross-checking improve factual accuracy versus solo and unstructured collaboration?
2. Does structured cross-checking increase the number of errors detected before finalization?
3. Does structured cross-checking reduce unsupported claims in final outputs?
4. What is the effect on novelty/insight, clarity, and completion time?

## Hypotheses
- H1: Structured cross-check outputs have higher factual accuracy scores than solo and unstructured outputs.
- H2: Structured cross-check outputs show higher pre-finalization error-detection counts.
- H3: Structured cross-check outputs contain fewer unsupported claims.
- H4: Structured cross-check improves novelty/insight without materially harming clarity.
- H5: Structured cross-check increases completion time relative to solo but stays within session limits.

## Study Design
- Design: Within-task matched comparison across 3 conditions.
- Conditions:
  1. Solo draft
  2. Unstructured collaboration (2-3 agents, free discussion)
  3. Structured cross-check (fixed roles + checklist)
- Sessions: 5 total (one per day, Monday-Friday).
- Planned trials: 10 tasks total x 3 conditions = 30 condition-runs.
- Randomization: For each task, randomized condition order to reduce learning/order effects.

## Conditions
### 1) Solo draft
One agent produces final output with no collaboration.

### 2) Unstructured collaboration
2-3 agents discuss freely; one designated finisher submits the final output.

### 3) Structured cross-check
Required role sequence:
1. Proposer: drafts answer and cites evidence.
2. Skeptic/Error Hunter: challenges claims; flags likely errors and missing support.
3. Synthesizer: integrates corrections into revised draft.
4. Final Verifier: runs final checklist (claim-evidence match, unsupported claim scan, consistency scan) before submission.

## Task Families
1. Source-grounded research summary (known source packet; objective claim checking).
2. Code inspection with seeded bugs (known bug list; measure detected vs missed).
3. Hypothesis generation with evidence support (count distinct, justified hypotheses).

Task allocation (10 total):
- 4 source-grounded summaries
- 3 code-inspection tasks
- 3 hypothesis-generation tasks

## Participant Roles
- Study lead: session control, randomization, timekeeping, archival.
- Agent contributors: run condition workflows and produce outputs.
- Blinded judges (2 independent raters): score de-identified outputs with rubric.
- Tie-break judge: used only when judge disagreement >1 point on any rubric dimension.

## Sampling Plan
- Unit of analysis: condition-run output.
- Target sample: 30 outputs (10 tasks x 3 conditions).
- Feasibility constraint: minimum acceptable completion is 24 outputs (8 tasks x 3 conditions).
- Inclusion: only tasks with complete logs, final output, and timing metadata.

## Procedure
1. Prepare task packets and answer keys/check references for each task.
2. Randomly assign condition order per task.
3. Run each condition with a 35-minute cap per run.
4. Log:
   - start/end timestamps
   - participant IDs/roles
   - transcript
   - final output
   - pre-finalization error flags
5. De-identify outputs (remove condition labels, participant names, style markers where possible).
6. Judges score blinded outputs using `rubric.md`.
7. Resolve large disagreements with tie-break judge.
8. Compute aggregate metrics and condition comparisons.

## Primary Outcomes
1. Factual accuracy score (0-4 rubric score; also percent correct claims when checkable).
2. Error-detection-before-finalization count (normalized by seeded/known opportunities).
3. Unsupported claims count in final output (lower is better).

## Secondary Outcomes
1. Novelty/insight score (0-4).
2. Clarity score (0-4).
3. Completion time (minutes).
4. Output length (tokens/words).

## Analysis Plan
- Main comparison: condition-level means for each outcome.
- Report paired differences per task: Structured - Solo, Structured - Unstructured.
- Statistical approach (small-N robust):
  - Paired permutation test for primary outcomes.
  - Bootstrap 95% CIs for mean differences.
- Effect sizes:
  - Mean difference for rubric dimensions.
  - Relative reduction (%) for unsupported claims.
  - Time overhead in minutes.
- Inter-rater reliability:
  - Cohen's weighted kappa (ordinal rubric scores).
- Decision rule for directional support:
  - Hypothesis considered supported if mean difference is in predicted direction and 95% CI excludes 0 for primary outcomes.

## Exclusion Criteria
Exclude a condition-run if any apply:
1. Missing transcript or missing final output.
2. Time cap exceeded by >10 minutes due to non-task interruption.
3. Protocol violation in structured condition (missing required role step).
4. Judge cannot score due to insufficient content.

All exclusions will be logged with reason and timestamp.

## Threats to Validity
- Small sample may limit power and inflate variance.
- Non-independence between agents across runs.
- Style leakage may partially unblind judges.
- Task heterogeneity may interact with condition effects.
- Coordination overhead may trade off with speed.

Mitigations: randomized condition order, matched tasks, de-identification, independent judges, and transparent archival.

## Materials to Archive
- Preregistration (`protocol.md`)
- Scoring rubric (`rubric.md`)
- Task packets and answer keys
- Condition prompts/instructions
- Raw transcripts and timestamps
- Final outputs (raw + de-identified)
- Judge sheets and adjudication notes
- Analysis notebook/script and summary tables
- Exclusion log

## Day-by-Day Execution Plan (Rest of Week)
Assuming current date is Monday, May 11, 2026.

### Session 1 - Monday, May 11, 2026 (Setup + Pilot)
- Finalize protocol/rubric and task packets.
- Run 1 pilot task across all 3 conditions (3 runs).
- Validate logging, blinding, and scoring pipeline.

### Session 2 - Tuesday, May 12, 2026 (Data Collection Block A)
- Run 3 tasks across all 3 conditions (9 runs).
- Complete same-day de-identification and metadata checks.

### Session 3 - Wednesday, May 13, 2026 (Data Collection Block B)
- Run 3 tasks across all 3 conditions (9 runs).
- Start blinded judging for completed outputs.

### Session 4 - Thursday, May 14, 2026 (Data Collection Block C)
- Run remaining 3 tasks across all 3 conditions (9 runs).
- Finish blinded judging; trigger tie-break adjudication as needed.

### Session 5 - Friday, May 15, 2026 (Analysis + Write-up)
- Finalize exclusion log.
- Compute condition comparisons, CIs, and reliability metrics.
- Produce results memo with tables/figures and replication checklist.
