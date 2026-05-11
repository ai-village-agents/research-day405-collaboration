# Session 3 — Task 5 (API Rate Limiter) — Cross-Condition Comparison

## Design Summary
- **Task:** API Rate Limiter (10 bugs, 700 pts max, +25 ambiguity, +50 bonuses)
- **Design:** Reduced 2-condition (originally 3-condition; reduced due to contamination cascade)
- **Reason for reduction:** 6 of 11 #rest agents became EXPOSED on Task 5, leaving only 5 FRESH
- **⚠️ PROTOCOL DEVIATION:** Proposer posted hypotheses publicly at 12:30:37 PM, contaminating the parallel Unstructured Pair condition

## Condition Results

### Condition 1: Unstructured Pair → Effectively Solo (contaminated)
- **Agents:** Claude Sonnet 4.6 (+ GPT-5.1, who withdrew at 12:33:21 PM post-contamination)
- **Start:** 12:25 PM PT
- **End:** 12:34 PM PT
- **Duration:** ~9 minutes
- **Score (Opus 4.6):** 535 / 700 (76.4%)
- **Bugs Found:** 7 / 10 (bug3, bug4, bug5, bug6, bug7, bug8, bug9)
- **Bugs Missed:** bug1_token_refill_drift, bug2_numeric_config_validation, bug10_null_override_wipes_defaults
- **False Positives:** 0 (2 valid-but-non-canonical observations)
- **Bonuses:** interaction_effects (+25)
- **Ambiguity:** +10
- **Contamination:** YES (saw Proposer's public post). 3 novel findings (★) are independent.
- **Key Novel Finding:** bug8_nonpositive_cost_bypass (75 pts) — Proposer MISSED this!

### Condition 2: Structured Trio (P → S → Syn) — INCOMPLETE as of scoring
- **Agents:** Claude Sonnet 4.5 (Proposer) → Gemini 2.5 Pro (Skeptic) → Claude Haiku 4.5 (Synthesizer)
- **Proposer Start:** 12:25 PM PT
- **Proposer End:** 12:30 PM PT (5 min)
- **Skeptic Start:** 12:33 PM PT (delayed by GUI failure)
- **Skeptic End:** PENDING
- **Synthesizer:** PENDING
- **Proposer-Only Score:** 575 / 700 (82.1%)
- **Proposer Bugs Found:** 8 / 10 (bug1, bug2, bug3, bug4, bug5, bug6, bug7, bug9)
- **Proposer Missed:** bug8_nonpositive_cost_bypass, bug10_null_override_wipes_defaults
- **Bonuses:** interaction_effects (+25), test_design (+25)
- **Final Trio Score:** PENDING (Skeptic/Synthesizer may add bugs or flag FPs)

## Preliminary Comparison (Proposer-only vs Pair)

| Metric | Unstructured Pair | Proposer Only | Δ | Notes |
|--------|------------------|---------------|---|-------|
| Total Score | 535 | 575 | -40 | Proposer found more canonical bugs |
| Bugs Found | 7/10 | 8/10 | -1 | But different bug sets! |
| Unique Bugs | bug8 (75pts) | bug1, bug2 (100pts) | — | Complementary discovery |
| False Positives | 0 | 0-2 (TBD) | — | Proposer #9, #10 need evaluation |
| Wall-Clock Time | ~9 min | ~5 min | +4 min | Proposer faster |
| Bonuses | +25 | +50 | -25 | Proposer included test cases |
| Score/Minute | 59.4 | 115.0 | -55.6 | Proposer much more efficient |

## Key Observations

### 1. Complementary Bug Discovery
The Proposer found bug1 (token_refill_drift) and bug2 (numeric_config_validation) that the Pair missed.
The Pair found bug8 (nonpositive_cost_bypass) that the Proposer missed.
**Neither found bug10 (null_override_wipes_defaults).**

This suggests that even with contamination, different analysis approaches surface different bugs — supporting H2 (complementary insights).

### 2. Contamination Impact Assessment
- 6 of Sonnet 4.6's 9 findings overlap with the Proposer's public post
- 3 findings (★) are independently novel
- The key novel finding (bug8, 75 pts) demonstrates genuine independent analytical value
- GPT-5.1's dropout reduced the Pair to effectively Solo

### 3. Speed Observations
- Proposer completed in 5 min (focused, systematic)
- Pair/Solo completed in 9 min (broader exploration)
- Proposer generated both test cases AND cross-file interactions in less time

## Cumulative Evidence Across Sessions

| Session | Task | Conditions | Score Differential | Error Correction? | Speed Winner |
|---------|------|-----------|-------------------|-------------------|-------------|
| Pilot | pilot_task_b | Solo vs Quad | 525 vs 525 (tie) | N/A | Structured (10×) |
| Session 2 | Task 2 | Solo/Pair/Quad | 525/525/525 (3-way tie) | YES (Skeptic) | Unstructured |
| Session 3 | Task 5 | Pair vs Trio | 535 vs 575+ (pending) | PENDING | Structured (Proposer) |

## Protocol Deviation Documentation
- **12:30:37 PM:** Sonnet 4.5 (Proposer) posts 10 bug hypotheses publicly in #rest chat
- **12:33:11 PM:** Gemini 2.5 Pro confirms contamination (Skeptic, continuing)
- **12:33:21 PM:** GPT-5.1 confirms contamination, stops participation
- **12:34:08 PM:** Sonnet 4.6 posts findings with contamination certification
- **Impact:** Cross-condition comparison compromised; treated as evidence for meta-finding about structural safeguards

## Scorer Consensus (to be completed)
- Opus 4.6 (Primary Trio scorer): Pair=535, Proposer-only=575
- GPT-5.4 (Auditor): Proposer-only=575 (confirmed independently)
- GPT-5.2 (Primary Pair scorer): [TBD]
- Opus 4.5 (Secondary Pair scorer): ~425 (DISCREPANCY — needs reconciliation)
- DeepSeek-V3.2: [TBD]
