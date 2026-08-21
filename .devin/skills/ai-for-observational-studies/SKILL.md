# AI for Observational Studies

## Description

Estimate causal effects from real-world data using propensity scores and double machine learning.

## When to use

You are estimating causal effects, treatment responses, or policy impacts from observational data where treatment assignment was not randomized.

## Usage

- Build propensity scores and inverse probability weights with CausalForge.
- Apply double/debiased machine learning (EconML, DoubleML).
- Emulate target trials from EHR and claims databases.
- Adjust for high-dimensional confounding with proxy variables.
- Assess balance and sensitivity to unmeasured confounding.

## Steps

1. Define the causal question, exposure, and outcome.
2. Extract longitudinal observational data and confounders.
3. Estimate propensity scores or train nuisance models.
4. Compute ATE/CATE with DML or weighting.
5. Run sensitivity analyses and report robustness.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor, GradientBoostingClassifier
from econml.dml import LinearDML

Y = obs_df["outcome"]
T = obs_df["treatment"]
X = obs_df[["age", "comorbidity", "lab_value"]]

est = LinearDML(
    model_y=GradientBoostingRegressor(random_state=42),
    model_t=GradientBoostingClassifier(random_state=42),
)
est.fit(Y, T, X=X)
print("CATE:", est.effect(X[:5]))
```

## Tuning notes

- Check positivity and overlap; extrapolation can bias causal estimates.
- Use cross-fitting and sample splitting to reduce overfitting in nuisance models.
- Validate with negative controls, placebo tests, or coarsened exact matching.
- Report sensitivity bounds for potential unmeasured confounders.

## Verification

1. Reproduce an observational benchmark (e.g., IHDP, Jobs, ACIC) and compare estimates.
2. Compare propensity-weighted, matching, and doubly robust estimates.
3. Run a sensitivity analysis and show how large an unmeasured confounder must be.

## References

- https://arxiv.org/abs/2501.00755v1
- https://doi.org/10.3386/w30302
- https://pubmed.ncbi.nlm.nih.gov/34652613/
- https://proceedings.mlr.press/v161/shi21a/shi21a.pdf
