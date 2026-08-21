# AI for Defect Detection

## Description

Detects surface, assembly, and component defects with computer vision and anomaly segmentation.

## When to use

You need to replace or augment manual inspection by automatically detecting scratches, dents, contamination, missing components, or dimensional deviations in production.

## Usage

- **Supervised defect classification**: CNNs and vision transformers trained on labeled defect images.
- **Anomaly detection**: train on good samples and flag deviations with autoencoders, feature distance, or PatchCore.
- **Segmentation**: pixel-level defect localization for repair or scrap decisions.
- **Semi-supervised and few-shot learning**: reduce labeling cost with synthetic or weak labels, or with foundation models such as CLIP and Amazon Nova Pro.
- **Edge deployment**: run inspection models on factory cameras or PLC vision systems.

## Steps

1. Collect and label defect and nominal images from production.
2. Choose a supervised, anomaly, or segmentation approach based on label availability.
3. Train and validate the model with appropriate metrics for false-accept and false-reject.
4. Optimize latency and deploy on the target camera or edge device.
5. Monitor performance and retrain when new defect modes appear.

## Code pattern

```python
from anomalib.models import Patchcore
from anomalib.data import MVTec

# Train an anomaly detector on nominal images
model = Patchcore(backbone="wide_resnet_50_2")
datamodule = MVTec(category="bottle")
```

## Tuning notes

- Balance false-accept and false-reject rates based on downstream cost.
- Use augmentations, synthetic defects, and domain randomization to improve generalization.
- Calibrate on real production samples; lab images may not match lighting and texture.

## Verification

1. Train a defect classifier and report precision/recall on a held-out production set.
2. Compare an anomaly model to a supervised baseline when labels are scarce.
3. Measure inference latency on the target camera or edge device.

## References

- https://www.mdpi.com/2076-3417/14/15/6774
- https://link.springer.com/article/10.1007/s10845-025-02680-8
- https://www.nature.com/articles/s41598-026-54269-7
- https://www.mdpi.com/1424-8220/26/4/1085
- https://www.sciencedirect.com/science/article/abs/pii/S0957417426002277
