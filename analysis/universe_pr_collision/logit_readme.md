# Numpy-only logistic regression quickstart

- Run: `analysis/universe_pr_collision/fit_logit_numpy.py` (defaults to `data/historical/universe_pr_collision_features_2026-05-11_v3.csv`, drops outcome=='open' unless `--include_open`). Choose a preset with `--preset {base,with_size,with_labels}` (default: `base`) or pass a custom comma list via `--features` (cannot combine with `--preset`). Use `--ridge 1e-4` to strengthen the ridge, or tweak `--max-iter` / `--tol`.
- The model always includes an intercept and uses IRLS/Newton with a small ridge term to avoid singular Hessians. Coefficients are log-odds; `odds_ratio = exp(coef)`. Wald z/p use a normal approximation; SE comes from the inverse Hessian. The 95% CI shown is for the odds ratio (exp(coef ± 1.96*SE)).
- Caveat: tiny N, heuristic labels/features, no standardization or validation split—interpret directions only, not significance or causal effects.

Preset examples:
- Base: `analysis/universe_pr_collision/fit_logit_numpy.py --preset base`
- With size: `analysis/universe_pr_collision/fit_logit_numpy.py --preset with_size`
- With labels: `analysis/universe_pr_collision/fit_logit_numpy.py --preset with_labels`

Example output (first ~25 lines) using the default preset (`base`):

```
WARNING: Small-N, convenience features, no train/test split; treat coefficients as directional only.
WARNING: Heuristic labels may embed annotation bias; odds ratios are not causal.
Data: data/historical/universe_pr_collision_features_2026-05-11_v3.csv
Features: collided, appendLikeHeuristic, replacementRiskHeuristic, staleRangeHeuristic
N=89, positives=22, iterations=16, log_likelihood=-47.2945
feature                            coef   odds_ratio         se          z          p            or_95ci
--------------------------------------------------------------------------------------------------------
intercept                       -1.5854       0.2049     0.5770     -2.748     0.0060 [ 0.066,  0.635]
collided                         0.3307       1.3920     0.6144      0.538     0.5903 [ 0.418,  4.641]
appendLikeHeuristic              0.6518       1.9190     0.6223      1.047     0.2949 [ 0.567,  6.498]
replacementRiskHeuristic       -11.2863       0.0000   285.2928     -0.040     0.9684 [ 0.000, 8801353116082675445759257478057880294917176380125966726158899173520850388575379683153919080380009288790576067584947722002148993387727192457227341910048013152425964491822083936371813822647820769153370083694681970737289483971391409191124992.000]
staleRangeHeuristic            -11.1625       0.0000   286.7415     -0.039     0.9689 [ 0.000, 170394811675336375787677637630218574964940994543239035224314478920288984688294606086180170422491128022708957692020984313135162249030967223743966069306348072946279473859559251917900136773037705064142475608656544034190935511849746946364276736.000]
```
