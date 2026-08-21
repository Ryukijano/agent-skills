# AI for Longitudinal Studies

## Description

Model repeated measurements over time to track disease progression, treatment response, and biomarker trajectories.

## When to use

You are analyzing repeated observations over time, predicting future trajectories, or handling attrition and irregular sampling in longitudinal health, social, or behavioral data.

## Usage

- Impute sparse EHR and wearable time series with MUSE-Net or SADI.
- Build mixed-effects and trajectory models in R lme4 or Python statsmodels.
- Detect change points in patient trajectories.
- Forecast future clinical events from longitudinal panels.
- Integrate EHR with accelerometer, glucose, or blood pressure wearables.

## Steps

1. Extract longitudinal patient records and define the outcome trajectory.
2. Handle irregular sampling, missing values, and informative dropout.
3. Engineer time-varying features (slopes, area-under-curve, lag windows).
4. Train mixed-effects, joint, or deep sequence models.
5. Evaluate with individual-specific predictions and calibration.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import GroupKFold

# Long-format data with subject IDs
X = df[["time", "age", "biomarker", "treatment"]]
y = df["outcome"]
g = df["subject_id"]

model = GradientBoostingRegressor(random_state=42)
for train_idx, test_idx in GroupKFold(n_splits=5).split(X, y, g):
    model.fit(X.iloc[train_idx], y.iloc[train_idx])
    preds = model.predict(X.iloc[test_idx])
```

## Tuning notes

- Use subject-aware splitting to avoid leakage across individuals.
- Prefer models that handle varying sequence lengths (RNNs, transformers, mixed models).
- Inspect residuals for autocorrelation and heteroscedasticity over time.
- Document assumptions about missingness (MCAR, MAR, MNAR).

## Verification

1. Compare a longitudinal ML model to a mixed-effects baseline on held-out time points.
2. Show that predictions degrade gracefully when sequences are truncated or sparse.
3. Validate that temporal ordering is preserved in all train/test splits.

## References

- https://doi.org/10.3390/math14122084
- https://doi.org/10.1007/s10462-023-10561-w
- https://doi.org/10.1007/s10462-023-10677-z
- https://doi.org/10.1093/jamia/ocad168
