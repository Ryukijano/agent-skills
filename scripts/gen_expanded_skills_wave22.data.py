SKILLS = [
    {
        "name": "data-engineering-best-practices",
        "title": "Data Engineering Best Practices",
        "description": "Data lifecycle management, data quality, observability, lineage, testing, version control, and infrastructure-as-code for robust data systems.",
        "devin_body": r'''
## When to use

You are building or operating data systems that need to be reliable, observable, cost-effective, and maintainable for analytics and ML.

## Key concepts

- **Data engineering lifecycle**: data generation, ingestion, storage, transformation, serving, and governance.
- **Data quality**: schema contracts, validation, unit tests, and anomaly detection (Great Expectations, dbt tests, Pandera).
- **Data lineage and catalog**: trace data flow with OpenLineage, DataHub, Amundsen, or Apache Atlas.
- **Infrastructure as code**: define pipelines, storage, and compute in Terraform, Pulumi, or CloudFormation.
- **Version control and CI/CD**: Git, dbt Slim CI, pre-commit hooks, and environment promotion.
- **Observability**: pipeline health, data freshness, volume, schema, and distribution monitoring.

## Code pattern

```python
import great_expectations as gx
import pandas as pd

context = gx.get_context()
df = pd.read_parquet("s3://bucket/events/")

source = context.data_sources.add_pandas("rides")
batch_definition = source.add_dataframe_asset(name="rides_df")

checkpoint = gx.Checkpoint(
    name="rides_checkpoint",
    validation_definitions=[
        gx.ValidationDefinition(
            name="rides_validation",
            data=batch_definition,
            suite=gx.ExpectationSuite(
                name="rides_suite",
                expectations=[
                    gx.expectations.ExpectColumnValuesToNotBeNull(column="ride_id"),
                    gx.expectations.ExpectColumnValuesToBeBetween(
                        column="duration_min", min_value=0, max_value=180
                    ),
                ],
            ),
        )
    ],
)
result = checkpoint.run()
print(result.success)
```

## Tuning notes

- Design for idempotency and incremental loads to reduce cost and enable backfills.
- Define SLAs and data contracts with upstream producers.
- Partition and cluster by query patterns; use Parquet/Zarr for analytical workloads.
- Treat data pipelines as software: code review, linting, type checking, and automated tests.

## Verification

1. Create a pipeline with data quality checks and verify failures block downstream jobs.
2. Generate a lineage graph from OpenLineage or DataHub for a multi-step pipeline.
3. Refactor a brittle ad-hoc script into version-controlled, tested, idempotent tasks.
''',
        "references": [
            "https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/",
            "https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/data-engineering-principles.html",
            "https://docs.getdbt.com/best-practices/best-practice-workflows",
            "https://docs.greatexpectations.io/docs/core/run_validations/",
            "https://dagster.io/learn/data-engineering-on-aws",
        ],
    },
    {
        "name": "data-pipelines-ml",
        "title": "Data Pipelines for ML",
        "description": "Orchestrating end-to-end ML workflows with task dependencies, artifact tracking, retries, and reproducibility.",
        "devin_body": r'''
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
''',
        "references": [
            "https://www.kubeflow.org/docs/components/pipelines/",
            "https://airflow.apache.org/docs/apache-airflow/stable/",
            "https://www.oreilly.com/library/view/building-machine-learning/9781492053187/",
            "https://docs.dagster.io/examples/full-pipelines/ml",
            "https://mlflow.org/docs/latest/",
        ],
    },
    {
        "name": "etl-and-elt",
        "title": "ETL and ELT",
        "description": "Extract, transform, load patterns and the modern extract, load, transform paradigm with tooling and trade-offs.",
        "devin_body": r'''
## When to use

You need to move and reshape data between source systems and a destination such as a warehouse, lake, or operational database.

## Key concepts

- **ETL**: transform before loading, stronger control, often batch, classic enterprise pattern.
- **ELT**: load raw data first, transform in the warehouse, faster iteration, leverages warehouse compute.
- **Incremental loading**: detect new/changed records with CDC, timestamps, or change tracking.
- **Idempotency and retries**: ensure reruns produce the same result.
- **Data quality gates**: validate before/after load with dbt tests or Great Expectations.

## Code pattern

```python
import duckdb

# ELT pattern: raw data already in warehouse/lake
con = duckdb.connect("warehouse.duckdb")
con.sql("""
    CREATE OR REPLACE TABLE staging.orders AS
    SELECT * FROM read_parquet('s3://lake/raw/orders/*/*.parquet')
""")

con.sql("""
    CREATE OR REPLACE TABLE marts.daily_revenue AS
    SELECT
        order_date,
        SUM(amount) AS revenue
    FROM staging.orders
    WHERE status = 'completed'
    GROUP BY order_date
""")
```

## Tuning notes

- Prefer ELT when the warehouse is elastic and raw history has analytical value.
- Use ETL for heavy normalization, PII scrubbing, or low-latency operational loads.
- Stage data with clear layer names (bronze/silver/gold or raw/staging/marts).
- Track run timestamps and row counts for auditability and backfills.

## Verification

1. Implement an incremental ETL job and verify backfill yields the same output.
2. Rebuild a report using only raw-loaded data and dbt models.
3. Compare cost/latency of ETL vs ELT for the same workload.
''',
        "references": [
            "https://docs.getdbt.com/best-practices/best-practice-workflows",
            "https://stripe.com/resources/more/what-is-elt",
            "https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html",
            "https://docs.getdbt.com/docs/introduction",
        ],
    },
    {
        "name": "data-warehousing",
        "title": "Data Warehousing",
        "description": "Cloud data warehouses, dimensional modeling, indexing, partitioning, and workload optimization.",
        "devin_body": r'''
## When to use

You need to store and query large volumes of structured, analytics-ready data with SQL, BI, and ML workloads.

## Key concepts

- **OLAP vs OLTP**: analytics workloads favor columnar storage and massive parallelism.
- **Cloud warehouses**: Snowflake, BigQuery, Redshift, Azure Synapse, Databricks SQL.
- **Dimensional modeling**: facts, dimensions, star/snowflake schemas, slowly changing dimensions.
- **Partitioning and clustering**: prune scans and reduce query cost.
- **Materialized views and ELT**: pre-aggregate and cache common queries.
- **Workload management**: concurrency, queues, scaling, and cost controls.

## Code pattern

```sql
-- BigQuery: partitioned, clustered fact table
CREATE OR REPLACE TABLE mydataset.fact_orders
PARTITION BY order_date
CLUSTER BY customer_id
AS
SELECT
    order_id,
    customer_id,
    order_date,
    amount,
    status
FROM mydataset.staging_orders;
```

## Tuning notes

- Choose partitioning keys with high cardinality and common filter usage.
- Avoid over-partitioning; aim for partition sizes greater than 1 GB in BigQuery.
- Use materialized views for repeated aggregations, but monitor freshness.
- Align warehouse size and concurrency to actual workload patterns.

## Verification

1. Design a star schema and load it into a cloud warehouse.
2. Compare query cost and runtime with and without partitioning.
3. Build a materialized view and measure incremental refresh latency.
''',
        "references": [
            "https://docs.snowflake.com/",
            "https://docs.cloud.google.com/bigquery/docs",
            "https://docs.aws.amazon.com/redshift/latest/dg/welcome.html",
            "https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/",
        ],
    },
    {
        "name": "data-lakes",
        "title": "Data Lakes",
        "description": "Object storage, open table formats, lakehouse architecture, and batch/stream unification for ML and analytics.",
        "devin_body": r'''
## When to use

You need a cost-effective, flexible repository for raw and structured data at scale, often supporting both analytics and ML.

## Key concepts

- **Object storage**: S3, ADLS, GCS, MinIO as lake foundations.
- **Open table formats**: Apache Iceberg, Delta Lake, Apache Hudi for ACID, time travel, schema evolution.
- **Lakehouse**: combine data lake storage with warehouse-like performance and governance.
- **File formats**: Parquet, ORC, Avro, and columnar compression.
- **Metadata and catalog**: Hive metastore, AWS Glue Data Catalog, Unity Catalog, Lake Formation.

## Code pattern

```python
from deltalake import DeltaTable, write_deltalake
import pandas as pd

df = pd.DataFrame({
    "id": range(1000),
    "value": [x * 0.1 for x in range(1000)],
    "date": pd.date_range("2024-01-01", periods=1000, freq="h"),
})

write_deltalake("s3://lake/events/", df, mode="overwrite", partition_by=["date"])

dt = DeltaTable("s3://lake/events/")
print(dt.version())
df_old = dt.load_as_version(0)
```

## Tuning notes

- Partition by low-cardinality, high-filter columns; avoid too many small files.
- Use Z-ordering or clustering for high-cardinality predicates (Delta, Iceberg).
- Schedule compaction and vacuum to control metadata and storage growth.
- Enforce schema evolution and track table history.

## Verification

1. Create a Delta Lake or Iceberg table on object storage.
2. Demonstrate time travel by reading a previous snapshot.
3. Measure query improvement from partitioning and compaction.
''',
        "references": [
            "https://iceberg.apache.org/docs/latest/",
            "https://docs.delta.io/",
            "https://hudi.apache.org/",
            "https://aws.amazon.com/blogs/big-data/choosing-an-open-table-format-for-your-transactional-data-lake-on-aws/",
            "https://delta.io/",
        ],
    },
    {
        "name": "streaming-data",
        "title": "Streaming Data",
        "description": "Real-time data ingestion and processing with stream processors, message brokers, and event-time semantics.",
        "devin_body": r'''
## When to use

You have continuous, unbounded data (logs, events, sensors, clickstreams) and need low-latency ingestion, processing, or serving.

## Key concepts

- **Message brokers**: Kafka, RabbitMQ, Pulsar, NATS.
- **Stream processing**: Flink, Kafka Streams, Spark Structured Streaming, ksqldb.
- **Event time vs processing time**: watermarks, windows, late data handling.
- **Delivery semantics**: at-most-once, at-least-once, exactly-once.
- **State and checkpointing**: durable state, failure recovery, idempotent sinks.

## Code pattern

```python
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment

env = StreamExecutionEnvironment.get_execution_environment()
t_env = StreamTableEnvironment.create(env)

t_env.execute_sql("""
    CREATE TABLE events (
        event_id STRING,
        event_time TIMESTAMP(3),
        WATERMARK FOR event_time AS event_time - INTERVAL '5' SECOND
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'events',
        'properties.bootstrap.servers' = 'localhost:9092',
        'format' = 'json'
    )
""")

t_env.execute_sql("""
    SELECT
        TUMBLE_START(event_time, INTERVAL '1' MINUTE) AS window_start,
        COUNT(*) AS cnt
    FROM events
    GROUP BY TUMBLE(event_time, INTERVAL '1' MINUTE)
""").print()
```

## Tuning notes

- Use event time with watermarks for out-of-order data.
- Tune buffer and parallelism to match throughput and latency targets.
- Choose at-least-once by default; exactly-once only where needed and supported.
- Store offsets and checkpoints externally for recoverability.

## Verification

1. Ingest a Kafka stream and compute windowed aggregates with Flink or Spark.
2. Simulate late records and verify watermark behavior.
3. Restart a job from a checkpoint and confirm no data loss or duplicates.
''',
        "references": [
            "https://kafka.apache.org/documentation/",
            "https://nightlies.apache.org/flink/flink-docs-release-1.20/",
            "https://spark.apache.org/docs/latest/structured-streaming-programming-guide",
            "https://www.rabbitmq.com/docs",
            "https://www.confluent.io/resources/white-paper/event-driven-microservices/",
        ],
    },
    {
        "name": "api-development",
        "title": "API Development",
        "description": "REST, gRPC, and GraphQL API design, implementation, documentation, and versioning for ML services.",
        "devin_body": r'''
## When to use

You are exposing functionality (predictions, data, features) to clients, frontends, or other services via a network API.

## Key concepts

- **REST**: resource-oriented, HTTP verbs, stateless, hypermedia-driven design.
- **API contract and documentation**: OpenAPI/Swagger, automatic docs.
- **Validation**: Pydantic, JSON Schema, proto3.
- **Authentication and authorization**: OAuth2, JWT, API keys.
- **Versioning and deprecation**: URI, header, or media-type versioning.
- **gRPC/GraphQL**: high-performance RPC and flexible query languages.

## Code pattern

```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PredictRequest(BaseModel):
    text: str
    top_k: int = 3

class PredictResponse(BaseModel):
    labels: list[str]
    scores: list[float]

@app.post("/predict", response_model=PredictResponse, tags=["inference"])
def predict(req: PredictRequest):
    # model inference placeholder
    return PredictResponse(labels=["class_a", "class_b"], scores=[0.9, 0.1])
```

## Tuning notes

- Design for idempotency and clear error responses.
- Return consistent status codes; use 204 for empty deletes.
- Use pagination and rate limiting for large collections.
- Generate client SDKs from OpenAPI and keep contracts in version control.

## Verification

1. Build a FastAPI service with OpenAPI docs and Pydantic validation.
2. Implement JWT or API-key auth and test protected endpoints.
3. Add versioning and verify backward-compatible client behavior.
''',
        "references": [
            "https://fastapi.tiangolo.com/",
            "https://spec.openapis.org/oas/latest",
            "https://grpc.io/docs/what-is-grpc/introduction/",
            "https://learn.microsoft.com/en-us/azure/architecture/best-practices/api-design",
            "https://blog.postman.com/rest-api-best-practices/",
        ],
    },
    {
        "name": "backend-engineering",
        "title": "Backend Engineering",
        "description": "Server-side development, async task queues, databases, caching, and resilience patterns for ML products.",
        "devin_body": r'''
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
''',
        "references": [
            "https://fastapi.tiangolo.com/",
            "https://docs.celeryq.dev/en/stable/",
            "https://redis.io/docs/latest/",
            "https://12factor.net/",
            "https://www.postgresql.org/docs/current/",
        ],
    },
    {
        "name": "frontend-engineering",
        "title": "Frontend Engineering",
        "description": "Building user interfaces for ML-powered applications with modern frameworks, state management, and data visualization.",
        "devin_body": r'''
## When to use

You need a web or mobile UI to collect input, display predictions, visualize model outputs, or monitor ML systems.

## Key concepts

- **Component frameworks**: React, Svelte, Vue, Angular.
- **State management**: hooks, Redux, Zustand, Pinia, Svelte stores.
- **Data fetching**: REST/GraphQL clients, TanStack Query, SWR.
- **Visualization**: D3, Chart.js, Plotly, Recharts, Vega-Lite.
- **Performance**: code splitting, virtualization, memoization, lazy loading.
- **ML-specific UI**: confidence scores, explanations, feedback loops, A/B tests.

## Code pattern

```jsx
import { useState } from "react";

function PredictionForm() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const res = await fetch("/api/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    const data = await res.json();
    setResult(data);
  };

  return (
    <form onSubmit={handleSubmit}>
      <input value={text} onChange={(e) => setText(e.target.value)} />
      <button type="submit">Predict</button>
      {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
    </form>
  );
}
```

## Tuning notes

- Keep UI state close to where it is used; lift only when needed.
- Debounce input for real-time features and throttle expensive renders.
- Use Suspense and error boundaries for async boundaries.
- Design for accessibility and responsive layouts.

## Verification

1. Build a React/Svelte/Vue form that calls a prediction API.
2. Add a chart that visualizes model confidence distributions.
3. Run Lighthouse or web-vitals checks and optimize metrics.
''',
        "references": [
            "https://react.dev/learn",
            "https://svelte.dev/docs",
            "https://vuejs.org/",
            "https://developer.mozilla.org/en-US/docs/Learn",
            "https://d3js.org/",
        ],
    },
    {
        "name": "full-stack-ml",
        "title": "Full-Stack ML",
        "description": "End-to-end ML applications spanning data, model, API, frontend, deployment, and monitoring.",
        "devin_body": r'''
## When to use

You need to take an ML model from experiment to a deployed product with users, feedback, and continuous iteration.

## Key concepts

- **Full stack ML lifecycle**: data, training, serving, UI, deployment, monitoring.
- **Model serving**: REST/gRPC APIs, batch, edge, serverless.
- **Frontend integration**: interactive demos, dashboards, real-time inference.
- **MLOps**: experiment tracking, model registry, CI/CD, feature stores.
- **Deployment**: Docker, Kubernetes, serverless, CDK.
- **Feedback loops**: capture predictions, user actions, and retraining triggers.

## Code pattern

```python
# FastAPI backend
from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("model.pkl")

class PredictRequest(BaseModel):
    text: str

@app.post("/predict")
def predict(req: PredictRequest):
    proba = model.predict_proba([req.text])[0]
    return {
        "label": model.classes_[proba.argmax()],
        "confidence": float(proba.max()),
    }
```

```jsx
// React frontend
import { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);

  const predict = async () => {
    const res = await fetch("/api/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });
    setResult(await res.json());
  };

  return (
    <div>
      <input value={text} onChange={(e) => setText(e.target.value)} />
      <button onClick={predict}>Predict</button>
      <pre>{JSON.stringify(result, null, 2)}</pre>
    </div>
  );
}
```

## Tuning notes

- Start simple and add complexity only when needed.
- Containerize the API and frontend; use a reverse proxy or API gateway.
- Track experiments and register models before deployment.
- Monitor latency, error rates, and prediction distributions in production.

## Verification

1. Train a model, serve it via FastAPI, and call it from a React frontend.
2. Containerize the app with Docker Compose and run end-to-end tests.
3. Add MLflow tracking and a simple Grafana dashboard for monitoring.
''',
        "references": [
            "https://madewithml.com/",
            "https://github.com/GokuMohandas/Made-With-ML",
            "https://fullstackdeeplearning.com/",
            "https://www.oreilly.com/library/view/designing-machine-learning/9781098107956/",
            "https://github.com/pipinho13/churnguard",
        ],
    },
    {
        "name": "microservices",
        "title": "Microservices",
        "description": "Small, independently deployable services, inter-service communication, containers, and service discovery.",
        "devin_body": r'''
## When to use

Your application is large enough that independent scaling, deployment, and team ownership of capabilities outweigh the cost of distributed-system complexity.

## Key concepts

- **Bounded contexts and DDD**: split services by business capability, not technical layer.
- **Inter-service communication**: REST, gRPC, message brokers (async).
- **Container orchestration**: Docker, Kubernetes, Helm.
- **Service discovery and load balancing**: DNS, ingress, sidecars, service mesh.
- **Resilience**: retries, timeouts, circuit breakers, bulkheads, graceful degradation.
- **Observability**: distributed tracing, centralized logs, metrics.

## Code pattern

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: inference-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: inference
  template:
    metadata:
      labels:
        app: inference
    spec:
      containers:
        - name: inference
          image: myregistry/inference:v1.2
          ports:
            - containerPort: 8000
          livenessProbe:
            httpGet:
              path: /health
              port: 8000
          readinessProbe:
            httpGet:
              path: /ready
              port: 8000
```

## Tuning notes

- Avoid nanoservices; start with a well-factored monolith if the domain is unclear.
- Prefer async messaging for loose coupling; use synchronous calls only when required.
- Keep services stateless; externalize session and state to caches/databases.
- Implement CI/CD, canary deployments, and automated rollback for each service.

## Verification

1. Split a monolith API into two services and deploy with Docker Compose or Kubernetes.
2. Add a gRPC or message-broker integration and measure latency and resilience.
3. Implement health probes, metrics, and a failing-service fallback.
''',
        "references": [
            "https://martinfowler.com/microservices/",
            "https://microservices.io/",
            "https://kubernetes.io/docs/home/",
            "https://grpc.io/docs/",
            "https://martinfowler.com/articles/microservice-trade-offs.html",
        ],
    },
    {
        "name": "event-driven-architecture",
        "title": "Event-Driven Architecture",
        "description": "Events, event brokers, event sourcing, CQRS, and event-driven microservices for scalable, decoupled systems.",
        "devin_body": r'''
## When to use

You have multiple services or subsystems that need to react to state changes asynchronously, with loose coupling and auditability.

## Key concepts

- **Events and event brokers**: producers, consumers, topics, partitions, delivery semantics.
- **Event-driven microservices**: services communicate via events, not direct calls.
- **Event sourcing**: store state as a sequence of events; replay to reconstruct state.
- **CQRS**: separate read and write models, often materialized from events.
- **Patterns**: saga, outbox, event collaboration, stream-table joins.
- **Brokers**: Kafka, Pulsar, RabbitMQ, NATS, cloud event services.

## Code pattern

```python
from kafka import KafkaProducer, KafkaConsumer
import json

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

producer.send("orders", {"order_id": "123", "event": "OrderCreated", "amount": 99.0})

consumer = KafkaConsumer(
    "orders",
    bootstrap_servers=["localhost:9092"],
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    group_id="inventory-service",
    auto_offset_reset="earliest",
)

for msg in consumer:
    print(msg.value)
    # trigger downstream action
```

## Tuning notes

- Design events as facts (e.g., OrderCreated), not commands or internal state dumps.
- Choose delivery semantics based on correctness needs; exactly-once is expensive.
- Use schemas (Avro/Protobuf/JSON Schema) with a registry for compatibility.
- Plan for consumer lag, replay, and event retention.

## Verification

1. Build a producer/consumer pair with Kafka or RabbitMQ.
2. Implement event sourcing with an aggregate that replays events to rebuild state.
3. Design a saga or outbox pattern to maintain consistency across services.
''',
        "references": [
            "https://kafka.apache.org/documentation/",
            "https://martinfowler.com/eaaDev/EventSourcing.html",
            "https://www.oreilly.com/library/view/designing-event-driven-systems/9781492038252/titlepage01.html",
            "https://www.rabbitmq.com/docs",
            "https://developer.confluent.io/courses/microservices/event-driven-architecture/",
        ],
    },
]
