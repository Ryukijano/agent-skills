# AI for Data Quality

## Description

Automated profiling, anomaly detection, data cleaning, imputation, validation, and continuous data quality monitoring for ML and analytics.

## When to use

You need to detect, measure, and improve the accuracy, completeness, consistency, and timeliness of datasets used for analytics or ML.

## Usage

- **Profiling and scoring**: compute quality dimensions across schema, values, and distributions.
- **Anomaly detection**: use statistical or ML models to flag outliers and drift.
- **Data cleaning**: auto-correct, impute, or standardize values.
- **Validation rules**: encode constraints and monitor rule violations.
- **Drift monitoring**: track data distribution and schema changes over time.

## Steps

1. Profile the dataset and define quality dimensions and thresholds.
2. Build or integrate an anomaly detector and validation rule engine.
3. Clean and impute data while preserving lineage.
4. Monitor quality metrics in dashboards and alerts.
5. Retrain models when quality issues or drift are detected.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import IsolationForest

X = df.select_dtypes(include="number").fillna(0)
clf = IsolationForest(contamination=0.05, random_state=42)
df["anomaly_score"] = clf.decision_function(X)
```

## Tuning notes

- Tune contamination based on empirical false-positive rates.
- Distinguish between data bugs and legitimate distribution shift.
- Validate cleaning steps with business stakeholders.

## Verification

1. Compute quality scores before and after cleaning on a known-dirty dataset.
2. Detect and report the top anomalous records and their features.
3. Compare a model trained on cleaned data to one trained on raw data.

## References

- https://doi.org/10.1145/3592616
- https://doi.org/10.1016/j.infsof.2023.107268
- https://doi.org/10.1145/3722214
- https://doi.org/10.1109/aitest62860.2024.00023

## References

- https://doi.org/10.1145/3592616
- https://doi.org/10.1016/j.infsof.2023.107268
- https://doi.org/10.1145/3722214
- https://doi.org/10.1109/aitest62860.2024.00023
