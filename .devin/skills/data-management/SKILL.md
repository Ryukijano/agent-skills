---
name: data-management
description: Manage research datasets with versioning, hashing, split documentation, and leak-free partitioning. Use when setting up data pipelines, documenting dataset splits, preventing train/test leakage, or organizing large-scale ML data.
---

## Research Data Management

### Dataset versioning

```python
import hashlib, json, os
from pathlib import Path

def hash_dataset(directory: str) -> dict:
    """Compute SHA256 of all files in a dataset directory."""
    hashes = {}
    for f in sorted(Path(directory).rglob("*")):
        if f.is_file():
            h = hashlib.sha256(f.read_bytes()).hexdigest()[:16]
            hashes[str(f.relative_to(directory))] = h
    return {"file_count": len(hashes), "files": hashes}

# Save alongside experiment config
dataset_hash = hash_dataset("data/cholec80_frames")
with open("outputs/run_001/dataset_hash.json", "w") as f:
    json.dump(dataset_hash, f, indent=2)
```

### Split documentation

Always document which data goes where:

```yaml
# configs/splits/my_split.yaml
dataset: cholec80
description: "Leak-free SSL split for CholecTrack20 evaluation"
splits:
  ssl_train:
    videos: [video02, video03, ...]  # 73 videos
    notes: "Excludes CT20 train+val+test"
  detection_train:
    videos: [video02, video03, ...]  # CT20 training set
  detection_val:
    videos: [video30, video110]       # CT20 validation
  detection_test:
    videos: [video01, video06, ...]   # CT20 test
leak_check: "No video appears in both ssl_train and detection_{train,val,test}"
```

### Leak-free partitioning rules

1. **Never** share videos between SSL pretraining and downstream evaluation
2. Document the source of each split explicitly
3. When using public datasets, follow their official splits
4. Track patient/video-level splits, not frame-level (frames from same video leak)

### Data directory structure

```
data/
├── raw/                    # Original, immutable data
│   └── cholec80/
├── processed/              # Preprocessed, cached
│   └── cholec80_frames/
├── splits/                 # Split definitions (YAML)
│   └── ct20_c80_ssl_splits.yaml
└── README.md               # Data provenance, licenses, preprocessing
```

### Data README template

```markdown
# Dataset: <name>

## Source
- Original URL: ...
- License: ...
- Downloaded: YYYY-MM-DD

## Preprocessing
- Resized to 224x224
- Normalized with ImageNet mean/std
- Extracted frames at 1 FPS

## Splits
See `splits/` directory for YAML definitions.
- SSL train: 73 videos (leak-free from CT20)
- Detection train/val/test: CT20 official splits
```
