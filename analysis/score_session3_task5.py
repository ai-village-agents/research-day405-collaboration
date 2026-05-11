#!/usr/bin/env python3
"""
Scoring helper for Session 3 Task 5 (API Rate Limiter).
Total: 700 points (10 bugs across 3 tiers, 2 bonuses)

Bug points:
- EASY (100 points total): 2 bugs × 50 points each
- MEDIUM (225 points total): 3 bugs × 75 points each  
- HARD (275 points total): 4 bugs × 68.75 points each (rounded to nearest 25 for rubric)

Bonuses:
- Interaction effects: +25 points
- Test design: +25 points
- Ambiguity credit: +0 to +25 points (discretionary)

Penalties:
- False positives: -50 points per incorrect bug claim
"""

import sys

BUG_POINTS = {
    # Easy bugs (50 points each)
    "bug1_token_refill_drift": 50,
    "bug2_config_validation_missing": 50,
    
    # Medium bugs (75 points each) 
    "bug3_bucket_overflow": 75,
    "bug4_race_condition": 75,
    "bug5_memory_leak": 75,
    
    # Hard bugs (68.75 → 68 for rubric, treat as 70 for calculation)
    "bug6_clock_monotonicity": 70,
    "bug7_missing_headers": 70,
    "bug8_cost_leq_zero_unlimited": 70,
    "bug9_error_handling": 70,
    "bug10_shallow_merge": 70,
}

BONUSES = {
    "interaction_effects": 25,
    "test_design": 25,
}

def calculate_score(found_bugs, fixed_bugs, bonuses, ambiguity_credit=0, false_positive_deduction=0):
    """
    Calculate score for Task 5 submission.
    
    Args:
        found_bugs: list of bug keys found (e.g., ["bug1_token_refill_drift", "bug2_config_validation_missing"])
        fixed_bugs: list of bug keys correctly fixed and explained
        bonuses: list of bonus keys earned
        ambiguity_credit: discretionary credit (0-25)
        false_positive_deduction: number of incorrect bug claims × 50
        
    Returns:
        dict with score breakdown
    """
    # Score for found bugs
    found_score = sum(BUG_POINTS.get(bug, 0) for bug in found_bugs)
    
    # Score for fixed bugs (subset of found)
    fixed_score = sum(BUG_POINTS.get(bug, 0) for bug in fixed_bugs if bug in found_bugs)
    
    # Bonuses
    bonus_score = sum(BONUSES.get(bonus, 0) for bonus in bonuses)
    
    # Total
    base_score = found_score
    adjusted_score = base_score + bonus_score + ambiguity_credit - false_positive_deduction
    
    return {
        "base_found": found_score,
        "base_fixed": fixed_score,
        "bonuses": bonus_score,
        "ambiguity_credit": ambiguity_credit,
        "false_positive_deduction": false_positive_deduction,
        "total": adjusted_score,
        "max_possible": 700,
        "percent": round(adjusted_score / 700 * 100, 2),
    }

def print_rubric():
    """Print scoring rubric for Task 5."""
    print("\n" + "="*60)
    print("TASK 5 SCORING RUBRIC (API Rate Limiter)")
    print("="*60)
    
    print("\n--- BUGS (10 total, 700 points) ---")
    
    print("\nEASY BUGS (2 bugs, 50 points each):")
    print("  1. bug1_token_refill_drift (50 pts)")
    print("  2. bug2_config_validation_missing (50 pts)")
    
    print("\nMEDIUM BUGS (3 bugs, 75 points each):")
    print("  3. bug3_bucket_overflow (75 pts)")
    print("  4. bug4_race_condition (75 pts)")
    print("  5. bug5_memory_leak (75 pts)")
    
    print("\nHARD BUGS (5 bugs, 70 points each):")
    print("  6. bug6_clock_monotonicity (70 pts)")
    print("  7. bug7_missing_headers (70 pts)")
    print("  8. bug8_cost_leq_zero_unlimited (70 pts)")
    print("  9. bug9_error_handling (70 pts)")
    print(" 10. bug10_shallow_merge (70 pts)")
    
    print("\n--- BONUSES (up to +50 points) ---")
    for bonus, points in BONUSES.items():
        print(f"  {bonus}: +{points} pts")
    
    print("\n--- PENALTIES ---")
    print("  False positive: -50 pts per incorrect bug claim")
    
    print("\n--- DISCRETIONARY ---")
    print("  Ambiguity credit: +0 to +25 pts")
    
    print("\n" + "="*60)
    print(f"MAX SCORE: 700 + 50 + 25 = 775 possible")
    print("="*60)

def print_template():
    """Print manual scoring template."""
    print("\n" + "="*60)
    print("MANUAL SCORING TEMPLATE FOR TASK 5")
    print("="*60)
    print("\nBug Finding Tracking:")
    for i in range(1, 11):
        print(f"  [ ] bug{i}_... [ ] Found [ ] Fixed")
    
    print("\nBonuses:")
    for bonus in BONUSES:
        print(f"  [ ] {bonus} (+{BONUSES[bonus]} pts)")
    
    print("\nPenalties:")
    print("  [ ] False positives: _____ × 50 = _____ pts deduction")
    
    print("\nDiscretionary:")
    print("  [ ] Ambiguity credit: _____ pts (0-25)")
    
    print("\n" + "="*60)

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description="Score Session 3 Task 5 submissions")
    parser.add_argument("--rubric", action="store_true", help="Print scoring rubric")
    parser.add_argument("--template", action="store_true", help="Print manual scoring template")
    parser.add_argument("--found", help="Comma-separated list of found bug keys")
    parser.add_argument("--fixed", help="Comma-separated list of fixed bug keys")
    parser.add_argument("--bonuses", help="Comma-separated list of bonus keys")
    parser.add_argument("--ambiguity", type=int, default=0, help="Ambiguity credit (0-25)")
    parser.add_argument("--false-positive-deduction", type=int, default=0, 
                       help="False positive deduction (number incorrect × 50)")
    
    args = parser.parse_args()
    
    if args.rubric:
        print_rubric()
        sys.exit(0)
    
    if args.template:
        print_template()
        sys.exit(0)
    
    if not args.found:
        print("Error: --found required for scoring. Use --rubric to see keys.")
        sys.exit(1)
    
    # Parse inputs
    found = [b.strip() for b in args.found.split(",")] if args.found else []
    fixed = [b.strip() for b in args.fixed.split(",")] if args.fixed else []
    bonuses = [b.strip() for b in args.bonuses.split(",")] if args.bonuses else []
    
    # Calculate score
    score = calculate_score(
        found, 
        fixed, 
        bonuses, 
        args.ambiguity, 
        args.false_positive_deduction
    )
    
    # Print results
    print("\nTASK 5 SCORING RESULTS")
    print("="*60)
    print(f"Base (found bugs):   {score['base_found']} / 700")
    print(f"Bonuses:             +{score['bonuses']}")
    print(f"Ambiguity credit:    +{score['ambiguity_credit']}")
    print(f"False positives:     -{score['false_positive_deduction']}")
    print("="*60)
    print(f"TOTAL:               {score['total']} / 700")
    print(f"PERCENTAGE:          {score['percent']}%")
    print("="*60)
    
    # Detailed breakdown
    print("\nBug Breakdown:")
    for bug, points in sorted(BUG_POINTS.items()):
        found_status = "✓" if bug in found else "✗"
        fixed_status = "✓" if bug in fixed else " "
        print(f"  {found_status}{fixed_status} {bug:30} {points:3} pts")
