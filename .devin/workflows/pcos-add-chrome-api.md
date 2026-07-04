---
description: Add a new Chrome Built-in AI API to the PCOS routing pipeline
---

## Add a New Chrome Built-in AI API

1. **Add the ChromeAPI enum value** in `broker/router/router.py`:
   ```python
   class ChromeAPI(str, Enum):
       NEW_API = "new_api"
   ```

2. **Add keyword table** for API selection:
   ```python
   _NEW_API_KEYWORDS = {"new_api_keyword1", "new_api_keyword2"}
   ```

3. **Add selection branch** in `_select_chrome_api()`:
   ```python
   if any(w in text for w in _NEW_API_KEYWORDS):
       return ChromeAPI.NEW_API
   ```

4. **Add system prompt** in `broker/planner/planner.py` `_SYSTEM_PROMPTS`:
   ```python
   Surface.CHROME_BUILTIN_AI: "You are a helpful assistant using the New API...",
   ```

5. **Add Chrome API params** in `_CHROME_API_PARAMS`:
   ```python
   ChromeAPI.NEW_API: {"type": "...", "format": "..."},
   ```

6. **Add test** in `tests/test_router.py`:
   ```python
   def test_new_api_routes_correctly(self):
       t = _task(text="new_api_keyword1 this text", is_webpage_grounded=True, is_short=True, task_type=TaskType.TRANSFORM)
       d = route(t)
       assert d.surface == Surface.CHROME_BUILTIN_AI
       assert d.chrome_api == ChromeAPI.NEW_API
   ```

7. **Add badge** in `apps/chrome-extension/sidepanel.html`:
   ```html
   <span class="api-badge" data-api="new_api">New API</span>
   ```

8. **Add implementation** in `apps/chrome-extension/chrome_ai.js`:
   ```javascript
   async newApi(text, options) {
       const session = await ai.newApi.create(options);
       const result = await session.process(text);
       session.destroy();
       return result;
   }
   ```

9. **Run tests**:
   ```bash
   python -m pytest tests/test_router.py tests/test_integration.py -q
   ```

10. **Update docs**: `docs/api-reference.md`, `docs/chrome-extension.md`, `README.md`
