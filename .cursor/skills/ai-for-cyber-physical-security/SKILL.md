# AI for Cyber-Physical Security

## Description

Securing industrial control systems, SCADA anomaly detection, physical invariants, and cross-layer intrusion detection.

## When to use

You are protecting power, water, manufacturing, or transport systems
where IT, OT, and physical processes must be defended together.

## Key concepts

- **ICS/SCADA security**: network and process telemetry monitoring.
- **Anomaly detection with invariants**: learning normal physical and
  logical relationships in sensor data.
- **Attack detection and attribution**: multi-stage cyber-physical
  attack chains and provenance analysis.
- **Resilient control**: safe fallback and recovery for compromised
  processes.
- **Digital twins**: simulation-based stress testing and response
  planning.

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

- https://arxiv.org/html/2411.10918
- https://arxiv.org/html/2607.05989
- https://arxiv.org/abs/2603.16588v1
- https://arxiv.org/html/2507.14387
- https://arxiv.org/html/2603.10676v2
