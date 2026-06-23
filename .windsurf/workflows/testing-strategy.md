---
description: Design and implement testing strategy for ML research code
---

## Testing Strategy Setup

1. Install pytest:
   ```bash
   pip install pytest pytest-cov
   ```

2. Create test directory structure:
   ```bash
   mkdir -p tests
   touch tests/__init__.py tests/conftest.py
   ```

3. Write `tests/conftest.py` with shared fixtures (device, small_batch, model).

4. Write smoke tests (`tests/test_smoke.py`): import all modules, instantiate models.

5. Write unit tests for model components: check output shapes, backward pass.

6. Write data pipeline tests: check dataset length, sample shapes, label correctness.

7. Write loss function tests: non-negativity, gradient flow, edge cases.

8. Run all tests:
   ```bash
   pytest tests/ -v --tb=short
   ```

9. Add test running to pre-commit or CI.

10. Summarize: test count, coverage, any failing tests.
