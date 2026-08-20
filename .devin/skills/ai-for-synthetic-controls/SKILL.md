# AI for Synthetic Controls

## Description

Machine learning for constructing, validating, and extending synthetic and virtual control arms from observational data to augment clinical and policy evaluation.

## When to use

You have one or a few treated units and many untreated donor units, and need a credible counterfactual trajectory from a weighted combination of donors.

## Usage

- **Classic synthetic controls**: build a weighted donor pool to match pre-treatment outcomes.
- **Penalized and sparse synthetic controls**: regularize unit and feature weights.
- **Deep representation learning**: learn low-dimensional embeddings for better donor matching.
- **External and virtual control arms**: augment single-arm trials with historical or real-world controls.

## Steps

1. Define the treated unit, pre-treatment period, donor pool, and outcome of interest.
2. Select predictor variables and fit a weighted combination of donors to pre-treatment outcomes.
3. Evaluate pre-treatment fit and generate the counterfactual trajectory.
4. Compute treatment effects and placebo-based inferential procedures.
5. Assess robustness to donor pool composition and weight sparsity.

## Code pattern

```python
import numpy as np
import pandas as pd
from scipy.optimize import minimize

# Pre-treatment outcome matrix: rows = time, columns = control units
Y_pre = donor_df.loc[donor_df["pre"] == 1, control_units].values
y_treated = treated_df.loc[treated_df["pre"] == 1, "outcome"].values

def sc_loss(w):
    return np.mean((Y_pre @ w - y_treated) ** 2)

res = minimize(sc_loss, x0=np.ones(Y_pre.shape[1]) / Y_pre.shape[1],
               method="SLSQP", bounds=[(0, 1)] * Y_pre.shape[1],
               constraints={"type": "eq", "fun": lambda w: np.sum(w) - 1})
```

## Tuning notes

- Exclude donors that are poor matches or place high weight on a single unit.
- Use cross-validation on pre-treatment periods to choose regularization.
- Apply placebo tests and leave-one-out robustness checks.
- Be cautious when using synthetic controls as primary evidence in regulatory settings.

## Verification

1. Replicate the California tobacco-control synthetic control case study.
2. Compare classic SCM, penalized SCM, and a learned-representation baseline.
3. Run placebo inference and show that treatment effects exceed the null distribution.

## References

- https://www.bis.org/publ/work1181.pdf
- https://doi.org/10.22541/au.176072431.11742213/v1
- https://arxiv.org/html/2602.04611
- https://microsoft.github.io/SparseSC/
- https://www.mit.edu/~jhainm/Paper/ccs.pdf

## References

- https://www.bis.org/publ/work1181.pdf
- https://doi.org/10.22541/au.176072431.11742213/v1
- https://arxiv.org/html/2602.04611
- https://microsoft.github.io/SparseSC/
- https://www.mit.edu/~jhainm/Paper/ccs.pdf
