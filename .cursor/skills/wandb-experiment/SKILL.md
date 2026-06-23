---
name: wandb-experiment
description: Set up and use Weights & Biases (WandB) for ML experiment tracking. Use when initializing WandB runs, logging metrics, managing experiment configs, comparing runs, or debugging WandB integration issues.
---

## WandB Experiment Tracking

### Setup

```bash
pip install wandb
wandb login  # Enter API key from https://wandb.ai/authorize
```

### Basic usage in training scripts

```python
import wandb

# Initialize run
wandb.init(
    project="tdv-cholec",
    name="tdv-vitb14-stage0",
    config={
        "backbone": "dinov2_vitb14",
        "batch_size": 8,
        "lr": 1e-4,
        "num_frames": 4,
        # ... all hyperparameters
    },
)

# Log metrics every N steps
wandb.log({
    "loss": loss.item(),
    "lr": current_lr,
    "mse_loss": mse_loss.item(),
    "dino_loss": dino_loss.item(),
}, step=global_step)

# Log gradients (optional, expensive)
wandb.watch(model, log="gradients", log_freq=100)

# Finish
wandb.finish()
```

### Best practices

1. **Log config dict**: Pass your full YAML config to `wandb.init(config=...)`
2. **Use step= explicitly**: Don't rely on implicit step increments
3. **Log train + val separately**: Use prefixes like `train/loss`, `val/mAP`
4. **Log learning rate**: Track LR schedule for debugging
5. **Use groups for ablations**: `group="lora-rank-sweep"` ties related runs together
6. **Tag runs**: `tags=["stage0", "tdv", "vitb14"]` for filtering

### Comparing runs

```python
# Load and compare runs via API
import wandb
api = wandb.Api()

# Get runs from a project
runs = api.runs("tdv-cholec", order="-summary_metrics.loss")
for run in runs:
    print(f"{run.name}: loss={run.summary.get('loss', 'N/A')}, "
          f"lr={run.config.get('lr', 'N/A')}")
```

### Debugging WandB issues

1. **Offline mode**: `export WANDB_MODE=offline` when no internet on compute nodes
2. **Sync later**: `wandb sync wandb/offline-run-*/`
3. **Disable on debug**: `export WANDB_MODE=disabled` or `wandb.init(mode="disabled")`
4. **Slurm + WandB**: Set `WANDB_DIR=/scratch/kcwp264/wandb` to avoid HOME quota issues
5. **DDP + WandB**: Only log on rank 0: `if int(os.environ.get("RANK", 0)) == 0:`
