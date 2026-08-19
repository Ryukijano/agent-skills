# tcgen05 and Tensor Memory on Datacenter Blackwell

## Description

Programming datacenter Blackwell (sm_100/sm_103) with tcgen05.mma, TMEM, TMA multicast, and CTA-pair operations.

## When to use

You have B100, B200, or GB200 (sm_100/sm_103) and are writing or porting kernels that need the new Blackwell ISA.

## Key concepts

- **tcgen05.mma**: new datacenter-Blackwell Tensor Core instruction family. Single-thread issue, larger tiles, accumulators in **TMEM** (Tensor Memory).
- **TMEM**: 256 KB per SM, dedicated accumulator memory. Not present on consumer Blackwell (sm_120/sm_121).
- **TMA multicast + clusters**: cluster sizes up to 16 CTAs, multicast loads reduce L2 traffic.
- **CTA-pair operations**: 2-CTA `tcgen05.mma` instructions for larger tiles (e.g., 256×128).

## Code pattern

```ptx
// tcgen05 is single-thread issue; not a warpgroup
.reg .pred p;
.reg .b64 tmem_d, tmem_a, tmem_b;
tcgen05.mma.cta_group::1.kind::f16 [%tmem_d], %tmem_a, %tmem_b, %tmem_c;
tcgen05.commit;
```

In CUTLASS 3.x, use `cutlass::arch::Sm100` and `KernelTmaWarpSpecializedCooperative` or `Pingpong` schedules.

## Tuning notes

- Binaries compiled for sm_100 will **not** run on sm_120/sm_121. PTX with tcgen05 cannot be assembled for sm_120.
- Use `sm_100a` or `sm_103a` for arch-specific features.
- SMEM is 228 KB per block (vs 99 KB on sm_120/sm_121).
- TMEM is not addressable like SMEM; it is dedicated to tcgen05 accumulators.

## Verification

1. Compile a simple FP16 `tcgen05.mma` for `sm_100a` and run on B200/GB200.
2. Confirm `nvidia-smi` reports `B200` or `GB200` and compute capability 10.0/10.3.
3. Profile with Nsight Compute: look for `tcgen05.mma` in the SASS and high tensor core utilization.

## References

- https://0xsero.github.io/blackwell-gpu-wiki/blackwell/tcgen05-and-tmem/
- https://docs.nvidia.com/cutlass/latest/media/docs/cpp/blackwell_functionality.html
- https://pyptx.dev/guides/blackwell-gemm/
- https://docs.nvidia.com/cuda/blackwell-tuning-guide/
