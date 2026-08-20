# Data Pipelines for ML

## Description

Orchestrating end-to-end ML workflows with task dependencies, artifact tracking, retries, and reproducibility.

## When to use

You need to automate the ML lifecycle from data ingestion and feature engineering to training, evaluation, and deployment.

## Key concepts

- **DAG-based orchestration**: Airflow, Kubeflow Pipelines, Prefect, Dagster.
- **Pipeline components**: containerized, reusable steps with explicit inputs/outputs.
- **Artifact tracking**: datasets, models, metrics, and parameters.
- **Caching and idempotency**: avoid re-running unchanged steps.
- **Environment parity**: dev/staging/prod pipelines share container images and dependencies.

## Code pattern

```python
from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def extract():
    return {"rows": 10000}

def train(**ctx):
    rows = ctx["ti"].xcom_pull(task_ids="extract")["rows"]
    print(f"Training on {rows} rows")

with DAG(
    "ml_pipeline",
    start_date=datetime(2025, 1, 1),
    schedule=timedelta(days=1),
    catchup=False,
) as dag:
    t1 = PythonOperator(task_id="extract", python_callable=extract)
    t2 = PythonOperator(task_id="train", python_callable=train)
    t1 >> t2
```

## Tuning notes

- Keep tasks small and idempotent; pass lightweight metadata via XCom or artifact store.
- Use KubernetesPodOperator or containerized components to isolate dependencies.
- Track lineage and versions with MLflow or experiment tracking.
- Test DAGs locally before deploying to the scheduler.

## Verification

1. Build an Airflow or Kubeflow pipeline that ingests, trains, and evaluates a model.
2. Trigger a re-run with unchanged inputs and confirm caching skips steps.
3. Compare runtimes and failure recovery between local and distributed orchestrators.

## References

- https://www.kubeflow.org/docs/components/pipelines/
- https://airflow.apache.org/docs/apache-airflow/stable/
- https://www.oreilly.com/library/view/building-machine-learning/9781492053187/
- https://docs.dagster.io/examples/full-pipelines/ml
- https://mlflow.org/docs/latest/
