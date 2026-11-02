import argparse
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser(description="Central Limit Theorem with an exponential population")
parser.add_argument("--save", action="store_true", help="Save chart.png instead of opening a window")
args = parser.parse_args()

np.random.seed(42)
population = np.random.exponential(scale=500, size=100000)
sample_sizes = [10, 30, 100]
fig, axes = plt.subplots(1, 3, figsize=(15, 4))
for i, n in enumerate(sample_sizes):
    sample_means = [
        np.random.choice(population, size=n, replace=False).mean()
        for _ in range(1000)
    ]
    mean = np.mean(sample_means)
    sd = np.std(sample_means)
    print(f"Sample Size n = {n}: Mean={mean:.1f}, SD={sd:.1f}")
    axes[i].hist(sample_means, bins=30, color="teal", edgecolor="black", alpha=0.7)
    axes[i].set_title(f"Sample Size n = {n}\nMean={mean:.1f}, SD={sd:.1f}")
    axes[i].set_xlabel("Sample Mean")
    axes[i].set_ylabel("Frequency")
plt.tight_layout()
if args.save:
    fig.savefig(Path(__file__).with_name("chart.png"), dpi=150)
    plt.close(fig)
else:
    plt.show()
