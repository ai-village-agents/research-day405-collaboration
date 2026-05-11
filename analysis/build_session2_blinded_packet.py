#!/usr/bin/env python3
"""Build a blinded Session 2 packet from a run log.

Usage:
  python3 analysis/build_session2_blinded_packet.py \
    --input experiments/session2/runs/solo_gpt-5-1_task2_analyzeUserActivity.md \
    --output analysis/session2_blinded_packets/output_A.md

The script removes metadata, timestamps, participant names, and condition labels,
and keeps the substantive analytical content beginning at the first `## Bugs Found`
or `## Final output` section if present.
"""

from __future__ import annotations

import argparse
from pathlib import Path

START_MARKERS = [
    "## Final output",
    "## Bugs Found",
    "## Bug Report",
    "## Summary",
]

HEADER = "# Blinded Output\n\n## Task family\nSeeded bug inspection.\n\n## Final output\n\n"


def strip_leading_metadata(text: str) -> str:
    for marker in START_MARKERS:
        idx = text.find(marker)
        if idx != -1:
            return text[idx:]
    return text


def sanitize(text: str) -> str:
    replacements = {
        "GPT-5.1": "[BLINDED]",
        "GPT-5.2": "[BLINDED]",
        "GPT-5.4": "[BLINDED]",
        "GPT-5": "[BLINDED]",
        "Claude Sonnet 4.5": "[BLINDED]",
        "Claude Sonnet 4.6": "[BLINDED]",
        "Claude Haiku 4.5": "[BLINDED]",
        "Claude Opus 4.5": "[BLINDED]",
        "Claude Opus 4.6": "[BLINDED]",
        "Gemini 2.5 Pro": "[BLINDED]",
        "DeepSeek-V3.2": "[BLINDED]",
        "**Condition:** Solo": "**Condition:** [BLINDED]",
        "**Condition:** Unstructured": "**Condition:** [BLINDED]",
        "**Condition:** Structured": "**Condition:** [BLINDED]",
        "**Participants:**": "**Participants:** [BLINDED]",
        "**Participant:**": "**Participant:** [BLINDED]",
        "**Start time:**": "**Start time:** [BLINDED]",
        "**End time:**": "**End time:** [BLINDED]",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a blinded Session 2 packet from a run log")
    parser.add_argument("--input", required=True, help="Input run-log markdown file")
    parser.add_argument("--output", required=True, help="Output blinded markdown file")
    args = parser.parse_args()

    src = Path(args.input)
    dst = Path(args.output)

    text = src.read_text()
    body = strip_leading_metadata(text).strip()
    body = sanitize(body)

    dst.write_text(HEADER + body + "\n")
    print(f"Wrote blinded packet: {dst}")


if __name__ == "__main__":
    main()
