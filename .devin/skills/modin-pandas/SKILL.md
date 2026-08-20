# Modin Pandas

## Description

Drop-in distributed, parallel pandas replacement using Modin with Ray or Dask backends.

## When to use

You have pandas code that is slow or runs out of memory on large DataFrames and want a near-drop-in parallel replacement.

## Key concepts

- **Modin**: parallel DataFrame library exposing the pandas API.
- **Execution engines**: Ray, Dask, HDK, or Python unidist.
- **Lazy vs eager**: operations are distributed and parallelized under the hood.
- **Out-of-core**: process DataFrames larger than memory on a single machine.
- **API compatibility**: most pandas methods work; unsupported ones fall back or warn.

## Code pattern

```python
# import modin.pandas as pd
import modin.pandas as pd

df = pd.read_csv("large_dataset.csv")
df.groupby("category").agg({"value": "mean"}).compute()  # modin exposes .compute()
```

## Tuning notes

- Use the Ray or Dask backend depending on your cluster setup.
- Some pandas operations are not yet fully optimized; check Modin docs for coverage.
- For very small dataframes, native pandas may be faster due to lower overhead.

## Verification

1. Run a representative pandas notebook with `import modin.pandas as pd`.
2. Compare wall-clock time and peak RAM against the original pandas run.
3. Validate that output matches pandas exactly on a sample dataset.

## References

- https://modin.org/
- https://github.com/modin-project/modin/
- https://modin.readthedocs.io/en/latest/getting_started/quickstart.html
- https://modin.readthedocs.io/en/latest/getting_started/why_modin/pandas.html
