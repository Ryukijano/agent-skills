# AI for Nephrology

## Description

Use machine learning to predict chronic kidney disease progression, acute kidney injury, dialysis outcomes, and transplant success.

## When to use

You are building models to predict CKD progression, detect acute kidney injury early, optimize dialysis, allocate kidneys, or analyze renal biopsy and histopathology images.

## Usage

- Risk-stratify CKD progression using eGFR trajectories, albuminuria, and comorbidities.
- Build EHR-based early-warning models for in-hospital acute kidney injury.
- Optimize dialysis treatment adequacy and predict access failure.
- Match donors and recipients, predict rejection, and forecast graft survival.
- Segment and classify glomerular lesions in renal biopsy images.

## Steps

1. Assemble longitudinal EHR, labs, pathology, and imaging data for kidney-related endpoints.
2. Define prediction targets (AKI, CKD progression, graft survival, lesion type) and time windows.
3. Train and validate predictive models with time-based splits and competing-risk handling.
4. Integrate predictions into nephrology workflows as decision support.
5. Audit for disparities in race, ethnicity, geography, and access to care.
6. Monitor model performance across health systems and retrain as guidelines evolve.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import TimeSeriesSplit

# Predict 90-day AKI from structured EHR features
X = df[["age", "baseline_creatinine", "diabetes", "nephrotoxin_exposure"]]
y = df["aki_within_90d"]

cv = TimeSeriesSplit(n_splits=5)
model = GradientBoostingClassifier(random_state=42)
for train_idx, test_idx in cv.split(X):
    model.fit(X.iloc[train_idx], y.iloc[train_idx])
    print("AUROC:", model.score(X.iloc[test_idx], y.iloc[test_idx]))
```

## Tuning notes

- Use time-based splits; eGFR and creatinine are longitudinal and future labs must not leak.
- Competing risks (death, ESKD, transplant) often require survival or Fine-Gray models.
- External validate across health systems because CKD prevalence and lab assays vary.
- Monitor for disparities in race, ethnicity, and access to care.

## Verification

1. Train a CKD progression model and compare time-dependent AUC to KDIGO staging.
2. Build an AKI early-warning pipeline with hourly EHR windows and alert latency analysis.
3. Evaluate glomerulus segmentation on PAS-stained renal biopsy patches against pathologist annotations.

## References

- https://doi.org/10.1016/j.xkme.2024.100927
- https://doi.org/10.1007/s11255-024-04165-8
- https://pmc.ncbi.nlm.nih.gov/articles/PMC10103234/
- https://doi.org/10.2215/CJN.0000000000000068
