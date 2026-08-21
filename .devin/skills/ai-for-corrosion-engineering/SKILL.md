# AI for Corrosion Engineering

## Description

Use AI to predict corrosion rates, monitor cathodic protection, optimize materials and coatings and extend asset life for pipelines and industrial infrastructure.

## When to use

You are managing corrosion risk in infrastructure, pipelines, marine, automotive, or energy assets and need to predict corrosion rates, interpret electrochemical data, schedule inspections, select materials, or evaluate protection systems.

## Usage

- **Predict rates**: model corrosion from environment, material, coating, and operating data.
- **Monitor CP**: assess cathodic protection current, potential, and stray-current effects.
- **Estimate remaining life**: combine inspection, EIS, and thickness data.
- **Optimize materials**: select alloys, coatings, and inhibitors for the environment.
- **Plan inspections**: prioritize high-risk locations and extend in-line inspection intervals.

## Steps

1. Collect environmental, material, coating, and inspection data for the asset.
2. Train corrosion-rate or remaining-life models and validate against coupons or pull tests.
3. Integrate CP monitoring data and flag under- or over-protection conditions.
4. Map corrosion risk across the asset using a digital twin or knowledge graph.
5. Recommend materials, coatings, or inhibitors and simulate their effect.
6. Update the model with new inspections and optimize maintenance schedules.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict corrosion rate from environment and material features
X = df[["pH", "Cl_ppm", "temperature_C", "dissolved_O2_ppm", "alloy_Cr_pct"]]
y = df["corrosion_rate_mmpy"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Corrosion is highly environment- and time-dependent; include exposure duration and test standards.
- Data are often sparse and imbalanced; use transfer learning from similar environments.
- EIS spectra require careful preprocessing and equivalent-circuit assumptions.
- Combine physics-based electrochemical models with ML for extrapolation reliability.

## Verification

1. Predict corrosion rate for a given environment and compare to ASTM immersion or electrochemical tests.
2. Classify EIS spectra by equivalent circuit and validate against expert fitting.
3. Forecast remaining service life of a coating or component and compare to field pull data.

## References

- https://doi.org/10.1002/maco.70127
- https://iopscience.iop.org/article/10.1149/1945-7111/aceab2
- https://www.nature.com/articles/s41598-025-18575-w
- https://doi.org/10.1007/s10791-026-10458-6
- https://doi.org/10.1038/s41529-022-00218-4
