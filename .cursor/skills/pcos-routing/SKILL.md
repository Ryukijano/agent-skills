# PCOS Routing Decision Tree

The PCOS Context Broker uses a **deterministic** routing decision tree — no LLM reasoning for routing, just policy-based dispatch.

## Decision Priority (top to bottom)

1. **Private or offline** → `android_litert_functiongemma` (never leaves device)
2. **Multimodal non-web** → `android_litert_functiongemma` (Chrome can't do image/audio locally)
3. **Short + browser-grounded + transform** → `chrome_builtin_ai` (select Chrome API by keyword)
4. **Personal context required** → `piecesos_memory_then_local` (query LTM first)
5. **Action/tool call** → `android_litert_functiongemma` (FunctionGemma on-device)
6. **Explicit user escalation** → `cloud_llm_escalation` (user asked for it)
7. **Exceeds local limits or long reasoning** → `cloud_llm_escalation` (last resort)
8. **Default** → Chrome if short+web-grounded, else Android Gemma full

## Chrome API Selection (step 3)

Keyword-based selection from task text:
- `summarize`, `summary`, `tldr` → **Summarizer**
- `translate`, `to french/german/...` → **Translator**
- `detect language`, `what language` → **Language Detector**
- `rewrite`, `rephrase`, `paraphrase` → **Rewriter**
- `proofread`, `grammar`, `fix typos` → **Proofreader**
- `write`, `draft`, `compose` → **Writer**
- fallback → **Prompt API**

## Surfaces

| Surface | Enum Value | Latency Budget |
|---------|-----------|----------------|
| Chrome Built-in AI | `chrome_builtin_ai` | 200ms |
| Android FunctionGemma | `android_litert_functiongemma` | 1000ms |
| Android Gemma Full | `android_litert_gemma_full` | 2000ms |
| PiecesOS Memory | `piecesos_memory_then_local` | 2000ms |
| Cloud LLM | `cloud_llm_escalation` | 3000ms |

## Key Files

- `broker/router/router.py` — routing decision tree and Chrome API selection
- `broker/planner/planner.py` — execution plan builder
- `broker/context/context_schema.py` — TaskObject, PCOSContext schemas
- `broker/routers/route_router.py` — FastAPI endpoints for /route and /execute

## Adding a New Chrome API

1. Add enum value to `ChromeAPI` in `broker/router/router.py`
2. Add keyword table (e.g. `_NEW_API_KEYWORDS = {"keyword1", "keyword2"}`)
3. Add selection branch in `_select_chrome_api()`
4. Add system prompt in `broker/planner/planner.py` `_SYSTEM_PROMPTS`
5. Add Chrome API params in `_CHROME_API_PARAMS`
6. Add test in `tests/test_router.py`
7. Add badge in `apps/chrome-extension/sidepanel.html`
8. Add implementation in `apps/chrome-extension/chrome_ai.js`

## Debugging Routing

```bash
# Test routing locally
curl -X POST http://localhost:8000/route \
  -H 'Content-Type: application/json' \
  -d '{"task": {"text": "summarize this", "is_webpage_grounded": true, "is_short": true, "task_type": "transform"}}'

# Run routing tests
python -m pytest tests/test_router.py -q

# Run integration tests
python -m pytest tests/test_integration.py -q
```
