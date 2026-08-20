# AI for Semiconductor Manufacturing

## Description

Machine learning for semiconductor fabrication yield enhancement, wafer defect detection, equipment fault classification, process control, and advanced lithography/etch modeling.

## When to use

You are working with wafer fabrication data, trying to predict die yield, classify wafer or equipment faults, build virtual metrology models, or optimize lithography and etch processes.

## Key concepts

- **Yield and WAT prediction**: models that map equipment, process, and inline metrology data to final test yield.
- **Fault detection and classification (FDC)**: anomaly detection on tool trace data for chamber drift or misprocess.
- **Virtual metrology**: inferring wafer properties from process data when inline measurement is sparse.
- **Lithography and etch**: hotspot detection, overlay correction, critical dimension prediction, and endpoint control.
- **Run-to-run control**: adaptive adjustment of recipe parameters using feedback from measured outputs.

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
