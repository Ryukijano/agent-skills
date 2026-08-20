# AI for Observational Studies

## Description

Causal machine learning for treatment-effect estimation, propensity scoring, confounding adjustment, and sensitivity analysis in observational data.

## When to use

You are estimating causal effects, treatment responses, or policy impacts from observational data where treatment assignment was not randomized.

## Usage

- **Propensity and inverse probability weighting**: balance treatment groups.
- **Doubly robust estimation**: combine outcome and treatment models for robust inference.
- **Representation learning**: learn low-dimensional adjustment sets from high-dimensional covariates.
- **Sensitivity analysis**: quantify robustness to unmeasured confounding.

## Steps

1. Define the causal estimand, treatment, outcome, and covariates.
2. Assess overlap and trim units outside the common support.
3. Fit flexible outcome and propensity models with cross-fitting.
4. Estimate the effect using AIPW, targeted maximum likelihood, or matching.
5. Conduct sensitivity analyses and report bounds under confounding scenarios.

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
