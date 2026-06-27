---
name: pre-commit-setup
description: Set up pre-commit hooks with ruff, formatting, and common checks for Python projects. Use when initializing code quality tooling, configuring automated checks on commit, or standardizing a repo.
---

## Pre-commit Setup

### Quick start

```bash
pip install pre-commit ruff
```

### .pre-commit-config.yaml

```yaml
repos:
  - repo: https://github.com/astral-sh/ruff-pre-commit
    rev: v0.9.0
    hooks:
      - id: ruff
        args: [--fix]
      - id: ruff-format
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: trailing-whitespace
      - id: end-of-file-fixer
      - id: check-yaml
      - id: check-added-large-files
        args: [--maxkb=500]
      - id: check-merge-conflict
```

### Install and run

```bash
pre-commit install
pre-commit run --all-files
```
