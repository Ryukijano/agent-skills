---
description: Manage research datasets with versioning, hashing, and leak-free partitioning
---

## Data Management Setup

1. Audit current data directory structure:
   ```bash
   find data/ -maxdepth 2 -type d | head -20
   ```

2. Create standard structure if missing:
   ```bash
   mkdir -p data/raw data/processed data/splits
   ```

3. Document dataset splits in YAML:
   ```yaml
   # data/splits/my_split.yaml
   dataset: <name>
   splits:
     ssl_train: { videos: [...] }
     detection_train: { videos: [...] }
     detection_val: { videos: [...] }
   leak_check: "No overlap between ssl_train and detection_*"
   ```

4. Verify no leakage between splits:
   ```bash
   python -c "
   import yaml
   splits = yaml.safe_load(open('data/splits/my_split.yaml'))
   ssl = set(splits['splits']['ssl_train']['videos'])
   det = set(splits['splits']['detection_train']['videos'])
   assert not ssl & det, 'LEAK DETECTED'
   print('No leakage found')
   "
   ```

5. Write `data/README.md` with source, license, preprocessing info.

6. Summarize: dataset structure, splits, leak check results.
