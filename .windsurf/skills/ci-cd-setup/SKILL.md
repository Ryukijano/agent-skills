---
name: ci-cd-setup
description: Set up CI/CD pipelines for ML research projects using GitHub Actions. Use when creating workflows for automated testing, linting, pre-commit checks, or model evaluation on push/PR.
---

## CI/CD for ML Research Projects

### Minimal GitHub Actions workflow

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main, dev]
  pull_request:
    branches: [main]

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"
      - run: pip install ruff
      - run: ruff check .
      - run: ruff format --check .

  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"
      - run: pip install -e ".[dev]"
      - run: pytest tests/ -v --tb=short
```

### Pre-commit CI workflow

```yaml
# .github/workflows/pre-commit.yml
name: pre-commit

on:
  pull_request:
  push:
    branches: [main]

jobs:
  pre-commit:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: "3.10"
      - run: pip install pre-commit
      - run: pre-commit run --all-files
```

### GPU CI (self-hosted runner)

```yaml
# .github/workflows/gpu-test.yml
name: GPU Smoke Test

on:
  pull_request:
    branches: [main]

jobs:
  gpu-test:
    runs-on: self-hosted  # requires GPU self-hosted runner
    steps:
      - uses: actions/checkout@v4
      - run: |
          source /scratch/kcwp264/conda/etc/profile.d/conda.sh
          conda activate <env>
          python train.py --config configs/smoke_test.yaml --max-steps 2
```

### Best practices

1. **Keep CI fast** — smoke tests only, < 5 min
2. **Cache dependencies** — use `actions/cache` or `setup-python` cache
3. **Don't run full training in CI** — use `--max-steps 2` smoke tests
4. **Separate lint and test jobs** — parallel execution
5. **Badge in README** — `![CI](https://github.com/<user>/<repo>/actions/workflows/ci.yml/badge.svg)`
6. **Pre-commit handles style** — CI handles correctness
