---
name: experiment-tracking
description: Track ML experiments with structured logging, hyperparameter management, and result comparison. Use when designing experiment pipelines, managing ablation studies, comparing runs, or integrating experiment tracking with WandB/TensorBoard/MLflow.
---

## ML Experiment Tracking

### What to track per experiment

| Category | Fields | Storage |
|----------|--------|---------|
| **Config** | All hyperparameters, model architecture, data paths | YAML file in output dir |
| **Environment** | Git commit, Python/torch/CUDA versions, GPU model | JSON in output dir |
| **Metrics** | Loss, accuracy, mAP, custom metrics at each step/epoch | WandB / TensorBoard |
| **Artifacts** | Best checkpoint, final checkpoint, config snapshot | Filesystem |
| **Data** | Dataset version, split definition, preprocessing pipeline | Config + hash |

### Directory structure for experiment outputs

```
outputs/
├── <experiment_name>/
│   ├── config.yaml          # Full config snapshot
│   ├── env_info.json        # Environment + git commit
│   ├── best.pth.tar         # Best model checkpoint
│   ├── final.pth.tar        # Final model checkpoint
│   ├── metrics.json         # Final metrics summary
│   ├── train_log.csv        # Per-step metrics (optional)
│   └── wandb_run_id.txt     # WandB run ID for cross-reference
```

### Experiment naming convention

```
<project>-<model>-<key_hp>-<date>
```

Examples:
```
tdv-cholec-vitb14-surgenet-stage0-20260621
surgi-mot-dinov2-lora-r8-stage1-20260618
endofm-lv-vits14-ssl-pretrain-20260615
```

### Hyperparameter sweep management

```python
# Define sweep as a grid
sweep_config = {
    "method": "grid",
    "parameters": {
        "lr": {"values": [1e-4, 5e-5, 1e-5]},
        "batch_size": {"values": [4, 8, 16]},
        "lora_rank": {"values": [4, 8, 16]},
    },
}

# Or via WandB sweeps
import wandb
sweep_id = wandb.sweep(sweep_config, project="tdv-cholec")
wandb.agent(sweep_id, function=train_fn, count=27)
```

### Result comparison table

After a set of experiments, produce a comparison table:

```markdown
| Run | Backbone | LR | LoRA r | Val mAP@50 | MOTA | Notes |
|-----|----------|-----|--------|------------|------|-------|
| baseline | DINOv2-B | 2e-4 | — | 0.12 | 35 | Frozen encoder |
| lora-r8 | DINOv2-B | 1e-4 | 8 | 0.28 | 52 | start_block=3 |
| lora-r16 | DINOv2-B | 1e-4 | 16 | 0.25 | 48 | start_block=0 |
| tdv+lora-r8 | DINOv2-B | 1e-4 | 8 | 0.35 | 61 | TDV pretrain + LoRA |
```

### Best practices

1. **Never run experiments on dirty branches** — commit or stash first
2. **One config per experiment** — don't change configs mid-run
3. **Log everything, filter later** — cheaper to log than to re-run
4. **Use groups for ablations** — `group="lora-rank-sweep"` ties related runs
5. **Tag runs** — `tags=["stage0", "tdv", "vitb14"]` for filtering
6. **Note failures too** — record why an experiment failed (OOM, NaN, etc.)
7. **Reference commits in notes** — "results from commit abc123"
