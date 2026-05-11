# Session 3 — Task 5 — Scoring Checklist

Use this checklist alongside `task5_scoring_template.md` and `task5_scoring_detailed.md`. Do not surface bug keys or point values outside the scoring team.

## Step-by-step

1) Verify wall-clock timing data
- Collect start/end timestamps from the run submission (PT).
- Confirm the artifact path under `experiments/session3/runs/`.
- Compute and record wall-clock duration in both templates; flag any gaps or mismatches.

2) Prep evidence and bug/bonus decisions
- Read the submission once end-to-end, then map each claim to the bug/bonus keys listed in the concise template (do not add new keys).
- For each potential bug claim, capture exact quotes/screenshots for the detailed template’s Evidence/Notes fields.
- Note any edge cases, partial fixes, or ambiguous wording that will require judgment.

3) Run the scoring script with proper arguments
- From repo root, execute the scorer once you have your FOUND/FIXED/bonus decisions and ambiguity/false-positive counts:
  ```bash
  python3 analysis/score_session3_task5.py \
    --found <bug_keys...> \
    --fixed <bug_keys...> \
    --bonuses <bonus_keys...> \
    --ambiguity <0-25> \
    --false-positives <N>
  ```
- Use only keys defined in `task5_scoring_template.md`; leave an argument empty (e.g., `--bonuses`) if none apply.

4) Cross-check results with the detailed scoring template
- Populate every section of `task5_scoring_detailed.md`: metadata, bug-by-bug, bonuses, false positives, ambiguity credit, and process notes.
- Ensure FOUND/FIXED labels and counts match the scorer arguments; reconcile any discrepancies before finalizing.
- Verify that evidence snippets support each scored decision and that missing evidence is noted.

5) Document any scoring judgment calls
- In the detailed template Notes fields, describe why borderline claims were accepted or rejected and how partial fixes were interpreted.
- If ambiguity credit is given, justify it clearly; if withheld despite unclear wording, note why.
- Record any protocol deviations affecting timing or scoring confidence.

6) Calculate and record the final score
- Confirm the script output matches the sum expected from the template (base points plus/minus bonuses and false positives, plus any ambiguity credit).
- Store the final numeric score and the exact command used in both templates.
- If reruns are needed (e.g., after fixing an entry), overwrite prior tallies and keep only the final authoritative score.
