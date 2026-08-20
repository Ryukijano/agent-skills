# Dask-ML

## Description

Distributed and out-of-core machine learning with Dask and scikit-learn, XGBoost, and hyperparameter search.

## When to use

You want to scale scikit-learn-style ML workloads across multiple cores or machines without rewriting to a new framework.

## Key concepts

- **Dask collections**: Dask Array, DataFrame, and Bag for partitioned, lazy data.
- **Dask-ML estimators**: distributed preprocessing, clustering, and regression.
- **Joblib backend**: parallelize scikit-learn with Dask clusters.
- **Parallel meta-estimators**: `ParallelPostFit`, `Incremental` for larger-than-memory prediction.
- **XGBoost/Dask integration**: train distributed XGBoost on Dask arrays/DataFrames.

## Code pattern

```python
from dask_ml.cluster import KMeans
from dask_ml.datasets import make_blobs

X, y = make_blobs(n_samples=1_000_000, chunks=100_000)
clf = KMeans(n_clusters=10)
clf.fit(X)
```

## Tuning notes

- Chunk size affects overhead; aim for ~100 MB chunks for in-memory workloads.
- Use Dask's dashboard to diagnose stragglers and data transfer.
- Prefer `Incremental` and partial_fit for streaming/online models.

## Verification

1. Run a Dask-ML estimator on a dataset that does not fit in local RAM.
2. Compare results to the equivalent scikit-learn single-machine run.
3. Inspect the Dask dashboard for task scheduling and memory usage.

## References

- https://ml.dask.org/
- https://ml.dask.org/joblib
- https://examples.dask.org/machine-learning.html
- https://ml.dask.org/meta-estimators.html
