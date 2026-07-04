---
description: Run PCOS test suite and fix failures
---

## PCOS Test & Verify

1. **Run all tests**:
   ```bash
   python -m pytest tests/ -q --tb=short
   ```

2. **Run only unit tests** (routing logic):
   ```bash
   python -m pytest tests/test_router.py -q
   ```

3. **Run only integration tests** (end-to-end route→execute→plan):
   ```bash
   python -m pytest tests/test_integration.py -q
   ```

4. **Run a specific test**:
   ```bash
   python -m pytest tests/test_router.py::TestChromeBuiltinAI::test_summarize_routes_to_summarizer -q
   ```

5. **Verify broker imports**:
   ```bash
   python -c "from broker.main import app; assert app.title == 'PCOS Context Broker'"
   python -c "from broker.config import get_settings; s = get_settings(); assert s.broker_port > 0"
   python -c "from broker.logging import get_logger; log = get_logger('test'); log.info('ok', x=42)"
   ```

6. **Lint with ruff**:
   ```bash
   pip install ruff
   ruff check broker/ memory/ tests/ --output-format=github
   ```

7. **If tests fail**:
   - Check the error traceback for the specific file and line
   - For routing failures: verify TaskObject fields match the expected decision tree branch
   - For integration failures: check that test assertions match actual routing behavior (e.g., `is_webpage_grounded` must be `True` for Chrome routing)
   - For import errors: ensure all dependencies in `requirements.txt` are installed

8. **Check coverage**:
   ```bash
   pip install pytest-cov
   python -m pytest tests/ --cov=broker --cov-report=term-missing
   ```
