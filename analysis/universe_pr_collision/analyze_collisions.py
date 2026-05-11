#!/usr/bin/env python3
"""Analyze index-range collisions in PR titles.

Input: JSONL from fetch_universe_prs.py (one PR per line).
Output:
  - CSV of per-PR features
  - Markdown summary with key stats

Collision definition (default): two PRs collide if their title ranges overlap AND they were open concurrently.
"""

import argparse
import csv
import dataclasses
import datetime as dt
import json
import math
import re
from typing import Dict, Iterable, List, Optional, Tuple

RANGE_RE = re.compile(r"\((\d{1,8})\s*[-–]\s*(\d{1,8})\)")


def parse_iso(ts: Optional[str]) -> Optional[dt.datetime]:
    if not ts:
        return None
    # GitHub timestamps are like 2026-05-08T20:46:52Z
    if ts.endswith("Z"):
        ts = ts[:-1] + "+00:00"
    return dt.datetime.fromisoformat(ts)


@dataclasses.dataclass
class PR:
    number: int
    title: str
    state: str
    author: str
    created_at: dt.datetime
    closed_at: Optional[dt.datetime]
    merged_at: Optional[dt.datetime]
    additions: int
    deletions: int
    changed_files: int
    url: str

    range_start: Optional[int] = None
    range_end: Optional[int] = None

    def outcome(self) -> str:
        if self.merged_at is not None:
            return "merged"
        if self.state.upper() == "OPEN":
            return "open"
        return "closed"

    def end_time(self, now: dt.datetime) -> dt.datetime:
        return self.merged_at or self.closed_at or now

    def duration_hours(self, now: dt.datetime) -> Optional[float]:
        end = self.merged_at or self.closed_at
        if end is None:
            return None
        return (end - self.created_at).total_seconds() / 3600.0


def parse_range(title: str) -> Optional[Tuple[int, int]]:
    m = RANGE_RE.search(title)
    if not m:
        return None
    a, b = int(m.group(1)), int(m.group(2))
    if a > b:
        a, b = b, a
    return a, b


def overlaps(a: Tuple[int, int], b: Tuple[int, int]) -> bool:
    return max(a[0], b[0]) <= min(a[1], b[1])


def load_prs(path: str) -> List[PR]:
    prs: List[PR] = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            obj = json.loads(line)
            author = (obj.get("author") or {}).get("login") or ""
            pr = PR(
                number=int(obj["number"]),
                title=obj.get("title", ""),
                state=obj.get("state", ""),
                author=author,
                created_at=parse_iso(obj.get("createdAt")) or dt.datetime.min.replace(tzinfo=dt.timezone.utc),
                closed_at=parse_iso(obj.get("closedAt")),
                merged_at=parse_iso(obj.get("mergedAt")),
                additions=int(obj.get("additions") or 0),
                deletions=int(obj.get("deletions") or 0),
                changed_files=int(obj.get("changedFiles") or 0),
                url=obj.get("url", ""),
            )
            rng = parse_range(pr.title)
            if rng:
                pr.range_start, pr.range_end = rng
            prs.append(pr)
    return prs


def compute_collision_features(prs: List[PR]) -> List[Dict]:
    now = dt.datetime.now(dt.timezone.utc)

    # Only PRs with parseable ranges participate in collision logic.
    ranged = [p for p in prs if p.range_start is not None and p.range_end is not None]

    # Sort by created time ascending for sweep.
    ranged.sort(key=lambda p: p.created_at)

    rows: List[Dict] = []

    # O(n^2) is fine for <= ~5000; we can optimize later if needed.
    for i, p in enumerate(ranged):
        p_range = (p.range_start, p.range_end)
        active_collisions = 0
        all_prior_overlaps = 0
        overlapping_prior_numbers: List[int] = []

        for j in range(i):
            q = ranged[j]
            q_range = (q.range_start, q.range_end)
            if not overlaps(p_range, q_range):
                continue
            all_prior_overlaps += 1
            # Concurrent-open collision: q still open when p opened.
            if q.end_time(now) > p.created_at:
                active_collisions += 1
                overlapping_prior_numbers.append(q.number)

        duration_h = p.duration_hours(now)
        rows.append(
            {
                "number": p.number,
                "url": p.url,
                "title": p.title,
                "author": p.author,
                "createdAt": p.created_at.isoformat(),
                "closedAt": p.closed_at.isoformat() if p.closed_at else "",
                "mergedAt": p.merged_at.isoformat() if p.merged_at else "",
                "outcome": p.outcome(),
                "durationHours": "" if duration_h is None else f"{duration_h:.4f}",
                "rangeStart": p.range_start,
                "rangeEnd": p.range_end,
                "rangeSize": (p.range_end - p.range_start + 1),
                "additions": p.additions,
                "deletions": p.deletions,
                "changedFiles": p.changed_files,
                "activeCollisionCount": active_collisions,
                "priorOverlapCount": all_prior_overlaps,
                "overlappingPriorPRs": ",".join(map(str, overlapping_prior_numbers)),
            }
        )

    return rows


def summarize(rows: List[Dict]) -> str:
    def is_merged(r):
        return r["outcome"] == "merged"

    def has_collision(r):
        return int(r["activeCollisionCount"]) > 0

    n = len(rows)
    if n == 0:
        return "No PRs with parseable title ranges found."

    merged = sum(1 for r in rows if is_merged(r))
    collision = sum(1 for r in rows if has_collision(r))
    merged_collision = sum(1 for r in rows if has_collision(r) and is_merged(r))
    merged_nocoll = sum(1 for r in rows if (not has_collision(r)) and is_merged(r))
    nocoll = n - collision

    def rate(num, den):
        return 0.0 if den == 0 else num / den

    return "\n".join(
        [
            f"Total ranged PRs analyzed: {n}",
            f"Merged: {merged} ({rate(merged, n):.1%})",
            f"Had >=1 active collision at creation: {collision} ({rate(collision, n):.1%})",
            f"Merge rate with collision: {merged_collision}/{collision} ({rate(merged_collision, collision):.1%})",
            f"Merge rate without collision: {merged_nocoll}/{nocoll} ({rate(merged_nocoll, nocoll):.1%})",
        ]
    )


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="inp", required=True)
    ap.add_argument("--out_csv", required=True)
    ap.add_argument("--out_md", required=True)
    args = ap.parse_args()

    prs = load_prs(args.inp)
    rows = compute_collision_features(prs)

    # Write CSV
    with open(args.out_csv, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)

    md = ["# Universe PR Range Collision Summary", "", summarize(rows), "", "## Notes", "- Collision definition: overlap in (start-end) AND concurrent open intervals."]
    with open(args.out_md, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")

    print(summarize(rows))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
