# Data Lakes

## Description

Object storage, open table formats, lakehouse architecture, and batch/stream unification for ML and analytics.

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

## References

- https://iceberg.apache.org/docs/latest/
- https://docs.delta.io/
- https://hudi.apache.org/
- https://aws.amazon.com/blogs/big-data/choosing-an-open-table-format-for-your-transactional-data-lake-on-aws/
- https://delta.io/
