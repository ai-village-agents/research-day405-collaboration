#!/usr/bin/env python3
"""Build a blinded Session 2 packet from a run log.

Usage:
  python3 analysis/build_session2_blinded_packet.py \
    --input experiments/session2/runs/solo_gpt-5-1_task2_analyzeUserActivity.md \
    --output analysis/session2_blinded_packets/output_A.md

The script removes metadata, timestamps, participant names, and condition labels,
and keeps only substantive analytical content.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

START_MARKERS = [
    "## Bugs Found",
    "## Bug-by-Bug Analysis",
    "## Bug Report",
    "## Final output",
    "## Summary",
    "## Executive Summary",
]

HEADER = "# Blinded Output\n\n## Task family\nSeeded bug inspection.\n\n## Final output\n\n"


def strip_leading_metadata(text: str) -> str:
    positions = [text.find(marker) for marker in START_MARKERS if text.find(marker) != -1]
    if positions:
        return text[min(positions):]
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
    }
    for old, new in replacements.items():
        text = text.replace(old, new)

    text = re.sub(r"^\*\*Condition:\*\*.*$", "**Condition:** [BLINDED]", text, flags=re.MULTILINE)
    text = re.sub(r"^\*\*Participants?:\*\*.*$", "**Participants:** [BLINDED]", text, flags=re.MULTILINE)
    text = re.sub(r"^\*\*Start time:\*\*.*$", "**Start time:** [BLINDED]", text, flags=re.MULTILINE)
    text = re.sub(r"^\*\*End time:\*\*.*$", "**End time:** [BLINDED]", text, flags=re.MULTILINE)
    text = re.sub(r"^\*\*(Timestamp|Time):\*\*.*$", "**Timestamp:** [BLINDED]", text, flags=re.MULTILINE)
    text = re.sub(r"^\*\*(Report compiled by|Synthesizer|Integrating|Reviewer|Reviewing|Handoff to Verifier.*):\*\*.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^## Repository Output Location.*?(?=^---$|\Z)", "", text, flags=re.MULTILINE | re.DOTALL)
    text = re.sub(r"^---\n\*\*Report compiled by:.*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a blinded Session 2 packet from a run log")
    parser.add_argument("--input", required=True, help="Input run-log markdown file")
    parser.add_argument("--output", required=True, help="Output blinded markdown file")
    args = parser.parse_args()

    src = Path(args.input)
    dst = Path(args.output)

    text = src.read_text()
    body = strip_leading_metadata(text)
    body = sanitize(body)

    dst.write_text(HEADER + body + "\n")
    print(f"Wrote blinded packet: {dst}")


if __name__ == "__main__":
    main()
