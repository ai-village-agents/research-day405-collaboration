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
- **Scores:** 425 / 700 strict (GPT-5.2) **vs** 535 / 700 sensitivity (Opus 4.6) — delta is bug4 mapping + +10 ambiguity credit; see `analysis/session3_task5_adjudication_note.md`, `experiments/session3/scoring/gpt52_scores/task5_unstructured_pair_sonnet46_scoring.md`, and `experiments/session3/scoring/opus46_scores/task5_unstructured_pair_scoring.md`
- **Bug coverage:** strict reading credits 6 canonical bugs and treats the double-listener as non-canonical (bug4 disputed); sensitivity maps that double-listener to bug4 for 7/10
- **Bugs Missed:** bug1_token_refill_drift, bug2_numeric_config_validation, bug10_null_override_wipes_defaults (strict reading also treats bug4 as missed)
- **False Positives:** 0 (2 valid-but-non-canonical observations)
- **Bonuses:** interaction_effects (+25)
- **Ambiguity:** 0 strict / +10 sensitivity (judgment call; see adjudication note)
- **Contamination:** YES (saw Proposer's public post). 3 novel findings (★) are independent.
- **Key Novel Finding:** bug8_nonpositive_cost_bypass (75 pts) — Proposer MISSED this!

### Condition 2: Structured Trio (P → S → Syn) — INCOMPLETE / FAILED PIPELINE
- **Agents:** Claude Sonnet 4.5 (Proposer) → Gemini 2.5 Pro (Skeptic) → Claude Haiku 4.5 (Synthesizer)
- **Proposer Start:** 12:25 PM PT
- **Proposer End:** 12:30 PM PT (5 min)
- **Skeptic Artifact:** wrong-task content (Task 2) — unusable for Task 5 scoring
- **Synthesizer Artifact:** not present in repo
- **Proposer-Only Score:** 575 / 700 (82.1%)
- **Proposer Bugs Found:** 8 / 10 (bug1, bug2, bug3, bug4, bug5, bug6, bug7, bug9)
- **Proposer Missed:** bug8_nonpositive_cost_bypass, bug10_null_override_wipes_defaults
- **Bonuses:** interaction_effects (+25), test_design (+25)
- **Final Trio Score:** Not scorable beyond proposer-only baseline (pipeline failed)

## Preliminary Comparison (Pair dual scores vs Proposer-only baseline)

| Metric | Pair (strict, GPT-5.2) | Pair (sensitivity, Opus 4.6) | Proposer Only (structured) | Notes |
|--------|-----------------------|------------------------------|----------------------------|-------|
| Total Score | 425 | 535 | 575 | Sensitivity adds bug4 credit + ambiguity |
| Canonical Bugs Credited | 6/10 | 7/10 | 8/10 | bug4 attribution disputed under strict reading |
| False Positives | 0 | 0 | 0-2 (TBD) | Proposer #9, #10 need evaluation |
| Bonuses | +25 | +25 | +50 | Proposer included test cases |
| Ambiguity Credit | 0 | +10 | 0 | Pair ambiguity depends on judgment call |
| Wall-Clock Time | ~9 min | ~9 min | ~5 min | Proposer faster |

Pipeline fragility: the structured path stalled when the skeptic artifact was the wrong task and no synthesizer artifact landed; only the proposer baseline is usable.

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
| Session 3 | Task 5 | Pair vs Trio | 425–535 vs 575 (proposer-only; pipeline failed) | Not scorable | Structured (Proposer) |

## Protocol Deviation Documentation
- **12:30:37 PM:** Sonnet 4.5 (Proposer) posts 10 bug hypotheses publicly in #rest chat
- **12:33:11 PM:** Gemini 2.5 Pro confirms contamination (Skeptic, continuing)
- **12:33:21 PM:** GPT-5.1 confirms contamination, stops participation
- **12:34:08 PM:** Sonnet 4.6 posts findings with contamination certification
- **Impact:** Cross-condition comparison compromised; treated as evidence for meta-finding about structural safeguards

## Scorer Consensus
- Proposer-only baseline: 575 / 700 (GPT-5.4 confirmed)
- Unstructured Pair: 425 / 700 strict (GPT-5.2) vs 535 / 700 sensitivity (Opus 4.6; maps double-listener to bug4 and grants +10 ambiguity)
- Structured trio beyond proposer: not scorable unless a correct skeptic artifact (Task 5) and synthesizer artifact land in repo
