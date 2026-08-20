# AI for Ecology

## Description

Species distribution modeling, habitat suitability, biodiversity monitoring, and ecological forecasting using ML and remote sensing.

## When to use

You are modeling species distributions, predicting biodiversity, or analyzing ecological communities across space and time.

## Key concepts

- **Species distribution models (SDMs)**: correlate occurrence or abundance with environmental covariates.
- **Habitat suitability**: estimate the probability of species presence under current and future conditions.
- **Acoustic and camera-trap monitoring**: automate detection and classification of vocalizations and images.
- **Occupancy and abundance models**: hierarchical models for imperfect detection.
- **Ecological forecasting**: predict phenology, migrations, and ecosystem state changes.

## Code pattern

```python
import xarray as xr
from sklearn.ensemble import GradientBoostingClassifier

# Environmental covariates from raster stack
cov = xr.open_dataset("environmental_covariates.nc")
X = cov.to_dataframe().dropna()
y = presence_absence_labels  # 1/0 at sampled locations

model = GradientBoostingClassifier(n_estimators=200)
model.fit(X, y)
```

## Tuning notes

- Use spatial cross-validation to avoid optimistic performance estimates.
- Choose background/pseudo-absence points carefully and account for sampling bias.
- Project models to future climate only within the range of training conditions.
- Interpret partial dependence and response curves for ecological plausibility.

## Verification

1. Train an SDM on presence/absence data and evaluate with spatial CV AUC-PR.
2. Generate a habitat-suitability map and compare to independent survey data.
3. Test transfer to a different region or time period and quantify extrapolation.

## References

- https://doi.org/10.1145/3460112.3471966
- https://doi.org/10.1007/s10462-024-11074-w
- https://doi.org/10.1146/annurev.ecolsys.110308.120159
- https://doi.org/10.1038/s41559-024-02435-3
