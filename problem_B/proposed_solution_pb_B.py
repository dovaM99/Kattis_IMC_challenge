"""Proposed optimized solution for IMC Challenge Problem B.

The task works on a sliced data file where each line contains a slice
of numeric values.  The script summarises each slice by computing the
sum and mean, providing a compact representation useful for further
analysis or scoring.
"""

from __future__ import annotations
from pathlib import Path


def summarize_slices(path: str) -> list[dict]:
    """Return statistics for each slice in the file."""
    summaries = []
    with open(path) as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            values = [float(v) for v in line.split()]
            total = sum(values)
            count = len(values)
            summaries.append(
                {
                    "count": count,
                    "sum": total,
                    "mean": total / count if count else 0.0,
                }
            )
    return summaries


if __name__ == "__main__":
    data_file = Path(__file__).resolve().parents[1] / "data" / "sliced_data.txt"
    for idx, stats in enumerate(summarize_slices(str(data_file)), start=1):
        print(f"slice {idx}: count={stats['count']} sum={stats['sum']} mean={stats['mean']}")
