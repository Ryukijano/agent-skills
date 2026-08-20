# AI for Fisheries

## Description

Fish stock assessment, catch forecasting, aquaculture monitoring, eDNA, and IUU fishing detection with ML.

## When to use

You are managing or studying fisheries, aquaculture, or marine ecosystems and need to predict catch, identify species, or detect illegal fishing.

## Key concepts

- **Stock assessment and catch forecasting**: relate catch or abundance to environmental and effort covariates.
- **eDNA metabarcoding**: detect species from environmental samples using sequencing and ML classifiers.
- **Acoustic and sonar surveys**: classify echograms and estimate fish biomass.
- **Aquaculture monitoring**: water quality, feeding, disease, and welfare prediction.
- **IUU detection**: analyze vessel AIS trajectories and imagery for illegal activity.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

df = pd.read_csv("fisheries_catch.csv")
X = df[["sst", "chlorophyll", "depth", "effort_hours"]]
y = df["catch_kg"]

model = GradientBoostingRegressor(n_estimators=200)
model.fit(X, y)
```

## Tuning notes

- Catch data are often zero-inflated; consider hurdle or zero-inflated models.
- Use spatial or temporal cross-validation to avoid data leakage.
- Integrate biological priors and management scenarios for decision support.
- Interpret models with SHAP to understand driver importance.

## Verification

1. Forecast catch or CPUE and compare against a surplus-production model.
2. Classify species from eDNA reads and evaluate taxonomic assignment accuracy.
3. Detect anomalous vessel tracks and compare to known IUU incident records.

## References

- https://doi.org/10.3390/bdcc10010019
- https://doi.org/10.1080/23308249.2024.2423189
- https://doi.org/10.3390/fishes10020074
- https://doi.org/10.1016/j.aquaculture.2025.743602
