# AI for IoT

## Description

TinyML, edge AI, anomaly detection, device fingerprinting, and predictive maintenance for IoT systems.

## When to use

You are deploying intelligence on IoT sensors, gateways, or edge devices for monitoring, predictive maintenance, anomaly detection, or control.

## Key concepts

- **TinyML and edge AI**: run compressed models on microcontrollers and gateways.
- **IoT device fingerprinting**: identify devices from traffic or sensor signatures.
- **Time-series anomaly detection**: LSTM, TCN, and transformers for sensor streams.
- **Predictive maintenance**: forecast failures from vibration, temperature, or current.
- **Security and privacy**: lightweight encryption, federated learning, and anomaly detection.

## Code pattern

```python
from sklearn.ensemble import IsolationForest
import pandas as pd

# Sensor time-series features: mean, std, min, max over a window
X = df[["temp_mean", "temp_std", "humidity_mean", "vibration_peak"]]

clf = IsolationForest(contamination=0.02, random_state=42)
df["anomaly"] = clf.fit_predict(X)
```

## Tuning notes

- IoT devices are resource-constrained; quantize, prune, or distill models.
- Use streaming/online learning to adapt to changing environments.
- Balance communication cost with model accuracy through offloading or federated learning.
- Validate on real device traces and consider class imbalance for rare events.

## Verification

1. Train a TinyML anomaly detector and measure inference latency on a target board.
2. Build a device-fingerprinting classifier and evaluate on unseen device models.
3. Predict equipment failure and compare to a rule-based maintenance schedule.

## References

- https://arxiv.org/html/2410.19998v1
- https://doi.org/10.1145/3690639
- https://ar5iv.labs.arxiv.org/html/2011.08612
- https://arxiv.org/html/2406.03820
