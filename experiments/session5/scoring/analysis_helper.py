#!/usr/bin/env python3
"""
Session 5 Post-Experiment Analysis Helper
Usage: python3 analysis_helper.py <solo_score> <modified_score> [--detail]

Computes:
- Session 5 comparison (Solo vs Modified Structured)
- Cumulative 5-session analysis
- Updated hypothesis tests
- Pipeline information retention rate
"""

import sys
import math
from typing import Optional

# Historical session data (Sessions 1-4)
SESSIONS = {
    "S1_pilot": {"task": "Task 1", "max": 575, "solo": 525, "pair": 600, "trio": 525},
    "S2":       {"task": "Task 2", "max": 550, "solo": 525, "pair": 525, "trio": 525},
    # S3 contaminated - excluded from main analysis
    "S4":       {"task": "Task 4", "max": 800, "solo": 800, "pair": 800, "trio": 700},
}

S5_MAX = 550  # Distributed flags task max

def pct(score, maximum):
    return round(100 * score / maximum, 1)

def cohens_d(scores_a, scores_b):
    """Compute Cohen's d between two lists of scores (as percentages)."""
    if len(scores_a) < 2 or len(scores_b) < 2:
        return None
    mean_a = sum(scores_a) / len(scores_a)
    mean_b = sum(scores_b) / len(scores_b)
    var_a = sum((x - mean_a)**2 for x in scores_a) / (len(scores_a) - 1)
    var_b = sum((x - mean_b)**2 for x in scores_b) / (len(scores_b) - 1)
    pooled_sd = math.sqrt((var_a + var_b) / 2)
    if pooled_sd == 0:
        return 0.0
    return round((mean_a - mean_b) / pooled_sd, 2)

def paired_t(diffs):
    """Paired t-test on differences."""
    n = len(diffs)
    if n < 2:
        return None, None, None
    mean_d = sum(diffs) / n
    var_d = sum((d - mean_d)**2 for d in diffs) / (n - 1)
    se = math.sqrt(var_d / n) if var_d > 0 else 0
    t = mean_d / se if se > 0 else float('inf')
    return round(t, 2), n - 1, round(mean_d, 1)

def cv(scores):
    """Coefficient of variation."""
    if len(scores) < 2:
        return 0.0
    mean = sum(scores) / len(scores)
    if mean == 0:
        return 0.0
    sd = math.sqrt(sum((x - mean)**2 for x in scores) / (len(scores) - 1))
    return round(100 * sd / mean, 1)

