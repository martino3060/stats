import argparse
from pathlib import Path

import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Poisson PMF: lambda=4")
parser.add_argument("--save", action="store_true", help="Save chart.png instead of opening a window")
args = parser.parse_args()

lam = 4
k = np.arange(0, 15)
pmf_poisson = stats.poisson.pmf(k, lam)
print(f"P(X=3) = {stats.poisson.pmf(3, lam):.5f}")
plt.bar(k, pmf_poisson, color="orange", edgecolor="black")
plt.title(r"Poisson PMF ($\lambda=4$ complaints/day)")
plt.xlabel("Number of Events (k)")
plt.ylabel("Probability")
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.tight_layout()
if args.save:
    plt.savefig(Path(__file__).with_name("chart.png"), dpi=150)
    plt.close()
else:
    plt.show()
