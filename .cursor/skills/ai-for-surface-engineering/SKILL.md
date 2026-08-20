# AI for Surface Engineering

## Description

Machine learning for surface modification processes: thermal spray, laser cladding/peening, shot peening, plasma electrolytic oxidation, surface texturing, and residual stress optimization.

## When to use

You are modifying a component's surface to improve wear, fatigue, or corrosion resistance, and need to optimize thermal spray, laser surface treatment, peening, or surface texturing parameters and predict surface integrity.

## Key concepts

- **Thermal spraying**: HVOF, HVAF, plasma spray, cold spray, and coating microstructure/property prediction.
- **Laser surface treatments**: laser cladding, shock peening, texturing, and surface alloying.
- **Mechanical surface enhancement**: shot peening, laser peening, and deep rolling for residual stress.
- **Surface integrity metrics**: roughness, hardness, residual stress, coating thickness, and adhesion.
- **Functional surfaces**: texture, wettability, friction, and fatigue life optimization.

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
