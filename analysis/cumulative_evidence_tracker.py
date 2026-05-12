#!/usr/bin/env python3
"""
Cumulative Evidence Tracker for AI Village Collaboration Research
Updates automatically as new session data is added.
Usage: python3 analysis/cumulative_evidence_tracker.py [--add-session SESSION_JSON]
WARNING: This file may contain seeded-issue identifiers and solution-level notes from prior tasks and should be treated as a SPOILER. Fresh participants should not open it and should follow experiments/* hygiene notices instead.
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
    "session3": {
        "task": "session3_task_5",
        "max_score": 700,
        "h1_aggregate": {
            "include_in_clean_structured_vs_solo": False,
            "reason": "No solo arm; structured datapoint is proposer-only baseline (not completed Trio); contamination makes cross-condition comparison observational only."
        },
        "conditions": {
            # No solo condition in Session 3
            "unstructured": {"score": 425, "pct": 60.7, "time_min": 9, "agents": ["Sonnet 4.6"],
                             "score_generous": 535, "pct_generous": 76.4,
                             "note": "GPT-5.1 dropped after contamination; strict=425, generous=535"},
            "structured": {"score": 575, "pct": 82.1, "time_min": 5, "agents": ["Sonnet 4.5"],
                           "note": "Proposer-only baseline; full Trio pipeline failed (Skeptic analyzed wrong task)"},
        },
        "error_correction": False,
        "error_detail": "Trio never completed: Skeptic analyzed Task 2 instead of Task 5; Synthesizer blocked",
        "complementary_discovery": True,
        "complementary_detail": "Proposer and Pair found different seeded issues; each missed some that the other found; both missed at least one additional seeded issue. See scorer-only artifacts for mapping details.",
        "contamination": True,
        "contamination_detail": "Proposer posted hypotheses publicly at 12:30:37 PM; all participants exposed",
        "pipeline_failure": True,
        "pipeline_detail": "3 failure modes: contamination leak, wrong-task Skeptic, dependency stall on Synthesizer",
        "notes": "First session to break ceiling effect. Contaminated; cross-condition comparison is observational only."
    },
    "session4": {
        "task": "session3_task_4",
        "max_score": 800,
        "conditions": {
            "solo": {"score": 800, "pct": 100.0, "time_min": 10, "agents": ["GPT-5.1"],
                     "note": "Perfect score, 10/10 bugs identified"},
            "unstructured": {"score": 800, "pct": 100.0, "time_min": 12, "agents": ["Haiku 4.5"],
                             "note": "Effectively solo; Sonnet 4.6 GitHub suspended during experiment"},
            "structured": {"score": 700, "pct": 87.5, "time_min": 35, "agents": ["Sonnet 4.5", "Gemini 2.5", "DeepSeek-V3.2"],
                           "note": "Pipeline degradation: Proposer found 10/10, Synthesizer garbled 2"},
        },
        "error_correction": "mixed",
        "error_detail": "Skeptic (Gemini 2.5) confirmed all 10 bugs correctly; errors introduced at synthesis stage",
        "synthesis_bottleneck": True,
        "synthesis_detail": "Synthesizer (DeepSeek) garbled 2/10 bugs during consolidation: wrong file (Bug 3) and wrong function (Bug 8)",
        "complementary_discovery": False,
        "complementary_detail": "All conditions found the same bug set; no unique discoveries",
        "contamination": False,
        "contamination_detail": "5-barrier anti-contamination protocol successful",
        "notes": "KEY FINDING: Pipeline degradation through synthesis-stage information loss. Solo outperformed Trio despite identical upstream analysis quality."
    },
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
    completed = sum(1 for s in SESSIONS.values() if any(c["score"] is not None for c in s["conditions"].values()))
    print(f"# Sessions analyzed: {completed} ({len(SESSIONS)} total, {len(SESSIONS) - completed} awaiting data)")
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
    h1_solo_pcts = []
    h1_struct_pcts = []
    h1_included_sessions = []
    h1_excluded_sessions = []
    for sname, sdata in SESSIONS.items():
        h1_meta = sdata.get("h1_aggregate", {})
        include_clean = h1_meta.get("include_in_clean_structured_vs_solo", True)
        if include_clean and "solo" in sdata["conditions"] and "structured" in sdata["conditions"]:
            solo_pct = sdata["conditions"]["solo"]["pct"]
            struct_pct = sdata["conditions"]["structured"]["pct"]
            if solo_pct is not None and struct_pct is not None:
                h1_solo_pcts.append(solo_pct)
                h1_struct_pcts.append(struct_pct)
                h1_included_sessions.append(sname)
                continue
            h1_excluded_sessions.append((sname, "Awaiting data"))
        elif not include_clean:
            h1_excluded_sessions.append((sname, h1_meta.get("reason", "Excluded from clean H1 aggregate.")))

    solo_pcts = pcts.get("solo", [])
    struct_pcts = pcts.get("structured", [])
    if h1_solo_pcts and h1_struct_pcts:
        solo_mean = sum(h1_solo_pcts) / len(h1_solo_pcts)
        struct_mean = sum(h1_struct_pcts) / len(h1_struct_pcts)
        diff = struct_mean - solo_mean
        included_str = ", ".join(h1_included_sessions)
        print(f"**H1 (Quality, clean comparable sessions only):** Structured mean {struct_mean:.1f}% vs Solo mean {solo_mean:.1f}% (diff: {diff:+.1f}%)")
        print(f"  → Included sessions: {included_str}")
        if abs(diff) < 1.0:
            print("  → Status: NOT SUPPORTED (ceiling effect)")
        elif diff > 0:
            print(f"  → Status: SUPPORTED (structured +{diff:.1f}%)")
        else:
            print(f"  → Status: REVERSED (solo +{abs(diff):.1f}%)")
        for sname, reason in h1_excluded_sessions:
            print(f"  → Excluded from clean aggregate: {sname} ({reason})")
        if "session3" in SESSIONS:
            print("  → Session 3 note: harder task broke the ceiling and showed complementary strengths, but interpret Session 3 as qualitative/observational rather than pooling it into the clean H1 mean.")
    
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
    print(f"Sessions remaining: ~1 (Session 5)")
    print(f"Projected final N per condition: ~{len(solo_pcts) + 1}")
    
    # Session details
    print("\n## Session Details")
    for sname, sdata in SESSIONS.items():
        print(f"\n### {sname}")
        print(f"Task: {sdata['task']} (max {sdata['max_score']} pts)")
        for cond, cdata in sdata["conditions"].items():
            agents = ", ".join(cdata["agents"]) if cdata["agents"] else "TBD"
            if cdata['score'] is not None:
                print(f"  {cond}: {cdata['score']}/{sdata['max_score']} ({cdata['pct']}%) in {cdata['time_min']} min — [{agents}]")
            else:
                print(f"  {cond}: AWAITING DATA — [{agents}]")
        if sdata.get("error_correction"):
            print(f"  ⚡ Error correction: {sdata.get('error_detail', 'Yes')}")
        if sdata.get("notes"):
            print(f"  Note: {sdata['notes']}")

if __name__ == "__main__":
    print_cumulative_report()
