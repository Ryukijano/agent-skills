---
description: Debug PCOS routing — why a task routes to the wrong surface
---

## Debug PCOS Routing

1. **Reproduce the issue** — call the route endpoint with the problematic task:
   ```bash
   curl -X POST http://localhost:8000/route \
     -H 'Content-Type: application/json' \
     -d '{"task": {"text": "THE TASK TEXT", "is_webpage_grounded": true, "is_short": true, "task_type": "transform"}}'
   ```

2. **Check the returned surface and reason** — the `reason` field explains which rule matched.

3. **Trace the decision tree** (in `broker/router/router.py` `route()`):
   - Is `is_private()` true? → Android FunctionGemma (step 1)
   - Is `is_offline()` true? → Android FunctionGemma (step 1)
   - Is modality IMAGE/AUDIO and not webpage-grounded? → Android (step 2)
   - Is `is_webpage_grounded` AND `is_short` AND `task_type == TRANSFORM`? → Chrome (step 3)
   - Is `requires_personal_context`? → PiecesOS (step 4)
   - Is `requires_action`? → FunctionGemma (step 5)
   - Is `user_explicit_escalate`? → Cloud (step 6)
   - Is `exceeds_local_limits` or long reasoning? → Cloud (step 7)
   - Default: Chrome if short+web, else Android Gemma

4. **Check task properties** — verify the TaskObject fields match expectations:
   ```python
   from broker.context.context_schema import TaskObject
   t = TaskObject(text="your text", is_webpage_grounded=True, is_short=True, task_type="transform")
   print(f"private={t.is_private()}, short={t.is_short}, grounded={t.is_webpage_grounded}")
   ```

5. **Check Chrome API selection** — if routed to Chrome but wrong API:
   ```python
   from broker.router.router import _select_chrome_api
   api = _select_chrome_api(t)
   print(f"Selected API: {api}")
   ```

6. **Run tests**:
   ```bash
   python -m pytest tests/test_router.py -q --tb=short
   ```

7. **Check logs** — structured logs show the routing decision:
   ```json
   {"msg": "request_routed", "surface": "chrome_builtin_ai", "latency_ms": 2.3}
   ```
