# Debug PCOS Routing

Debug why a task routes to the wrong surface.

## Steps

1. Call the route endpoint with the problematic task:
   ```bash
   curl -X POST http://localhost:8000/route \
     -H 'Content-Type: application/json' \
     -d '{"task": {"text": "THE TASK TEXT", "is_webpage_grounded": true, "is_short": true, "task_type": "transform"}}'
   ```

2. Check the `surface` and `reason` fields in the response.

3. Trace the decision tree in `broker/router/router.py` `route()`:
   - Private/offline → Android FunctionGemma
   - Multimodal non-web → Android
   - Short + web-grounded + transform → Chrome (check `_select_chrome_api`)
   - Personal context → PiecesOS
   - Action → FunctionGemma
   - Explicit escalate → Cloud
   - Exceeds limits / long reasoning → Cloud
   - Default → Chrome if short+web, else Android Gemma

4. Verify TaskObject fields match expectations.

5. Run: `python -m pytest tests/test_router.py -q --tb=short`

6. Check structured logs for the routing decision.

See skill: `pcos-routing`
