# AI for Biomarkers

## Description

Discover and validate biomarkers by integrating genomics, proteomics, and imaging data.

## When to use

You are discovering, validating, or translating biomarkers from high-dimensional omics, imaging, or multi-modal clinical data.

## Usage

- Integrate multi-omics with Flexynesis, IntegrAO, or Omics BioAnalytics.
- Discover diagnostic and prognostic signatures with MILTON.
- Build predictive panels from blood, imaging, and digital biomarkers.
- Validate biomarkers in independent cohorts and trials.
- Interpret biological pathways with feature importance.

## Steps

1. Collect omics, imaging, and clinical phenotype data.
2. Normalize, impute, and align multi-modal features.
3. Train multi-omics integration and feature-selection models.
4. Validate in held-out and external cohorts.
5. Characterize biological mechanism and clinical utility.

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
- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8650485/
- https://ai.nejm.org/doi/full/10.1056/AIoa2400867
