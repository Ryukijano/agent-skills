---
description: Convert a training checkpoint to deployment-ready format
---

## Checkpoint to Deployment

Convert a training checkpoint into a deployment-ready format for inference.

1. Identify the checkpoint file:
   ```bash
   ls -la outputs/<run_name>/best.pth.tar
   ```

2. Load the checkpoint and inspect its contents:
   ```python
   import torch
   ckpt = torch.load('outputs/<run_name>/best.pth.tar', map_location='cpu')
   print(f"Keys: {list(ckpt.keys())}")
   print(f"Step: {ckpt.get('step', 'N/A')}")
   print(f"Loss: {ckpt.get('loss', 'N/A')}")
   ```

3. Extract the model state dict and strip training-only keys:
   ```python
   # Remove optimizer state, EMA teacher, etc.
   model_sd = ckpt['model_state_dict']

   # If the model has EMA teacher, keep only the student/frame encoder
   clean_sd = {}
   for k, v in model_sd.items():
       if 'teacher' in k or 'ema' in k:
           continue
       if 'dino_head' in k or 'ibot_head' in k:
           continue  # Remove self-distillation heads
       if 'motion_encoder' in k:
           continue  # Remove motion encoder (not needed for inference)
       clean_sd[k] = v

   print(f"Original keys: {len(model_sd)}, Cleaned keys: {len(clean_sd)}")
   ```

4. Save the clean state dict:
   ```python
   torch.save(clean_sd, 'outputs/<run_name>/deployment.pth')
   ```

5. If extracting just the encoder for downstream tasks:
   ```python
   encoder_sd = {}
   for k, v in model_sd.items():
       if k.startswith('frame_encoder.encoder.'):
           encoder_sd[k.replace('frame_encoder.encoder.', '')] = v
   torch.save(encoder_sd, 'outputs/<run_name>/encoder.pth')
   print(f"Encoder keys: {len(encoder_sd)}")
   ```

6. Verify the saved checkpoint loads correctly:
   ```python
   # Load into a fresh model
   model = build_model(config)  # Your model builder
   missing, unexpected = model.load_state_dict(clean_sd, strict=False)
   print(f"Missing: {len(missing)}, Unexpected: {len(unexpected)}")
   assert len(missing) == 0 or all('loss' not in k for k in missing)
   ```

7. Run a quick inference test:
   ```python
   model.eval()
   with torch.no_grad():
       dummy = torch.randn(1, 3, 224, 224)
       output = model(dummy)
   print(f"Output shape: {output.shape}")
   ```

8. Document the checkpoint:
   - Training step and epoch
   - Validation metrics at checkpoint time
   - Model architecture and config
   - Data it was trained on
   - Any preprocessing requirements

9. Summarize the deployment checkpoint path and usage instructions.
