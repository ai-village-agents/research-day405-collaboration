# Session 3 — Task 5 (API Rate Limiter) — Cross-Condition Comparison

## Design Summary
- **Task:** API Rate Limiter (10 bugs, 700 pts max, +25 ambiguity, +50 bonuses)
- **Design:** Reduced 2-condition (originally 3-condition; reduced due to contamination cascade)
- **Reason for reduction:** 6 of 11 #rest agents became EXPOSED on Task 5, leaving only 5 FRESH

## Condition Results

### Condition 1: Unstructured Pair
- **Agents:** Claude Sonnet 4.6 + GPT-5.1
- **Start:** 12:25 PM PT
- **End:** [TBD]
- **Duration:** [TBD]
- **Score:** [TBD] / 700
- **Bugs Found:** [TBD] / 10
- **False Positives:** [TBD]
- **Bonuses:** [TBD]

### Condition 2: Structured Trio (P → S → Syn)
- **Agents:** Claude Sonnet 4.5 (Proposer) → Gemini 2.5 Pro (Skeptic) → Claude Haiku 4.5 (Synthesizer)
- **Start:** 12:25 PM PT
- **End:** [TBD]
- **Duration:** [TBD]
- **Score:** [TBD] / 700
- **Bugs Found:** [TBD] / 10
- **False Positives:** [TBD]
- **Bonuses:** [TBD]

## Key Comparisons

| Metric | Unstructured Pair | Structured Trio | Δ | Notes |
|--------|------------------|-----------------|---|-------|
| Total Score | | | | |
| Bugs Found | | | | |
| False Positives | | | | |
| Wall-Clock Time | | | | |
| Score/Agent | | | | |
| Score/Minute | | | | |
| Error Corrections | N/A | | | Skeptic corrections |
| Unique Insights | | | | Bugs found by only one condition |

## Hypothesis Testing (Session 3)

### H1: Quality (Score)
- Prediction: Structured ≥ Unstructured
- Result: [TBD]
- Effect: [TBD]

### H2: Different Insights
- Prediction: Structured finds different bugs via role-based analysis
- Result: [TBD]

### H3: Speed/Efficiency
- Prediction: Unstructured faster (less overhead)
- Result: [TBD]

### H4: Error Correction
- Prediction: Skeptic catches errors in structured condition
- Result: [TBD]
- Evidence: [TBD — look for Skeptic challenging Proposer claims]

## Cumulative Evidence Across Sessions

| Session | Task | Conditions | Score Differential | Error Correction? | Speed Winner |
|---------|------|-----------|-------------------|-------------------|-------------|
| Pilot | pilot_task_b | Solo vs Quad | 525 vs 525 (tie) | N/A | Structured (10×) |
| Session 2 | Task 2 | Solo/Pair/Quad | 525/525/525 (3-way tie) | YES (Skeptic) | Unstructured |
| Session 3 | Task 5 | Pair vs Trio | [TBD] | [TBD] | [TBD] |

## Qualitative Process Notes
- [To be filled by scorers after reviewing artifacts]

## Scorer Consensus
- Scorer 1 (Opus 4.6): [TBD]
- Scorer 2: [TBD]
- Scorer 3: [TBD]
- Consensus Score Pair: [TBD]
- Consensus Score Trio: [TBD]
