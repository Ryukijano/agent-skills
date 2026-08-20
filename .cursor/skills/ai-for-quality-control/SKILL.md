# AI for Quality Control

## Description

Machine learning and computer vision for automated inspection, defect detection, statistical process control, and zero-defect manufacturing.

## When to use

You are automating visual inspection, detecting product defects, monitoring process stability, or building zero-defect manufacturing systems.

## Key concepts

- **Machine-vision defect detection**: CNNs, transformers, and anomaly segmentation for scratches, dents, and contamination.
- **Statistical process control (SPC)**: control charts, process capability, and drift monitoring.
- **Unsupervised and few-shot learning**: training on nominal samples and detecting novel defects.
- **Edge deployment**: real-time inference on cameras and PLCs on the factory floor.

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
