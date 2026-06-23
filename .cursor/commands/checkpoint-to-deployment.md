# Checkpoint to Deployment

Convert a training checkpoint into a clean deployment / inference artifact.

## 1. Inspect the checkpoint
```bash
python -c '
import torch
ckpt = torch.load("outputs/mot/<run>/best.pth.tar", map_location="cpu")
print("keys:", list(ckpt.keys()))
print("step:", ckpt.get("step"))
print("best_metric:", ckpt.get("best_metric"))
if "model" in ckpt:
    print("model keys sample:", list(ckpt["model"].keys())[:10])
'
```

## 2. Decide extraction mode
- **Full detector for inference**: keep model weights + any inference-only heads.
- **Encoder only** (for downstream pretrain or other tasks): filter keys starting with the encoder prefix.
- **Strip training state**: remove `optimizer`, `ema_model`, `scaler`, loss histories.

For TDV pretrain encoder extraction:
```python
# Typical in training script or post-hoc
state = torch.load("outputs/tdv_pretrain/best.pth.tar")["model"]
encoder_sd = {k: v for k, v in state.items() if k.startswith("frame_encoder.encoder.")}
torch.save(encoder_sd, "outputs/tdv_pretrain/tdv_frame_encoder.pth")
```

## 3. Load into fresh model (strict=False audit)
```python
model = build_model(cfg)  # fresh
missing, unexpected = model.load_state_dict(encoder_sd, strict=False)
print("Missing:", missing[:5] if missing else "None")
print("Unexpected:", unexpected[:5] if unexpected else "None")
```

## 4. Smoke inference
```python
model.eval()
with torch.no_grad():
    dummy = torch.randn(1, 3, 224, 224).cuda()
    out = model(dummy)
print("Output shape:", getattr(out, 'shape', type(out)))
```

## 5. Document the artifact
Create `outputs/<run>/DEPLOYMENT.md`:
- Training step / best val metric
- Architecture (backbone size, LoRA rank if any)
- Data it saw (splits, leak-free note)
- Preprocessing (resize 224, normalize ImageNet stats or dataset stats)
- How to load: code snippet

## 6. For release
- Hash the file: `sha256sum deployment.pth >> SHA256SUMS`
- Store alongside config and environment export.

Apply skills: `tdv-pretrain`, `surgical-mot-eval`, `reproducibility`, `paper-code-release`.

Never ship a checkpoint that hasn't passed smoke eval + verification gate.
