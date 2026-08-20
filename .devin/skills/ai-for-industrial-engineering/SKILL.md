# AI for Industrial Engineering

## Description

AI for production planning, scheduling, quality control, ergonomics, operations research, and process improvement.

## When to use

You are optimizing production, scheduling jobs, controlling quality, balancing assembly lines, or improving supply-chain operations.

## Usage

- **Production planning and scheduling**: job-shop, flow-shop, and real-time rescheduling.
- **Quality control and SPC**: defect detection, predictive quality, and root-cause analysis.
- **Operations research and optimization**: MILP, constraint programming, and heuristics.
- **Ergonomics and human factors**: motion analysis, workload, and safety.
- **Digital lean and process mining**: bottleneck detection and value-stream analysis.

## Steps

1. Collect MES/ERP/IoT data on production, quality, maintenance, and schedules.
2. Engineer features for throughput, quality, and resource utilization.
3. Train scheduling, quality, or maintenance optimization models.
4. Validate against baseline KPIs and constraints in simulation.
5. Deploy and retrain with live production feedback.

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
