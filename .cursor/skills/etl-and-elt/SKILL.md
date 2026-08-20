# ETL and ELT

## Description

Extract, transform, load patterns and the modern extract, load, transform paradigm with tooling and trade-offs.

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

## References

- https://docs.getdbt.com/best-practices/best-practice-workflows
- https://stripe.com/resources/more/what-is-elt
- https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html
- https://docs.getdbt.com/docs/introduction
