# AI for Rail

## Description

Use machine learning to monitor rail infrastructure, predict failures, optimize timetables, and manage service disruptions.

## When to use

You are monitoring track and rolling stock, predicting rail failures, optimizing timetables, or managing service disruptions.

## Usage

- Detect rail, sleeper, and track-geometry defects from inspection and sensor data.
- Predict wheelset, bearing, brake, and HVAC failures in rolling stock.
- Optimize timetables and rescheduling under delays.
- Forecast passenger flow and energy use for eco-driving.

## Steps

1. Aggregate track geometry, inspection images, and rolling-stock sensor streams.
2. Engineer per-route features to account for geography and seasonality.
3. Train an anomaly or survival model for rare infrastructure and component failures.
4. Validate recall and false-positive trade-offs with maintenance crews.
5. Integrate predictions into timetable optimization and dispatch dashboards.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import IsolationForest

# Detect anomalies in track geometry measurements
X = np.load("track_geometry_features.npy")
clf = IsolationForest(contamination=0.01, random_state=42).fit(X)
anomalies = clf.predict(X)
```

## Tuning notes

- Railway data is highly seasonal and geographically variable; model per route or line.
- Infrastructure failures are rare; use anomaly detection or survival models.
- Safety and service availability constraints dominate cost optimization.

## Verification

1. Train a track-defect detector on geometry/inspection data and evaluate recall.
2. Build a train delay prediction model from historical operations data.
3. Simulate a timetable disruption and compare an optimization-based recovery plan to a manual baseline.

## References

- https://doi.org/10.3390/s26030906
- https://www.networkrail.co.uk/industry-and-commercial/insight-using-ai-to-run-a-reliable-railway/
- https://doi.org/10.1016/j.autcon.2026.107102
- https://doi.org/10.1007/s10994-024-06559-2
