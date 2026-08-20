# AI for Demand Response

## Description

Machine learning for load flexibility estimation, demand response program design, virtual power plant dispatch, and dynamic pricing.

## When to use

You need to unlock flexible load, operate a virtual power plant, design demand-response programs, or optimize time-varying tariffs.

## Usage

- **Baseline load estimation**: estimate counterfactual consumption for settlement.
- **Virtual power plant dispatch**: aggregate and control distributed flexible resources.
- **Dynamic pricing and tariffs**: optimize time-of-use or real-time prices.
- **Customer segmentation and targeting**: enroll and nudge the most flexible participants.

## Steps

1. Collect AMI, thermostat, EV, and building energy data with timestamps.
2. Identify flexible loads and estimate counterfactual baselines.
3. Train forecasting, classification, or reinforcement learning models.
4. Validate on randomized pilots or natural experiments.
5. Deploy dispatch and pricing signals with feedback and telemetry.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Estimate flexible capacity from historical load and weather
X = df[["hour", "temperature", "baseline_load", "tariff"]]
y = df["flexible_load"]

model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Control for weather, occupancy, and economic confounders in baseline estimation.
- Use causal estimators when evaluating demand-response effects.
- Provide customer comfort and fairness constraints in automated control.

## Verification

1. Compare predicted baseline to a control group or weather-normalized baseline.
2. Run a DR event and measure actual vs. predicted load curtailment.
3. Backtest a VPP dispatch policy in a distribution system simulator.

## References

- https://www.mdpi.com/1996-1073/19/4/1084
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0339606
- https://www.mdpi.com/1996-1073/18/23/6341
- https://www.mdpi.com/1996-1073/18/18/4844

## References

- https://www.mdpi.com/1996-1073/19/4/1084
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0339606
- https://www.mdpi.com/1996-1073/18/23/6341
- https://www.mdpi.com/1996-1073/18/18/4844
