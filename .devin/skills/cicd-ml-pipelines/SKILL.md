# CI/CD for Machine Learning

## Description

GitHub Actions, GitLab CI, pre-commit, artifact registries, and model promotion gates for ML pipelines.

## When to use

You want to automate testing, training, and deployment of ML models with proper gates.

## Key concepts

- **Code CI**: lint, unit tests, type checks, sample inference on every PR.
- **Model CD**: retrain on schedule, validate metrics, promote to staging/prod.
- **Self-hosted runners**: GPU runners for training jobs on GH Actions / GitLab CI.
- **Artifact registries**: Docker Hub, GHCR, GitLab Container Registry for images; DVC or model registry for weights.
- **Pre-commit**: `black`, `ruff`, `mypy`, `pytest`.

## Code pattern

```yaml
# .github/workflows/ml.yml
name: ML CI
on: [push]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
      - run: pip install -r requirements.txt
      - run: pytest tests/
```

## Tuning notes

- Cache dependencies and DVC-tracked data in CI.
- Use parent-child pipelines for multi-stage ML workflows.
- Add a gate: block promotion if validation metric regresses vs baseline.

## Verification

1. Open a PR and confirm CI runs lint, tests, and sample inference.
2. Verify model retraining triggers on schedule and metrics are logged.
3. Confirm rollback to previous model artifact works.

## References

- https://github.com/mlrepa/cicd-for-modern-ai
- https://docs.github.com/en/actions
- https://dvc.org/doc/use-cases/versioning-data-and-models
- https://pre-commit.com/
