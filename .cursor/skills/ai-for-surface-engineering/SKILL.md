# AI for Surface Engineering

## Description

Use machine learning to optimize surface treatments such as thermal spray, laser cladding and shot peening while predicting residual stress and coating adhesion as well as wear resistance.

## When to use

You are modifying a component's surface to improve wear, fatigue, or corrosion resistance, and need to optimize thermal spray, laser surface treatment, peening, or surface texturing parameters and predict surface integrity.

## Usage

- **Predict residual stress**: model peening, cladding, and thermal spray stress fields.
- **Optimize spray parameters**: tune gas flow, standoff, and powder feed for coating quality.
- **Select processes**: match surface treatments to wear, corrosion, and fatigue requirements.
- **Detect defects**: identify porosity, delamination, and cracks in coatings.
- **Build process-property maps**: link parameters to hardness, adhesion, and microstructure.

## Steps

1. Collect process parameters and post-treatment measurements for the surface process.
2. Train surrogate models to predict residual stress, coating thickness, and properties.
3. Use the models to optimize parameters and reduce DOE cost.
4. Validate predicted residual stress and microstructure with XRD, microscopy, or mechanical tests.
5. Inspect coatings for porosity, adhesion, and defects and feed results back.
6. Deploy optimized recipes and monitor for process drift.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor

# Predict residual stress from peening or spray parameters
X = df[["laser_power_W", "spot_size_mm", "pulse_duration_ns", "overlap_pct", "material_yield_MPa"]]
y = df["surface_residual_stress_MPa"]
model = GradientBoostingRegressor(random_state=42).fit(X, y)
```

## Tuning notes

- Surface engineering datasets are small and expensive; use Gaussian processes or physics-informed models.
- Process parameters couple strongly with material and powder/particle properties.
- Residual stress and roughness depend on measurement method and location; standardize them.
- Validate microstructure and mechanical performance with cross-sectional microscopy and fatigue tests.

## Verification

1. Predict coating thickness or porosity from spray parameters and compare to SEM analysis.
2. Optimize shot peening parameters to reach a target residual stress profile.
3. Predict surface roughness after laser texturing and compare to profilometry.

## References

- https://doi.org/10.1007/s44251-025-00113-5
- https://doi.org/10.1007/s11666-026-02258-7
- https://doi.org/10.1088/2053-1591/ad1a7f
- https://www.mdpi.com/2076-3417/11/7/2888
- https://doi.org/10.1007/s00339-026-09601-3
