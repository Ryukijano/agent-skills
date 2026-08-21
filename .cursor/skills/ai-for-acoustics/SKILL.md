# AI for Acoustics

## Description

Use machine learning to localize sources, classify bioacoustic events, monitor structural health, and model spatial sound fields.

## When to use

You are analyzing acoustic recordings, localizing sources, classifying animal calls, or predicting sound fields.

## Usage

- Localize sound sources from microphone arrays using TDOA and beamforming features.
- Classify animal calls, marine mammals, and environmental sound events.
- Detect cracks and corrosion via acoustic emission and guided-wave analysis.
- Reconstruct room impulse responses and spatial audio scenes.

## Steps

1. Capture and time-synchronize multichannel audio or acoustic-emission waveforms.
2. Compute spectrograms, mel features, or TDOA embeddings matched to the signal of interest.
3. Train a classifier, localizer, or inverse model with physics-informed augmentations.
4. Validate against ground-truth labels or known source positions.
5. Deploy for real-time structural monitoring or ecological field surveys.

## Code pattern

```python
import librosa

# Load audio and compute a mel spectrogram
y, sr = librosa.load("recording.wav", sr=16000)
spec = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=64)
spec_db = librosa.power_to_db(spec, ref=np.max)
```

## Tuning notes

- Match time-frequency resolution to the signal of interest.
- Augment with reverb, noise, and direction-of-arrival variations.
- Consider physical wave constraints and microphone array geometry.

## Verification

1. Classify environmental sound events on a labeled dataset.
2. Localize a sound source from multichannel recordings.
3. Reconstruct a room impulse response from sparse measurements.

## References

- https://doi.org/10.1038/s44384-025-00021-w
- https://arxiv.org/abs/1905.04418
- https://arxiv.org/abs/2504.16289
- https://arxiv.org/abs/2508.21470
