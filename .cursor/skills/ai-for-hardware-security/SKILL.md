# AI for Hardware Security

## Description

Use machine learning to detect Trojans, analyze side-channel leakage, evaluate PUFs, and secure accelerators.

## When to use

You are assessing the security of ASICs, FPGAs, or AI accelerators; detecting Trojans, side-channel leakage, or PUF vulnerabilities; or designing trusted hardware.

## Usage

- Classify power and electromagnetic traces to recover keys or detect side-channel leakage.
- Detect anomalous circuit behavior and layout features of hardware Trojans.
- Assess PUF entropy, attack robustness, and anti-counterfeiting properties.
- Monitor neural accelerators at run time for fault and Trojan attacks.

## Steps

1. Collect side-channel, layout, or run-time traces under varying conditions.
2. Train a classifier or anomaly detector for the target threat (Trojan, leakage, fault).
3. Validate the model on unseen attack scenarios and device corners.
4. Integrate detection into a test, supply-chain, or run-time monitoring flow.
5. Evaluate security overhead in area, power, and latency against performance.
6. Update the model as new Trojan designs or attack strategies emerge.

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
