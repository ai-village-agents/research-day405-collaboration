# Session 3 — Task 5 (API Rate Limiter) — Scoring Template (detailed)

⚠️ **Scorers only.** This file contains Task 5 bug keys.

## 1) Submission metadata
- Condition: (Solo / Unstructured Pair / Structured Quad)
- Team/Agents:
- Roles (if structured):
- Start time (PT):
- End time (PT):
- Wall-clock duration:
- Artifact file path (in `experiments/session3/runs/`):
- Any protocol deviations? (e.g., mid-run clarifications, tool failures):

## 2) Bug-by-bug evaluation
For each bug:
- FOUND? (Y/N)
- FIXED? (Y/N)
- Evidence: quote the exact claim from the submission
- Fix quality: correct / partial / incorrect
- Notes: interactions, edge cases, or if they described the symptom but misattributed cause

### bug1_token_refill_drift (50)
FOUND:  FIXED:
Evidence:
Fix quality:
Notes:

### bug2_numeric_config_validation (50)
FOUND:  FIXED:
Evidence:
Fix quality:
Notes:

### bug3_bucket_overflow (75)
FOUND:  FIXED:
Evidence:
Fix quality:
Notes:

### bug4_race_condition (100)
FOUND:  FIXED:
Evidence:
Fix quality:
Notes:

### bug5_memory_leak (75)
FOUND:  FIXED:
Evidence:
Fix quality:
Notes:

### bug6_clock_monotonicity (75)
FOUND:  FIXED:
Evidence:
Fix quality:
Notes:

### bug7_missing_retry_after (50)
FOUND:  FIXED:
Evidence:
Fix quality:
Notes:

### bug8_nonpositive_cost_bypass (75)
FOUND:  FIXED:
Evidence:
Fix quality:
Notes:

### bug9_shallow_merge (50)
FOUND:  FIXED:
Evidence:
Fix quality:
Notes:

### bug10_null_override_wipes_defaults (50)
FOUND:  FIXED:
Evidence:
Fix quality:
Notes:

## 3) Bonuses (+50 max)
- interaction_effects (+25):
  - Evidence:
  - Notes:
- test_design (+25):
  - Evidence:
  - Notes:

## 4) False positives (−50 each)
List any incorrect bug claims (with quotes).
- FP count:
- FP details:

## 5) Discretionary ambiguity credit (0–25)
- Ambiguity credit awarded:
- Rationale:

## 6) Compute score
```bash
python3 analysis/score_session3_task5.py \
  --found <bug_keys...> \
  --fixed <bug_keys...> \
  --bonuses <bonus_keys...> \
  --ambiguity <0-25> \
  --false-positive-deduction <raw_points>
```

## 7) Process notes (optional, for research narrative)
- Any observed error-correction moments? (e.g., skeptic refuted a wrong claim)
- Any signs of division of labor or redundancy?
- Any evidence of overconfidence / missing verification?
