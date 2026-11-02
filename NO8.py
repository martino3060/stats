import numpy as np
from scipy import stats

bottles = np.array([498, 502, 497, 501, 499, 503, 496, 500])
t_stat, p_val = stats.ttest_1samp(bottles, popmean=500)
print(f"t-statistic: {t_stat:.3f}")
print(f"p-value: {p_val:.4f}")
