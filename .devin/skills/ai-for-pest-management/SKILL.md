# AI for Pest Management

## Description

Detect and count insect pests with smart traps, pheromones, and computer vision.

## When to use

You need to detect, identify, count, or forecast insect pests to inform scouting, traps, biological control, or pesticide application decisions.

## Usage

- Deploy smart traps with YOLO-Evo, Yolo-pest, or YOLOv9-TrapPest.
- Monitor pest dynamics and degree-day models.
- Predict outbreak risk from weather and trap counts.
- Target spraying with IPM thresholds.
- Build georeferenced pest maps.

## Steps

1. Deploy pheromone traps with cameras and IoT.
2. Collect images and count labels across locations.
3. Train detection and counting models.
4. Integrate with weather and degree-day predictions.
5. Validate against manual scouting and treatment outcomes.

## Code pattern

```python
from ultralytics import YOLO

model = YOLO("yolov8n-cls.pt")
model.train(data="pest_images", epochs=50, imgsz=224)
```

## Tuning notes

- Many pest species are rare and visually similar; use transfer learning and taxonomic experts.
- Avoid harming beneficial insects and pollinators in model training and deployment.
- Pest populations are dynamic; refresh models and thresholds by season and region.
- Combine economic thresholds with model confidence for decision support.

## Verification

1. Report precision and recall for pest detection on field-collected images.
2. Compare model-based trap counts to manual counts.
3. Evaluate spray-timing recommendations against a scouting-only baseline.

## References

- https://www.mdpi.com/2073-4395/15/7/1629
- https://resjournals.onlinelibrary.wiley.com/doi/10.1111/afe.12630
- https://www.sciencedirect.com/science/article/abs/pii/S1161030126000596
- https://doi.org/10.22271/27889289.2026.v6.i3a.259
