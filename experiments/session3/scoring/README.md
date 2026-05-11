# Session 3 scoring artifacts

Place scoring sheets and scored evaluations here only after all Session 3 run artifacts are submitted.

Do not expose scoring files or answer-key material to participants before submission.

## Task 5 scorer quick start (API Rate Limiter pivot)

Use these scorer-only files after all Task 5 run artifacts are submitted:
- `experiments/session3/scoring/task5_scoring_template.md`
- `experiments/session3/scoring/task5_scoring_detailed.md`
- `analysis/score_session3_task5.py`

Useful commands:
- `python3 analysis/score_session3_task5.py --rubric`
- `python3 analysis/score_session3_task5.py --template`

CLI inputs:
- `--found` = comma-separated bug keys found by the team
- `--fixed` = comma-separated bug keys materially fixed by the team
- `--bonuses` = comma-separated bonus keys
- `--ambiguity` = 0..25
- `--false-positive-deduction` = raw-point deduction (incorrect claims × 50)

Example:
- `python3 analysis/score_session3_task5.py --found key1,key2 --fixed key1 --bonuses interaction,test_design --ambiguity 0 --false-positive-deduction 50`

Reminder:
- do not expose any scoring file or bug-key material to participants before they submit final artifacts
- record wall-clock timing separately in the run artifact, not in the scoring sheet
