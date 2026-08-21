# AI for Preservation

## Description

Use AI to monitor environmental conditions, predict degradation, prioritize conservation actions, or build digital twins for heritage preservation.

## When to use

You need to monitor environmental conditions, predict degradation, prioritize conservation actions, or build digital twins for heritage preservation.

## Usage

- Assess environmental and material risk factors.
- Model degradation and pest/disease spread.
- Prioritize preservation actions and budgets.
- Monitor condition changes.

## Steps

1. Assess environmental and material risk factors.
2. Model degradation and pest/disease spread.
3. Prioritize preservation actions and budgets.
4. Monitor condition changes.
5. Calibrate with conservators and preventive-conservation data.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

## Code pattern

```python
from sklearn.ensemble import GradientBoostingRegressor

# Predict a preservation risk index from environmental time series
model = GradientBoostingRegressor(random_state=42)
model.fit(X_train, y_risk)
risk_forecast = model.predict(X_future)
```

## Tuning notes

- Heritage systems are slow-moving and data-sparse; use physics-informed features and strong baselines.
- Integrate expert conservation knowledge into model design and alert thresholds.
- Respect intervention constraints; preservation models should support, not replace, conservators.

## Verification

1. Forecast microclimate conditions for a site and compare to sensor readings.
2. Detect damage in building images and map risk zones against expert surveys.
3. Build a digital twin dashboard and validate that alerts align with observed conditions.

## References

- https://doi.org/10.3390/buildings14123979
- https://www.mdpi.com/2220-9964/15/1/1
- https://www.nature.com/articles/s40494-025-02038-6
- https://link.springer.com/article/10.1007/s12065-024-00959-y
- https://doi.org/10.1088/1742-6596/3217/1/012006
