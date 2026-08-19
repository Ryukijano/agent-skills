# Monitoring and Observability for ML

## Description

Prometheus, Grafana, Weights & Biases, MLflow, Evidently, and drift detection for production ML.

## When to use

You have models in production and need to monitor infrastructure, model performance, and data drift.

## Key concepts

- **Infrastructure**: Prometheus + Grafana for GPU utilization, latency, throughput.
- **Experiment tracking**: W&B, MLflow, Neptune, Aim.
- **Model observability**: Evidently for drift, data quality, performance degradation.
- **Alerting**: Grafana alerts on metrics, Evidently triggers retraining.

## Code pattern

```python
import wandb
wandb.init(project="science-ml", config=config)
wandb.log({"loss": loss, "val_acc": acc})
```

Prometheus scrape:

```yaml
scrape_configs:
  - job_name: 'triton'
    static_configs:
      - targets: ['triton:8002']
```

## Tuning notes

- Combine infra monitoring (Prometheus) with model monitoring (Evidently/W&B).
- Track data distribution drift as early as possible.
- Use champion/challenger pattern for model promotion.

## Verification

1. Set up a Grafana dashboard showing GPU utilization and request latency.
2. Log a training run to W&B or MLflow and compare to previous runs.
3. Run Evidently on a dataset shift and confirm it flags drift.

## References

- https://prometheus.io/docs/introduction/overview/
- https://www.evidentlyai.com/
- https://mlflow.org/
- https://docs.wandb.ai/
