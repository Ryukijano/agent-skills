---
name: checkpoint-to-deployment
description: Convert a training checkpoint to deployment-ready format by stripping training-only state. Use when preparing models for inference, extracting encoder weights, or cleaning checkpoints for release.
---

## Checkpoint to Deployment

### Steps

1. Load checkpoint: `ckpt = torch.load('outputs/<run>/best.pth.tar')`
2. Strip training-only keys: remove optimizer state, EMA teacher, DINO/iBOT heads, motion encoder
3. Save clean state dict: `torch.save(clean_sd, 'outputs/<run>/deployment.pth')`
4. Extract encoder only: filter keys starting with `frame_encoder.encoder.`
5. Verify: load into fresh model, check missing/unexpected keys
6. Run inference test: `model.eval(); output = model(dummy_input)`
7. Document: training step, val metrics, architecture, data, preprocessing
