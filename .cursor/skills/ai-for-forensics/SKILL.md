# AI for Digital Forensics

## Description

ML for image authentication, deepfake detection, authorship attribution, and anomaly detection in forensic evidence.

## When to use

You are verifying digital evidence, detecting synthetic media, or attributing authorship.

## Key concepts

- **Deepfake detection**: identify GAN or diffusion-generated images, audio, video.
- **Image forgery detection**: copy-move, splicing, and manipulation traces.
- **Authorship attribution**: stylometry and behavioral biometrics.
- **Anomaly detection**: identify unusual patterns in logs or network traffic.

## Code pattern

```python
from transformers import AutoModelForImageClassification, AutoImageProcessor

processor = AutoImageProcessor.from_pretrained("prithivMLmods/Deepfake-vs-Real-8000")
model = AutoModelForImageClassification.from_pretrained("prithivMLmods/Deepfake-vs-Real-8000")
```

## Tuning notes

- Adversarial generators evolve quickly; use ensemble and metadata checks.
- Report confidence and uncertainty; legal evidence needs transparency.
- Maintain chain of custody and avoid altering evidence.

## Verification

1. Build a deepfake detector and test on held-out generation methods.
2. Detect a copy-move forgery in an image.
3. Attribute authorship of a short text and evaluate robustness.

## References

- https://arxiv.org/abs/2404.11163
- https://github.com/grip-unina/TruFor
- https://github.com/polimi-ispl/icpr2020dfdc
- https://pages.nist.gov/frvt/
