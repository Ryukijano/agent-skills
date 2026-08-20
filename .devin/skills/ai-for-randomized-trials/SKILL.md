# AI for Randomized Trials

## Description

Machine learning for heterogeneous treatment effects, covariate adjustment, adaptive randomization, and efficient inference in randomized controlled trials.

## When to use

You are analyzing an RCT and want to estimate average or heterogeneous treatment effects, adjust for covariates to improve power, or design adaptive randomization and interim analyses.

## Usage

- **Heterogeneous treatment effects**: identify subgroups that benefit most or least.
- **Covariate adjustment**: improve precision using baseline prognostic variables.
- **Adaptive designs**: inform response-adaptive randomization and enrichment.
- **Efficient inference**: combine machine learning with valid randomization inference.

## Steps

1. Lock the analysis plan, including adjustment variables and subgroups, before unblinding.
2. Fit flexible outcome and propensity nuisance models with cross-fitting.
3. Estimate average and conditional treatment effects with appropriate inference.
4. Test for treatment-effect heterogeneity using pre-specified subgroups or learned partitions.
5. Report confidence intervals and control the family-wise error rate for subgroup analyses.

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

## References

- https://www.nber.org/system/files/working_papers/w24678/w24678.pdf
- https://proceedings.mlr.press/v286/chen25b.html
- https://www.nature.com/articles/s41598-025-10566-1
- https://jamanetwork.com/journals/jamanetworkopen/fullarticle/2800273
- https://link.springer.com/article/10.1186/s13063-020-4076-y
