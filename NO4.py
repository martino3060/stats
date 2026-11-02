import argparse
from pathlib import Path

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Binomial PMF: n=5, p=0.3")
parser.add_argument("--save", action="store_true", help="Save chart.png instead of opening a window")
args = parser.parse_args()

n, p = 5, 0.3
k = np.arange(0, n + 1)
pmf = stats.binom.pmf(k, n, p)
for val, prob in zip(k, pmf):
    print(f"P(X={val}) = {prob:.5f}")
plt.bar(k, pmf, color="steelblue", edgecolor="black")
plt.title("Binomial PMF (n=5, p=0.3)")
plt.xlabel("Number of Successes (k)")
plt.ylabel("Probability")
plt.xticks(k)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
if args.save:
    plt.savefig(Path(__file__).with_name("chart.png"), dpi=150)
    plt.close()
else:
    plt.show()
