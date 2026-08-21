# AI for Industrial Engineering

## Description

Use AI to optimize production scheduling, quality control, and supply chains.

## When to use

You are optimizing production, scheduling jobs, controlling quality, balancing assembly lines, or improving supply-chain operations.

## Usage

- Predict job-shop bottlenecks and optimize schedules with OR-Tools.
- Detect process mining patterns and inefficiencies (ProM, Celonis).
- Forecast demand and inventory levels across the supply chain.
- Predict defect risk in manufacturing with SPC and vision.
- Optimize workstation ergonomics and labor allocation.

## Steps

1. Map the production process and data sources (ERP, MES, IoT).
2. Extract features for throughput, quality, and resource utilization.
3. Train scheduling, forecasting, or classification models.
4. Deploy into APS, MES, or planning dashboards.
5. Measure KPIs and retrain on new production runs.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict a quality metric from process parameters
X = df[["temperature", "pressure", "cycle_time", "operator_shift"]]
y = df["defect_rate"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Use chronological splits and respect production constraints.
- Balance throughput, quality, and energy objectives.
- Integrate AI with MES, ERP, and IoT data for real-world impact.

## Verification

1. Build a predictive quality model and compare to an SPC control chart.
2. Schedule a small job shop and compare makespan to a rule-based schedule.
3. Detect a bottleneck from process-mining event logs.

## References

- https://doi.org/10.1016/j.cie.2023.109662
- https://doi.org/10.1016/j.cirp.2024.04.101
- https://dl.acm.org/doi/10.1145/3800000.3800162
- https://doi.org/10.46254/gc03.20250318
