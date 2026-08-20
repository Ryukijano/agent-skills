# AI for Economics

## Description

Causal inference, policy evaluation, nowcasting, heterogeneous treatment effects, and demand estimation for economic and policy analysis.

## When to use

You are evaluating economic policies, estimating treatment effects, nowcasting macro indicators, or modeling consumer/worker behavior from observational or panel data.

## Key concepts

- **Causal ML**: use machine learning to estimate average and heterogeneous treatment effects (e.g., causal forests, double/debiased machine learning).
- **Policy evaluation without controls**: forecast counterfactual outcomes for treated units using pre-treatment data and ML forecasters.
- **Nowcasting**: predict current-quarter GDP, inflation, or employment before official releases by combining high-frequency data.
- **Demand and elasticity estimation**: recover price/causal effects on demand with endogeneity controls.

## Code pattern

```python
import pandas as pd
from econml.dml import LinearDML
from sklearn.ensemble import GradientBoostingRegressor

# Causal effect of a policy/treatment on an outcome
Y = df["outcome"]
T = df["treatment"]
X = df[["region", "pre_trend", "demographic"]]

est = LinearDML(
    model_y=GradientBoostingRegressor(),
    model_t=GradientBoostingRegressor(),
)
est.fit(Y, T, X=X)
print("ATE:", est.ate_)
print("CATE intervals:", est.ate__interval())
```

## Tuning notes

- Use out-of-fold nuisance predictions and cross-fitting to avoid overfitting in causal ML.
- For nowcasting, prefer models that handle ragged edges and mixed frequencies (factor models, MIDAS, LSTM).
- Validate counterfactual forecasts with placebo tests and pre-trend checks.

## Verification

1. Replicate a difference-in-differences or synthetic-control result with a causal ML estimator.
2. Build a nowcast of a macro variable and compare to a benchmark AR model.
3. Estimate a price elasticity and test robustness to confounders.

## References

- https://doi.org/10.1146/annurev-economics-080217-053433
- https://arxiv.org/html/2312.05858v2
- https://arxiv.org/html/2208.03489
- https://www.annualreviews.org/content/journals/10.1146/annurev-economics-080217-053214
