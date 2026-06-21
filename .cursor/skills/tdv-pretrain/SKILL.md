---
name: tdv-pretrain
description: Run TDV (Temporal Difference in Vision) pretraining for surgical video domain adaptation. Use when setting up TDV training, configuring the frame encoder and motion encoder, debugging TDV losses, or extracting pretrained encoder weights for downstream detection.
---

## TDV Pretraining for Surgical Video

### Core idea

TDV learns: `frame_encoder(F_t) + motion_encoder(F_{t+1} - F_t) ≈ teacher_encoder(F_{t+1})`

The frame encoder is DINOv2; the motion encoder is a lightweight cross-attention ViT.
An EMA teacher provides stable targets for self-distillation.

### Key files

- `core_app/models/tdv_model.py` — Full TDV model
- `core_app/models/tdv_losses.py` — Center-sharpened MSE + DINO cross-entropy losses
- `core_app/tdv_dataloader.py` — Cholec80 video dataloader
- `scripts/pretrain_tdv.py` — Training script
- `configs/train_mot/dinov2/tdv-pretrain.yaml` — Config
- `jobs/tdv-pretrain.slurm` — SLURM job script

### Running pretraining

```bash
# Single GPU
python scripts/pretrain_tdv.py --config configs/train_mot/dinov2/tdv-pretrain.yaml

# DDP (3x L40S)
torchrun --nproc_per_node=3 scripts/pretrain_tdv.py \
    --config configs/train_mot/dinov2/tdv-pretrain.yaml --ddp

# Via Slurm
sbatch jobs/tdv-pretrain.slurm
```

### Key hyperparameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `num_frames` | 4 | Consecutive frames per sample (T) |
| `batch_size` | 8 | Per-GPU batch size |
| `img_size` | 224 | Input resolution (must be multiple of 14) |
| `motion_encoder_depth` | 4 | Number of motion encoder blocks |
| `ema_momentum` | 0.996 | Teacher EMA momentum |
| `mse_loss_weight` | 1.0 | Reconstruction loss weight |
| `dino_loss_weight` | 1.0 | DINO self-distillation loss weight |
| `motion_loss_weight` | 0.1 | Motion capture regularization weight |
| `peak_lr` | 1e-4 | Peak learning rate |
| `max_steps` | 50000 | Total training steps |
| `warmup_steps` | 1000 | Linear warmup steps |

### Loss components

1. **MSE reconstruction**: `||predicted_next - teacher_target||²` with centering/sharpening
2. **DINO cross-entropy**: Self-distillation on CLS tokens via softmax cross-entropy
3. **iBOT cross-entropy**: Self-distillation on patch tokens (optional)
4. **Motion capture**: `relu(min_ratio - embed_diff/pixel_diff)` — ensures embeddings change with motion

### Extracting encoder for downstream detection

After training, extract the frame encoder:
```python
# The training script automatically saves:
# outputs/tdv_pretrain/tdv_frame_encoder.pth
# outputs/tdv_pretrain/best.pth.tar  (full checkpoint)
# outputs/tdv_pretrain/final.pth.tar

# Use in detection config:
# encoder_checkpoint: outputs/tdv_pretrain/tdv_frame_encoder.pth
```

### Debugging TDV training

1. **Loss not decreasing**: Check that EMA teacher is being updated (`model.ema_update()`)
2. **NaN losses**: Clamp DINO head logits, reduce learning rate, check for static frames
3. **Motion encoder not learning**: Check `rgb_diff` is non-zero, verify cross-attention condition
4. **OOM with large backbone**: Use `dinov2_vits14` (384-dim) instead of `dinov2_vitb14` (768-dim)
5. **Low variance in embeddings**: Check `variance` and `off_diag_covariance` metrics in logs
