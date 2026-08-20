# Data Engineering Best Practices

## Description

Data lifecycle management, data quality, observability, lineage, testing, version control, and infrastructure-as-code for robust data systems.

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

## References

- https://www.oreilly.com/library/view/fundamentals-of-data/9781098108298/
- https://docs.aws.amazon.com/prescriptive-guidance/latest/modern-data-centric-use-cases/data-engineering-principles.html
- https://docs.getdbt.com/best-practices/best-practice-workflows
- https://docs.greatexpectations.io/docs/core/run_validations/
- https://dagster.io/learn/data-engineering-on-aws
