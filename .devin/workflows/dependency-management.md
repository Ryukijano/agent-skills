---
description: Manage Python dependencies for ML research projects using lock files and pyproject.toml
---

## Dependency Management

1. Audit current dependencies:
   ```bash
   pip list --format=columns | head -30
   ls requirements.txt environment.yml pyproject.toml 2>/dev/null
   ```

2. Create or update `pyproject.toml` with explicit dependencies:
   ```toml
   [project]
   dependencies = ["torch>=2.4", "numpy", "wandb", "tqdm", "pyyaml", "einops"]
   ```

3. Generate lock file:
   ```bash
   pip freeze --exclude-editable > requirements-lock.txt
   ```

4. Check for version conflicts:
   ```bash
   pip check
   ```

5. Remove unused dependencies:
   ```bash
   pip install pipdeptree
   pipdeptree --warn  # shows warnings for missing/conflicting deps
   ```

6. Commit lock file:
   ```bash
   git add requirements-lock.txt pyproject.toml
   git commit -m "chore: pin dependencies"
   ```

7. Summarize: dependency count, any conflicts found, lock file location.
