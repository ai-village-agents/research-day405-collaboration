#!/usr/bin/env python3
"""
Pilot Experiment Scoring Tool
Multi-Agent Coordination Research - Day 405
"""

# Bug scoring rubric
BUGS = {
    1: {"name": "Assignment vs Comparison", "severity": "Critical", "find_points": 50, "fix_points": 50},
    2: {"name": "Off-by-One Error", "severity": "Critical", "find_points": 50, "fix_points": 50},
    3: {"name": "Object vs Set", "severity": "Low", "find_points": 25, "fix_points": 25},
    4: {"name": "Case Sensitivity", "severity": "Medium", "find_points": 50, "fix_points": 50},
    5: {"name": "Array vs Length", "severity": "Medium", "find_points": 50, "fix_points": 50},
    6: {"name": "AND vs OR Logic", "severity": "Critical", "find_points": 50, "fix_points": 50},
}

BONUS_EDGE_CASES = 25
BONUS_TEST_CASES = 25
MAX_SCORE = 600 + BONUS_EDGE_CASES + BONUS_TEST_CASES

def score_submission(bugs_found: list, bugs_fixed: list, edge_cases: bool = False, test_cases: bool = False) -> dict:
    """Score a pilot submission."""
    score = 0
    details = []
    
    for bug_id in bugs_found:
        if bug_id in BUGS:
            bug = BUGS[bug_id]
            points = bug["find_points"]
            if bug_id in bugs_fixed:
                points += bug["fix_points"]
            score += points
            details.append(f"Bug {bug_id} ({bug['name']}): +{points}")
    
    if edge_cases:
        score += BONUS_EDGE_CASES
        details.append(f"Edge cases bonus: +{BONUS_EDGE_CASES}")
    
    if test_cases:
        score += BONUS_TEST_CASES
        details.append(f"Test cases bonus: +{BONUS_TEST_CASES}")
    
    return {
        "total_score": score,
        "max_possible": MAX_SCORE,
        "percentage": round(score / MAX_SCORE * 100, 1),
        "bugs_found": len(bugs_found),
        "bugs_fixed": len(bugs_fixed),
        "details": details
    }

# Example scoring for unstructured pair (Opus 4.5 + Sonnet 4.5)
if __name__ == "__main__":
    print("=" * 60)
    print("PILOT EXPERIMENT SCORING")
    print("=" * 60)
    
    # Unstructured Pair Results
    unstructured = score_submission(
        bugs_found=[1, 2, 3, 4, 5, 6],
        bugs_fixed=[1, 2, 3, 4, 5, 6],
        edge_cases=True,
        test_cases=True
    )
    
    print("\n📊 UNSTRUCTURED PAIR (Claude Opus 4.5 + Claude Sonnet 4.5)")
    print(f"   Score: {unstructured['total_score']}/{unstructured['max_possible']} ({unstructured['percentage']}%)")
    print(f"   Bugs Found: {unstructured['bugs_found']}/6")
    print(f"   Bugs Fixed: {unstructured['bugs_fixed']}/6")
    for detail in unstructured['details']:
        print(f"   - {detail}")
    
    print("\n" + "=" * 60)
    print("Awaiting Solo (GPT-5.1) results for comparison...")
    print("=" * 60)
