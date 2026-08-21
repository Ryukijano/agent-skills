# AI for Randomized Trials

## Description

Estimate heterogeneous treatment effects and subgroup benefits in randomized experiments.

## When to use

You are analyzing an RCT and want to estimate average or heterogeneous treatment effects, adjust for covariates to improve power, or design adaptive randomization and interim analyses.

## Usage

- Estimate conditional average treatment effects with causal forests (grf).
- Identify responder subgroups using uplift and ITE models.
- Adjust for covariates to improve precision of ATE.
- Detect treatment effect heterogeneity across sites and demographics.
- Power adaptive enrichment and basket trials.

## Steps

1. Lock the randomization schedule and outcome variables.
2. Pre-specify covariates and subgroup hypotheses.
3. Train causal forest or meta-learner models for CATE/ITE.
4. Rank subgroups by estimated benefit and uncertainty.
5. Validate with cross-fitting and false discovery control.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from econml.dml import LinearDML

# RCT data with randomized treatment
Y = rct_df["outcome"]
T = rct_df["treatment"]
X = rct_df[["age", "sex", "baseline_score"]]

est = LinearDML(
    model_y=GradientBoostingRegressor(random_state=42),
    model_t=GradientBoostingRegressor(random_state=42),
)
est.fit(Y, T, X=X)
print("ATE:", est.ate_)
```

## Tuning notes

- Preserve randomization-based inference; do not data-mine treatment assignment.
- Cross-fit nuisance models to avoid overfitting bias in doubly robust estimators.
- Pre-specify subgroups; post-hoc subgroup discovery requires multiplicity control.
- Use positive controls or simulations to verify type-I error and power.

## Verification

1. Replicate a published RCT analysis with an ML-adjusted estimator and compare SEs.
2. Simulate null and alternative scenarios to confirm valid coverage of confidence intervals.
3. Compare heterogeneous effect estimates between causal forest and linear interaction models.

## References

- https://www.nber.org/system/files/working_papers/w24678/w24678.pdf
- https://proceedings.mlr.press/v286/chen25b.html
- https://www.nature.com/articles/s41598-025-10566-1
- https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2800273
- https://link.springer.com/article/10.1186/s13063-020-4076-y
