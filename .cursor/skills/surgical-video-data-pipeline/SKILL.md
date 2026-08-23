---
name: surgical-video-data-pipeline
description: >-
  Cholec80 / CholecTrack20 data pipeline: frame extraction, smoke stratification,
  leak-free splits, dataloader patterns for TDV pretrain and MOT.
---

## Surgical Video Data Pipeline

### Sources
- Cholec80 for pretraining (long procedures).
- CholecTrack20 for MOT (tool annotations on selected videos).

### Leak policy (enforced)
See `data-management` and `surgical-mot-eval`. Never let CT20 test overlap videos into pretrain corpora used for the reported pipeline.

### Smoke stratification
Many evals stratify by smoke level (none / light / heavy) because smoke heavily impacts detection/tracking.

### Dataloaders
- TorchCodec or PyAV for decode (FFmpeg 6.x on the env).
- Frame sampling: consecutive for TDV (num_frames=4 typical); stride for longer context.
- Strong augmentation for detection; lighter for pretrain.

Related: `data-management`, `tdv-pretrain`, `mot-training-workflow`.
