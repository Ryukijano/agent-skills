# AI for Satellite Imaging

## Description

Apply remote-sensing foundation models and deep learning to classify land cover, detect changes, and map disasters from satellite and aerial imagery.

## When to use

You are analyzing satellite or aerial imagery for land cover, change detection, or environmental monitoring.

## Usage

- Fine-tune remote-sensing foundation models for land-use/land-cover classification and few-shot EO tasks.
- Fuse optical, SAR, LiDAR, and hyperspectral data for robust multi-modal Earth observation.
- Detect land-cover and infrastructure changes between multi-temporal images.
- Segment and locate objects such as buildings, crops, forests, and water bodies at scale.

## Steps

1. Curate multi-temporal and multi-sensor imagery for the target region and task (classification, change, segmentation).
2. Choose a remote-sensing foundation model (e.g., SkySense++, Prithvi, SatMamba) and fine-tune it on labeled data.
3. Build a change-detection pipeline that aligns multi-temporal images and highlights altered pixels or polygons.
4. Run segmentation or object detection to map buildings, crops, forests, or water bodies and evaluate IoU/mAP.
5. Validate against ground-truth labels and cross-test generalization across geographies and seasons.
6. Deploy the pipeline for operational monitoring such as disaster response, urban growth, or agricultural surveys.

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
