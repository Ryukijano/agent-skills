# AI for Acoustics

## Description

Machine learning for source localization, room acoustics, bioacoustics, structural health monitoring, and spatial audio.

## When to use

You are analyzing acoustic recordings, localizing sources, classifying animal calls, or predicting sound fields.

## Key concepts

- **Spectrograms and mel features**: time-frequency representations for classification.
- **Beamforming and source separation**: multichannel spatial audio methods.
- **Room impulse responses**: reverberation and geometry inference.
- **Physics-informed acoustics**: wave-equation constraints in neural models.

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
