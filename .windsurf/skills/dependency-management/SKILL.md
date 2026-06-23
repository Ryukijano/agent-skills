---
name: dependency-management
description: Manage Python dependencies for ML research projects using requirements.txt, environment.yml, pyproject.toml, or uv. Use when creating lock files, resolving version conflicts, migrating to uv, or troubleshooting import errors.
---

## Dependency Management for ML Projects

### Tool comparison

| Tool | Config | Lock file | Speed | Use case |
|------|--------|-----------|-------|----------|
| **pip** | `requirements.txt` | `requirements-lock.txt` | Slow | Simple projects |
| **conda** | `environment.yml` | — | Slow | CUDA/non-Python deps |
| **uv** | `pyproject.toml` | `uv.lock` | 10-100x faster | Modern Python projects |
| **poetry** | `pyproject.toml` | `poetry.lock` | Medium | Packaging + deps |

### Minimal requirements.txt (ML project)

```
# Core
torch>=2.4
torchvision
numpy<2.0  # pin if compatibility issues

# Training
wandb
tqdm
pyyaml
einops

# Data
opencv-python
pillow
pandas
scikit-learn

# Viz
matplotlib
```

### Lock file generation

```bash
# pip
pip freeze --exclude-editable > requirements-lock.txt

# conda
conda env export --no-builds > environment.yml

# uv (recommended)
uv pip compile pyproject.toml -o uv.lock
uv pip sync uv.lock
```

### pyproject.toml for ML

```toml
[project]
name = "my-ml-project"
version = "0.1.0"
requires-python = ">=3.10"
dependencies = [
    "torch>=2.4",
    "torchvision",
    "numpy",
    "wandb",
    "tqdm",
    "pyyaml",
    "einops",
    "opencv-python",
    "scikit-learn",
]

[project.optional-dependencies]
dev = ["pytest", "ruff", "basedpyright", "pre-commit"]
viz = ["matplotlib", "seaborn"]
```

### Common dependency conflicts

| Conflict | Fix |
|----------|-----|
| numpy 1.x vs 2.x | Pin `numpy<2.0` if older torch versions |
| torch CUDA version | Install from `--index-url https://download.pytorch.org/whl/cu126` |
| opencv-python vs opencv-python-headless | Use `headless` on servers (no GUI) |
| protobuf version | Pin if wandb/tensorboard conflict |
| torchcodec vs ffmpeg | Ensure FFmpeg 6.x; set `LD_LIBRARY_PATH` |

### Version pinning strategy

- **Research projects**: Pin major versions, allow patches (`torch>=2.4,<3`)
- **Paper releases**: Full lock file (`requirements-lock.txt` or `uv.lock`)
- **Libraries**: Minimal constraints, let users choose
