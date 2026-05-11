# Session 3 — Task 5 (API Rate Limiter) — Scoring Template (concise)

⚠️ **Scorers only.** This file contains Task 5 bug keys.

## Submission metadata
- Condition: (Solo / Unstructured Pair / Structured Quad)
- Team/Agents:
- Start time (PT):
- End time (PT):
- Wall-clock duration:
- Artifact file path (in `experiments/session3/runs/`):

## Scoring inputs

### Bugs (10 total; 650 base points)
Mark **FOUND** if correctly identified; **FIXED** if a correct fix is proposed.

- [ ] bug1_token_refill_drift (50)
- [ ] bug2_numeric_config_validation (50)
- [ ] bug3_bucket_overflow (75)
- [ ] bug4_race_condition (100)
- [ ] bug5_memory_leak (75)
- [ ] bug6_clock_monotonicity (75)
- [ ] bug7_missing_retry_after (50)
- [ ] bug8_nonpositive_cost_bypass (75)
- [ ] bug9_shallow_merge (50)
- [ ] bug10_null_override_wipes_defaults (50)

### Bonuses (+50 max)
- [ ] interaction_effects (+25)
- [ ] test_design (+25)

### Discretionary
- Ambiguity credit (0–25):
- Notes:

### False positives
List any **incorrect bug claims** (each is −50).
- FP1:
- FP2:

## Score command
Use the scorer script:

```bash
python3 analysis/score_session3_task5.py \
  --found <bug_keys...> \
  --fixed <bug_keys...> \
  --bonuses <bonus_keys...> \
  --ambiguity <0-25> \
  --false-positives <N>
```

(Recommended reporting max = 700; absolute top with ambiguity = 725.)
