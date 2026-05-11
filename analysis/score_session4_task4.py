#!/usr/bin/env python3
"""
Session 4 Task 4 Scoring Script
Scorer: Opus 4.6 (task creator — exposed, scorer-only role)

Usage: python3 analysis/score_session4_task4.py <submission_file>
"""

import sys
import re
import os

# Bug definitions with keywords for matching
BUGS = {
    "bug1_off_by_one": {
        "name": "Off-by-one in reserveItems loop",
        "file": "inventory.js",
        "tier": "Easy",
        "points": 50,
        "keywords": ["off.by.one", "<=.*length", "i <= items.length", "boundary", "undefined.*item",
                     "items\\[items\\.length\\]", "loop.*bound", "fencepost"],
    },
    "bug2_missing_await": {
        "name": "Missing await on reserveItems",
        "file": "order.js",
        "tier": "Easy",
        "points": 50,
        "keywords": ["missing.*await", "not.*await", "promise.*not.*resolve", "reserveItems.*await",
                     "async.*not.*await", "reservation.*promise", "unawaited"],
    },
    "bug3_loose_equality": {
        "name": "Loose equality in cancelOrder",
        "file": "order.js",
        "tier": "Easy",
        "points": 50,
        "keywords": ["loose.*equal", "!=.*!==", "cancel.*order.*equal", "type.*coercion",
                     "strict.*equal", "!=.*instead.*!=="],
    },
    "bug4_race_condition": {
        "name": "Race condition in reserveItems",
        "file": "inventory.js",
        "tier": "Hard",
        "points": 100,
        "keywords": ["race.*condition", "concurrent.*reserv", "no.*lock", "lock.*not.*check",
                     "reservationLock.*never.*used", "over.?sell", "over.?reserv", "mutex",
                     "atomicity", "lock.*red.*herring"],
    },
    "bug5_discount_order": {
        "name": "Discount stacking order violates spec",
        "file": "pricing.js",
        "tier": "Medium",
        "points": 75,
        "keywords": ["discount.*order", "flat.*before.*percent", "percent.*before.*flat",
                     "stacking.*order", "sort.*discount", "spec.*flat.*first",
                     "discount.*sequence", "wrong.*discount.*order"],
    },
    "bug6_floating_point": {
        "name": "Floating-point arithmetic",
        "file": "pricing.js",
        "tier": "Medium",
        "points": 75,
        "keywords": ["float.*point", "precision", "0\\.1.*0\\.2", "rounding",
                     "\\bcents\\b", "Math\\.round", "decimal.*error", "ieee.*754"],
    },
    "bug7_tax_prediscount": {
        "name": "Tax on pre-discount amount",
        "file": "pricing.js",
        "tier": "Medium",
        "points": 75,
        "keywords": ["tax.*pre.?discount", "tax.*before.*discount", "tax.*wrong.*base",
                     "subtotal.*not.*discounted", "discountedSubtotal.*not.*used",
                     "tax.*original.*price", "overcharg.*tax"],
    },
    "bug8_state_leak": {
        "name": "Internal state leak via getInventorySummary",
        "file": "inventory.js",
        "tier": "Hard",
        "points": 100,
        "keywords": ["state.*leak", "_stockRef", "internal.*reference", "mutat.*stock",
                     "direct.*reference", "shared.*mutable", "encapsulation.*break",
                     "summary.*leak", "stock.*reference"],
    },
    "bug9_some_vs_every": {
        "name": "validateOrder uses some() instead of every()",
        "file": "order.js",
        "tier": "Hard",
        "points": 75,
        "keywords": ["some.*every", "every.*some", "some\\(\\).*instead.*every",
                     "validation.*some", "any.*instead.*all", "items\\.some.*should.*every"],
    },
    "bug10_json_undefined": {
        "name": "JSON deep copy strips undefined values",
        "file": "order.js",
        "tier": "Hard",
        "points": 75,
        "keywords": ["json.*strip.*undefined", "stringify.*undefined", "json.*parse.*stringify",
                     "undefined.*lost", "deep.*copy.*undefined", "structuredClone",
                     "json.*serializ.*undefined", "silent.*data.*loss"],
    },
}

BONUS_CROSS_FILE = {
    "name": "Cross-file interaction effects",
    "points": 50,
    "keywords": ["cross.?file", "interaction.*effect", "bug.*2.*mask.*bug.*1",
                 "await.*mask.*off.by.one", "bug.*8.*pricing", "stock.*ref.*pric",
                 "bug.*5.*bug.*7.*compound", "bug.*9.*bug.*2"],
}

