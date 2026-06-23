---
name: reproducibility
description: Ensure ML research reproducibility through seeds, config logging, environment capture, and deterministic training. Use when setting up reproducible experiments, preparing code for paper submission, or auditing a project for reproducibility gaps.
---

## ML Research Reproducibility

### Core principles

1. **Same code + same data + same environment = same results**
2. Every experiment must be traceable to a specific git commit
3. All stochasticity must be controlled with explicit seeds
4. Configs, metrics, and environment must be logged alongside results

### Seed management

```python
import os
import random
import numpy as np
import torch

def set_all_seeds(seed: int = 42):
    """Set all random seeds for reproducibility."""
    os.environ['PYTHONHASHSEED'] = str(seed)
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)
    # For full determinism (may slow training):
    # torch.backends.cudnn.deterministic = True
    # torch.backends.cudnn.benchmark = False
    # torch.use_deterministic_algorithms(True)
```

### Config logging

Every experiment run must save its full config:

```python
import json, yaml, hashlib, subprocess

def log_experiment(config, output_dir):
    # Save config
    with open(f"{output_dir}/config.yaml", "w") as f:
        yaml.dump(config, f)

    # Record git commit
    commit = subprocess.check_output(["git", "rev-parse", "HEAD"]).decode().strip()
    dirty = bool(subprocess.check_output(["git", "status", "--porcelain"]).strip())

    # Record environment
    env_info = {
        "git_commit": commit,
        "git_dirty": dirty,
        "python_version": sys.version,
        "torch_version": torch.__version__,
        "cuda_version": torch.version.cuda,
        "gpu": torch.cuda.get_device_name(0) if torch.cuda.is_available() else "N/A",
        "seed": config.get("seed", 42),
        "timestamp": datetime.now().isoformat(),
    }
    with open(f"{output_dir}/env_info.json", "w") as f:
        json.dump(env_info, f, indent=2)
```

### Environment capture

```bash
# Conda environment
conda env export --no-builds > environment.yml

# pip freeze (fallback)
pip freeze > requirements.txt

# Full lock file (recommended)
pip freeze --exclude-editable > requirements-lock.txt

# Docker container (gold standard)
docker save myimage:tag -o myimage.tar
```

### Reproducibility checklist

- [ ] All seeds set (Python, NumPy, PyTorch, CUDA)
- [ ] Config saved as YAML/JSON alongside results
- [ ] Git commit hash recorded in experiment log
- [ ] `environment.yml` or `requirements-lock.txt` committed
- [ ] Dataset version or hash recorded
- [ ] Training script can be re-run with single command: `python train.py --config <path>`
- [ ] Random data augmentation seed controlled
- [ ] Results saved with enough metadata to identify the run
- [ ] No hardcoded paths (use config or environment variables)
- [ ] `torch.backends.cudnn.deterministic = True` if bit-exact repro needed

### Common reproducibility failures

| Failure | Cause | Fix |
|---------|-------|-----|
| Different results across runs | Non-deterministic CUDA ops | Set `cudnn.deterministic=True`, `use_deterministic_algorithms(True)` |
| Can't reproduce old experiment | Code changed since run | Pin git commit in experiment log |
| Different results on different GPU | Hardware-dependent ops | Accept non-bit-exact cross-GPU repro; focus on statistical repro |
| Data preprocessing changed | Silent data pipeline edits | Version datasets; hash data files |
| Environment drift | Conda/pip packages updated | Use lock files or containers |
