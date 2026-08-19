# High-Performance Scientific Data Formats for GPU ML

## Description

Zarr, TensorStore, WebDataset, HDF5/NetCDF, KvikIO, and direct-to-GPU I/O pipelines.

## When to use

You are building data loaders for large scientific datasets (weather, molecular, imaging) and need GPU-friendly storage.

## Key concepts

- **Zarr**: chunked N-dimensional arrays; supports GPU sharding (zarr-python 3.x).
- **TensorStore**: C++ backend for Zarr/N5/Neuroglancer; high-throughput reads.
- **WebDataset**: tar-based streaming; scales to hundreds of GPUs.
- **KvikIO**: direct GDS / POSIX / cuFile reads into GPU memory.
- **CuPy + Zarr**: zero-copy-ish GPU arrays from Zarr stores.

## Code pattern

```python
import zarr
import cupy as cp

store = zarr.storage.FSStore("gs://bucket/data.zarr", mode="r")
z = zarr.open_array(store, path="temperature")
chunk = z[:1024, :1024]  # returns NumPy or CuPy depending on config
```

## Tuning notes

- Chunk size should match the model's batch/shard shape.
- Use `zarr.shuffle` or WebDataset shard shuffling to avoid I/O bottlenecks.
- For UMA/GB10, `KvikIO` and `cupy.from_dlpack` can avoid extra copies.

## Verification

1. Benchmark `zarr.open_array(...)[0:1000]` vs `h5py`/NetCDF read.
2. Run a DataLoader with WebDataset and measure samples/s per GPU.
3. Verify `kvikio` can read a file directly into a `cupy` array.

## References

- https://zarr.dev/
- https://google.github.io/tensorstore/
- https://github.com/webdataset/webdataset
- https://xarray.dev/blog/gpu-pipeline
