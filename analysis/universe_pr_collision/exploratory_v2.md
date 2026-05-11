# Exploratory stats: Universe PR range collisions (v2 features)

Dataset: `data/historical/universe_pr_collision_features_2026-05-11_v2.csv`
N ranged PRs: 90

## Merge rates by slice

| Slice | N | Merged | Merge rate |
|---|---:|---:|---:|
| Overall | 90 | 22 | 24.4% |
| Collided at creation | 17 | 5 | 29.4% |
| No collision at creation | 73 | 17 | 23.3% |
| Append-like heuristic | 64 | 18 | 28.1% |
| Not append-like | 26 | 4 | 15.4% |
| Replacement-risk heuristic | 4 | 0 | 0.0% |
| Not replacement-risk | 86 | 22 | 25.6% |

## Within collided-at-creation PRs

- Append-like: 4/11 merged (36.4%) vs 1/6 (16.7%)
- Replacement-risk: 0/1 merged (0.0%) vs 5/16 (31.2%)
- Any label keyword in last comment: 2/6 merged (33.3%) vs 3/11 (27.3%)

## Last-comment keyword label prevalence

| Label | Count | % of ranged PRs |
|---|---:|---:|
| label_stale | 23 | 25.6% |
| label_replacement_risk | 8 | 8.9% |
| label_merge_conflict | 8 | 8.9% |
| label_collision_claimed | 3 | 3.3% |
| label_any | 29 | 32.2% |

## Cautions

- This is a single snapshot window (latest ~612 PRs fetched, 90 ranged).
- Last-comment labels are a crude proxy for closure reason; comments may be absent or not diagnostic.
- Replacement-risk heuristic is extremely sparse here (4/90), so rate estimates are unstable.
