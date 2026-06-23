---
name: dependency-management
description: >-
  Managing Python dependencies for research reproducibility: pyproject vs
  requirements, lock files, pinning strategy, conflict resolution, env export.
---

## Dependency Management

### Pinning policy
- Research day-to-day: major version pins (`torch>=2.4,<3`).
- Paper / release: full lock file (`uv.lock`, `requirements-lock.txt`, or conda env export).
- Libraries you publish: minimal constraints; let downstream choose.

### Recommended modern flow
Use `uv` or `pip-tools` or conda + explicit export.

```bash
uv pip compile pyproject.toml -o requirements-lock.txt
```

### On HPC (AIRE / Spark)
Install into /scratch area. Export with `--no-builds` to avoid host-specific builds.

### Conflict diagnosis
`pip check`, `conda list`, or `uv pip tree`.

Record in `ENV.md` or run notes the resolved versions for key packages (torch, torchvision, opencv, wandb, etc.).

Related: `reproducibility`, `code-quality`, `ci-cd-setup`.
