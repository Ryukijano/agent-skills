---
name: observability-and-instrumentation
description: >-
  Add logging, metrics, tracing, and health checks to applications. Use when
  monitoring, debugging in production, or improving system observability.
---

# Observability and Instrumentation

## Three Pillars
- **Logs**: Structured (JSON), levels DEBUG-CRITICAL, include context
- **Metrics**: Counters, gauges, histograms (Prometheus, W&B, TensorBoard)
- **Traces**: OpenTelemetry spans across services

## Health Checks
- Liveness: process running (HTTP 200)
- Readiness: dependencies OK (DB, GPU, cache)

## ML-Specific
- W&B: loss, accuracy, GPU utilization, experiment tracking
- TensorBoard: training curves, model graphs
- Log: epoch, step, loss, lr, GPU memory, throughput
- Alert on: loss=NaN, GPU OOM, training stall

## Python Logging
```python
import logging
logger = logging.getLogger(__name__)
logger.info("Training started", extra={"epoch": 1, "lr": 1e-4})
```
