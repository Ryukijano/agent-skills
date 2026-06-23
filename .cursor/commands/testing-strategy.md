# Testing Strategy Implementation

1. Add `tests/test_smoke.py` that imports the main model and runs 1–2 forward steps (CPU OK).
2. Add unit tests for loss functions and metrics with synthetic data.
3. Add a small integration test: dataloader batch → model → loss → backward (1 step).
4. (Optional) Add property tests with hypothesis for shapes/invariants.
5. Wire smoke into pre-commit or CI (do not run full training).
6. For any bug fix, add a regression test that would have caught it.
7. Document how to run the test matrix in README.
8. Run `pytest -q` as part of verification gate on changes.

Apply `testing-strategy`, `code-quality`.
