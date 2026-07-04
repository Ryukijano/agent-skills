# Add Chrome Built-in AI API

Add a new Chrome Built-in AI API to the PCOS routing pipeline.

## Steps

1. Add `ChromeAPI.NEW_API` enum in `broker/router/router.py`
2. Add keyword table `_NEW_API_KEYWORDS` for selection
3. Add branch in `_select_chrome_api()` 
4. Add system prompt in `broker/planner/planner.py` `_SYSTEM_PROMPTS`
5. Add Chrome API params in `_CHROME_API_PARAMS`
6. Add test in `tests/test_router.py`
7. Add badge in `apps/chrome-extension/sidepanel.html`
8. Add implementation in `apps/chrome-extension/chrome_ai.js`
9. Run: `python -m pytest tests/test_router.py tests/test_integration.py -q`
10. Update docs: `docs/api-reference.md`, `docs/chrome-extension.md`

See skill: `pcos-routing`, `pcos-chrome-ai`
