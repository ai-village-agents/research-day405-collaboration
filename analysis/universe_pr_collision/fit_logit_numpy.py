#!/usr/bin/env python3
"""Lightweight logistic regression via IRLS/Newton using only numpy.

Defaults are tuned for the collision-feature CSV snapshot in data/historical.
"""

import argparse
import math
import sys
from typing import Dict, Iterable, List, Tuple

import numpy as np
import pandas as pd


DEFAULT_DATA_PATH = "data/historical/universe_pr_collision_features_2026-05-11_v3.csv"


PRESETS: Dict[str, List[str]] = {
    "base": ["collided", "appendLikeHeuristic", "replacementRiskHeuristic", "staleRangeHeuristic"],
    "with_size": [
        "collided",
        "appendLikeHeuristic",
        "replacementRiskHeuristic",
        "staleRangeHeuristic",
        "log1p_totalChangedLines",
        "delToAddRatio",
    ],
    "with_labels": [
        "collided",
        "appendLikeHeuristic",
        "replacementRiskHeuristic",
        "staleRangeHeuristic",
        "log1p_totalChangedLines",
        "delToAddRatio",
        "label_any",
    ],
}


def safe_sigmoid(x: np.ndarray) -> np.ndarray:
    # Clip to avoid overflow/underflow in exp.
    x_clip = np.clip(x, -50, 50)
    return 1.0 / (1.0 + np.exp(-x_clip))


def normal_cdf(x: np.ndarray) -> np.ndarray:
    erf_vec = np.vectorize(math.erf)
    return 0.5 * (1.0 + erf_vec(x / math.sqrt(2)))


def logistic_regression_irls(
    X: np.ndarray, y: np.ndarray, ridge: float = 1e-6, max_iter: int = 50, tol: float = 1e-6
) -> Tuple[np.ndarray, np.ndarray, int]:
    """Fit logistic regression via IRLS with optional ridge (not applied to intercept)."""
    n, p = X.shape
    beta = np.zeros(p)
    penalty = np.eye(p)
    penalty[0, 0] = 0.0  # do not penalize intercept

    for it in range(1, max_iter + 1):
        linear = X @ beta
        mu = safe_sigmoid(linear)
        w = mu * (1.0 - mu)
        # Guard against exact 0 weights.
        w = np.clip(w, 1e-12, None)
        WX = X * w[:, None]
        hessian = X.T @ WX + ridge * penalty
        grad = X.T @ (y - mu) - ridge * (penalty @ beta)
        try:
            delta = np.linalg.solve(hessian, grad)
        except np.linalg.LinAlgError:
            delta = np.linalg.pinv(hessian) @ grad
        beta_new = beta + delta
        if np.linalg.norm(delta, ord=2) < tol:
            beta = beta_new
            return beta, np.linalg.pinv(hessian), it
        beta = beta_new
    return beta, np.linalg.pinv(hessian), max_iter


def log_likelihood(X: np.ndarray, y: np.ndarray, beta: np.ndarray) -> float:
    linear = X @ beta
    p = safe_sigmoid(linear)
    eps = 1e-12
    return float(np.sum(y * np.log(p + eps) + (1.0 - y) * np.log(1.0 - p + eps)))


def compute_collided(df: pd.DataFrame) -> pd.Series:
    if "collided" in df.columns:
        return df["collided"]
    # Treat any concurrent-open collision count > 0 as collided.
    if "activeCollisionCount" in df.columns:
        return (df["activeCollisionCount"].fillna(0).astype(float) > 0).astype(int)
    if "priorOverlapCount" in df.columns:
        return (df["priorOverlapCount"].fillna(0).astype(float) > 0).astype(int)
    raise ValueError("Could not infer 'collided' indicator from available columns.")


def build_design_matrix(df: pd.DataFrame, feature_names: List[str]) -> Tuple[np.ndarray, List[str]]:
    features: List[np.ndarray] = []
    final_names: List[str] = []
    for name in feature_names:
        if name == "log1p_totalChangedLines":
            col = np.log1p(pd.to_numeric(df["totalChangedLines"], errors="coerce").fillna(0.0).to_numpy(dtype=float))
        elif name == "delToAddRatio":
            col = pd.to_numeric(df["delToAddRatio"], errors="coerce").fillna(0.0).to_numpy(dtype=float)
        elif name == "collided":
            col = compute_collided(df).to_numpy(dtype=float)
        else:
            if name not in df.columns:
                raise ValueError(f"Feature '{name}' missing from data columns.")
            col = pd.to_numeric(df[name], errors="coerce").fillna(0.0).to_numpy(dtype=float)
        features.append(col)
        final_names.append(name)
    X = np.column_stack([np.ones(len(df))] + features)
    return X, ["intercept"] + final_names


