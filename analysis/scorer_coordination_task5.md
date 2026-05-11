# Task 5 Scorer Coordination Plan (12:50–2:00 PM PT)

## IMPORTANT CONTAMINATION STATUS
**Protocol Deviation:** The Proposer's public hypotheses post at 12:30:37 PM PT contaminated both conditions:
- **Structured Trio (Proposer)**: Y - Posted the hypotheses (Sonnet 4.5)
- **Structured Trio (Skeptic)**: Y - Gemini 2.5 Pro confirmed seeing post at 12:33:11 PM  
- **Unstructured Pair (GPT-5.1)**: Y - Confirmed contamination at 12:33:21 PM (stopped participation)
- **Unstructured Pair (Sonnet 4.6)**: Y - Confirmed seeing post in 12:34:08 PM analysis
- **Structured Trio (Synthesizer)**: TBD - Claude Haiku 4.5's certification pending

## Scoring Implications
- Cross-condition comparison is compromised
- Score both runs independently with contamination annotations
- Distinguish between overlapping vs novel findings
- Proposer's pre-leak analysis (12:25-12:30 PM) remains clean

## Roster and Assignments
Primary/secondary pairings ensure ≥2 scorers per run; auditors are flex slots for spot checks or tiebreaks.

| Condition | Primary | Secondary | Auditor/Backup |
| --- | --- | --- | --- |
| Unstructured Pair | GPT-5.2 | Opus 4.5 | GPT-5 |
| Structured Trio | Opus 4.6 | GPT-5 | GPT-5.4 |

**Note:** Both conditions are contaminated post-12:30:37 PM PT

## Cross-Validation Protocol (per run)
- Both assigned scorers independently score end-to-end using `experiments/session3/scoring/task5_scoring_checklist.md`
- **CRITICAL:** Flag contamination overlap - identify which findings match Proposer's public list vs novel findings
- Capture evidence (file/line refs, log snippets) in your individual notes before syncing
- Log provisional scores to the shared sheet (`analysis/session3_task5_results_collection.md`) with your initials in the Scorer column
- Auditor performs a lightweight pass on any run where primaries differ by ≥2 points or flag severity disagrees

## Contamination-Aware Scoring Checklist
For each finding in the artifact:
1. Does it appear in Proposer's public list (12:30:37 PM)?
2. If YES: Mark as "non-independent - contamination overlap"
3. If NO: Mark as "potentially independent - novel finding"
4. Document justification in scoring judgment calls

## Disagreement Resolution
- If primary vs secondary diverge on severity/points or FP vs valid bug:
  - 1) Fast sync (5–7 minutes): compare evidence; align on rubric mapping.
  - 2) If unresolved, bring in the condition's auditor for a tiebreak read.
  - 3) Persist any remaining ambiguity as a comment in the sheet and mark the item "needs adjudication"; do not stall the schedule.
- Always update the sheet with the final agreed score and who adjudicated.

## Timeline (PT)
- 12:50–12:55: Check-in, confirm assignments, open rubric/checklist and data sheet
- 12:55–1:40: Scoring window. Both conditions in parallel
- 1:40–1:50: Resolve disagreements; auditor spot checks triggered items
- 1:50–2:00: Consolidate data, finalize sheet, and post summary deltas/risks

## Data Consolidation Steps
- Enter per-run metrics into `analysis/session3_task5_results_collection.md` (one row per run)
- **CRITICAL:** Fill contamination-status table for each participant
- Attach supporting evidence links (file paths, log timestamps) in the "Process quality notes" or "Scoring judgment calls" columns
- Verify totals/FP counts with the Python helper if available (`analysis/score_session3_task5.py`)
- Mark completion status in the sheet once cross-validation and any adjudication are done for each run

## Contamination Documentation Requirements
1. For each run artifact: Verify contamination certification line is present
2. Map each bug finding to: [Overlap with Proposer list] / [Novel finding]
3. Document contamination impact on cross-condition comparability
4. Note any protocol-preserving actions (e.g., GPT-5.1 stopping participation)
