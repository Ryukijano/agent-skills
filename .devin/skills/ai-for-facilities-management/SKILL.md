# AI for Facilities Management

## Description

Predictive maintenance, fault detection, digital twins, and AI-enabled asset lifecycle management for built facilities.

## When to use

You are managing maintenance, energy, and asset performance in commercial, industrial, or institutional facilities.

## Usage

- **Predictive maintenance**: forecast equipment faults and remaining useful life.
- **Fault detection and diagnostics**: use rule-ML hybrids for HVAC, lighting, and AHU.
- **Asset digital twins**: update condition models from IoT and work orders.
- **Energy optimization**: use ML and RL to reduce operating cost and carbon.

## Steps

1. Ingest sensor, BMS, CMMS, and asset master data.
2. Label faults, failures, and maintenance events.
3. Train predictive models (XGBoost, LSTM, autoencoders).
4. Deploy real-time anomaly alerts and work-order integration.
5. Continuously retrain on new data and feedback.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import IsolationForest

# Anomaly detection on HVAC time series
X = df[['supply_temp', 'return_temp', 'fan_speed', 'damper_pos']]
clf = IsolationForest(contamination=0.05, random_state=42)
df['anomaly'] = clf.fit_predict(X)
```

## Tuning notes

- Balance class imbalance with resampling or cost-sensitive learning.
- Use physics-aware features such as delta-T and setpoint deviations.
- Integrate human-in-the-loop for maintenance decisions.

## Verification

1. Predict AHU faults on a labeled building dataset.
2. Compare predictive maintenance alerts to a calendar-based program.
3. Show reduction in unplanned downtime or energy cost.

## References

- https://doi.org/10.1108/f-02-2025-0032
- https://www.mdpi.com/2075-5309/15/4/630
- https://doi.org/10.3389/fbuil.2025.1734945
- https://doi.org/10.3390/buildings15224129
- https://ec-3.org/publication/ec32025_369/
