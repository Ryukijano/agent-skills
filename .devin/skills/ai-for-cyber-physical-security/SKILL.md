# AI for Cyber-Physical Security

## Description

Use machine learning to secure industrial control systems, detect SCADA anomalies, learn physical invariants, and trace cross-layer cyber-physical attacks.

## When to use

You are protecting power, water, manufacturing, or transport systems
where IT, OT, and physical processes must be defended together.

## Usage

- Monitor network and process telemetry for ICS and SCADA anomalies.
- Learn physical invariants and flag residual anomalies in sensor data.
- Trace multi-stage attack chains across IT, OT, and physical layers.
- Plan safe fallback and recovery actions for compromised processes.

## Steps

1. Ingest network and process sensor data from a CPS dataset or testbed.
2. Encode physical invariants and known safe states as features.
3. Train an anomaly or sequence model to detect attacks and process faults.
4. Validate on labeled CPS datasets such as SWaT or WADI.
5. Define and test safe fallback procedures before automated response.

## Code pattern

```python
import numpy as np
from scipy.stats import zscore

# Detect physical-process anomalies from normalized sensor residuals
residuals = y_true - y_predicted
flags = np.abs(zscore(residuals)) > 3.5
```

## Tuning notes

- Model both network and physical behavior; attackers may hide in one
  layer while affecting the other.
- Use physics-aware features and known invariants to reduce false positives.
- Validate against labeled ICS/CPS datasets such as SWaT or WADI.
- Plan safe fallback procedures before deploying automated responses.

## Verification

1. Run an anomaly detector on a labeled CPS dataset and report F1 and FPR.
2. Identify a multi-stage attack chain using process and network logs.
3. Verify that a control fallback keeps the process within safe limits.

## References

- https://arxiv.org/abs/2411.10918
- https://arxiv.org/abs/2607.05989
- https://arxiv.org/abs/2603.16588v1
- https://arxiv.org/abs/2507.14387
- https://arxiv.org/abs/2603.10676v2
