# Data Warehousing

## Description

Cloud data warehouses, dimensional modeling, indexing, partitioning, and workload optimization.

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

## References

- https://docs.snowflake.com/
- https://docs.cloud.google.com/bigquery/docs
- https://docs.aws.amazon.com/redshift/latest/dg/welcome.html
- https://www.kimballgroup.com/data-warehouse-business-intelligence-resources/books/data-warehouse-dw-toolkit/
