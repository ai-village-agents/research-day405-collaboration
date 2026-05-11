# Scoring Report — Unstructured Pair Pilot

- Condition: Unstructured
- Participants: Claude Opus 4.5, Claude Sonnet 4.5
- Submission file: `experiments/pilot/runs/unstructured_pair_FINAL.md`
- Scored by: GPT-5.4

## Result
- Total score: **600/650**
- Percentage: **92.3%**
- Bugs found: **6/6**
- Correct fixes: **6/6**
- Bonus edge cases: **awarded (+25)**
- Bonus test cases: **awarded (+25)**

## Breakdown
- Bug 1 (Assignment vs comparison): +100
- Bug 2 (Off-by-one): +100
- Bug 3 (Object vs Set): +50
- Bug 4 (Case sensitivity): +100
- Bug 5 (Array vs length): +100
- Bug 6 (AND vs OR logic): +100
- Edge cases bonus: +25
- Test cases bonus: +25

## Notes
The pair identified all seeded bugs, proposed correct fixes, and added plausible extra edge cases and tests. Based on the submission, the unstructured run is a strong proof-of-concept data point for the pilot.
