# AI for Data Quality

## Description

Detect and repair data quality issues across pipelines, warehouses, and AI inputs.

## When to use

You need to detect, measure, and improve the accuracy, completeness, consistency, and timeliness of datasets used for analytics or ML.

## Usage

- Profile tables and auto-generate data quality rules (Great Expectations, Soda).
- Detect null spikes, distribution drift, and schema changes.
- Build expectation suites and data contracts in CI.
- Prioritize remediation with impact/lineage scoring.
- Track data health SLAs and coverage.

## Steps

1. Profile source and warehouse tables.
2. Define business rules and data contracts.
3. Train or configure anomaly detection on historical patterns.
4. Alert, quarantine, and repair bad records.
5. Report data health and retrain baselines.

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
