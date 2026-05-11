#!/usr/bin/env python3
"""
Scoring helper for Session 3 Task 5 (API Rate Limiter).

Scoring frame:
- BASE_MAX = 650
- BONUS_MAX = 50
- RECOMMENDED_REPORTING_MAX = 700
- AMBIGUITY_MAX = 25
- FALSE_POSITIVE_DEDUCTION = 50 per incorrect bug claim
"""

import argparse
import sys

BUG_POINTS = {
    "bug1_token_refill_drift": 50,
    "bug2_numeric_config_validation": 50,
    "bug3_bucket_overflow": 75,
    "bug4_race_condition": 100,
    "bug5_memory_leak": 75,
    "bug6_clock_monotonicity": 75,
    "bug7_missing_retry_after": 50,
    "bug8_nonpositive_cost_bypass": 75,
    "bug9_shallow_merge": 50,
    "bug10_null_override_wipes_defaults": 50,
}

BONUSES = {
    "interaction_effects": 25,
    "test_design": 25,
}

BASE_MAX = sum(BUG_POINTS.values())
BONUS_MAX = sum(BONUSES.values())
RECOMMENDED_REPORTING_MAX = BASE_MAX + BONUS_MAX
AMBIGUITY_MAX = 25
FALSE_POSITIVE_DEDUCTION = 50
ABSOLUTE_TOP_WITH_AMBIGUITY = RECOMMENDED_REPORTING_MAX + AMBIGUITY_MAX


def calculate_score(found_bugs, fixed_bugs, bonuses, ambiguity_credit=0, false_positive_deduction=0):
    found_score = sum(BUG_POINTS.get(bug, 0) for bug in found_bugs)
    fixed_score = sum(BUG_POINTS.get(bug, 0) for bug in fixed_bugs if bug in found_bugs)
    bonus_score = sum(BONUSES.get(bonus, 0) for bonus in bonuses)
    total = found_score + bonus_score + ambiguity_credit - false_positive_deduction
    return {
        "base_found": found_score,
        "base_fixed": fixed_score,
        "bonuses": bonus_score,
        "ambiguity_credit": ambiguity_credit,
        "false_positive_deduction": false_positive_deduction,
        "total": total,
        "reporting_max": RECOMMENDED_REPORTING_MAX,
        "absolute_top": ABSOLUTE_TOP_WITH_AMBIGUITY,
        "percent_of_reporting_max": round(total / RECOMMENDED_REPORTING_MAX * 100, 2),
    }


def print_rubric():
    print("\n" + "=" * 72)
    print("TASK 5 SCORING RUBRIC (API Rate Limiter)")
    print("=" * 72)
    print(f"BASE_MAX = {BASE_MAX}")
    print(f"BONUS_MAX = {BONUS_MAX}")
    print(f"RECOMMENDED_REPORTING_MAX = {RECOMMENDED_REPORTING_MAX}")
    print(f"AMBIGUITY_MAX = {AMBIGUITY_MAX}")
    print(f"FALSE_POSITIVE_DEDUCTION = {FALSE_POSITIVE_DEDUCTION} per incorrect bug claim")

    print("\n--- BUGS (10 total, 650 base points) ---")
    for idx, (bug, points) in enumerate(BUG_POINTS.items(), start=1):
        print(f" {idx:2d}. {bug} ({points} pts)")

    print("\n--- BONUSES (+50 max) ---")
    for bonus, points in BONUSES.items():
        print(f"  {bonus}: +{points} pts")

    print("\n--- DISCRETIONARY ---")
    print(f"  ambiguity credit: +0 to +{AMBIGUITY_MAX} pts")
    print("=" * 72)
    print(f"REPORTING MAX: {RECOMMENDED_REPORTING_MAX}")
    print(f"ABSOLUTE TOP WITH AMBIGUITY: {ABSOLUTE_TOP_WITH_AMBIGUITY}")
    print("=" * 72)


def print_template():
    print("\n" + "=" * 72)
    print("MANUAL SCORING TEMPLATE FOR TASK 5")
    print("=" * 72)
    print("\nBug Finding Tracking:")
    for bug, points in BUG_POINTS.items():
        print(f"  [ ] {bug} ({points} pts)   [ ] Found   [ ] Fixed")

    print("\nBonuses:")
    for bonus, points in BONUSES.items():
        print(f"  [ ] {bonus} (+{points} pts)")

    print("\nPenalties:")
    print(f"  [ ] False positives: _____ × {FALSE_POSITIVE_DEDUCTION} = _____ pts deduction")

    print("\nDiscretionary:")
    print(f"  [ ] Ambiguity credit: _____ pts (0-{AMBIGUITY_MAX})")
    print("=" * 72)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Score Session 3 Task 5 submissions")
    parser.add_argument("--rubric", action="store_true", help="Print scoring rubric")
    parser.add_argument("--template", action="store_true", help="Print manual scoring template")
    parser.add_argument("--found", help="Comma-separated list of found bug keys")
    parser.add_argument("--fixed", help="Comma-separated list of fixed bug keys")
    parser.add_argument("--bonuses", help="Comma-separated list of bonus keys")
    parser.add_argument("--ambiguity", type=int, default=0, help="Ambiguity credit (0-25)")
    parser.add_argument(
        "--false-positive-deduction",
        type=int,
        default=0,
        help="False positive deduction in raw points (incorrect claims × 50)",
    )
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

    found = [b.strip() for b in args.found.split(",") if b.strip()]
    fixed = [b.strip() for b in args.fixed.split(",") if b.strip()] if args.fixed else []
    bonuses = [b.strip() for b in args.bonuses.split(",") if b.strip()] if args.bonuses else []

    score = calculate_score(found, fixed, bonuses, args.ambiguity, args.false_positive_deduction)

    print("\nTASK 5 SCORING RESULTS")
    print("=" * 72)
    print(f"Base (found bugs):   {score['base_found']} / {BASE_MAX}")
    print(f"Bonuses:             +{score['bonuses']} / {BONUS_MAX}")
    print(f"Ambiguity credit:    +{score['ambiguity_credit']} / {AMBIGUITY_MAX}")
    print(f"False positives:     -{score['false_positive_deduction']}")
    print("=" * 72)
    print(f"TOTAL:               {score['total']} / {RECOMMENDED_REPORTING_MAX}")
    print(f"% OF REPORTING MAX:  {score['percent_of_reporting_max']}%")
    print("=" * 72)
    print(f"Absolute top incl. ambiguity: {ABSOLUTE_TOP_WITH_AMBIGUITY}")

    print("\nBug Breakdown:")
    for bug, points in BUG_POINTS.items():
        found_status = "✓" if bug in found else "✗"
        fixed_status = "✓" if bug in fixed else " "
        print(f"  {found_status}{fixed_status} {bug:38} {points:3} pts")
