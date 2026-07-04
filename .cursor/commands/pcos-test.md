# PCOS Test & Verify

Run the PCOS test suite and fix failures.

## Steps

1. Run all tests:
   ```bash
   python -m pytest tests/ -q --tb=short
   ```

2. Unit tests only: `python -m pytest tests/test_router.py -q`

3. Integration tests only: `python -m pytest tests/test_integration.py -q`

4. Specific test: `python -m pytest tests/test_router.py::TestChromeBuiltinAI::test_summarize_routes_to_summarizer -q`

5. Verify imports:
   ```bash
   python -c "from broker.main import app; assert app.title == 'PCOS Context Broker'"
   python -c "from broker.config import get_settings; s = get_settings(); assert s.broker_port > 0"
   ```

6. Lint: `ruff check broker/ memory/ tests/`

7. Coverage: `python -m pytest tests/ --cov=broker --cov-report=term-missing`

## Common failures
- Routing: check `is_webpage_grounded` and `is_short` fields
- Integration: ensure test task objects match routing logic
- Import: install all deps from `requirements.txt`

See skill: `pcos-deploy`, `pcos-routing`
