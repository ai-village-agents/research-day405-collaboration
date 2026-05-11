#!/usr/bin/env python3
"""Scoring helper for Session 2 Task 2 (analyzeUserActivity).

This script assists reviewers in applying the seeded-issue rubric. It supports:
    * Printing a manual checklist template with Markdown checkboxes.
    * Interactive or CLI-driven scoring for the five known bugs.
    * Optional bonus awards (up to 50 points total).
    * Emitting a Markdown report summarizing the scoring decisions.
"""

from __future__ import annotations

import argparse
from dataclasses import dataclass
from typing import Dict, Iterable, List, Set


@dataclass(frozen=True)
class Bug:
    """Simple container for bug metadata and scoring values."""

    key: str
    title: str
    line_hint: int
    find_points: int
    fix_points: int
    summary: str


BUGS: List[Bug] = [
    Bug(
        key="bug1_assignment_vs_comparison",
        title="Bug 1 — Assignment vs Comparison",
        line_hint=17,
        find_points=100,
        fix_points=25,
        summary="Uses '=' instead of '===' when checking records length.",
    ),
    Bug(
        key="bug2_off_by_one_loop",
        title="Bug 2 — Off-by-One Loop Bounds",
        line_hint=24,
        find_points=100,
        fix_points=25,
        summary="Iterates with '<=' causing undefined access at records.length.",
    ),
    Bug(
        key="bug3_nan_increment_pattern",
        title="Bug 3 — NaN Increment Pattern",
        line_hint=31,
        find_points=50,
        fix_points=25,
        summary="Relies on NaN fallback; should default to zero before increment.",
    ),
    Bug(
        key="bug4_boolean_sort_comparator",
        title="Bug 4 — Boolean Sort Comparator",
        line_hint=43,
        find_points=75,
        fix_points=25,
        summary="Comparator returns boolean; needs numeric difference for stable sort.",
    ),
    Bug(
        key="bug5_arbitrary_filter_cap",
        title="Bug 5 — Arbitrary Filter Cap",
        line_hint=47,
        find_points=50,
        fix_points=25,
        summary="Upper bound excludes power users; remove '< 100' constraint.",
    ),
]

BUG_INDEX: Dict[str, Bug] = {bug.key: bug for bug in BUGS}

BASE_MAX = sum(bug.find_points + bug.fix_points for bug in BUGS)

BONUS_CATEGORIES = {
    "interaction_effects": {
        "label": "Identified interaction effects between bugs",
        "points": 25,
    },
    "comprehensive_tests": {
        "label": "Suggested comprehensive regression tests",
        "points": 25,
    },
}

BONUS_MAX = sum(info["points"] for info in BONUS_CATEGORIES.values())
TOTAL_MAX = BASE_MAX + BONUS_MAX


def parse_csv(value: str | None) -> Set[str]:
    """Parse a comma-separated list into a set of trimmed strings."""
    if not value:
        return set()
    return {item.strip() for item in value.split(",") if item.strip()}


def prompt_boolean(prompt: str) -> bool:
    """Prompt the user for a yes/no answer until they respond."""
    while True:
        answer = input(f"{prompt} [y/N]: ").strip().lower()
        if answer in {"y", "yes"}:
            return True
        if answer in {"n", "no", ""}:
            return False
        print("Please respond with 'y' or 'n'.")


def prompt_bonus_selection() -> Set[str]:
    """Interactively collect which bonus categories apply."""
    awarded: Set[str] = set()
    for key, info in BONUS_CATEGORIES.items():
        if prompt_boolean(f"Award bonus for {info['label']} ({info['points']} pts)?"):
            awarded.add(key)
    return awarded


def score_submission(found_keys: Iterable[str], fixed_keys: Iterable[str], bonus_keys: Iterable[str]) -> Dict[str, object]:
    """Compute point totals for the provided rubric selections."""
    found_set = set(found_keys)
    fixed_set = set(fixed_keys)

    per_bug_details = []
    base_score = 0

    for bug in BUGS:
        found = bug.key in found_set
        fixed = bug.key in fixed_set
        points = 0
        if found:
            points += bug.find_points
        if fixed:
            points += bug.fix_points
        base_score += points
        per_bug_details.append(
            {
                "bug": bug,
                "found": found,
                "fixed": fixed,
                "points": points,
            }
        )

    bonus_awarded = []
    bonus_total = 0
    for key in bonus_keys:
        info = BONUS_CATEGORIES.get(key)
        if info:
            bonus_total += info["points"]
            bonus_awarded.append((key, info))

    total_score = base_score + bonus_total
    percentage = (total_score / TOTAL_MAX * 100) if TOTAL_MAX else 0.0

    return {
        "per_bug": per_bug_details,
        "base_score": base_score,
        "bonus_score": bonus_total,
        "bonus_awarded": bonus_awarded,
        "total_score": total_score,
        "percentage": percentage,
    }


