import pandas as pd

sales = pd.Series([42, 38, 51, 29, 46, 34, 61, 40, 37, 44])
variance = sales.var(ddof=1)
std_dev = sales.std(ddof=1)
print(f"Sample Variance: {variance:.2f}")
print(f"Sample Std Dev: {std_dev:.2f}")
