# AI for Viticulture

## Description

Improve grape quality, yield, and disease management with vineyard AI.

## When to use

You are managing a vineyard and want to monitor vine health, detect diseases, estimate yield and grape quality, or optimise irrigation, fertilisation, and harvest timing.

## Usage

- Map vines, count buds, and detect diseases with Cropsy or AgScout.
- Predict yield and harvest windows from canopy and cluster data.
- Monitor virus and fungal disease risk.
- Optimize irrigation and spraying by zone.
- Track pruning and canopy development.

## Steps

1. Capture drone, tractor, or smartphone imagery by block.
2. Label vines, clusters, symptoms, and yield data.
3. Train detection, segmentation, and yield models.
4. Generate prescription maps for spray and irrigation.
5. Validate with harvest weights and lab analysis.

## Code pattern

```python
import numpy as np

red = image[..., 2]   # red band
nir = image[..., 3]   # near-infrared band
ndvi = (nir - red) / (nir + red + 1e-8)
```

## Tuning notes

- Capture vineyard spatial heterogeneity (soil, slope, aspect, cultivar, age).
- Use multi-year data to separate seasonal effects from management effects.
- Calibrate maturity and quality models with laboratory measurements.
- Integrate with existing winegrowing practices and sustainability goals.

## Verification

1. Detect downy mildew or leafroll and compare to vineyard scouting.
2. Estimate yield per vine and compare to harvest weights.
3. Predict grape sugar and acidity and validate with lab results.

## References

- https://doi.org/10.1111/1541-4337.70523
- https://doi.org/10.3390/horticulturae12060719
- https://doi.org/10.1016/j.aiia.2025.08.001
- https://www.mdpi.com/2076-3417/14/22/10277
