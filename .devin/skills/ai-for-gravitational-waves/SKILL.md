# AI for Gravitational-Wave Astronomy

## Description

Deep learning for compact binary coalescence search, parameter estimation, and glitch classification.

## When to use

You are searching LIGO/Virgo/KAGRA data for compact binary mergers or estimating source parameters.

## Key concepts

- **Matched filtering vs deep learning**: trade-offs and hybrid pipelines.
- **Signal-to-noise time series**: deep-learning classifiers on SNR data.
- **Parameter estimation with normalizing flows**: AMPLFI, DINGO.
- **Glitch detection and mitigation**: separate non-Gaussian transients.

## Code pattern

```python
import numpy as np

# Simplified: train a 1D CNN on whitened strain snippets
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Flatten, Dense

model = Sequential([Conv1D(32, 16, activation='relu', input_shape=(4096, 1)),
                    MaxPooling1D(4), Flatten(), Dense(1, activation='sigmoid')])
```

## Tuning notes

- Data is highly imbalanced; use synthetic injections and background samples.
- Models must generalize across detector noise and hardware configurations.
- Calibrate output probabilities and report false-alarm rates.

## Verification

1. Train a detector on simulated binary black-hole waveforms.
2. Measure sensitivity at a fixed false-alarm rate.
3. Estimate chirp mass and compare to injected parameters.

## References

- https://journals.aps.org/prd/abstract/10.1103/PhysRevD.111.024035
- https://arxiv.org/abs/2501.13846
- https://a3d3.ai/a3d3-team-leads-the-first-end-to-end-machine-learning-based-real-time-search-for-binary-black-holes/
- https://github.com/alecgunny/deep-crackle
