import pandas as pd

sales = pd.Series([42, 38, 51, 29, 46, 34, 61, 40, 37, 44])
print("Mean:", sales.mean())
print("Median:", sales.median())
print("Mode:", sales.mode().tolist())
