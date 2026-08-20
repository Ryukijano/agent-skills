# AI for Biomarkers

## Description

Machine learning for omics-based biomarker discovery, sparse signature selection, multi-modal integration, and clinical validation.

## When to use

You are discovering, validating, or translating biomarkers from high-dimensional omics, imaging, or multi-modal clinical data.

## Usage

- **Signature discovery**: identify sparse, reproducible biomarker panels.
- **Multi-omic integration**: combine genomics, proteomics, metabolomics, and imaging.
- **Predictive vs prognostic markers**: distinguish treatment-modifying from disease-risk biomarkers.
- **Clinical validation**: lock models and test on independent cohorts and intended-use populations.

## Steps

1. Assemble discovery and validation cohorts with clear inclusion/exclusion criteria.
2. Preprocess and harmonize multi-modal data and batch-correct where needed.
3. Apply sparse or regularized ML to select candidate biomarkers.
4. Lock the model and evaluate on an independent validation cohort.
5. Assess biological plausibility, regulatory path, and clinical actionability.

## Code pattern

```python
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import SelectKBest, f_classif

X = omics_df.drop("outcome", axis=1)
y = omics_df["outcome"]

selector = SelectKBest(f_classif, k=20)
X_sel = selector.fit_transform(X, y)
model = LogisticRegression(max_iter=1000, penalty="l1", solver="liblinear").fit(X_sel, y)
```

## Tuning notes

- Keep discovery and validation data strictly separate and time-ordered.
- Use regularization and stability selection to avoid overfitting high-dimensional data.
- Validate batch effects, measurement platforms, and population diversity.
- Document the locked model, thresholds, and intended-use claim.

## Verification

1. Reproduce a published biomarker signature and test it on a held-out cohort.
2. Compare sparse ML-selected biomarkers to univariate ranking and stability-selection baselines.
3. Report sensitivity, specificity, and calibration in the intended-use population.

## References

- https://www.nature.com/articles/s41587-023-02033-x
- https://doi.org/10.1371/journal.pcbi.1010357
- https://doi.org/10.1136/bmjopen-2021-053674
- https://ai.nejm.org/doi/full/10.1056/AIoa2400867
