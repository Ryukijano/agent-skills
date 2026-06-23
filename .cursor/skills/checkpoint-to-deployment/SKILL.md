---
name: checkpoint-to-deployment
description: How to extract clean, reproducible deployment weights from training checkpoints (strip optimizer/EMA/SSL heads, document provenance). Companion to /checkpoint-to-deployment.
---

## Checkpoint to Deployment Knowledge

### What to keep vs strip
- Keep: model weights for inference path.
- Strip: optimizer state, EMA shadow, scaler state, training history unless you have a reason.
- For encoders: filter to the backbone/encoder submodule only.

### Provenance required in DEPLOYMENT.md
- Git commit + training step + best val metric at extraction.
- Backbone size, LoRA rank (if any), data splits used.
- Preprocessing (resolution, normalization).
- How to load + expected input/output.

### Verification
Fresh model load + dummy forward must succeed with no missing/unexpected keys that matter.

Related: `reproducibility`, `tdv-pretrain`, `surgical-mot-eval`, `paper-code-release`.
