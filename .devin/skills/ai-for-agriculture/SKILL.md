# AI for Agriculture

## Description

Crop monitoring, yield prediction, pest detection, and precision agriculture with ML and remote sensing.

## When to use

You are monitoring crops, predicting yields, detecting disease, or managing irrigation and nutrients.

## Key concepts

- **Crop classification and mapping**: from satellite or drone imagery.
- **Yield prediction**: combine weather, soil, and remote-sensing features.
- **Pest and disease detection**: computer vision on leaf and field images.
- **Precision agriculture**: variable-rate input recommendations.

## Code pattern

```python
from torchvision.models import resnet18
import torch

model = resnet18(pretrained=True)
# Replace the final layer for crop-disease classification
model.fc = torch.nn.Linear(model.fc.in_features, num_classes)
```

## Tuning notes

- Season and region dominate; use domain-adaptation or fine-tuning.
- Ground-truth data is expensive; use weak and semi-supervised learning.
- Consider environmental and economic impact in deployment.

## Verification

1. Classify crop types from Sentinel-2 time series.
2. Predict yield for a small region and compare to reported values.
3. Detect a plant disease from leaf images with a small model.

## References

- https://github.com/Project-Platypus/Rivanna
- https://arxiv.org/abs/2403.01724
- https://torchgeo.readthedocs.io/
- https://cropmonitor.org/
