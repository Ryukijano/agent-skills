---
name: blackwell-sm121-targeting-gb10
description: >-
  Correctly target the GB10 (SM121) architecture: sm_121 vs sm_121f vs sm_121a, PTX version requirements, Triton ptxas setup, and common compile/runtime errors on DGX Spark.
---

# Targeting Blackwell SM121 / GB10 DGX Spark

## Overview

NVIDIA "Blackwell" is not one architecture. Datacenter Blackwell (B100/B200) is SM10x with `tcgen05`, TMEM, and NVSwitch. Consumer and workstation Blackwell (RTX 50 series, RTX PRO 6000, DGX Spark GB10) is SM12x. **SM121 does not have tcgen05, TMEM, WGMMA, or DSMEM.**

This skill is about compiling and launching kernels so they actually run on GB10 instead of failing with `INVALID_PTX`, `no kernel image`, or silent wrong results.

## sm_121, sm_121f, sm_121a

| Target | Meaning | Use case |
|--------|---------|----------|
| `sm_121` | Baseline SM121 | Normal FP32/FP16/BF16 kernels without Tensor Core FP8/FP4 block scaling |
| `sm_121f` | Family mode | Enables `kind::f8f6f4` and `kind::mxf4nvf4` dense block-scaled MMA |
| `sm_121a` | Arch-specific | Required for `mma.sp` sparse block-scaled FP4/FP8 |

Use `sm_121a` if you are unsure; it is a superset of `sm_121f`. For nvcc:
```bash
nvcc -arch=sm_121a -O2 -lineinfo -std=c++17 kernel.cu -o kernel
```

For Triton you need the system ptxas and the correct arch list:
```bash
export TRITON_PTXAS_PATH=/usr/local/cuda/bin/ptxas
export TORCH_CUDA_ARCH_LIST="12.1+PTX"
unset TRITON_OVERRIDE_ARCH   # do NOT set sm_90
```

## PTX version requirement

- CUDA 13.0 ships PTX 9.0.
- `kind::mxf4nvf4.block_scale` (block-scaled FP4) requires **PTX 9.1+**.
- Driver 580.x (CUDA 13.0) will fail to JIT PTX 9.1 with `CUDA_ERROR_UNSUPPORTED_PTX_VERSION`.
- Driver 590+ (CUDA 13.1+) is required for FP4 block-scaled MMA.

So if you compile `-arch=sm_121a` but your driver is 580.x, the kernel may ptxas-assemble but fail at module load.

## Common errors and fixes

| Error | Cause | Fix |
|-------|-------|-----|
| `ptxas error: Feature '...' not supported on .target 'sm_121'` | Using base `sm_121` for FP4/FP8 block scale | Use `sm_121f` or `sm_121a` |
| `CUDA_ERROR_INVALID_PTX` at load | Same as above, or PTX 9.1 on driver 580.x | Use correct arch or upgrade driver |
| `ptxas fatal: Value 'sm_121a' is not defined` | Triton/PyTorch using old bundled ptxas | `TRITON_PTXAS_PATH=/usr/local/cuda/bin/ptxas` |
| `no kernel image is available for execution on the device` | Triton compiled for sm_90 or missing sm_121 | Set `TORCH_CUDA_ARCH_LIST=12.1+PTX` and use system ptxas |
| `tcgen05.mma` not supported on sm_121a | Using datacenter Blackwell PTX | Use warp-level `mma.sync` instead |

## What works and what does not on SM121

| Feature | SM121 (GB10) | SM100 (B200) |
|---------|--------------|--------------|
| Tensor Cores | ✅ Ampere-style `mma.sync` | ✅ `tcgen05` / WGMMA |
| FP8/FP4 block scale | ✅ with `kind::` modifier | ✅ native / TMEM |
| TMEM | ❌ No | ✅ Yes |
| WGMMA | ❌ No | ✅ Yes |
| DSMEM / clusters | ❌ No | ✅ Yes |
| TMA (`cp.async.bulk.tensor`) | ⚠️ Not reliably exposed | ✅ Yes |
| Shared mem / block | 99 KB max | 227 KB max |
| Shared mem / SM | 128 KB | 228 KB |
| Max warps / SM | 48 | 64 |

## Tuning notes

- Default to `sm_121a` for any kernel using FP8/FP4 block-scaled MMA; `sm_121f` is sufficient for dense FP8/FP4 and `sm_121` only for plain FP32/FP16/BF16.
- Set `TRITON_PTXAS_PATH` to the system `ptxas` from CUDA 13.0+ and avoid `TRITON_OVERRIDE_ARCH=sm90`.
- Pin `TORCH_CUDA_ARCH_LIST=12.1+PTX` for PyTorch builds on DGX Spark.
- Check `cat /proc/driver/nvidia/version` before using `kind::mxf4nvf4.block_scale`: it needs driver 590+/PTX 9.1.
- Test a plain FP16 `mma.sync` first to confirm basic targeting works before adding FP8/FP4 modifiers.

## Triton / PyTorch on GB10

PyTorch stable wheels for Blackwell are a moving target. For DGX Spark you generally need:
- PyTorch compiled with `sm_121` support.
- System `ptxas` from CUDA 13.0+.
- `TORCH_CUDA_ARCH_LIST=12.1+PTX`.

Do not set `TRITON_OVERRIDE_ARCH=sm90`; it causes Triton to emit Hopper PTX that the driver rejects or that runs incorrectly on SM121.

## Verification

1. Build a minimal FP16 `mma.sync` kernel with `-arch=sm_121` and confirm it runs.
2. Build the same kernel with FP8 `kind::f8f6f4` using `-arch=sm_121a` and confirm `INVALID_PTX` goes away.
3. Run `nvidia-smi` and `cat /proc/driver/nvidia/version` to confirm driver version ≥ 580.
4. For FP4 block scaling, confirm driver ≥ 590 or accept that you cannot load the kernel.

## Reference

- `cuda-blackwell-labs/projects/25_fp8_fp4_gemm/`
- `cuda-blackwell-labs/projects/26_triton_gb10/`
- `cuda-blackwell-labs/projects/28_wgmma_tmem/`
- NVIDIA Blackwell Compatibility Guide: https://docs.nvidia.com/cuda/blackwell-compatibility-guide/
- Triton SM121 recipe: https://github.com/triton-lang/triton/issues/10331
- Modular SM121 FP4 issue: https://github.com/modular/modular/issues/6597
- Blackwell GPU Wiki: https://0xsero.github.io/blackwell-gpu-wiki/blackwell/sm100-vs-sm120/

