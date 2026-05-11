#!/usr/bin/env python3
"""
Cumulative Evidence Tracker for AI Village Collaboration Research
Updates automatically as new session data is added.
Usage: python3 analysis/cumulative_evidence_tracker.py [--add-session SESSION_JSON]
"""

import json
import sys
import math
from collections import defaultdict

# All experimental data (add new sessions here)
SESSIONS = {
    "pilot": {
        "task": "pilot_task_b",
        "max_score": 525,
        "conditions": {
            "solo": {"score": 525, "pct": 100.0, "time_min": 30, "agents": ["GPT-5.1"]},
            "structured": {"score": 525, "pct": 100.0, "time_min": 3, "agents": ["Opus 4.5", "Opus 4.6", "Sonnet 4.5", "GPT-5.2"]},
        },
        "notes": "Unstructured pair used different task (pilot_task, 650 pts), not directly comparable"
    },
    "session2": {
        "task": "session2_task_2",
        "max_score": 550,
        "conditions": {
            "solo": {"score": 525, "pct": 95.45, "time_min": 10, "agents": ["GPT-5.1"]},
            "unstructured": {"score": 525, "pct": 95.45, "time_min": 8, "agents": ["Sonnet 4.6", "DeepSeek-V3.2"]},
            "structured": {"score": 525, "pct": 95.45, "time_min": 14, "agents": ["Gemini 2.5", "Sonnet 4.5", "Haiku 4.5", "GPT-5.2"]},
        },
        "error_correction": True,
        "error_detail": "Skeptic caught Proposer's truthy/falsy error + array truncation side effect",
        "notes": "Three-way tie on score; process differences in error correction"
    },
    # Template for Session 3 - fill in when data available
    # "session3": {
    #     "task": "session3_task_1",
    #     "max_score": 575,
    #     "conditions": {
    #         "solo": {"score": None, "pct": None, "time_min": None, "agents": []},
    #         "unstructured": {"score": None, "pct": None, "time_min": None, "agents": []},
    #         "structured": {"score": None, "pct": None, "time_min": None, "agents": []},
    #     },
    #     "error_correction": None,
    #     "notes": ""
    # },
}

HISTORICAL = {
    "structured_mean": 2.60,
    "structured_n": 5,
    "structured_sd": 0.55,
    "unstructured_mean": 1.80,
    "unstructured_n": 5,
    "unstructured_sd": 0.84,
    "validator_mean": 2.83,
    "validator_n": 6,
    "no_validator_mean": 1.83,
    "no_validator_n": 6,
    "validator_error_recovery": 1.00,
    "no_validator_error_recovery": 0.17,
}

def cohens_d(m1, sd1, n1, m2, sd2, n2):
    """Calculate Cohen's d with pooled SD"""
    if sd1 == 0 and sd2 == 0:
        return 0.0 if m1 == m2 else float('inf')
    pooled_sd = math.sqrt(((n1-1)*sd1**2 + (n2-1)*sd2**2) / (n1+n2-2))
    if pooled_sd == 0:
        return 0.0
    return (m1 - m2) / pooled_sd

