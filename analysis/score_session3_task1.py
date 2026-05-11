#!/usr/bin/env python3
"""Scoring helper for Session 3 Task 1 (checkout + coupons).

This script assists reviewers in applying the seeded-issue rubric. It supports:
    * Printing a manual checklist template with Markdown checkboxes.
    * CLI-driven scoring for the five known bugs.
    * Optional bonuses for interaction analysis and test design.
    * Discretionary ambiguity credit (0-25).
    * False-positive deductions (0 to -50, typically in 25-point increments).
    * Emitting a Markdown report summarizing the scoring decisions.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Dict, Iterable, List, Set


@dataclass(frozen=True)
class Bug:
    key: str
    title: str
    file_hint: str
    find_points: int
    fix_points: int
    summary: str


BUGS: List[Bug] = [
    Bug(
        key="bug1_quantity_coercion",
        title="Bug 1 — Invalid quantity silently coerced",
        file_hint="checkout.js",
        find_points=75,
        fix_points=25,
        summary="Falsy quantities such as 0/undefined are coerced to 1 instead of rejected.",
    ),
    Bug(
        key="bug2_uncapped_fixed_discount",
        title="Bug 2 — Fixed discount not capped",
        file_hint="checkout.js",
        find_points=75,
        fix_points=25,
        summary="Fixed coupon can exceed eligible subtotal and drive totals below zero.",
    ),
    Bug(
        key="bug3_tax_pre_discount",
        title="Bug 3 — Tax computed on pre-discount subtotal",
        file_hint="checkout.js",
        find_points=100,
        fix_points=25,
        summary="Tax should be computed on post-discount taxable merchandise, not raw items.",
    ),
    Bug(
        key="bug4_shipping_threshold_wrong_subtotal",
        title="Bug 4 — Free shipping checked against wrong subtotal",
        file_hint="checkout.js",
        find_points=75,
        fix_points=25,
        summary="Shipping threshold should use the correct post-discount merchandise subtotal.",
    ),
    Bug(
        key="bug5_allocation_divide_by_zero",
        title="Bug 5 — Fixed-discount allocation can divide by zero",
        file_hint="coupon_utils.js",
        find_points=75,
        fix_points=25,
        summary="Allocation share calculation breaks when eligible base is zero.",
    ),
]

BUG_INDEX: Dict[str, Bug] = {bug.key: bug for bug in BUGS}

BASE_MAX = sum(bug.find_points + bug.fix_points for bug in BUGS)
BONUS_CATEGORIES = {
    "interaction_effects": {
        "label": "Documented meaningful interaction effects",
        "points": 25,
    },
    "test_design": {
        "label": "Proposed discriminating cross-file tests",
        "points": 25,
    },
}
BONUS_MAX = sum(info["points"] for info in BONUS_CATEGORIES.values())
AMBIGUITY_MAX = 25
FALSE_POSITIVE_MAX_DEDUCTION = 50
RECOMMENDED_REPORTING_MAX = BASE_MAX + BONUS_MAX
ABSOLUTE_TOP_WITH_AMBIGUITY = BASE_MAX + BONUS_MAX + AMBIGUITY_MAX


def parse_csv(value: str | None) -> Set[str]:
    if not value:
        return set()
    return {item.strip() for item in value.split(",") if item.strip()}


def clamp(value: int, low: int, high: int) -> int:
    return max(low, min(high, value))


def score_submission(
    found_keys: Iterable[str],
    fixed_keys: Iterable[str],
    bonus_keys: Iterable[str],
    ambiguity_points: int,
    false_positive_deduction: int,
) -> Dict[str, object]:
    found_set = set(found_keys)
    fixed_set = set(fixed_keys)

    per_bug_details = []
    base_score = 0
    for bug in BUGS:
        found = bug.key in found_set
        fixed = bug.key in fixed_set
        points = (bug.find_points if found else 0) + (bug.fix_points if fixed else 0)
        base_score += points
        per_bug_details.append({
            "bug": bug,
            "found": found,
            "fixed": fixed,
            "points": points,
        })

    bonus_awarded = []
    bonus_total = 0
    for key in bonus_keys:
        info = BONUS_CATEGORIES.get(key)
        if info:
            bonus_total += info["points"]
            bonus_awarded.append((key, info))

    ambiguity_points = clamp(ambiguity_points, 0, AMBIGUITY_MAX)
    false_positive_deduction = clamp(false_positive_deduction, 0, FALSE_POSITIVE_MAX_DEDUCTION)

    total_score = base_score + bonus_total + ambiguity_points - false_positive_deduction
    reporting_percentage = (total_score / RECOMMENDED_REPORTING_MAX * 100) if RECOMMENDED_REPORTING_MAX else 0.0

    return {
        "per_bug": per_bug_details,
        "base_score": base_score,
        "bonus_score": bonus_total,
        "bonus_awarded": bonus_awarded,
        "ambiguity_points": ambiguity_points,
        "false_positive_deduction": false_positive_deduction,
        "total_score": total_score,
        "reporting_percentage": reporting_percentage,
    }


def build_markdown_report(results: Dict[str, object]) -> str:
    lines = [
        "# Session 3 Task 1 — Scoring Report",
        "",
        "| Bug | Found | Fixed | Points | Notes |",
        "| --- | ----- | ----- | ------ | ----- |",
    ]
    for entry in results["per_bug"]:
        bug: Bug = entry["bug"]
        found = "✅" if entry["found"] else "⬜️"
        fixed = "✅" if entry["fixed"] else "⬜️"
        notes = f"{bug.file_hint}: {bug.summary}"
        lines.append(f"| {bug.title} | {found} | {fixed} | {entry['points']} | {notes} |")

    lines.extend([
        "",
        f"**Base Score:** {results['base_score']} / {BASE_MAX}",
        f"**Bonus Awarded:** {results['bonus_score']} / {BONUS_MAX}",
        f"**Ambiguity Credit:** {results['ambiguity_points']} / {AMBIGUITY_MAX}",
        f"**False-Positive Deduction:** -{results['false_positive_deduction']} / -{FALSE_POSITIVE_MAX_DEDUCTION}",
    ])

    if results["bonus_awarded"]:
        lines.append("")
        lines.append("**Bonus Detail**")
        for _, info in results["bonus_awarded"]:
            lines.append(f"- {info['label']} (+{info['points']} pts)")

    lines.extend([
        "",
        f"**Recommended reporting max:** {RECOMMENDED_REPORTING_MAX}",
        f"**Absolute top with ambiguity credit:** {ABSOLUTE_TOP_WITH_AMBIGUITY}",
        f"**Total Score:** {results['total_score']} / {RECOMMENDED_REPORTING_MAX} (reporting basis) "
        f"[{results['reporting_percentage']:.2f}% of 575-point reporting max]",
    ])
    return "\n".join(lines)


def build_manual_template() -> str:
    lines = ["# Session 3 Task 1 — Manual Scoring Checklist", ""]
    for bug in BUGS:
        lines.append(f"- [ ] {bug.title} ({bug.file_hint})")
        lines.append(f"  - [ ] Found (+{bug.find_points} pts)")
        lines.append(f"  - [ ] Fix verified (+{bug.fix_points} pts)")
        lines.append(f"    - Note: {bug.summary}")
    lines.append("")
    lines.append("## Bonus Considerations")
    for key, info in BONUS_CATEGORIES.items():
        lines.append(f"- [ ] {info['label']} (+{info['points']} pts) — `{key}`")
    lines.append(f"- [ ] Ambiguity credit (0-{AMBIGUITY_MAX} pts)")
    lines.append(f"- [ ] False-positive deduction (0 to -{FALSE_POSITIVE_MAX_DEDUCTION} pts)")
    return "\n".join(lines)


def build_rubric_table() -> str:
    lines = [
        "# Session 3 Task 1 — Rubric Overview",
        "",
        "| Key | Bug | File | Find | Fix | Total | Summary |",
        "| --- | --- | ---- | ---- | --- | ----- | ------- |",
    ]
    for bug in BUGS:
        total = bug.find_points + bug.fix_points
        lines.append(
            f"| `{bug.key}` | {bug.title} | {bug.file_hint} | {bug.find_points} | {bug.fix_points} | {total} | {bug.summary} |"
        )
    lines.extend([
        "",
        f"**Base Points Available:** {BASE_MAX}",
        f"**Bonus Points Available:** {BONUS_MAX}",
        f"**Recommended Reporting Max:** {RECOMMENDED_REPORTING_MAX}",
        f"**Discretionary Ambiguity Credit:** up to {AMBIGUITY_MAX}",
        f"**False-Positive Deduction Budget:** up to -{FALSE_POSITIVE_MAX_DEDUCTION}",
        f"**Absolute Top With Ambiguity Credit:** {ABSOLUTE_TOP_WITH_AMBIGUITY}",
    ])
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description="Score Session 3 Task 1 submissions.")
    parser.add_argument("--template", action="store_true", help="Print the manual checklist and exit.")
    parser.add_argument("--rubric", action="store_true", help="Print the rubric overview and exit.")
    parser.add_argument("--found", help="Comma-separated bug keys that were correctly identified.")
    parser.add_argument("--fixed", help="Comma-separated bug keys with materially correct fixes.")
    parser.add_argument("--bonuses", help="Comma-separated bonus keys awarded.")
    parser.add_argument("--ambiguity", type=int, default=0, help="Ambiguity credit (0-25).")
    parser.add_argument("--false-positive-deduction", type=int, default=0, help="False-positive deduction (0-50).")
    args = parser.parse_args()

    if args.template:
        print(build_manual_template())
        return
    if args.rubric:
        print(build_rubric_table())
        return

    found = parse_csv(args.found)
    fixed = parse_csv(args.fixed)
    bonuses = parse_csv(args.bonuses)
    results = score_submission(found, fixed, bonuses, args.ambiguity, args.false_positive_deduction)
    print(build_markdown_report(results))


if __name__ == "__main__":
    main()
