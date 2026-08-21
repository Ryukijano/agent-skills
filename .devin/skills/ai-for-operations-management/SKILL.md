# AI for Operations Management

## Description

Use AI to optimize business processes, improve service levels, monitor quality, or augmenting operational decisions with data and AI.

## When to use

You are optimizing business processes, improving service levels, monitoring quality, or augmenting operational decisions with data and AI.

## Usage

- Reconstruct workflows from event logs.
- Forecast demand, capacity, and queues.
- Optimize staffing and scheduling.
- Deploy quality and anomaly detection.

## Steps

1. Reconstruct workflows from event logs.
2. Forecast demand, capacity, and queues.
3. Optimize staffing and scheduling.
4. Deploy quality and anomaly detection.
5. Compare as-designed and as-mined process maps.
6. Deploy in client engagements, capture requirements from discovery calls, and measure time-to-insight and decision quality (Task-GenAI Fit-style).

## Code pattern

```python
import pandas as pd
from scipy.optimize import linprog

# Simple staff-allocation LP to minimize cost while meeting service levels
c = hourly_cost
A_ub = -demand_by_hour
b_ub = -service_level_requirements
result = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=(0, max_staff))
```

## Tuning notes

- Combine prediction with optimization for decision-centric value.
- Model variability and queue dynamics, not just average demand.
- Use process-mining outputs to validate assumptions before building models.
- Keep humans accountable for high-consequence operational calls.

## Verification

1. Mine a process from event logs and compare to an as-designed map.
2. Optimize staffing or inventory and measure service-level improvement.
3. Deploy an anomaly detector and validate against known quality issues.

## References

- https://arxiv.org/abs/2507.17927
- https://arxiv.org/abs/2505.13580
- https://arxiv.org/abs/2510.03310
- https://arxiv.org/pdf/2601.06061
