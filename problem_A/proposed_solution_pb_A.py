"""Proposed optimized solution for IMC Challenge Problem A.

This script analyses a waveform dataset and extracts basic statistics.
The implementation uses only built-in Python features to keep the
solution lightweight and portable.
"""

from __future__ import annotations
from pathlib import Path


def analyze_waveform(path: str) -> dict:
    """Return statistics for waveform samples stored one per line."""
    with open(path) as file:
        samples = [float(value) for value in file.read().split()]
    total = sum(samples)
    count = len(samples)
    maximum = max(samples) if samples else 0.0
    minimum = min(samples) if samples else 0.0
    zero_crossings = sum(
        1 for i in range(1, count)
        if (samples[i - 1] >= 0) != (samples[i] >= 0)
    )
    average = total / count if count else 0.0
    return {
        "samples": count,
        "average": average,
        "max": maximum,
        "min": minimum,
        "zero_crossings": zero_crossings,
    }


if __name__ == "__main__":
    data_file = Path(__file__).resolve().parents[1] / "data" / "ana_waveform.txt"
    stats = analyze_waveform(str(data_file))
    for key, value in stats.items():
        print(f"{key}: {value}")
