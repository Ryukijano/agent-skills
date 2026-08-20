# PCOS Deployment & Observability

## Configuration

All config via environment variables with `PCOS_` prefix or `.env` file:

| Variable | Default | Description |
|----------|---------|-------------|
| `PCOS_BROKER_HOST` | `0.0.0.0` | Broker listen host |
| `PCOS_BROKER_PORT` | `8000` | Broker listen port |
| `PCOS_CORS_ORIGINS` | `["*"]` | CORS allowed origins |
| `PCOS_PIECESOS_HOST` | `localhost` | PiecesOS MCP host |
| `PCOS_PIECESOS_PORT` | `39300` | PiecesOS MCP port |
| `PCOS_BRIDGE_AUTH_TOKEN` | (empty) | WebSocket bridge auth |
| `PCOS_LOG_JSON` | `true` | Structured JSON logging |
| `PCOS_LATENCY_TARGET_ROUTE_MS` | `50` | Route latency budget |
| `PCOS_LATENCY_TARGET_EXECUTE_MS` | `500` | Execute latency budget |

## Running the Broker

```bash
pip install -r requirements.txt
cp .env.example .env  # optional
uvicorn broker.main:app --reload --port 8000
```

## Health Check

```bash
curl http://localhost:8000/health
```

Response includes:
- Service status (ok/degraded)
- Dependency health (PiecesOS, SQLite)
- Latency budgets for all surfaces

## Metrics

```bash
curl http://localhost:8000/metrics
```

Returns:
- Total request count
- Local hit rate (percentage handled on-device)
- Cloud escalation rate
- Per-surface breakdown
- Average latency

## Structured Logging

JSON-formatted logs with arbitrary key-value pairs:

```python
from broker.logging import get_logger
log = get_logger("broker.route")
log.info("request_routed", surface="chrome_builtin_ai", latency_ms=2.3, budget_ms=50)
```

Output:
```json
{"ts": "2026-07-04T12:00:00+00:00", "level": "INFO", "logger": "broker.route", "msg": "request_routed", "surface": "chrome_builtin_ai", "latency_ms": 2.3, "budget_ms": 50}
```

## CI (GitHub Actions)

`.github/workflows/ci.yml` runs on push/PR:
- Python 3.11 + 3.12 matrix
- Ruff lint
- Pytest
- Import verification

## HF Space Deployment

```bash
cd hf_space
docker build -t pcos-space .
docker run -p 7860:7860 pcos-space
```

The HF Space runs a Gradio UI that lets users interactively test routing decisions.

## MkDocs Documentation

```bash
pip install mkdocs-material mkdocstrings
mkdocs serve  # http://localhost:8000
mkdocs build  # static site in site/
```

## Key Files

- `broker/config.py` — pydantic-settings configuration
- `broker/logging.py` — StructuredLogger with JSON output
- `broker/routers/ops_router.py` — Health, metrics, memory endpoints
- `.github/workflows/ci.yml` — CI pipeline
- `hf_space/` — HF Space Gradio demo
- `mkdocs.yml` — Docs site config
- `.env.example` — Environment variable template

## Testing

```bash
# All tests
python -m pytest tests/ -q

# Unit only
python -m pytest tests/test_router.py -q

# Integration only
python -m pytest tests/test_integration.py -q
```
