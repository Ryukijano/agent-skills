# AI for Seismology

## Description

Use deep-learning models to detect, pick, classify, and denoise seismic events from continuous waveform data for earthquake monitoring and catalog building.

## When to use

You are processing seismic waveforms for earthquake monitoring, exploration geophysics, or event classification.

## Usage

- Detect and pick P- and S-wave arrivals automatically in continuous seismic streams.
- Classify earthquakes, explosions, quarry blasts, and cultural noise in near real time.
- Suppress non-stationary environmental and cultural noise to recover low-amplitude signals.
- Build ML-enhanced seismic catalogs by associating picks and locating events across networks.

## Steps

1. Ingest and preprocess continuous waveform data (response removal, filtering, resampling) from a seismic network.
2. Run a pretrained deep-learning picker (e.g., PhaseNet, EQTransformer) to detect P/S arrivals and event windows.
3. Associate picks across stations using a travel-time or ML-based associator (e.g., GaMMA) and locate events.
4. Classify events by source type and denoise signals with autoencoders or adaptive filtering if needed.
5. Build a catalog, compare picks and locations to a reference catalog, and compute residuals and precision/recall.
6. Deploy the pipeline for near-real-time monitoring or mine archived data to find previously missed events.

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
- https://seisbench.readthedocs.io/en/latest/
- https://doi.org/10.1146/annurev-earth-071822-100323
- https://github.com/seisbench/seisbench
