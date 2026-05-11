#!/usr/bin/env python3
"""Fetch pull request metadata from a GitHub repo via gh GraphQL, paging safely.

Writes JSONL (one PR node per line).

Includes the most recent PR comment (if any) to support crude closure-reason classification.

Example:
  python fetch_universe_prs.py --repo ai-village-agents/the-universe --max 1500 \
    --out data/historical/universe_prs_2026-05-11.jsonl
"""

import argparse
import json
import subprocess
from typing import Any, Dict, Optional, Tuple

QUERY = r"""
query($owner:String!, $name:String!, $cursor:String) {
  repository(owner:$owner, name:$name) {
    pullRequests(first: 100, after: $cursor,
      orderBy: {field: CREATED_AT, direction: DESC},
      states: [OPEN, CLOSED, MERGED]
    ) {
      pageInfo { hasNextPage endCursor }
      nodes {
        number
        title
        state
        createdAt
        closedAt
        mergedAt
        url
        author { login }
        baseRefName
        headRefName
        additions
        deletions
        changedFiles
        comments(last: 1) {
          nodes {
            author { login }
            body
            createdAt
          }
        }
      }
    }
  }
}
"""


def run_gh_graphql(owner: str, name: str, cursor: Optional[str]) -> Dict[str, Any]:
    cmd = [
        "gh",
        "api",
        "graphql",
        "-f",
        f"query={QUERY}",
        "-F",
        f"owner={owner}",
        "-F",
        f"name={name}",
    ]
    if cursor:
        cmd += ["-F", f"cursor={cursor}"]

    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if p.returncode != 0:
        raise RuntimeError(f"gh api graphql failed (code {p.returncode}): {p.stderr.strip()}")
    return json.loads(p.stdout)


def parse_repo(s: str) -> Tuple[str, str]:
    if "/" not in s:
        raise argparse.ArgumentTypeError("--repo must be like owner/name")
    owner, name = s.split("/", 1)
    if not owner or not name:
        raise argparse.ArgumentTypeError("--repo must be like owner/name")
    return owner, name


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--repo", type=parse_repo, required=True)
    ap.add_argument("--max", type=int, default=1000)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    owner, name = args.repo
    out_path = args.out

    wrote = 0
    cursor = None
    with open(out_path, "w", encoding="utf-8") as f:
        while wrote < args.max:
            resp = run_gh_graphql(owner, name, cursor)
            pr_conn = resp["data"]["repository"]["pullRequests"]
            nodes = pr_conn["nodes"]
            if not nodes:
                break

            for node in nodes:
                f.write(json.dumps(node, ensure_ascii=False) + "\n")
                wrote += 1
                if wrote >= args.max:
                    break

            if wrote >= args.max:
                break

            page = pr_conn["pageInfo"]
            if not page["hasNextPage"]:
                break
            cursor = page["endCursor"]

    print(f"Wrote {wrote} PR rows to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
