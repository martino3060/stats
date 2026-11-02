"""The manual omits the weight observations; supply them as arguments."""

import argparse

import numpy as np
from scipy import stats


def confidence_intervals(weights):
    values = np.asarray(weights, dtype=float)
    if values.ndim != 1 or values.size < 2 or not np.all(np.isfinite(values)):
        raise ValueError("Supply at least two finite weight observations.")
    mean = values.mean()
    standard_error = values.std(ddof=1) / np.sqrt(values.size)
    intervals = {}
    for level in (0.90, 0.95, 0.99):
        margin = stats.t.ppf((1 + level) / 2, df=values.size - 1) * standard_error
        intervals[level] = (mean - margin, mean + margin)
    return intervals


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("weights", type=float, nargs="+", help="Weight observations in a common unit")
    args = parser.parse_args()
    try:
        intervals = confidence_intervals(args.weights)
    except ValueError as error:
        parser.error(str(error))
    for level, (lower, upper) in intervals.items():
        print(f"{level:.0%} CI: ({lower:.2f}, {upper:.2f})")
