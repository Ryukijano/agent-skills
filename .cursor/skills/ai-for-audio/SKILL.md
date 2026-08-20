# AI for Audio

## Description

Audio enhancement, source separation, music generation, audio event detection, and speech enhancement.

## When to use

You are restoring, separating, generating, or analyzing audio for music, communications, or ambient sensing.

## Key concepts

- **Speech enhancement and denoising**: mask-based and generative approaches.
- **Source separation**: music demixing and speech separation.
- **Audio event detection and classification**: weakly supervised and transformer models.
- **Music generation**: symbolic and audio-domain diffusion and transformer models.
- **Audio super-resolution and bandwidth extension**: AERO, AEROMamba, and flow matching.

## Code pattern

```python
import torch
import torchaudio

waveform, sr = torchaudio.load("noisy.wav")
spec = torchaudio.transforms.Spectrogram(n_fft=512)(waveform)

mask = torch.sigmoid(model(spec))
enhanced = torchaudio.transforms.GriffinLim(n_fft=512)(spec * mask)
```

## Tuning notes

- Use loss functions aligned with human perception (PESQ, STOI, DNSMOS).
- Train on diverse noise and reverberation conditions.
- Avoid over-suppression of desired signals like music.
- Evaluate generalization on out-of-domain noise and speakers.

## Verification

1. Denoise speech and measure PESQ and STOI improvement over input.
2. Separate vocals from a music track and compute SDR.
3. Detect a set of audio events and compare F1 to a labeled test set.

## References

- https://arxiv.org/abs/2409.09642
- https://arxiv.org/abs/2501.15417
- https://arxiv.org/abs/2504.09381
- https://arxiv.org/abs/2502.02942
- https://arxiv.org/abs/2505.19476
