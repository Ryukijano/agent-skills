# ML Metadata and Lineage

## Description

ML Metadata (MLMD), MLflow, and Kubeflow lineage for tracking artifacts, executions, and provenance.

## When to use

You need to trace which data, code, and model versions produced a given artifact or prediction in an ML pipeline.

## Key concepts

- **ML Metadata (MLMD)**: store artifacts, executions, and contexts.
- **Lineage graph**: directed graph linking artifacts to executions and downstream artifacts.
- **MLflow Tracking**: log parameters, metrics, artifacts, and models.
- **Kubeflow Pipelines**: capture lineage across pipeline runs.
- **OpenLineage**: open standard for lineage metadata collection.

## Code pattern

```python
import mlflow

mlflow.set_experiment("forecasting")
with mlflow.start_run():
    mlflow.log_param("lr", 0.01)
    mlflow.log_metric("rmse", 3.4)
    mlflow.log_artifact("model.pkl")
    mlflow.sklearn.log_model(model, "model")
```

## Tuning notes

- Log everything deterministic (seeds, code commit, data version) for reproducibility.
- Use artifact stores and model registries for long-lived lineage.
- Link lineage across tools via consistent run IDs and artifact URIs.

## Verification

1. Log a model training run with parameters, metrics, and artifacts.
2. Query the lineage from raw data → features → model → predictions.
3. Demonstrate reproducibility by checking out a run and re-running it.

## References

- https://github.com/google/ml-metadata/
- https://www.kubeflow.org/docs/components/pipelines/concepts/metadata/
- https://mlflow.org/docs/latest/ml/tracking/
- https://github.com/mlflow/mlflow/
