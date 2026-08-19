# Distributed Storage for HPC and ML

## Description

Lustre, BeeGFS, GPFS, WekaFS, Ceph, Zarr, and TensorStore for high-throughput scientific data.

## When to use

You need high-throughput, parallel storage for large scientific datasets or model checkpoints.

## Key concepts

- **Lustre**: high-bandwidth parallel POSIX filesystem; MDS + OSS.
- **BeeGFS**: easy admin, distributed metadata, RDMA.
- **GPFS/Storage Scale**: enterprise HPC filesystem.
- **WekaFS**: NVMe-only, high IOPS for metadata-heavy AI.
- **Ceph**: unified object, block, file storage.
- **Zarr/TensorStore**: chunked, cloud-native array formats.

## Code pattern

```python
import zarr
z = zarr.open("s3://bucket/data.zarr", mode="r")
chunk = z[0:1024, 0:1024]
```

For Lustre striping:

```bash
lfs setstripe -c 4 -S 1M /path/to/dir
```

## Tuning notes

- Match file/chunk size to storage stripe size.
- Use object storage for archival; parallel filesystem for hot training data.
- TensorStore gives ACID-like multi-process access to Zarr.

## Verification

1. Run `fio` or `IOR` on the filesystem and compare bandwidth to expected.
2. Benchmark `zarr` reads against `h5py`/`netcdf`.
3. Check Lustre stripe settings with `lfs getstripe`.

## References

- https://www.beegfs.io/
- https://www.weka.io/
- https://google.github.io/tensorstore/
- https://zarr.dev/
