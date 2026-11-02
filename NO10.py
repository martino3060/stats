import pandas as pd
import statsmodels.api as sm

df = pd.DataFrame({
    "TV_Spend": [100, 150, 200, 250, 300],
    "Sales": [150, 200, 230, 280, 320],
})
X = sm.add_constant(df["TV_Spend"])
y = df["Sales"]
model = sm.OLS(y, X).fit()
print(f"Intercept (beta_0): {model.params['const']:.2f}")
print(f"Slope (beta_1): {model.params['TV_Spend']:.2f}")
print(f"R-squared: {model.rsquared:.4f}")
