# AI for Predictive Quality

## Description

In-process quality forecasting, virtual metrology, and causal quality models that predict final part quality from machine and sensor data before completion.

## When to use

You want to predict whether a part or batch will meet quality specifications while it is still in process, enabling early rework, scrap, or process adjustment.

## Usage

- **Virtual metrology (VM)**: estimate wafer or part properties from process sensor data without physical measurement.
- **In-situ quality prediction**: use tool-level data to forecast dimensional, mechanical, or electrical outcomes.
- **Causal quality models**: identify which process parameters causally drive quality variation.
- **Transfer learning**: adapt a quality model across recipes, tools, or factories.
- **Online updating**: refresh models with new metrology samples to handle drift.

## Steps

1. Collect tool sensor data and corresponding quality metrology aligned by part/batch.
2. Build a regression or classification model for the target quality characteristic.
3. Validate predictions on hold-out wafers or parts using time-aware splits.
4. Use feature attribution or causal analysis to identify controllable drivers.
5. Deploy inline and update the model as recipes or tools change.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingRegressor

# In-process quality prediction from tool sensor features
X = df[["power", "pressure", "duration", "gas_flow", "chuck_temp"]]
y = df["critical_dimension"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Ensure sensor data are sampled before the quality measurement to avoid target leakage.
- Use physics-aware features and recipe context to improve generalization.
- Track model drift as tools, consumables, and recipes change; retrain with active learning.

## Verification

1. Build a virtual metrology model and compare RMSE to actual metrology on hold-out wafers.
2. Predict scrap vs. good parts before final test and measure early rejection accuracy.
3. Validate causal drivers through a designed experiment or sensitivity analysis.

## References

- https://iopscience.iop.org/article/10.1088/1361-6501/adb05a
- https://link.springer.com/article/10.1007/s40962-025-01702-8
- https://www.mdpi.com/2227-9717/10/10/1966
- https://www.mdpi.com/2227-9717/13/4/962
- https://doi.org/10.1109/tsm.2017.2787550
