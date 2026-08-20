# Data Versioning

## Description

DVC, lakeFS, and Delta Lake for versioning datasets, models, and pipelines alongside code.

## When to use

You need to reproduce ML experiments, track dataset changes, and manage large artifacts beyond what Git can handle.

## Key concepts

- **DVC**: Git-like data version control with storage remotes (S3, GCS, Azure).
- **lakeFS**: Git-like branching/merging over object storage data lakes.
- **Delta Lake**: ACID transactions and time travel for Parquet tables.
- **Data registries**: central repositories of versioned datasets and models.
- **Reproducibility**: tie code, data, and pipeline versions together.

## Code pattern

```bash
# DVC workflow
dvc add data/raw
git add data/raw.dvc .gitignore
dvc push
```

```python
# Delta Lake time travel
from deltalake import DeltaTable

dt = DeltaTable("s3://bucket/training_data")
df = dt.load_as_version(5).to_pandas()
```

## Tuning notes

- Use `.dvc` files for large artifacts and keep metadata in Git.
- LakeFS is great for multi-table data lake versioning; DVC is project/ML focused.
- Delta Lake adds schema enforcement but requires a Spark/Delta Lake engine.

## Verification

1. Version a dataset, train a model, and reproduce the exact run later.
2. Roll back to a previous dataset version and rerun validation.
3. Compare DVC, lakeFS, and Delta Lake for your storage architecture.

## References

- https://dvc.org/
- https://doc.dvc.org/example-scenarios/versioning-data-and-models/tutorial
- https://lakefs.io/blog/dvc-vs-git-vs-dolt-vs-lakefs/
- https://devidevs.com/blog/data-versioning-ml-dvc-lakefs-delta-lake
