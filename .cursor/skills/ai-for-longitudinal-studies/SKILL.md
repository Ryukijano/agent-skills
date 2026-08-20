# AI for Longitudinal Studies

## Description

Machine learning and deep learning for repeated measurements, time-varying covariates, missing data, trajectories, and outcomes in longitudinal cohorts and EHR data.

## When to use

You are analyzing repeated observations over time, predicting future trajectories, or handling attrition and irregular sampling in longitudinal health, social, or behavioral data.

## Usage

- **Trajectory modeling**: predict individual or population-level progression over time.
- **Missing-data handling**: impute or model informative dropout and irregular visits.
- **Feature engineering**: encode time-varying covariates, slopes, and exposure histories.
- **Causal longitudinal analysis**: estimate dynamic treatment effects with sequential ignorability.

## Steps

1. Structure the data into long format with subject, time, and outcome columns.
2. Encode temporal patterns (lags, rolling summaries, time-since-event).
3. Choose a model suited to repeated measures (mixed-effects, RNN, transformer, or survival model).
4. Evaluate with time-aware cross-validation and check temporal leakage.
5. Report uncertainty and sensitivity to missing-data assumptions.

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

## References

- https://doi.org/10.3390/math14122084
- https://doi.org/10.1007/s10462-023-10561-w
- https://doi.org/10.1007/s10462-023-10677-z
- https://doi.org/10.1093/jamia/ocad168
