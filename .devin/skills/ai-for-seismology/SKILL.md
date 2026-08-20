# AI for Seismology

## Description

Machine learning for earthquake detection, phase picking, denoising, and seismic signal classification.

## When to use

You are processing seismic waveforms for earthquake monitoring, exploration geophysics, or event classification.

## Key concepts

- **Phase picking**: detect P- and S-wave arrivals automatically.
- **Event detection/classification**: distinguish earthquakes, explosions, quarry blasts, and noise.
- **Denoising and denoising autoencoders**: suppress cultural and environmental noise.
- **CataLog building**: ML-enhanced seismic catalogs from continuous data.

## Code pattern

```python
import seisbench

# Load a pretrained phase-picking model
picker = seisbench.models.PhaseNet.from_pretrained("instance")
annotations = picker.annotate(stream)
```

## Tuning notes

- Annotate with domain-specific data; transfer from pretrained models helps.
- Pay attention to non-stationary noise and station-specific effects.
- Validate detections against an expert-reviewed catalog.

## Verification

1. Pick phases on a small continuous seismic stream.
2. Compare picks to a reference catalog and compute residuals.
3. Run a detection model on noisy data and report precision/recall.

## References

- https://arxiv.org/abs/2603.17855
- https://seisbench.gempa.de/
- https://doi.org/10.1146/annurev-earth-071822-100323
- https://github.com/seisbench/seisbench