BONUS_TEST_CASES = {
    "name": "Test cases provided",
    "points": 50,
    "keywords": ["test.*case", "describe\\(", "it\\(", "expect\\(", "assert",
                 "function.*test", "async.*test", "beforeEach"],
}


def score_submission(filepath):
    """Score a submission file against the answer key."""
    with open(filepath, 'r') as f:
        content = f.read().lower()

    print(f"\n{'='*70}")
    print(f"SCORING: {os.path.basename(filepath)}")
    print(f"{'='*70}\n")

    total = 0
    found_bugs = []
    missed_bugs = []

    # Score each bug
    for bug_id, bug in BUGS.items():
        matched = False
        matching_keywords = []
        for kw in bug["keywords"]:
            if re.search(kw, content, re.IGNORECASE):
                matched = True
                matching_keywords.append(kw)

        if matched:
            found_bugs.append(bug_id)
            total += bug["points"]
            status = "✅ FOUND"
        else:
            missed_bugs.append(bug_id)
            status = "❌ MISSED"

        print(f"  {status} | {bug['tier']:6s} | {bug['points']:3d}pts | {bug['name']}")
        if matched:
            print(f"           Matched: {', '.join(matching_keywords[:3])}")

    # Score bonuses
    print(f"\n--- Bonuses ---")

    cross_file_found = False
    for kw in BONUS_CROSS_FILE["keywords"]:
        if re.search(kw, content, re.IGNORECASE):
            cross_file_found = True
            break
    if cross_file_found:
        total += BONUS_CROSS_FILE["points"]
        print(f"  ✅ Cross-file interaction: +{BONUS_CROSS_FILE['points']}pts")
    else:
        print(f"  ❌ Cross-file interaction: not found")

    test_found = False
    for kw in BONUS_TEST_CASES["keywords"]:
        if re.search(kw, content, re.IGNORECASE):
            test_found = True
            break
    if test_found:
        total += BONUS_TEST_CASES["points"]
        print(f"  ✅ Test cases: +{BONUS_TEST_CASES['points']}pts")
    else:
        print(f"  ❌ Test cases: not found")

    # Count potential false positives (rough heuristic)
    # This is just a flag — manual review needed
    fp_indicators = re.findall(r'bug\s*#?\s*\d+|issue\s*#?\s*\d+|problem\s*#?\s*\d+', content)

    # Summary
    capped_total = min(total, 800)
    print(f"\n{'='*70}")
    print(f"SCORE SUMMARY")
    print(f"{'='*70}")
    print(f"  Bugs found:  {len(found_bugs)}/{len(BUGS)}")
    print(f"  Raw total:   {total}")
    print(f"  Capped (800): {capped_total}")
    print(f"  Found:  {', '.join(found_bugs)}")
    print(f"  Missed: {', '.join(missed_bugs)}")
    print(f"\n⚠️  This is an AUTOMATED preliminary score.")
    print(f"    Manual review required for:")
    print(f"    - Partial credit decisions")
    print(f"    - False positive deductions (-25 each)")
    print(f"    - Ambiguous bug descriptions")
    print(f"{'='*70}\n")

    return {
        "file": filepath,
        "found": found_bugs,
        "missed": missed_bugs,
        "total": total,
        "capped": capped_total,
        "cross_file": cross_file_found,
        "test_cases": test_found,
    }


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 analysis/score_session4_task4.py <submission_file> [submission_file2 ...]")
        print("\nTo score all Session 4 submissions:")
        print("  python3 analysis/score_session4_task4.py experiments/session4/runs/*_task4.md")
        sys.exit(1)

    results = []
    for filepath in sys.argv[1:]:
        if os.path.exists(filepath):
            results.append(score_submission(filepath))
        else:
            print(f"File not found: {filepath}")

    # Comparison table if multiple submissions
    if len(results) > 1:
        print(f"\n{'='*70}")
        print(f"COMPARISON TABLE")
        print(f"{'='*70}")
        print(f"{'Condition':<40s} {'Bugs':>5s} {'Score':>6s} {'Capped':>7s}")
        print(f"{'-'*40} {'-'*5} {'-'*6} {'-'*7}")
        for r in results:
            name = os.path.basename(r['file']).replace('_task4.md', '')
            print(f"{name:<40s} {len(r['found']):>3d}/10 {r['total']:>5d} {r['capped']:>6d}/800")
