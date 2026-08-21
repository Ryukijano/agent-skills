# AI for Economics

## Description

Use AI for Economics to evaluate policies, estimate causal effects, nowcast macro indicators and model demand.

## When to use

You are evaluating economic policies, estimating treatment effects, nowcasting macro indicators, or modeling consumer/worker behavior from observational or panel data.


## Usage


- **Causal ML**: Estimate average and heterogeneous treatment effects (e.g., causal forests, double/debiased machine learning).
- **Policy evaluation without controls**: Forecast counterfactual outcomes for treated units using pre-treatment data and ML forecasters.
- **Nowcasting**: Predict current-quarter GDP, inflation, or employment before official releases by combining high-frequency data.
- **Demand and elasticity estimation**: Recover price/causal effects on demand with endogeneity controls.

## Steps

1. Collect and prepare observational or panel data on treatments, outcomes and covariates.
2. Evaluate economic policies.
3. Estimate treatment effects.
4. Nowcast macro indicators.
5. Validate by replicating a difference-in-differences or synthetic-control result with a causal ML estimator.
6. Deploy into the target workflow and monitor performance, drift, and outcomes.

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
- https://arxiv.org/abs/2312.05858v2
- https://arxiv.org/abs/2208.03489
- https://www.annualreviews.org/content/journals/10.1146/annurev-economics-080217-053214