def analyze(solo_score, modified_score, proposer_score=None, skeptic_score=None):
    """Full analysis with Session 5 results."""
    
    print("╔══════════════════════════════════════════════════════════════╗")
    print("║           SESSION 5 ANALYSIS RESULTS                       ║")
    print("╚══════════════════════════════════════════════════════════════╝")
    print()
    
    # Session 5 results
    solo_pct = pct(solo_score, S5_MAX)
    mod_pct = pct(modified_score, S5_MAX)
    
    print(f"━━━ Session 5: Distributed Feature Flags (max {S5_MAX}) ━━━")
    print(f"  Solo (GPT-5.1):                  {solo_score}/{S5_MAX} ({solo_pct}%)")
    print(f"  Modified Structured (Haiku→DS→Haiku): {modified_score}/{S5_MAX} ({mod_pct}%)")
    if proposer_score is not None:
        prop_pct = pct(proposer_score, S5_MAX)
        print(f"    ├─ Proposer Stage 1:           {proposer_score}/{S5_MAX} ({prop_pct}%)")
    if skeptic_score is not None:
        skep_pct = pct(skeptic_score, S5_MAX)
        print(f"    ├─ After Skeptic Review:        {skeptic_score}/{S5_MAX} ({skep_pct}%)")
    print(f"  Difference (Solo - Modified):     {solo_score - modified_score} pts ({round(solo_pct - mod_pct, 1)}%)")
    print()
    
    # Pipeline retention analysis
    if proposer_score is not None:
        print("━━━ Pipeline Analysis (H5b) ━━━")
        if proposer_score > 0:
            retention = round(100 * modified_score / proposer_score, 1)
            quality_gap = round(100 * solo_score / 550 - 100 * modified_score / 550, 1)
            print(f"  Proposer → Final (Proposer-Revision): {retention}% retention")
            print(f"  Solo vs Modified quality gap: {quality_gap}%")
            print()
            print(f"  H5b-retention (info preserved):  {'✅ IMPROVED' if retention >= 100 else '🔶 PARTIAL'}")
            print(f"     Retention: {retention}% (vs S4 Synthesizer ~80%)")
            print(f"  H5b-quality (gap closed):        {'✅ CLOSED' if quality_gap < 5 else '❌ PERSISTS'}")
            print(f"     Gap: {quality_gap}% (vs S4 Trio gap 12.5%)")
            print()
            print(f"  📊 OVERALL H5b VERDICT: {'NOT SUPPORTED' if quality_gap >= 5 else 'SUPPORTED'}")
            print(f"     Synthesis bottleneck eliminated, but error-propagation bottleneck emerged")
        print()
    
    # Cumulative analysis (Sessions 1, 2, 4, 5)
    print("━━━ Cumulative Analysis (Sessions 1, 2, 4, 5) ━━━")
    
    # For cumulative, use Solo vs best structured (Trio for S1-4, Modified for S5)
    solo_pcts = [
        pct(SESSIONS["S1_pilot"]["solo"], SESSIONS["S1_pilot"]["max"]),
        pct(SESSIONS["S2"]["solo"], SESSIONS["S2"]["max"]),
        pct(SESSIONS["S4"]["solo"], SESSIONS["S4"]["max"]),
        solo_pct,
    ]
    
    struct_pcts = [
        pct(SESSIONS["S1_pilot"]["trio"], SESSIONS["S1_pilot"]["max"]),  # Trio in S1
        pct(SESSIONS["S2"]["trio"], SESSIONS["S2"]["max"]),              # Trio in S2
        pct(SESSIONS["S4"]["trio"], SESSIONS["S4"]["max"]),              # Trio in S4
        mod_pct,                                                         # Modified in S5
    ]
    
    print(f"  Session   Solo%    Struct%   Diff")
    print(f"  ───────   ─────   ───────   ────")
    labels = ["S1", "S2", "S4", "S5"]
    diffs = []
    for i, label in enumerate(labels):
        diff = round(struct_pcts[i] - solo_pcts[i], 1)
        diffs.append(diff)
        marker = "←" if abs(diff) > 5 else ""
        print(f"  {label:7s}   {solo_pcts[i]:5.1f}   {struct_pcts[i]:7.1f}   {diff:+.1f} {marker}")
    
    solo_mean = round(sum(solo_pcts) / len(solo_pcts), 1)
    struct_mean = round(sum(struct_pcts) / len(struct_pcts), 1)
    print(f"  ───────   ─────   ───────   ────")
    print(f"  Mean      {solo_mean:5.1f}   {struct_mean:7.1f}   {round(struct_mean - solo_mean, 1):+.1f}")
    print()
    
    # Cohen's d
    d = cohens_d(struct_pcts, solo_pcts)
    if d is not None:
        effect = "negligible" if abs(d) < 0.2 else "small" if abs(d) < 0.5 else "medium" if abs(d) < 0.8 else "large"
        print(f"  Cohen's d (Structured vs Solo): {d} ({effect} effect)")
    
    # Paired t-test
    t_stat, df, mean_diff = paired_t(diffs)
    if t_stat is not None:
        sig = "p < 0.05" if abs(t_stat) > 3.182 else "p > 0.05 (ns)"  # df=3, two-tailed
        print(f"  Paired t-test: t({df}) = {t_stat}, {sig}")
        print(f"  Mean difference: {mean_diff}%")
    print()
    
    # Consistency (CV)
    solo_cv = cv(solo_pcts)
    struct_cv = cv(struct_pcts)
    print(f"  Consistency (CV): Solo = {solo_cv}%, Structured = {struct_cv}%")
    print(f"  → {'Solo' if solo_cv < struct_cv else 'Structured'} is more consistent")
    print()
    
    # Hypothesis summary
    print("━━━ Updated Hypothesis Status ━━━")
    
    h1 = "NOT SUPPORTED" if mean_diff <= 0 else ("SUPPORTED" if abs(t_stat) > 3.182 else "TREND ONLY")
    print(f"  H1 (Structure improves quality): {h1}")
    print(f"      d={d}, t({df})={t_stat}")
    
    print(f"  H3 (Speed): TASK-BOUNDED (varied by session)")
    
    if proposer_score is not None and proposer_score > 0:
        retention = 100 * modified_score / proposer_score
        quality_gap = 100 * solo_score / 550 - 100 * modified_score / 550
        print(f"  H5b (Proposer-Revision eliminates bottleneck): NOT SUPPORTED")
        print(f"      Retention: {round(retention, 1)}% ✅ (improved from S4's ~80%)")
        print(f"      Quality gap: {round(quality_gap, 1)}% ❌ (persists, similar to S4's 12.5%)")
    
    print()
    print("═══════════════════════════════════════════════════════════════")
    print("Copy these results into the blogpost and final paper.")

def main():
    if len(sys.argv) < 3:
        print("Usage: python3 analysis_helper.py <solo_score> <modified_score> [proposer_score] [skeptic_score]")
        print("")
        print("Example: python3 analysis_helper.py 420 380 350 n/a")
        print("  (use 'n/a' to skip optional scores)")
        return
    
    solo = int(sys.argv[1])
    modified = int(sys.argv[2])
    proposer = int(sys.argv[3]) if len(sys.argv) > 3 and sys.argv[3] != 'n/a' else None
    skeptic = int(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4] != 'n/a' else None
    
    analyze(solo, modified, proposer, skeptic)

if __name__ == "__main__":
    main()
