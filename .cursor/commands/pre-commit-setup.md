# Pre-commit Setup

1. `pip install pre-commit`.
2. Create or update `.pre-commit-config.yaml` with ruff + other desired hooks.
3. `pre-commit install`.
4. `pre-commit run --all-files` (first time will be slow as it sets up).
5. Make a trivial edit to a Python file, stage, and commit — verify hooks run.
6. Add "pre-commit" badge or note in contributing section if you have one.
7. Document in README how to bypass in emergencies (`git commit --no-verify`) — discourage.

Apply `pre-commit-setup`, `code-quality`.
