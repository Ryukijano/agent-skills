# AI for Glaciology

## Description

Glacier mapping, surface mass balance estimation, snow/ice classification, and climate-change impact assessment.

## When to use

You are delineating glacier boundaries, estimating surface mass balance, classifying ice facies, or projecting glacier change.

## Key concepts

- **Glacier segmentation**: deep learning for clean-ice, debris-covered, and snow/firn mapping.
- **Surface mass balance (SMB)**: temperature-index and machine-learning models.
- **Geodetic and glaciological data fusion**: MassBalanceMachine, OGGM, ERA5.
- **Multi-sensor inputs**: optical, SAR, DEM, and meteorological reanalysis.

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
