# DGX Spark UMA Memory and Thermal Tuning

## Description

Tuning DGX Spark's 128 GB unified LPDDR5X memory, page cache competition, thermal throttling, EC firmware, and CPU compilation flags.

## When to use

You are hitting OOM, thermal throttling, or unexpected slowdowns on a DGX Spark (GB10, sm_121) with its unified memory architecture.

## Key concepts

- **UMA**: CPU and GPU share the same 128 GB LPDDR5X pool. `cudaMemGetInfo` underreports allocatable memory because it ignores page cache and swap that the OS can reclaim.
- **Page cache competition**: Linux file cache uses the same physical memory as CUDA. Flush with `sync; echo 3 > /proc/sys/vm/drop_caches` before large allocations.
- **GPU memory cap**: vLLM `--gpu-memory-utilization` should be 0.85-0.87; never >0.90. For 131K context, drop to 0.82.
- **Thermal throttling**: EC firmware 0x0300 breaks the fan curve. Roll back to 0x02004e18.
- **CPU compilation**: GB10 is 10x Cortex-X925 + 10x Cortex-A725. Use `-mcpu=gb10` (GCC 15+/LLVM 21+) or `-march=armv9.2-a+sve2+bf16+i8mm`.

## Code pattern

```bash
# Reclaim memory
sudo sh -c 'sync; echo 3 > /proc/sys/vm/drop_caches'

# Tune VM for UMA
sudo sysctl -w vm.swappiness=0
sudo sysctl -w vm.vfs_cache_pressure=200
sudo sysctl -w vm.dirty_ratio=5
sudo sysctl -w vm.dirty_background_ratio=2
sudo sysctl -w vm.max_map_count=2097152

# EC firmware rollback
sudo fwupdmgr get-devices
sudo fwupdmgr downgrade <device-id>  # select 0x02004e18

# Compile for GB10
gcc -O3 -mcpu=gb10 -fopenmp ...
```

## Tuning notes

- Set `RAY_memory_monitor_refresh_ms=0` to prevent Ray from killing vLLM due to page-cache pressure.
- Pin driver to 580.x: `sudo apt-mark hold nvidia-driver-580` (590.x has UMA memory leak and CUDAGraph deadlock).
- Transparent huge pages: `echo madvise | sudo tee /sys/kernel/mm/transparent_hugepage/enabled`.

## Verification

1. Monitor `nvidia-smi dmon` and thermal zones under load; confirm no throttling.
2. Allocate a 90 GB tensor and confirm `cudaMemGetInfo` plus `/proc/meminfo` give consistent readings.
3. Compile a small OpenMP microbenchmark with `-mcpu=gb10` and compare to generic `-march=armv8-a`.

## References

- https://docs.nvidia.com/dgx/dgx-spark-porting-guide/optimization.html
- https://nvidia.custhelp.com/app/answers/detail/a_id/5728
- https://forums.developer.nvidia.com/t/nvidia-dgx-spark-gb10-thermal-throttling-fan-curve-fix-via-ec-firmware-rollback/377069
- https://github.com/llvm/llvm-project/commit/84e54515bc4e9dd4938121f4df7cc27bb89a0a43
