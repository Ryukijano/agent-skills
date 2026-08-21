# AI for Composites

## Description

Apply ML to design composites, optimize manufacturing, detect defects, and predict multiscale mechanical and thermal properties.

## When to use

You are engineering fiber-reinforced, polymer-matrix, metal-matrix, or ceramic-matrix composites and need to predict or optimize mechanical, thermal, or processing behavior.

## Usage

- Link microstructure features (fiber orientation, volume fraction, voids) to stiffness, strength, and toughness.
- Detect delaminations, voids, and fiber waviness from ultrasonic, X-ray, and thermography data.
- Optimize resin infusion, automated fiber placement, curing, and consolidation parameters.
- Build multiscale surrogates and inverse-design tools for tailored anisotropic composite properties.

## Steps

1. Collect composite microstructure images, NDE data, manufacturing parameters, and mechanical/thermal test results.
2. Extract microstructural features and train models to predict stiffness, strength, toughness, or thermal conductivity.
3. Train defect-detection classifiers/segmenters on NDE images and validate against destructive inspection.
4. Optimize manufacturing parameters (temperature, pressure, feed rate) using Bayesian or physics-informed methods.
5. Build multiscale or FE surrogates and use them for rapid design-space exploration.
6. Validate predicted properties and process settings with mechanical tests and quality inspections.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

df = pd.read_csv("composites.csv")  # fiber, matrix, vf, void, process
X = df[["fiber_volume_fraction", "void_fraction", "cure_temp_C"]]
y = df["tensile_strength_MPa"]
model = RandomForestRegressor().fit(X, y)
```

## Tuning notes

- Composite data are highly process-dependent; include manufacturing parameters, not just composition.
- Anisotropy and damage evolution require direction-specific features and possibly recurrent or graph models.
- Use non-destructive evaluation data to augment sparse mechanical test datasets.

## Verification

1. Predict a mechanical property (tensile/flexural/modulus) and validate against a test standard.
2. Detect defects in composite NDE images and compare to ground-truth destructive inspection.
3. Optimize an automated fiber placement or curing process and measure the resulting part quality.

## References

- https://link.springer.com/article/10.1007/s10443-025-10415-4
- https://doi.org/10.1002/pc.71029
- https://doi.org/10.1016/j.compositesb.2026.113658
- https://pubs.rsc.org/en/content/articlelanding/2025/ta/d5ta00982k
- https://accscience.com/journal/IJAMD/2/3/10.36922/IJAMD025210016
