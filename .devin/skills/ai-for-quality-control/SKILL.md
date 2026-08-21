# AI for Quality Control

## Description

Use machine learning and computer vision to inspect products, detect defects, monitor process stability, and move toward zero-defect manufacturing.

## When to use

You are automating visual inspection, detecting product defects, monitoring process stability, or building zero-defect manufacturing systems.

## Usage

- Classify and segment scratches, dents, and contamination from production images.
- Track control charts and process capability for drift and out-of-control points.
- Detect novel defects with unsupervised or few-shot anomaly models.
- Deploy real-time inspection on cameras and PLCs at the edge.

## Steps

1. Collect nominal and defect images from real production, not just clean labs.
2. Balance the dataset with augmentation, weighted loss, or anomaly methods.
3. Train and calibrate a classifier or segmentation model for false-accept/reject trade-offs.
4. Validate on a hold-out production sample with operator review.
5. Deploy at the edge and monitor drift over shifts and suppliers.

## Code pattern

```python
import torch
import torchvision.models as models

# Fine-tune a ResNet for binary defect classification
model = models.resnet18(pretrained=True)
model.fc = torch.nn.Linear(model.fc.in_features, 2)
# dataloader = DataLoader(...)  # nominal vs defect images
```

## Tuning notes

- Defect datasets are highly imbalanced; use augmentation, weighted loss, or anomaly detection.
- Optimize for both false-accept and false-reject rates based on business cost.
- Calibrate inspection systems on real production samples, not only clean lab images.

## Verification

1. Train a defect classifier on an industrial image dataset and measure precision/recall.
2. Build an SPC dashboard and flag out-of-control points in a process time series.
3. Compare an unsupervised anomaly model to supervised training with few labels.

## References

- https://link.springer.com/article/10.1007/s44245-026-00320-w
- https://www.mitutoyo.com/aiinspect/
- https://roboflow.com/ai/quality-control
- https://doi.org/10.3390/app16010037
