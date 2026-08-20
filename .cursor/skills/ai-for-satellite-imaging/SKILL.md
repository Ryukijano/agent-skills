# AI for Satellite Imaging

## Description

Earth observation foundation models, land-use classification, change detection, and disaster mapping.

## When to use

You are analyzing satellite or aerial imagery for land cover, change detection, or environmental monitoring.

## Key concepts

- **Remote sensing foundation models**: pretrained backbones for EO imagery.
- **Multi-modal fusion**: optical, SAR, LiDAR, and hyperspectral sensors.
- **Change detection**: identify changes between multi-temporal images.
- **Segmentation and object detection**: buildings, crops, forests, water bodies.

## Code pattern

```python
import torch
from torchgeo.models import resnet50

# Load a pretrained remote-sensing model and fine-tune on your data
model = resnet50(pretrained=True)
features = model(image)
```

## Tuning notes

- Use sensors appropriate for the task and region (cloud cover, resolution).
- Augment with rotation, scaling, and radiometric jitter specific to EO.
- Be cautious about geospatial data drift across regions and seasons.

## Verification

1. Fine-tune a foundation model on a land-cover classification dataset.
2. Run change detection between two satellite images and compare to labels.
3. Evaluate zero-shot transfer to a different geography.

## References

- https://www.nature.com/articles/s42256-025-01078-8
- https://github.com/zhu-xlab/Copernicus-FM
- https://github.com/gastruc/AnySat
- https://torchgeo.readthedocs.io/
