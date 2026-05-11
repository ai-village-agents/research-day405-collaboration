#!/usr/bin/env python3
"""
Compile all Session 4 scorer submissions into a comparison matrix.
Run after all scorers have committed their scores.
Usage: python3 analysis/compile_session4_scores.py
"""

import os
import re
import sys

SCORER_DIR = "experiments/session4/scoring/scores"
OUTPUT_FILE = "experiments/session4/scoring/session4_comparison.md"

CONDITIONS = {
    "solo": "Solo (GPT-5.1)",
    "pair": "Pair (Sonnet 4.6 + Haiku 4.5)",
    "trio": "Trio (Proposer→Skeptic→Synthesizer)"
}

BUG_LIST = [
    ("bug1_off_by_one", "Easy", 50),
    ("bug2_missing_await", "Easy", 50),
    ("bug3_loose_equality", "Easy", 50),
    ("bug4_race_condition", "Hard", 100),
    ("bug5_discount_order", "Medium", 75),
    ("bug6_floating_point", "Medium", 75),
    ("bug7_tax_prediscount", "Medium", 75),
    ("bug8_state_leak", "Hard", 100),
    ("bug9_some_vs_every", "Hard", 75),
    ("bug10_json_undefined", "Hard", 75),
]

def find_scorer_files():
    """Find all scorer files that have been filled in (not just placeholders)."""
    files = {}
    if not os.path.exists(SCORER_DIR):
        return files
    for f in os.listdir(SCORER_DIR):
        if f.endswith("_task4.md"):
            path = os.path.join(SCORER_DIR, f)
            with open(path) as fh:
                content = fh.read()
            # Skip placeholders (< 200 chars)
            if len(content) > 200:
                scorer_name = f.replace("scorer_", "").replace("_task4.md", "").replace("_pair", "")
                files[scorer_name] = {"path": path, "content": content}
    return files

def extract_score(content, condition_keyword):
    """Try to extract a numeric score for a condition from scorer content."""
    patterns = [
        rf'{condition_keyword}.*?(?:score|total|final).*?(\d+)',
        rf'(?:score|total|final).*?{condition_keyword}.*?(\d+)',
        rf'{condition_keyword}.*?(\d+)\s*/\s*800',
    ]
    for pat in patterns:
        match = re.search(pat, content, re.IGNORECASE | re.DOTALL)
        if match:
            score = int(match.group(1))
            if 0 <= score <= 800:
                return score
    return None

def main():
    scorer_files = find_scorer_files()
    
    if not scorer_files:
        print("No completed scorer files found yet.")
        print(f"Looking in: {SCORER_DIR}")
        return
    
    print(f"Found {len(scorer_files)} scorer submission(s):")
    for name, info in scorer_files.items():
        print(f"  - {name}: {info['path']}")
    
    # Build comparison output
    output = []
    output.append("# Session 4 Score Comparison\n")
    output.append(f"Generated: {os.popen('date').read().strip()}\n")
    output.append(f"Scorers found: {', '.join(scorer_files.keys())}\n")
    
    output.append("## Score Matrix\n")
    output.append("| Condition | " + " | ".join(scorer_files.keys()) + " | Avg | Δ Max |")
    output.append("|-----------|" + "|".join(["---"] * len(scorer_files)) + "|-----|-------|")
    
    for cond_key, cond_name in CONDITIONS.items():
        scores = {}
        for scorer, info in scorer_files.items():
            s = extract_score(info["content"], cond_key)
            scores[scorer] = s
        
        score_vals = [v for v in scores.values() if v is not None]
        avg = f"{sum(score_vals)/len(score_vals):.0f}" if score_vals else "?"
        delta = f"{max(score_vals) - min(score_vals)}" if len(score_vals) >= 2 else "N/A"
        
        row = f"| {cond_name} | " + " | ".join(
            str(scores[s]) if scores[s] is not None else "?" for s in scorer_files
        ) + f" | {avg} | {delta} |"
        output.append(row)
    
    output.append("")
    output.append("## Discrepancies >50 pts")
    output.append("*(Flagged for adjudication)*\n")
    output.append("_None detected yet — will be populated after scores are entered._\n")
    
    result = "\n".join(output)
    print("\n" + result)
    
    with open(OUTPUT_FILE, "w") as f:
        f.write(result)
    print(f"\nWritten to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
