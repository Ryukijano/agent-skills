# AI for Additive Manufacturing

## Description

Machine learning for powder-bed fusion, directed energy deposition, in-situ monitoring, defect detection, build simulation, and process parameter optimization in additive manufacturing.

## When to use

You are optimizing metal or polymer additive manufacturing processes, predicting part quality from build parameters, detecting defects from in-situ sensor data, or training surrogate models for residual stress and distortion.

## Key concepts

- **Process parameter mapping**: laser power, scan speed, hatch spacing, layer thickness, and energy density windows.
- **In-situ sensing**: melt-pool images, photodiodes, thermal cameras, acoustic emission, and spatter monitoring.
- **Defect classification**: porosity, lack of fusion, balling, keyholing, and crack detection from image or time-series data.
- **Build planning**: support design, orientation, scan strategy, and thermal history effects on microstructure.
- **Digital twins and surrogate models**: fast prediction of distortion, residual stress, and mechanical properties.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier

# Predict porosity class from PBF process features
X = df[["laser_power_W", "scan_speed_mm_s", "hatch_spacing_mm", "layer_thickness_mm"]]
y = df["porosity_class"]  # none / low / high
model = GradientBoostingClassifier(random_state=42).fit(X, y)
```

## Tuning notes

- Include physically meaningful features such as energy density and normalized enthalpy.
- In-situ data are high-rate and high-volume; downsample or window before model training.
- Class imbalance is common for defects; use stratified sampling, class weights, or anomaly detection.
- Validate across different machines, powder lots, and build geometries to check generalization.

## Verification

1. Train a defect classifier on melt-pool images and compare precision-recall per defect type.
2. Predict relative density from process parameters and compare to Archimedes or X-ray measurements.
3. Build a surrogate for distortion and validate against a full thermomechanical simulation.

## References

- https://doi.org/10.1007/s10845-024-02490-4
- https://www.sciencedirect.com/science/article/pii/S2588840424000933
- https://www.sciencedirect.com/science/article/abs/pii/S1526612523005212
- https://www.sciencedirect.com/science/article/abs/pii/S1526612526003907
- https://doi.org/10.1080/17452759.2023.2196266