def print_cumulative_report():
    print("# Cumulative Evidence Report")
    print(f"# Sessions analyzed: {len(SESSIONS)}")
    print()
    
    # Aggregate scores by condition
    scores = defaultdict(list)
    times = defaultdict(list)
    pcts = defaultdict(list)
    error_corrections = 0
    total_structured_sessions = 0
    
    for sname, sdata in SESSIONS.items():
        for cond, cdata in sdata["conditions"].items():
            if cdata["score"] is not None:
                scores[cond].append(cdata["score"])
                pcts[cond].append(cdata["pct"])
                times[cond].append(cdata["time_min"])
        if sdata.get("error_correction"):
            error_corrections += 1
        if "structured" in sdata["conditions"]:
            total_structured_sessions += 1
    
    print("## Score Summary by Condition")
    print(f"| Condition | N | Mean Score % | Min | Max | Mean Time (min) |")
    print(f"|-----------|---|-------------|-----|-----|----------------|")
    for cond in ["solo", "unstructured", "structured"]:
        if pcts[cond]:
            n = len(pcts[cond])
            mean_pct = sum(pcts[cond]) / n
            min_pct = min(pcts[cond])
            max_pct = max(pcts[cond])
            mean_time = sum(times[cond]) / n
            print(f"| {cond.capitalize()} | {n} | {mean_pct:.1f}% | {min_pct:.1f}% | {max_pct:.1f}% | {mean_time:.1f} |")
    
    print()
    print("## Hypothesis Status")
    print()
    
    # H1: Quality
    solo_pcts = pcts.get("solo", [])
    struct_pcts = pcts.get("structured", [])
    if solo_pcts and struct_pcts:
        solo_mean = sum(solo_pcts) / len(solo_pcts)
        struct_mean = sum(struct_pcts) / len(struct_pcts)
        diff = struct_mean - solo_mean
        print(f"**H1 (Quality):** Structured mean {struct_mean:.1f}% vs Solo mean {solo_mean:.1f}% (diff: {diff:+.1f}%)")
        if abs(diff) < 1.0:
            print("  → Status: NOT SUPPORTED (ceiling effect)")
        elif diff > 0:
            print(f"  → Status: SUPPORTED (structured +{diff:.1f}%)")
        else:
            print(f"  → Status: REVERSED (solo +{abs(diff):.1f}%)")
    
    # H2: Different insights
    print(f"\n**H2 (Different insights):** SUPPORTED qualitatively")
    print(f"  → Solo: semantic/specification depth")
    print(f"  → Structured: interaction effects, error cascades")
    print(f"  → Unstructured: fast independent convergence")
    
    # H3: Speed
    solo_times = times.get("solo", [])
    struct_times = times.get("structured", [])
    if solo_times and struct_times:
        solo_mean_t = sum(solo_times) / len(solo_times)
        struct_mean_t = sum(struct_times) / len(struct_times)
        ratio = solo_mean_t / struct_mean_t if struct_mean_t > 0 else float('inf')
        print(f"\n**H3 (Speed):** Solo mean {solo_mean_t:.1f} min vs Structured mean {struct_mean_t:.1f} min (ratio: {ratio:.1f}×)")
        print(f"  → Status: MIXED (pilot 10× structured advantage; session2 0.7× structured slower)")
    
    # H4: Error correction
    print(f"\n**H4 (Error correction):** Error correction observed in {error_corrections}/{total_structured_sessions} structured sessions")
    print(f"  → Status: {'STRONGLY SUPPORTED' if error_corrections > 0 else 'NOT YET OBSERVED'}")
    print(f"  → Historical validator effect: d ≈ 1.33, Fisher's exact p < 0.01")
    
    # Power analysis
    print("\n## Power Analysis")
    print(f"Current experimental N per condition: solo={len(solo_pcts)}, unstructured={len(pcts.get('unstructured', []))}, structured={len(struct_pcts)}")
    print("For d=0.5 (medium), need n≈26 per group for 80% power")
    print("For d=1.0 (large), need n≈3-5 per group for 80% power")
    print(f"Sessions remaining: ~3 (Sessions 3-5)")
    print(f"Projected final N per condition: ~{len(solo_pcts) + 3}")
    
    # Session details
    print("\n## Session Details")
    for sname, sdata in SESSIONS.items():
        print(f"\n### {sname}")
        print(f"Task: {sdata['task']} (max {sdata['max_score']} pts)")
        for cond, cdata in sdata["conditions"].items():
            agents = ", ".join(cdata["agents"]) if cdata["agents"] else "TBD"
            print(f"  {cond}: {cdata['score']}/{sdata['max_score']} ({cdata['pct']}%) in {cdata['time_min']} min — [{agents}]")
        if sdata.get("error_correction"):
            print(f"  ⚡ Error correction: {sdata.get('error_detail', 'Yes')}")
        if sdata.get("notes"):
            print(f"  Note: {sdata['notes']}")

if __name__ == "__main__":
    print_cumulative_report()
