# Backend Engineering

## Description

Server-side development, async task queues, databases, caching, and resilience patterns for ML products.

## When to use

You are building the server layer that handles model serving, data access, background jobs, and business logic for an ML application.

## Key concepts

- **Web frameworks**: FastAPI, Django, Flask, Node.js/Express.
- **Async task queues**: Celery, RQ, Dramatiq for long-running ML jobs.
- **Databases and ORMs**: PostgreSQL, SQLAlchemy, asyncpg; vector stores like pgvector.
- **Caching**: Redis, Memcached for features, predictions, and rate limits.
- **Resilience**: retries, circuit breakers, idempotency, graceful shutdown.
- **Observability**: structured logging, metrics, tracing, health checks.

## Code pattern

```python
from fastapi import FastAPI
from celery import Celery

celery_app = Celery(
    "ml_tasks",
    broker="redis://localhost:6379/0",
    backend="redis://localhost:6379/0",
)

@celery_app.task(bind=True, max_retries=3)
def train_model(self, dataset_id: int):
    try:
        # training logic
        return {"status": "completed"}
    except Exception as exc:
        raise self.retry(exc=exc, countdown=60)

app = FastAPI()

@app.post("/train/{dataset_id}")
def start_training(dataset_id: int):
    task = train_model.delay(dataset_id)
    return {"task_id": task.id, "status": "queued"}
```

## Tuning notes

- Offload long inference or training to workers; keep API routes responsive.
- Use connection pooling and async I/O to avoid blocking.
- Cache only deterministic, safe-to-stale predictions; version cache keys.
- Implement health, readiness, and liveness probes for deployments.

## Verification

1. Build a FastAPI backend with a Celery worker and Redis broker.
2. Simulate worker failure and confirm retry/requeue behavior.
3. Add caching and measure response time and hit ratio.

## References

- https://fastapi.tiangolo.com/
- https://docs.celeryq.dev/en/stable/
- https://redis.io/docs/latest/
- https://12factor.net/
- https://www.postgresql.org/docs/current/
