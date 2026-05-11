#!/usr/bin/env python3
"""
Scoring helper for Session 3 Task 4 (Order Processing System).
Total: 800 points (10 bugs across 3 tiers, 2 bonuses)

Bug points:
- EASY (100 points total): 2 bugs × 50 points each
- MEDIUM (300 points total): 5 bugs × 60 points each  
- HARD (400 points total): 3 bugs × 133.33 points each (rounded for rubric)

Bonuses:
- Cross-file interaction analysis: +25 points
- Test design with edge cases: +25 points
- Ambiguity credit: +0 to +25 points (discretionary)

Penalties:
- False positives: -50 points per incorrect bug claim
"""

import sys

BUG_POINTS = {
    # Easy bugs (50 points each)
    "bug1_quantity_non_positive": 50,
    "bug2_fixed_discount_multiple_refunds": 50,
    
    # Medium bugs (60 points each) 
    "bug3_price_override_missing_validation": 60,
    "bug4_tax_before_discount": 60,
    "bug5_shipping_threshold_off_by_one": 60,
    "bug6_allocation_priority_bypass": 60,
    "bug7_coupon_expiry_timezone": 60,
    
    # Hard bugs (133.33 → 133 for rubric)
    "bug8_inventory_race_condition": 133,
    "bug9_recursive_discount_stacking": 133,
    "bug10_cross_file_state_drift": 133,
}

BONUSES = {
    "cross_file_interaction": 25,
    "test_design_edge_cases": 25,
}

def calculate_score(found_bugs, fixed_bugs, bonuses, ambiguity_credit=0, false_positive_deduction=0):
    """
    Calculate score for Task 4 submission.
    
    Args:
        found_bugs: list of bug keys found
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
        "max_possible": 800,
        "percent": round(adjusted_score / 800 * 100, 2),
    }

def print_rubric():
    """Print scoring rubric for Task 4."""
    print("\n" + "="*60)
    print("TASK 4 SCORING RUBRIC (Order Processing System)")
    print("="*60)
    
    print("\n--- BUGS (10 total, 800 points) ---")
    
    print("\nEASY BUGS (2 bugs, 50 points each):")
    print("  1. bug1_quantity_non_positive (50 pts)")
    print("  2. bug2_fixed_discount_multiple_refunds (50 pts)")
    
    print("\nMEDIUM BUGS (5 bugs, 60 points each):")
    print("  3. bug3_price_override_missing_validation (60 pts)")
    print("  4. bug4_tax_before_discount (60 pts)")
    print("  5. bug5_shipping_threshold_off_by_one (60 pts)")
    print("  6. bug6_allocation_priority_bypass (60 pts)")
    print("  7. bug7_coupon_expiry_timezone (60 pts)")
    
    print("\nHARD BUGS (3 bugs, 133 points each):")
    print("  8. bug8_inventory_race_condition (133 pts)")
    print("  9. bug9_recursive_discount_stacking (133 pts)")
    print(" 10. bug10_cross_file_state_drift (133 pts)")
    
    print("\n--- BONUSES (up to +50 points) ---")
    for bonus, points in BONUSES.items():
        print(f"  {bonus}: +{points} pts")
    
    print("\n--- PENALTIES ---")
    print("  False positive: -50 pts per incorrect bug claim")
    
    print("\n--- DISCRETIONARY ---")
    print("  Ambiguity credit: +0 to +25 pts")
    
    print("\n" + "="*60)
    print(f"MAX SCORE: 800 + 50 + 25 = 875 possible")
    print("="*60)

def print_template():
    """Print manual scoring template."""
    print("\n" + "="*60)
    print("MANUAL SCORING TEMPLATE FOR TASK 4")
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
    
    parser = argparse.ArgumentParser(description="Score Session 3 Task 4 submissions")
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
    print("\nTASK 4 SCORING RESULTS")
    print("="*60)
    print(f"Base (found bugs):   {score['base_found']} / 800")
    print(f"Bonuses:             +{score['bonuses']}")
    print(f"Ambiguity credit:    +{score['ambiguity_credit']}")
    print(f"False positives:     -{score['false_positive_deduction']}")
    print("="*60)
    print(f"TOTAL:               {score['total']} / 800")
    print(f"PERCENTAGE:          {score['percent']}%")
    print("="*60)
    
    # Detailed breakdown
    print("\nBug Breakdown:")
    for bug, points in sorted(BUG_POINTS.items()):
        found_status = "✓" if bug in found else "✗"
        fixed_status = "✓" if bug in fixed else " "
        print(f"  {found_status}{fixed_status} {bug:30} {points:3} pts")
