#!/usr/bin/env python3
"""Task 2 Scoring Helper - analyzeUserActivity (500 base + 50 bonus = 550 max)"""

BUGS = {
    1: {"name": "Assignment instead of comparison", "line": 15, "severity": "CRITICAL", "points": 125,
        "description": "records.length = 0 should be records.length === 0"},
    2: {"name": "Off-by-one array bounds", "line": 22, "severity": "CRITICAL", "points": 125,
        "description": "i <= records.length should be i < records.length"},
    3: {"name": "NaN propagation risk", "line": 31, "severity": "MEDIUM", "points": 75,
        "description": "userCounts[x] + 1 || 1 should be (userCounts[x] || 0) + 1"},
    4: {"name": "Boolean sort comparator", "line": 43, "severity": "MEDIUM", "points": 100,
        "description": "a[1] > b[1] should return numeric difference b[1] - a[1]"},
    5: {"name": "Arbitrary filter excludes power users", "line": 47, "severity": "MEDIUM", "points": 75,
        "description": "Remove && u.actionCount < 100 or justify keeping it"},
}

BONUS = {
    "interaction_effects": {"points": 25, "description": "Identified how bugs interact (e.g., Bug 1+2 cascade)"},
    "test_cases": {"points": 25, "description": "Suggested comprehensive test cases"},
}

def score_submission(bugs_found, bugs_fixed, interaction_bonus=False, test_bonus=False):
    """Score a submission and return detailed breakdown."""
    total = 0
    details = []
    for bug_id, bug in BUGS.items():
        found = bug_id in bugs_found
        fixed = bug_id in bugs_fixed
        if found and fixed:
            pts = bug["points"]
        elif found:
            pts = bug["points"] // 2  # partial credit for finding without fixing
        else:
            pts = 0
        total += pts
        details.append(f"  Bug {bug_id} ({bug['name']}): {'FOUND' if found else 'MISSED'} / {'FIXED' if fixed else 'NOT FIXED'} = {pts}/{bug['points']}")
    
    bonus = 0
    if interaction_bonus:
        bonus += 25
        details.append(f"  Interaction Effects Bonus: +25")
    if test_bonus:
        bonus += 25
        details.append(f"  Test Cases Bonus: +25")
    
    total += bonus
    max_score = 550
    pct = total / max_score * 100
    
    print(f"\n{'='*50}")
    print(f"SCORE: {total}/{max_score} ({pct:.1f}%)")
    print(f"  Base: {total-bonus}/500 | Bonus: {bonus}/50")
    print(f"{'='*50}")
    for d in details:
        print(d)
    print(f"{'='*50}\n")
    return total, max_score, pct

if __name__ == "__main__":
    # Example: Score solo (GPT-5.1)
    print("=== Solo (GPT-5.1) Session 2 Task 2 ===")
    score_submission(
        bugs_found={1,2,3,4,5},
        bugs_fixed={1,2,3,4,5},
        interaction_bonus=True,
        test_bonus=False
    )
