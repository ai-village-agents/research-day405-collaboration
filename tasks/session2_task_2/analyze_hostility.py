"""
analyze_hostility.py
--------------------
Reads the JSON dataset describing system failures and prints the frequency of
each failure category. The script expects the JSON file to contain an array of
objects with a `failure_category` field, and uses pandas for the aggregation.
"""

from pathlib import Path
import sys

import pandas as pd


def main(json_filename: str = "system_failures_and_protocols.json") -> None:
    """Load the dataset and print simple frequency statistics."""
    json_path = Path(json_filename)

    # Validate that the expected JSON file exists before attempting to load it.
    if not json_path.exists():
        print(f"JSON file not found: {json_path.resolve()}", file=sys.stderr)
        sys.exit(1)

    try:
        # pandas handles JSON-to-DataFrame conversion, making aggregation easier.
        df = pd.read_json(json_path)
    except ValueError as exc:
        print(f"Failed to parse JSON: {exc}", file=sys.stderr)
        sys.exit(1)

    if "failure_category" not in df.columns:
        print("The dataset does not include a 'failure_category' column.", file=sys.stderr)
        sys.exit(1)

    # Count how often each failure category occurs, including missing categories.
    category_counts = df["failure_category"].value_counts(dropna=False).sort_values(ascending=False)

    print("Failure Category Frequency Analysis")
    print("-----------------------------------")
    for category, count in category_counts.items():
        label = "Unspecified" if pd.isna(category) else category
        print(f"{label}: {count}")


if __name__ == "__main__":
    main()
