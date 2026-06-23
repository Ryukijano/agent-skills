---
name: pre-commit-setup
description: Setting up pre-commit hooks for automatic lint, format, and basic checks on every commit. Fast feedback for code quality.
---

## Pre-commit

### Install
```bash
pip install pre-commit
pre-commit install
pre-commit run --all-files   # first run to populate
```

### Typical .pre-commit-config.yaml
```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.6.0
    hooks:
      - id: ruff
      - id: ruff-format
```

### Tips
- Keep hooks fast (< few seconds).
- CI still runs the full matrix; pre-commit is for the developer.
- For notebooks, consider nbqa or separate hooks.

Related: `code-quality`, `ci-cd-setup`.
