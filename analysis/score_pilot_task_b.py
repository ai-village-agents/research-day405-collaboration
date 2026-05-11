#!/usr/bin/env python3
"""Simple scorer for Task B seeded-issue evaluation."""

TASK_B_BUGS = {
    "assignment_in_filter": "Assignment in filter",
    "missing_tolowercase_invocation": "Missing toLowerCase() invocation",
    "math_round_precision_misuse": "Math.round precision misuse",
    "wrong_denominator_completion_rate": "Wrong denominator for completion_rate",
    "boolean_sort_comparator": "Boolean sort comparator",
}

POINTS_PER_IDENTIFICATION = 50
POINTS_PER_FIX = 50
BONUS_AMBIGUITY = 25
MAX_SCORE = 525


def score_submission(bugs_found, bugs_fixed, ambiguity_bonus=False):
    """Return scoring tuple for a submission.

    Args:
        bugs_found: Iterable of bug keys correctly identified.
        bugs_fixed: Iterable of bug keys with materially correct fixes.
        ambiguity_bonus: True if the meanDuration ambiguity bonus applies.

    Returns:
        (total_score, max_possible, percentage, bugs_found, bugs_fixed, details)
    """
    found_set = set(bugs_found or [])
    fixed_set = set(bugs_fixed or [])
    valid_keys = set(TASK_B_BUGS)

    found_valid = found_set & valid_keys
    fixed_valid = fixed_set & valid_keys

    found_points = len(found_valid) * POINTS_PER_IDENTIFICATION
    fixed_points = len(fixed_valid) * POINTS_PER_FIX
    bonus_points = BONUS_AMBIGUITY if ambiguity_bonus else 0

    total_score = min(found_points + fixed_points + bonus_points, MAX_SCORE)
    percentage = (total_score / MAX_SCORE) * 100 if MAX_SCORE else 0.0

    details = {
        "found_points": found_points,
        "fixed_points": fixed_points,
        "ambiguity_bonus_points": bonus_points,
        "count_found": len(found_valid),
        "count_fixed": len(fixed_valid),
        "ignored_found_keys": sorted(found_set - valid_keys),
        "ignored_fixed_keys": sorted(fixed_set - valid_keys),
    }

    return (
        total_score,
        MAX_SCORE,
        percentage,
        sorted(found_valid),
        sorted(fixed_valid),
        details,
    )


if __name__ == "__main__":
    print("Task B scorer template")
    print("Use score_submission(bugs_found, bugs_fixed, ambiguity_bonus=False).")
    print("Valid bug keys:")
    for key, label in TASK_B_BUGS.items():
        print(f"- {key}: {label}")
    print("")
    print("Blank template:")
    print("bugs_found = []")
    print("bugs_fixed = []")
    print("ambiguity_bonus = False")
