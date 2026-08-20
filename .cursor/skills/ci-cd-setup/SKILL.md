# CI/CD for ML Research

### What belongs in CI (fast & reliable)
- Lint + format (ruff)
- Type check (on core)
- Smoke tests (CPU, tiny data)
- Import + basic CLI help checks
- (Optional) tiny integration on CPU with synthetic data

### What does NOT belong
- Full multi-epoch training
- Large data downloads in every run (cache or use tiny fixtures)

### Example GitHub workflow skeleton
```yaml
on: [push, pull_request]
jobs:
  lint:
    runs-on: ubuntu-latest
    steps: [checkout, setup-python, pip install ruff, ruff check, ruff format --check]
  smoke:
    runs-on: ubuntu-latest
    steps: [..., pytest tests/test_smoke.py -q]
```

### Caching
Cache pip / uv / HF weights where possible (but be careful with large models).

### Badge
`![CI](https://github.com/user/repo/actions/workflows/ci.yml/badge.svg)`

Related: `code-quality`, `testing-strategy`, `pre-commit-setup`.