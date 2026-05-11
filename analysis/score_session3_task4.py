#!/usr/bin/env python3
"""
Scoring helper for Session 4 Task 4 (Order Processing System).

Canonical scoring frame:
- Base bugs: 725 points total
- Bonuses: up to 100 points total
- Raw maximum: 825 points
- Reported score: capped at 800 points
- False positives: -25 points each

This script is for scorer use only. It mirrors the canonical rubric in:
- tasks/session3_task_4/answer_key.md
- experiments/session4/scoring/scoring_template_task4.md
"""

import sys

BUG_POINTS = {
    "bug1_off_by_one_inventory_loop": 50,
    "bug2_missing_await_reserve_items": 50,
    "bug3_loose_equality_cancel_filter": 50,
    "bug4_inventory_race_condition": 100,
    "bug5_discount_stacking_order": 75,
    "bug6_floating_point_arithmetic": 75,
    "bug7_tax_on_pre_discount_amount": 75,
    "bug8_internal_state_reference_leak": 100,
    "bug9_some_vs_every_validation": 75,
    "bug10_json_stringify_undefined_loss": 75,
}

BONUSES = {
    "cross_file_interaction": 50,
    "test_cases": 50,
}

BASE_MAX = sum(BUG_POINTS.values())
BONUS_MAX = sum(BONUSES.values())
RAW_MAX = BASE_MAX + BONUS_MAX
REPORTED_MAX = 800
FALSE_POSITIVE_PENALTY = 25


def calculate_score(found_bugs, bonuses, false_positives=0):
    """Calculate raw and reported scores for a Task 4 submission."""
    unique_found = []
    for bug in found_bugs:
        if bug and bug not in unique_found:
            unique_found.append(bug)

    unique_bonuses = []
    for bonus in bonuses:
        if bonus and bonus not in unique_bonuses:
            unique_bonuses.append(bonus)

    base_score = sum(BUG_POINTS.get(bug, 0) for bug in unique_found)
    bonus_score = sum(BONUSES.get(bonus, 0) for bonus in unique_bonuses)
    penalty = false_positives * FALSE_POSITIVE_PENALTY
    raw_total = base_score + bonus_score - penalty
    reported_total = max(0, min(raw_total, REPORTED_MAX))

    return {
        "found_bugs": unique_found,
        "bonuses_awarded": unique_bonuses,
        "base_score": base_score,
        "bonus_score": bonus_score,
        "false_positives": false_positives,
        "penalty": penalty,
        "raw_total": raw_total,
        "reported_total": reported_total,
        "base_max": BASE_MAX,
        "bonus_max": BONUS_MAX,
        "raw_max": RAW_MAX,
        "reported_max": REPORTED_MAX,
        "raw_percent": round((raw_total / RAW_MAX) * 100, 2) if RAW_MAX else 0.0,
        "reported_percent": round((reported_total / REPORTED_MAX) * 100, 2) if REPORTED_MAX else 0.0,
    }


def print_rubric():
    """Print a non-spoiler scoring overview."""
    print("\n" + "=" * 72)
    print("SESSION 4 TASK 4 SCORING OVERVIEW (NON-SPOILER)")
    print("=" * 72)
    print(f"Base bugs total: {BASE_MAX} pts")
    print(f"Bonuses total:   {BONUS_MAX} pts")
    print(f"Raw maximum:     {RAW_MAX} pts")
    print(f"Reported cap:    {REPORTED_MAX} pts")
    print(f"False positives: -{FALSE_POSITIVE_PENALTY} pts each")
    print("\nWarning: Full rubric includes seeded bug identifiers and should not be printed in public logs.")
    print("Scorers can open experiments/session4/scoring/scoring_template_task4.md")
    print("or run this script with --full-rubric to view the detailed bug and bonus keys.")
    print("=" * 72)


