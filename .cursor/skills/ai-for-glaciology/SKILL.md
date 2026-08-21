# AI for Glaciology

## Description

Use AI to delineate glacier boundaries, estimating surface mass balance, classify ice facies, or project glacier change.

## When to use

You are delineating glacier boundaries, estimating surface mass balance, classifying ice facies, or projecting glacier change.

## Usage

- Fuse optical, SAR, DEM, and meteorological reanalysis.
- Segment glacier outlines (clean ice, debris, snow/firn).
- Estimate surface mass balance with point and geodetic data.
- Track area and elevation change over time.

## Steps

1. Fuse optical, SAR, DEM, and meteorological reanalysis.
2. Segment glacier outlines (clean ice, debris, snow/firn).
3. Estimate surface mass balance with point and geodetic data.
4. Track area and elevation change over time.
5. Validate against manual inventories and in-situ stakes.
6. Package results as FAIR digital twins and validate against independent field surveys and reference datasets (BioDT-style).

## Code pattern

```python
import segmentation_models_pytorch as smp

# U-Net/Transformer for glacier extent segmentation
model = smp.Unet("resnet50", in_channels=4, classes=3)
```

## Tuning notes

- Distinguish seasonal snow from glacier ice; use multi-temporal training.
- Fuse SAR and optical to improve cloud/debris-covered mapping.
- Calibrate SMB models with both point observations and geodetic mass balance.
- Use transfer learning from regional inventories to data-scarce glaciers.

## Verification

1. Segment glacier outlines and compare to manually digitized inventories.
2. Predict surface mass balance and evaluate against in-situ stakes.
3. Map debris-covered ice and quantify area change over a decade.

## References

- https://doi.org/10.1038/s41467-024-54956-x
- https://doi.org/10.5194/egusphere-egu26-11039
- https://www.sciencedirect.com/science/article/pii/S1569843222001212
- https://tc.copernicus.org/articles/19/1675/2025/
