# AI for Fisheries

## Description

Detect illegal, unreported, and unregulated fishing by fusing AIS tracks with satellite radar and vessel behavior models.

## When to use

You are managing or studying fisheries, aquaculture, or marine ecosystems and need to predict catch, identify species, or detect illegal fishing.

## Usage

- Forecast catch or abundance from environmental and effort covariates.
- Detect species from eDNA metabarcoding and sequence-classification workflows.
- Classify acoustic/sonar echograms and estimate fish biomass.
- Monitor aquaculture water quality, feeding, disease, and welfare, and detect IUU vessel activity.

## Steps

1. Ingest catch/effort, eDNA, acoustic, AIS, and environmental (SST, chlorophyll, depth) data.
2. Engineer spatial-temporal features and train a catch/CPUE forecast model, handling zero-inflation and seasonality.
3. Classify eDNA reads or metabarcoding sequences and compare taxonomic assignments to reference databases.
4. Process acoustic/sonar data to detect schools and estimate biomass, validating with trawl or visual surveys.
5. Build aquaculture monitoring models for water quality, feeding, and disease, and detect anomalous vessel trajectories for IUU activity.
6. Integrate forecasts and detections into fishery management dashboards and compare to surplus-production baselines.

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
