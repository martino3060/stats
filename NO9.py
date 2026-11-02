import numpy as np
from scipy import stats

shift_a = np.array([45, 48, 42, 50])
shift_b = np.array([52, 55, 50, 58])
# Equal population variances are assumed, matching the manual's default.
t_stat, p_val = stats.ttest_ind(shift_a, shift_b, equal_var=True)
print(f"t-statistic: {t_stat:.3f}")
print(f"p-value: {p_val:.4f}")
