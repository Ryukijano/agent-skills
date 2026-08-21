# AI for Semiconductor Manufacturing

## Description

Use AI to predict wafer yield, detect defects, run virtual metrology, schedule equipment and control advanced processes in high-volume semiconductor fabrication.

## When to use

You are working with wafer fabrication data, trying to predict die yield, classify wafer or equipment faults, build virtual metrology models, or optimize lithography and etch processes.

## Usage

- **Virtual metrology**: predict wafer properties such as film thickness and CD from tool sensor data.
- **Defect detection**: classify wafer defects, reticle defects, and macro defects from images.
- **Yield prediction**: combine process parameters, tool data, and inspection results to forecast yield.
- **Predictive maintenance**: forecast tool failures, chamber matching issues, and unscheduled downtime.
- **Run-to-run control**: adjust process recipes based on real-time predictions and feedback.

## Steps

1. Collect tool sensor data, process parameters, and inspection/metrology results per wafer.
2. Build a virtual metrology model for target properties and validate against physical measurements.
3. Train defect classifiers on wafer images and review precision-recall for each defect type.
4. Engineer wafer-level features for yield prediction and rank root causes.
5. Deploy a run-to-run controller that updates recipe parameters based on predictions.
6. Continuously retrain models as tools, products, and processes evolve.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import TimeSeriesSplit

# Predict final test yield from chamber and metrology features
X = df[["etch_time", "chamber_pressure", "rf_power", "cd_inline", "film_thickness"]]
y = df["final_test_yield"]
model = RandomForestRegressor(random_state=42)
for train, test in TimeSeriesSplit(n_splits=5).split(X):
    model.fit(X.iloc[train], y.iloc[train])
```

## Tuning notes

- Semiconductor data are high-dimensional, sparse, and confidential; use dimensionality reduction and cross-fitting.
- Tool trace data are time series; include temporal features and rolling statistics, not just single values.
- Concept drift is common as chambers age or products change; monitor model performance continuously.
- Use explainability to identify root causes and avoid spurious correlations from correlated process steps.

## Verification

1. Predict wafer yield from equipment data and compare to actual final test results on a held-out lot.
2. Build an FDC model that flags anomalous chambers and validate against known maintenance events.
3. Train a virtual metrology model for film thickness and compare to inline measurement.

## References

- https://doi.org/10.1109/AIAC63745.2024.10899729
- https://doi.org/10.1109/AIHCIR67580.2025.11404861
- https://doi.org/10.1007/s00170-026-18104-7
- https://www.mdpi.com/2076-3417/13/4/2660
- https://doi.org/10.1109/ACCESS.2021.3117576
