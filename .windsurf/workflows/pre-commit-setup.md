---
description: Set up pre-commit hooks with ruff, formatting, and common checks
---

## Pre-commit Setup

1. Install pre-commit and ruff:
   ```bash
   pip install pre-commit ruff
   ```

2. Create `.pre-commit-config.yaml` in the project root:
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
         - id: check-toml
         - id: mixed-line-ending
           args: [--fix=lf]
   ```

3. Create `pyproject.toml` with ruff config (if not present):
   ```toml
   [tool.ruff]
   line-length = 100
   target-version = "py310"

   [tool.ruff.lint]
   select = ["E", "F", "W", "I", "UP", "B", "C4", "SIM"]
   ```

4. Install the hooks:
   ```bash
   pre-commit install
   ```

5. Run on all files to fix existing issues:
   ```bash
   pre-commit run --all-files
   ```

6. Commit the configuration:
   ```bash
   git add .pre-commit-config.yaml pyproject.toml
   git commit -m "chore: add pre-commit with ruff"
   ```

7. Verify hooks run on next commit:
   ```bash
   echo "test" >> README.md
   git add README.md
   git commit -m "test: verify pre-commit"
   # Should see ruff checks run automatically
   ```