def build_markdown_report(results: Dict[str, object]) -> str:
    """Create a markdown summary of the scoring decisions."""
    lines = [
        "# Session 2 Task 2 — Scoring Report",
        "",
        "| Bug | Found | Fixed | Points | Notes |",
        "| --- | ----- | ----- | ------ | ----- |",
    ]

    for entry in results["per_bug"]:
        bug: Bug = entry["bug"]
        found = "✅" if entry["found"] else "⬜️"
        fixed = "✅" if entry["fixed"] else "⬜️"
        notes = f"Line {bug.line_hint}: {bug.summary}"
        lines.append(
            f"| {bug.title} | {found} | {fixed} | {entry['points']} | {notes} |"
        )

    lines.extend(
        [
            "",
            f"**Base Score:** {results['base_score']} / {BASE_MAX}",
            f"**Bonus Awarded:** {results['bonus_score']} / {BONUS_MAX}",
        ]
    )

    if results["bonus_awarded"]:
        lines.append("")
        lines.append("**Bonus Detail**")
        for key, info in results["bonus_awarded"]:
            lines.append(f"- {info['label']} (+{info['points']} pts)")

    lines.extend(
        [
            "",
            f"**Total Score:** {results['total_score']} / {TOTAL_MAX} "
            f"({results['percentage']:.2f}%)",
        ]
    )

    return "\n".join(lines)


def build_manual_template() -> str:
    """Return a Markdown checklist for manual scoring capture."""
    lines = ["# Session 2 Task 2 — Manual Scoring Checklist", ""]

    for bug in BUGS:
        lines.append(f"- [ ] {bug.title} (Line {bug.line_hint})")
        lines.append(f"  - [ ] Found (+{bug.find_points} pts)")
        lines.append(f"  - [ ] Fix verified (+{bug.fix_points} pts)")
        lines.append(f"    - Note: {bug.summary}")

    lines.append("")
    lines.append("## Bonus Considerations (max 50 pts)")
    for key, info in BONUS_CATEGORIES.items():
        lines.append(f"- [ ] {info['label']} (+{info['points']} pts) — `{key}`")

    return "\n".join(lines)


def build_rubric_table() -> str:
    """Return a Markdown table summarizing the full rubric."""
    lines = [
        "# Session 2 Task 2 — Rubric Overview",
        "",
        "| Key | Bug | Find | Fix | Total | Summary |",
        "| --- | --- | ---- | --- | ----- | ------- |",
    ]
    for bug in BUGS:
        total = bug.find_points + bug.fix_points
        lines.append(
            f"| `{bug.key}` | {bug.title} | {bug.find_points} | {bug.fix_points} | {total} | {bug.summary} |"
        )

    lines.extend(
        [
            "",
            f"**Base Points Available:** {BASE_MAX}",
            f"**Bonus Points Available:** {BONUS_MAX}",
            f"**Maximum Score:** {TOTAL_MAX}",
        ]
    )

    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Score Session 2 Task 2 submissions (analyzeUserActivity)."
    )
    parser.add_argument(
        "--template",
        action="store_true",
        help="Print the manual Markdown checklist and exit.",
    )
    parser.add_argument(
        "--rubric",
        action="store_true",
        help="Print the full rubric overview and exit.",
    )
    parser.add_argument(
        "--found",
        help="Comma-separated bug keys that were identified.",
    )
    parser.add_argument(
        "--fixed",
        help="Comma-separated bug keys that were correctly fixed.",
    )
    parser.add_argument(
        "--bonus",
        help=(
            "Comma-separated bonus keys awarded "
            f"(valid: {', '.join(BONUS_CATEGORIES)})"
        ),
    )
    parser.add_argument(
        "--non-interactive",
        action="store_true",
        help="Skip interactive prompts (requires --found/--fixed/--bonus inputs).",
    )

    args = parser.parse_args()

    if args.template:
        print(build_manual_template())
        return

    if args.rubric:
        print(build_rubric_table())
        return

    found = parse_csv(args.found)
    fixed = parse_csv(args.fixed)
    bonus = parse_csv(args.bonus)

    if not args.non_interactive:
        # Interactive mode asks for each bug unless already supplied via CLI.
        for bug in BUGS:
            if bug.key not in found:
                if prompt_boolean(f"Did the submission spot {bug.title}?"):
                    found.add(bug.key)
            if bug.key not in fixed:
                if prompt_boolean(f"Were fixes verified for {bug.title}?"):
                    fixed.add(bug.key)

        # Only prompt for bonus categories when not fully specified by CLI.
        claimed_bonus = set(bonus)
        remaining_bonus = set(BONUS_CATEGORIES) - claimed_bonus
        if remaining_bonus:
            awarded = prompt_bonus_selection()
            bonus |= awarded
    else:
        missing_inputs = []
        if len(found) == 0:
            missing_inputs.append("--found")
        if len(fixed) == 0:
            missing_inputs.append("--fixed")
        if missing_inputs:
            joined = ", ".join(missing_inputs)
            raise SystemExit(
                f"Non-interactive mode requires explicit values for: {joined}"
            )

    results = score_submission(found, fixed, bonus)
    report = build_markdown_report(results)
    print(report)


if __name__ == "__main__":
    main()
