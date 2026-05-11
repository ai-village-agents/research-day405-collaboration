#!/usr/bin/env python3
"""
Validate historical coordination dataset for consistency and completeness.
"""

import json
from pathlib import Path

def validate_all_eras():
    """Validate data/historical/all_eras.json for consistency."""
    
    with open('data/historical/all_eras.json', 'r') as f:
        data = json.load(f)
    
    # Handle the structure with "eras" key
    if 'eras' in data:
        cases = data['eras']
    else:
        cases = data if isinstance(data, list) else []
    
    issues = []
    
    # Check required fields
    required_fields = ['day_range', 'coordination_mode']
    for i, case in enumerate(cases):
        if not isinstance(case, dict):
            issues.append(f"Case {i} is not a dict: {type(case)}")
            continue
            
        for field in required_fields:
            if field not in case:
                issues.append(f"Case {i} ({case.get('case_id', 'unknown')}) missing required field: {field}")
    
    # Check day ranges don't overlap
    day_ranges = []
    for case in cases:
        if not isinstance(case, dict):
            continue
        if 'day_range' in case and isinstance(case['day_range'], str):
            if '–' in case['day_range'] or '-' in case['day_range']:
                parts = case['day_range'].replace('–', '-').split('-')
                if len(parts) == 2:
                    try:
                        start = int(parts[0].strip())
                        end = int(parts[1].strip())
                        day_ranges.append((start, end, case.get('project_name', 'unknown')))
                    except ValueError:
                        issues.append(f"Invalid day range format: {case['day_range']}")
    
    # Check for overlaps
    for i, (start1, end1, goal1) in enumerate(day_ranges):
        for j, (start2, end2, goal2) in enumerate(day_ranges[i+1:], i+1):
            if not (end1 < start2 or end2 < start1):
                issues.append(f"Overlapping day ranges: {goal1} ({start1}-{end1}) and {goal2} ({start2}-{end2})")
    
    return issues, cases

def check_coverage(cases):
    """Check which day ranges are covered vs gaps."""
    
    covered = set()
    for case in cases:
        if not isinstance(case, dict):
            continue
        if 'day_range' in case and isinstance(case['day_range'], str):
            if '–' in case['day_range'] or '-' in case['day_range']:
                parts = case['day_range'].replace('–', '-').split('-')
                if len(parts) == 2:
                    try:
                        start = int(parts[0].strip())
                        end = int(parts[1].strip())
                        covered.update(range(start, end+1))
                    except ValueError:
                        pass
    
    if covered:
        min_day = min(covered)
        max_day = max(covered)
        total_range = set(range(min_day, max_day+1))
        gaps = total_range - covered
        
        print(f"\nCoverage Analysis:")
        print(f"  Total cases: {len(cases)}")
        print(f"  Days covered: {len(covered)} days")
        print(f"  Range: Day {min_day} to Day {max_day}")
        print(f"  Coverage: {len(covered)/len(total_range)*100:.1f}%")
        
        if gaps:
            # Find contiguous gap ranges
            gap_ranges = []
            gaps_sorted = sorted(gaps)
            if gaps_sorted:
                start = gaps_sorted[0]
                end = gaps_sorted[0]
                for day in gaps_sorted[1:]:
                    if day == end + 1:
                        end = day
                    else:
                        gap_ranges.append((start, end))
                        start = day
                        end = day
                gap_ranges.append((start, end))
            
            print(f"\n  Gap ranges (total {len(gaps)} days uncovered):")
            for start, end in gap_ranges[:10]:  # Show first 10 gaps
                if start == end:
                    print(f"    Day {start}")
                else:
                    print(f"    Days {start}–{end} ({end-start+1} days)")
            
            if len(gap_ranges) > 10:
                print(f"    ... and {len(gap_ranges)-10} more gap ranges")

def analyze_coordination_modes(cases):
    """Analyze distribution of coordination modes."""
    
    mode_counts = {}
    for case in cases:
        if not isinstance(case, dict):
            continue
        mode = case.get('coordination_mode', 'unknown')
        mode_counts[mode] = mode_counts.get(mode, 0) + 1
    
    print(f"\n\nCoordination Mode Distribution:")
    for mode, count in sorted(mode_counts.items(), key=lambda x: x[1], reverse=True):
        print(f"  {mode}: {count} cases")

if __name__ == "__main__":
    print("Historical Data Validation")
    print("=" * 60)
    
    issues, cases = validate_all_eras()
    
    if issues:
        print("\n⚠️  Issues found:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("\n✅ No validation issues found")
    
    check_coverage(cases)
    analyze_coordination_modes(cases)
    
    print("\n" + "=" * 60)
    print("Validation complete")
