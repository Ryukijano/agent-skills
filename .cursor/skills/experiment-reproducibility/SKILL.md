---
name: experiment-reproducibility
description: >-
  Ensure experiments are fully reproducible: seeds, configs, environments, checkpoints. Use when preparing for paper submission, code release, or thesis defense.
---

# Experiment Reproducibility

## Overview
Complete reproducibility checklist for ML experiments, ensuring anyone can reproduce your results.

## Reproducibility Checklist

### 1. Random Seeds
```python
import torch
import numpy as np
import random

SEED = 42
torch.manual_seed(SEED)
torch.cuda.manual_seed_all(SEED)
np.random.seed(SEED)
random.seed(SEED)
torch.backends.cudnn.deterministic = True
torch.backends.cudnn.benchmark = False
```

### 2. Environment
```bash
# Export conda env
conda env export --no-builds > environment.yml

# Export pip
pip freeze > requirements.txt

# Or use uv for reproducible installs
uv pip compile > requirements.lock
```

### 3. Config Logging
```python
import json
config = {
    "seed": 42,
    "model": "dino_v2_vitl14",
    "lr": 1e-4,
    "batch_size": 32,
    "epochs": 100,
    "data_path": "/data/train/",
    "gpu": "NVIDIA GB10",
    "cuda_version": "13.0",
}
with open("config.json", "w") as f:
    json.dump(config, f, indent=2)
```

### 4. Checkpoint Saving
```python
checkpoint = {
    "epoch": epoch,
    "model_state_dict": model.state_dict(),
    "optimizer_state_dict": optimizer.state_dict(),
    "config": config,
    "metrics": {"val_loss": val_loss, "val_map": val_map},
}
torch.save(checkpoint, f"checkpoint_epoch_{epoch}.pt")
```

### 5. Data Versioning
- Hash datasets: `md5sum /data/train/*.jpg > data_hashes.txt`
- Document splits: train/val/test counts and sources
- Use DVC or HF Datasets for versioning

### 6. Hardware Documentation
- GPU model, CUDA version, driver version
- Training time per epoch, total training time
- Memory usage (peak GPU memory)

## MCP Tools for Reproducibility
```bash
# Log hardware info
python3 mcp_servers/dgx_monitor/server.py --cli cuda_info

# Track experiments
python3 mcp_servers/research_workflow/server.py --cli create_experiment --name "ablation_v1" --description "LoRA rank comparison"

# Log results
python3 mcp_servers/research_workflow/server.py --cli log_experiment --experiment "ablation_v1" --message "Rank=16, mAP=0.72, training_time=4h"
```

## Reference Files
- Skills: `reproducibility`, `reproducibility-checklist`, `experiment-tracking`
- MCP: `mcp_servers/dgx_monitor/server.py`, `mcp_servers/research_workflow/server.py`

