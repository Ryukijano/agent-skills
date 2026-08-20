# AI for Viticulture

## Description

AI for vineyard monitoring, grape and canopy sensing, disease detection, yield and quality prediction, and harvest decision support.

## When to use

You are managing a vineyard and want to monitor vine health, detect diseases, estimate yield and grape quality, or optimise irrigation, fertilisation, and harvest timing.

## Usage

- **Canopy and berry detection**: locate and count grape bunches from images and point clouds.
- **Disease and pest monitoring**: detect powdery mildew, downy mildew, and grapevine pests.
- **Yield and quality prediction**: forecast grape quantity and maturity (sugar, acidity).
- **Irrigation, fertilisation, and harvest scheduling**: support precision management and winery logistics.

## Steps

1. Collect drone, satellite, or proximal sensing data across vineyard blocks.
2. Gather weather, soil, and phenology records and link them to management zones.
3. Train detection and regression models for the specific grape variety and terroir.
4. Validate predictions at harvest and across multiple vintages.
5. Integrate outputs into vineyard management plans and winery receiving schedules.

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
