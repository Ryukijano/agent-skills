---
name: code-quality
description: Enforce code quality with formatting, linting, type checking, and pre-commit hooks for Python ML projects. Use when setting up ruff/black/mypy, configuring pre-commit, fixing lint errors, or establishing code style conventions.
---

## Code Quality for Python ML Projects

### Recommended toolchain (2026)

| Tool | Purpose | Config file |
|------|---------|-------------|
| **ruff** | Formatter + linter (replaces black + flake8) | `pyproject.toml` |
| **basedpyright** or **mypy** | Static type checker | `pyproject.toml` |
| **pre-commit** | Run checks on every commit | `.pre-commit-config.yaml` |
| **isort** | Import sorting (built into ruff) | — |

### Minimal pyproject.toml

```toml
[tool.ruff]
line-length = 100
target-version = "py310"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "UP", "B", "C4", "SIM"]
ignore = ["E501"]  # line length handled by formatter

[tool.ruff.format]
quote-style = "single"

[tool.basedpyright]
include = ["src", "tests"]
typeCheckingMode = "basic"
```

### Minimal .pre-commit-config.yaml

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

### Setup commands

```bash
pip install ruff basedpyright pre-commit
pre-commit install
pre-commit run --all-files  # run on entire repo
```

### ML-specific quality rules

1. **No `print()` in production code** — use `logging` or `tqdm.write()`
2. **No hardcoded paths** — use config or `Path(__file__).parent`
3. **No `import *`** — explicit imports only
4. **Type hints on public functions** — `def train(config: Dict[str, Any]) -> None:`
5. **No mutable default arguments** — `def foo(x: list = [])` → `def foo(x: Optional[list] = None)`
6. **No bare `except:`** — use `except Exception as e:` and log the error
7. **No unused imports** — ruff auto-removes these
8. **Docstrings on classes and public functions** — triple-quote, describe args and returns
