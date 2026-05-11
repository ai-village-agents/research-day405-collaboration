# Session 3 — Task 5 (API Rate Limiter) — GPT-5.2 Scoring Sheet (Unstructured Pair)

⚠️ **Scorers only.** This file contains Task 5 bug keys.

## Submission metadata
- Condition: Unstructured Pair
- Team/Agents: Claude Sonnet 4.6 + GPT-5.1
- Start time (PT): ~12:25 PM (pair start; artifact submitted ~12:34 per header)
- End time (PT): ~12:34 PM (submission time)
- Wall-clock duration: ~9 min (approx; based on stated times)
- Artifact file path (in `experiments/session3/runs/`):
  - `experiments/session3/runs/unstructured_pair_task5_claude_sonnet_4.6.md`
- Contamination certification: **YES** (saw proposer hypotheses posted publicly at 12:30:37 PM PT)

## Canonical bug-key mapping (FOUND/FIXED)
Notes: Submission includes several *additional* real issues (e.g., “double listener”, “silent token drain”, “middleware doesn’t expose stop()”) that are **not** among the 10 seeded bugs. These are **not** scored as false positives because they are plausible/true properties of the code; they simply don’t map to rubric keys.

### Bugs (10 total; 650 base points)
Mark **FOUND** if correctly identified; **FIXED** if a correct fix is proposed.

- [ ] bug1_token_refill_drift (50)
  - Evidence: Not claimed.
- [ ] bug2_numeric_config_validation (50)
  - Evidence: Not claimed.
- [x] bug3_bucket_overflow (75)
  - Evidence: “No cap on tokens; exceeds `capacity` during idle periods.” (limiter.js refill adds without cap)
  - Fix proposed: No.
- [ ] bug4_race_condition (100)
  - Evidence: Not claimed as check-then-decrement race.
- [x] bug5_memory_leak (75)
  - Evidence: “stop() doesn't remove backpressure listeners, causing memory leak.” (stop only clears interval)
  - Fix proposed: No.
- [x] bug6_clock_monotonicity (75)
  - Evidence: “`Date.now()` can go backwards; `process.hrtime.bigint()` preferred.” (timeSince)
  - Fix proposed: Partial suggestion only.
- [x] bug7_missing_retry_after (50)
  - Evidence: “429 responses missing `Retry-After` header…” (middleware.js)
  - Fix proposed: No.
- [x] bug8_nonpositive_cost_bypass (75)
  - Evidence: “getCost(req) returning 0 or negative bypasses rate limiting entirely.” (middleware.js → tryConsume(cost))
  - Fix proposed: No.
- [x] bug9_shallow_merge (50)
  - Evidence: “Object.assign replaces nested objects instead of merging them.” (config.js)
  - Fix proposed: No.
- [ ] bug10_null_override_wipes_defaults (50)
  - Evidence: Not claimed.

### Bonuses (+50 max)
- [x] interaction_effects (+25)
  - Evidence: “Bugs #2 + #3… cause double token deductions…” (their internal numbering; describes compounding behavior)
- [ ] test_design (+25)
  - Evidence: Not provided.

### Discretionary
- Ambiguity credit (0–25): 0
- Notes:
  - I did **not** apply a false positive penalty for the non-canonical findings, because they appear to describe real behaviors in the code, even if unseeded.

### False positives
List any **incorrect bug claims** (each is −50).
- None identified (0 × 50 = 0).

## Reproducible score command
```bash
python3 analysis/score_session3_task5.py \
  --found bug3_bucket_overflow,bug5_memory_leak,bug6_clock_monotonicity,bug7_missing_retry_after,bug8_nonpositive_cost_bypass,bug9_shallow_merge \
  --bonuses interaction_effects \
  --ambiguity 0 \
  --false-positive-deduction 0
```

## Script output (record)
(See below)

```
TASK 5 SCORING RESULTS
========================================================================
Base (found bugs):   400 / 650
Bonuses:             +25 / 50
Ambiguity credit:    +0 / 25
False positives:     -0
========================================================================
TOTAL:               425 / 700
% OF REPORTING MAX:  60.71%
========================================================================
Absolute top incl. ambiguity: 725

Bug Breakdown:
  ✗  bug1_token_refill_drift                 50 pts
  ✗  bug2_numeric_config_validation          50 pts
  ✓  bug3_bucket_overflow                    75 pts
  ✗  bug4_race_condition                    100 pts
  ✓  bug5_memory_leak                        75 pts
  ✓  bug6_clock_monotonicity                 75 pts
  ✓  bug7_missing_retry_after                50 pts
  ✓  bug8_nonpositive_cost_bypass            75 pts
  ✓  bug9_shallow_merge                      50 pts
  ✗  bug10_null_override_wipes_defaults      50 pts
```
