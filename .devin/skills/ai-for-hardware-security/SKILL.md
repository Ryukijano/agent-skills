# AI for Hardware Security

## Description

ML for side-channel analysis, hardware Trojan and PUF detection, supply-chain assurance, and secure accelerator design.

## When to use

You are assessing the security of ASICs, FPGAs, or AI accelerators; detecting Trojans, side-channel leakage, or PUF vulnerabilities; or designing trusted hardware.

## Key concepts

- **Side-channel analysis**: deep learning classifies power/electromagnetic traces to recover keys or detect leakage.
- **Hardware Trojan detection**: supervised and unsupervised ML identify anomalous circuit behavior or layout features.
- **PUFs and anti-counterfeiting**: ML models assess PUF entropy and attack robustness, or assist in PUF design.
- **Secure AI accelerators**: run-time monitoring and anomaly detection protect neural accelerators against fault/Trojan attacks.

## Code pattern

```python
import numpy as np
from sklearn.ensemble import IsolationForest

# Detect anomalous side-channel traces from a Trojan-infected IC
clf = IsolationForest(contamination=0.02).fit(traces)
anomaly_scores = clf.decision_function(test_traces)
```

## Tuning notes

- Collect traces under varying temperature, voltage, and process corners for robust models.
- Avoid overfitting to specific attack scenarios; validate against unseen Trojan designs.
- Balance security overhead (area, power, latency) with system performance.

## Verification

1. Train a CNN side-channel classifier and report key-recovery success on an open AES dataset.
2. Detect a set of unknown hardware Trojans using an unsupervised anomaly detector.
3. Evaluate a PUF's unpredictability and resistance to modeling attacks.

## References

- https://link.springer.com/article/10.1007/s41635-026-00182-4
- https://doi.org/10.3390/mi15010149
- https://doi.org/10.1109/satc65530.2025.11137155
- https://doi.org/10.3390/cryptography9010005
