---
name: vjepa-physics-world-model
description: V-JEPA and adaptive world model skills for intuitive physics understanding from video, including AdaJEPA, LeJEPA, and hierarchical latent world models. Core to DINO-Endo and surgical phase recognition research.
---

# V-JEPA Physics World Model

## Overview
V-JEPA (Video Joint Embedding Predictive Architecture) learns world models by predicting representations of future video patches, enabling emergent intuitive physics without explicit supervision.

## Key Papers (2025-2026)
- **Intuitive Physics from SSL** (Quentin Garrido, Meta): V-JEPA spontaneously learns object permanence, gravity, support relations from natural videos
- **AdaJEPA** (agenticlearning.ai/adajepa): Adaptive latent world model with dynamic context length
- **LeJEPA Identifiability** (klindtlab): Theoretical identifiability of JEPA latent representations
- **Hierarchical World Models (HWM)**: Planning with latent world models for long-horizon tasks
- **SLS-WM** (github.com/Tariolle/sls-wm): Structured Label Smoothing for discrete JEPA world models

## Application to Surgical Video (DINO-Endo)
```python
# Fine-tune V-JEPA2 for surgical phase recognition
from vjepa2 import VJEPA2Encoder
encoder = VJEPA2Encoder.from_pretrained('facebook/vjepa2-vitl')
# Extract spatiotemporal tokens for phase classification
tokens = encoder(surgical_video_clip)  # [B, T, N, D]
phase_logits = phase_head(tokens.mean(dim=(1,2)))
```

## Training Tips
- Use 16 frames at 256x256 for pretraining; scale to 64 frames for fine-tuning
- 3D-RoPE positional embeddings handle variable resolutions
- Progressive resolution scaling: train short sequences first
- Causal assumption (TDV): past predicts future representations

## Integration with HPC
- Use DGX Spark / H100 for V-JEPA2 pretraining
- SLURM array jobs for multi-scale evaluation
- Store embeddings in HDF5 for downstream probing tasks

## Related Skills
- `dgx-spark-cosmos3` — DGX Spark training environment
- `tdv-pretrain` — TDV pretraining on surgical video
- `3d-reconstruction-best-practices` — 3D reconstruction from endoscopic video

## Key References
- arXiv (Quentin Garrido): Intuitive physics from V-JEPA self-supervised learning
- agenticlearning.ai/adajepa (AdaJEPA adaptive world model)
- github.com/Tariolle/sls-wm (discrete world models)
- kevinghst.github.io/HWM (hierarchical planning)