def parse_features_arg(arg_val: str) -> List[str]:
    return [x.strip() for x in arg_val.split(",") if x.strip()]


def format_table(
    names: List[str], coef: np.ndarray, se: np.ndarray, z: np.ndarray, p_vals: np.ndarray
) -> str:
    lines = []
    header = f"{'feature':<28} {'coef':>10} {'odds_ratio':>12} {'se':>10} {'z':>10} {'p':>10} {'or_95ci':>18}"
    lines.append(header)
    lines.append("-" * len(header))
    for name, b, s, zv, pv in zip(names, coef, se, z, p_vals):
        or_val = math.exp(b)
        lo = math.exp(b - 1.96 * s)
        hi = math.exp(b + 1.96 * s)
        lines.append(
            f"{name:<28} {b:>10.4f} {or_val:>12.4f} {s:>10.4f} {zv:>10.3f} {pv:>10.4f} [{lo:>6.3f}, {hi:>6.3f}]"
        )
    return "\n".join(lines)


def main(argv: Iterable[str]) -> int:
    parser = argparse.ArgumentParser(description="Fit logistic regression on collision features using numpy only.")
    parser.add_argument("--data", default=DEFAULT_DATA_PATH, help="Path to CSV data (default: %(default)s)")
    parser.add_argument("--preset", choices=sorted(PRESETS.keys()), default=None, help="Feature preset (default: base).")
    parser.add_argument("--features", default=None, help="Comma-separated feature names. Cannot be combined with --preset.")
    parser.add_argument(
        "--include_open",
        action="store_true",
        help="Keep outcome=='open' rows as negatives instead of dropping them.",
    )
    parser.add_argument("--ridge", type=float, default=1e-6, help="L2 ridge penalty (default: 1e-6)")
    parser.add_argument("--max-iter", type=int, default=50, help="Maximum IRLS iterations (default: 50)")
    parser.add_argument("--tol", type=float, default=1e-6, help="Convergence tolerance on delta norm (default: 1e-6)")
    args = parser.parse_args(list(argv))

    df = pd.read_csv(args.data)
    df = df.copy()
    df["collided"] = compute_collided(df)
    df["totalChangedLines"] = pd.to_numeric(df["totalChangedLines"], errors="coerce").fillna(0.0)
    df["delToAddRatio"] = pd.to_numeric(df["delToAddRatio"], errors="coerce").fillna(0.0)

    if not args.include_open:
        df = df[df["outcome"] != "open"]

    target = (df["outcome"] == "merged").astype(float).to_numpy()
    if args.features and args.preset:
        raise ValueError("Provide only one of --preset or --features.")
    preset = args.preset or "base"
    if args.features:
        feature_list = parse_features_arg(args.features)
    else:
        feature_list = PRESETS[preset]
    X, names = build_design_matrix(df, feature_list)

    beta, inv_hess, iters = logistic_regression_irls(
        X, target, ridge=args.ridge, max_iter=args.max_iter, tol=args.tol
    )
    se = np.sqrt(np.clip(np.diag(inv_hess), 0, None))
    z_scores = np.where(se > 0, beta / se, 0.0)
    p_vals = 2.0 * (1.0 - normal_cdf(np.abs(z_scores)))
    ll = log_likelihood(X, target, beta)

    warnings = [
        "WARNING: Small-N, convenience features, no train/test split; treat coefficients as directional only.",
        "WARNING: Heuristic labels may embed annotation bias; odds ratios are not causal.",
    ]
    print("\n".join(warnings))
    print(f"Data: {args.data}")
    print(f"Features: {', '.join(feature_list)}")
    print(f"N={len(df)}, positives={int(target.sum())}, iterations={iters}, log_likelihood={ll:.4f}")
    print(format_table(names, beta, se, z_scores, p_vals))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