def print_full_rubric():
    """Print the canonical Task 4 rubric."""
    print("\n" + "=" * 72)
    print("SESSION 4 TASK 4 SCORING RUBRIC (ORDER PROCESSING SYSTEM)")
    print("=" * 72)
    print(f"Base bugs: {BASE_MAX} | Bonuses: {BONUS_MAX} | Raw max: {RAW_MAX} | Reported cap: {REPORTED_MAX}")
    print(f"False positives: -{FALSE_POSITIVE_PENALTY} each")

    print("\n--- BUGS ---")
    for idx, (bug, points) in enumerate(BUG_POINTS.items(), start=1):
        print(f" {idx:>2}. {bug:36} {points:>3} pts")

    print("\n--- BONUSES ---")
    for bonus, points in BONUSES.items():
        print(f" - {bonus:24} +{points} pts")

    print("\nScoring note: report final score as min(raw_total, 800).")
    print("=" * 72)


def print_template():
    """Print a manual scoring template."""
    print("\n" + "=" * 72)
    print("TASK 4 MANUAL SCORING TEMPLATE")
    print("=" * 72)
    print("\nFound bugs:")
    for bug, points in BUG_POINTS.items():
        print(f"  [ ] {bug} ({points} pts)")

    print("\nBonuses:")
    for bonus, points in BONUSES.items():
        print(f"  [ ] {bonus} (+{points} pts)")

    print(f"\nFalse positives: _____ × {FALSE_POSITIVE_PENALTY} = _____ pts deduction")
    print(f"Raw total max: {RAW_MAX} | Reported cap: {REPORTED_MAX}")
    print("=" * 72)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Score Session 4 Task 4 submissions")
    parser.add_argument("--rubric", action="store_true", help="Print non-spoiler scoring overview")
    parser.add_argument("--full-rubric", action="store_true", help="Print full scoring rubric with bug keys")
    parser.add_argument("--template", action="store_true", help="Print manual scoring template")
    parser.add_argument("--found", help="Comma-separated list of found canonical bug keys")
    parser.add_argument("--bonuses", help="Comma-separated list of earned bonus keys")
    parser.add_argument("--false-positives", type=int, default=0, help="Number of incorrect bug claims")

    args = parser.parse_args()

    if args.full_rubric:
        print_full_rubric()
        sys.exit(0)

    if args.rubric:
        print_rubric()
        sys.exit(0)

    if args.template:
        print_template()
        sys.exit(0)

    if not args.found:
        print(
            "Error: --found required for scoring. "
            "See experiments/session4/scoring/scoring_template_task4.md or use --full-rubric for bug keys."
        )
        sys.exit(1)

    found = [b.strip() for b in args.found.split(",")] if args.found else []
    bonuses = [b.strip() for b in args.bonuses.split(",")] if args.bonuses else []

    score = calculate_score(found, bonuses, args.false_positives)

    print("\nSESSION 4 TASK 4 SCORING RESULTS")
    print("=" * 72)
    print(f"Base score:         {score['base_score']} / {score['base_max']}")
    print(f"Bonuses:            +{score['bonus_score']} / {score['bonus_max']}")
    print(f"False positives:    -{score['penalty']} ({score['false_positives']} × {FALSE_POSITIVE_PENALTY})")
    print("-" * 72)
    print(f"RAW TOTAL:          {score['raw_total']} / {score['raw_max']} ({score['raw_percent']}%)")
    print(f"REPORTED TOTAL:     {score['reported_total']} / {score['reported_max']} ({score['reported_percent']}%)")
    print("=" * 72)

    print("\nFound bug breakdown:")
    for bug, points in BUG_POINTS.items():
        status = "✓" if bug in score['found_bugs'] else "✗"
        print(f"  {status} {bug:36} {points:>3} pts")

    print("\nBonus breakdown:")
    for bonus, points in BONUSES.items():
        status = "✓" if bonus in score['bonuses_awarded'] else "✗"
        print(f"  {status} {bonus:24} +{points} pts")
