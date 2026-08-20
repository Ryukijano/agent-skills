SKILLS = [
    {
        "name": "hopper-wgmma-tma",
        "title": "WGMMA and TMA on Hopper H100/H200",
        "description": "Low-level Hopper programming with `wgmma.mma_async`, `cp.async.bulk.tensor`, tensor maps, and mbarriers.",
        "devin_body": '''
## When to use

You are writing or optimizing kernels for H100/H200 (sm_90) and need the highest possible GEMM or attention throughput.

## Key concepts

- **WGMMA**: warpgroup-level (4 warps) asynchronous MMA. PTX is `wgmma.mma_async`. Different from `mma.sync` because one thread issues for the whole warpgroup.
- **TMA**: `cp.async.bulk.tensor` moves a tile from GMEM→SMEM using a pre-encoded `CUtensorMap`. The issuing thread does not participate in the load; hardware pulls the data.
- **mbarrier**: `mbarrier.arrive` / `mbarrier.wait` coordinate TMA arrivals and consumer starts.
- **Thread block clusters**: up to 8 CTAs on Hopper, enabling TMA multicast (same tile into multiple SMs) and distributed shared memory.

## Code pattern

```cpp
// Host: build tensor map for A (must be 128-byte aligned for f16/bf16)
CUtensorMap tmap_a;
cuTensorMapEncodeTiled(&tmap_a, CUtensorMapDataType::CU_TENSOR_MAP_DATA_TYPE_FLOAT16,
                       2, A, globalDim, globalStrides, boxDim, elementStrides,
                       CU_TENSOR_MAP_INTERLEAVE_NONE,
                       CU_TENSOR_MAP_SWIZZLE_128B,
                       CU_TENSOR_MAP_L2_PROMOTION_L2_256B,
                       CU_TENSOR_MAP_FLOAT_OOB_FILL_NONE);

// Device: one thread issues TMA load
cp.async.bulk.tensor.2d.shared::cta.global.mbarrier::complete_tx::bytes
    [sA], [tmap_a, {bx, by}], [mbar_ptr];
```

## Tuning notes

- WGMMA M is fixed at 64; N must be multiple of 8; K is 16 for f16/bf16, 32 for fp8/int8.
- FP8/int8 operands are K-major only for WGMMA.
- Match TMA swizzle to SMEM swizzle (e.g., `Layout.TMA_128B` for row width ≥128 bytes).
- SMEM per block is 228 KB on H100; use deep pipelining (4-6 stages) to hide latency.

## Verification

1. Compile for `sm_90a` with `-arch=sm_90a -gencode arch=compute_90a,code=sm_90a`.
2. Run a known-answer `wgmma.mma_async` FP16 64×64×16 tile and compare to cuBLAS.
3. Check Nsight Compute `Memory > Tensor Memory` and `Compute (Tensor Core)` sections.
''',
        "references": [
            "https://docs.nvidia.com/cuda/hopper-tuning-guide/",
            "https://pyptx.dev/guides/handwritten-gemm/",
            "https://pytorch.org/blog/hopper-tma-unit/",
            "https://github.com/NVIDIA/cutlass/blob/main/examples/python/CuTeDSL/hopper/dense_gemm.py"
        ],
    },
    {
        "name": "hopper-fp8-transformer-engine",
        "title": "FP8 Training with Transformer Engine on Hopper",
        "description": "FP8 recipes (E4M3/E5M2, current, delayed, and blockwise scaling) with Transformer Engine for LLM training.",
        "devin_body": '''
## When to use

You are training large transformers on H100/H200/Blackwell and want to use FP8 to reduce memory and increase throughput.

## Key concepts

- **E4M3** for forward activations and weights; **E5M2** for backward gradients.
- **Per-tensor scaling**: one scale per tensor. Fast but can lose precision for high dynamic range.
- **Delayed scaling**: uses the previous iteration's max-abs to set the current scale.
- **Current scaling**: computes scale from the current tensor.
- **Blockwise scaling**: scale per block (e.g., 128 elements) for fine-grained dynamic range. Newer, better for accuracy.

## Code pattern

```python
import transformer_engine.pytorch as te

# FP8 linear with current scaling recipe
model = te.Linear(4096, 4096)
# Use TransformerEngine recipe with blockwise scales for matmuls
```

## Tuning notes

- Keep first and last layers in BF16 for numerical stability.
- Use FP8 only for matrix multiplications; LayerNorm and embeddings stay in BF16.
- When accuracy regresses, switch to blockwise scaling or retain master weights in FP32.

## Verification

1. Run a small Transformer layer with and without FP8 and compare loss curves.
2. Check `te.fp8_autocast()` context produces the expected `amax` history.
3. Profile memory: FP8 should reduce activation and weight footprint by ~40-50%.
''',
        "references": [
            "https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/examples/fp8_primer.html",
            "https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/fp8_current_scaling/fp8_current_scaling.html",
            "https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/fp8_blockwise_scaling/fp8_blockwise_scaling.html",
            "https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/fp8_delayed_scaling/fp8_delayed_scaling.html"
        ],
    },
    {
        "name": "hopper-flashattention-3",
        "title": "FlashAttention-3 on Hopper",
        "description": "FlashAttention-3 warp specialization, WGMMA/TMA pipelining, and FP8 block quantization on H100/H200.",
        "devin_body": '''
## When to use

You need the fastest attention implementation on H100/H200, especially for long-context prefill and training.

## Key concepts

- **Asynchronous WGMMA + TMA** to overlap Q/K/V loads with the GEMM and softmax.
- **Producer/consumer warp groups**: one warp group handles TMA loads, the other executes WGMMA and softmax.
- **Online softmax**: running max and sum are tracked so the final P·V can be fused with the softmax.
- **FP8 block quantization**: Q/K/V are quantized to FP8 with incoherent processing to maintain accuracy.

## Code pattern

The upstream `flash-attention` repo provides `flash_attn_func` and `flash_attn_varlen_func`:

```python
from flash_attn import flash_attn_func
out = flash_attn_func(q, k, v, causal=False)
```

For profiling, set `FLASH_ATTENTION_TRITON_HOPPER` env to test the Triton path.

## Tuning notes

- FlashAttention-3 is Hopper-optimized; on Ada/Ampere it falls back to FlashAttention-2.
- Use `head_dim` 64/128 for best FP8 throughput; 256 may regress.
- For decode-heavy workloads, consider FlashAttention-2 or paged variants (FlashInfer) instead.

## Verification

1. Run `pytest tests/test_flash_attn.py -k "test_flash_attn_fp8"` on H100 if available.
2. Benchmark vs PyTorch SDPA and vs FlashAttention-2.
3. Check Nsight Compute: `sm__pipe_tensor_cycles_active` should be high during the kernel.
''',
        "references": [
            "https://tridao.me/publications/flash3/flash3.pdf",
            "https://tridao.me/blog/2024/flash3/",
            "https://github.com/Dao-AILab/flash-attention",
            "https://github.com/Dao-AILab/flash-attention/blob/main/AI/SM90_BLOCK_SIZE_TUNING.md"
        ],
    },
    {
        "name": "ada-l40s-optimization",
        "title": "L40S (Ada) Training and Inference Optimization",
        "description": "L40S-specific tuning: FP8, TensorRT-LLM/Triton, multi-GPU PCIe scaling, and media engines.",
        "devin_body": '''
## When to use

You have L40S (sm_89) hardware and need to decide whether to use it for training, inference, or video/vision workloads, and how to tune it.

## Key concepts

- **Ada Lovelace (sm_89)**: 4th-gen Tensor Cores, FP8 support, 48 GB GDDR6, 864 GB/s bandwidth, 142 RT cores.
- **No WGMMA, TMA, or thread block clusters** unlike Hopper. Use `mma.sync` or cuBLAS/cuDNN paths.
- **FP8** is supported from PTX 8.1 / CUDA 12.4+.
- **Multi-GPU is PCIe-only**; NCCL must use P2P/PCIe and may need IOMMU passthrough (`iommu=pt`).
- **Media engines**: 3× NVENC + 3× NVDEC with AV1 support; useful for video inference/transcoding.

## Code pattern

```python
import torch
# L40S supports FP8 E4M3/E5M2 and bfloat16
x = torch.randn(1024, 1024, device='cuda', dtype=torch.bfloat16)
```

For inference, use TensorRT-LLM with `--dtype bfloat16` or `--dtype fp8`.

## Tuning notes

- For 7B-13B model inference and fine-tuning, 48 GB is usually enough.
- Use TensorRT-LLM with paged attention for throughput.
- For multi-GPU L40S, set `NCCL_P2P_DISABLE=0` and verify `nvidia-smi topo -p2p`.
- If NCCL hangs, enable IOMMU passthrough: `iommu=pt` in kernel command line.

## Verification

1. Run `nvidia-smi` and confirm product name is `L40S` (compute capability 8.9).
2. Run a small FP8 GEMM via `torch._scaled_mm` and compare to BF16.
3. Run a TensorRT-LLM Llama-3-8B benchmark at batch size 1 and 8.
''',
        "references": [
            "https://www.nvidia.com/en-us/data-center/l40s/",
            "https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/",
            "https://forums.developer.nvidia.com/t/nccl-hangs-on-l40s-gpus-pcie-resolved-via-iommu-passthrough/368169",
            "https://developer.nvidia.com/optical-flow-sdk"
        ],
    },
    {
        "name": "blackwell-dc-tcgen05-tmem",
        "title": "tcgen05 and Tensor Memory on Datacenter Blackwell",
        "description": "Programming datacenter Blackwell (sm_100/sm_103) with tcgen05.mma, TMEM, TMA multicast, and CTA-pair operations.",
        "devin_body": '''
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
''',
        "references": [
            "https://0xsero.github.io/blackwell-gpu-wiki/blackwell/tcgen05-and-tmem/",
            "https://docs.nvidia.com/cutlass/latest/media/docs/cpp/blackwell_functionality.html",
            "https://pyptx.dev/guides/blackwell-gemm/",
            "https://docs.nvidia.com/cuda/blackwell-tuning-guide/"
        ],
    },
    {
        "name": "blackwell-dc-moepart-green-contexts",
        "title": "MLOPart, Green Contexts, and Disaggregated Serving on Blackwell",
        "description": "Resource partitioning (MLOPart, Green Contexts, MPS) and disaggregated prefill/decode serving for datacenter Blackwell.",
        "devin_body": '''
## When to use

You are running latency-sensitive or multi-tenant inference on B200/GB200, or designing a large-scale serving system with prefill/decode separation.

## Key concepts

- **MLOPart (Memory Locality Optimization Partition)**: B200/B300 only. Partitions a GPU into multiple logical CUDA devices with separate SMs and memory. Configured via MPS `mlopart` mode.
- **Green Contexts**: runtime API (`cudaGreenCtxCreate`) to allocate dedicated SMs to a kernel. Useful for latency isolation.
- **MPS static SM partitioning**: allocate SMs at MPS controller start.
- **Disaggregated serving**: separate prefill (compute-bound) and decode (memory-bound) pools. Requires NVLink/NVSwitch bandwidth; designed for GB200 NVL72.

## Code pattern

```bash
# Start MPS with MLOPart
echo "start_server -uid $UID -mlopart" | nvidia-cuda-mps-control

# Green Context
CUgreenCtx green;
cudaGreenCtxCreate(&green, device, devResource);
```

For disaggregated serving, use NVIDIA Dynamo or vLLM with `--disaggregation-config`.

## Tuning notes

- MLOPart and Green Contexts are **not** on consumer Blackwell (sm_120/sm_121) or GB10.
- GB200 NVL72 has 72 GPUs in a single NVLink domain; disaggregation makes sense there.
- GB10 is a single GPU with no NVSwitch, so disaggregation is not useful.

## Verification

1. On a B200, list MPS status: `nvidia-cuda-mps-control -d -S`.
2. Run two concurrent kernels with and without MLOPart; measure tail latency.
3. For disaggregated serving, benchmark prefill TPGS and decode TPGS separately and end-to-end.
''',
        "references": [
            "https://developer.nvidia.com/blog/boost-gpu-memory-performance-with-no-code-changes-using-nvidia-cuda-mps/",
            "https://developer.nvidia.com/blog/nvidia-cuda-13-1-powers-next-gen-gpu-programming-with-nvidia-cuda-tile-and-performance-gains/",
            "https://docs.nvidia.com/cuda/cuda-programming-guide/04-special-topics/green-contexts.html",
            "https://developer.nvidia.com/blog/how-nvidia-gb200-nvl72-and-nvidia-dynamo-boost-inference-performance-for-moe-models/"
        ],
    },
    {
        "name": "multigpu-nccl-topology",
        "title": "Multi-GPU Topology and NCCL Tuning",
        "description": "NCCL, NVLink/NVSwitch, PCIe, InfiniBand/RoCE, GPUDirect, and common topology hang fixes.",
        "devin_body": '''
## When to use

You are scaling training or inference across multiple GPUs or nodes on H100/H200/Blackwell/L40S and need to understand/tune the interconnect.

## Key concepts

- **NCCL rings and trees**: algorithm selection and protocol (Simple, LL, LL128). Tree is better for large all-reduce.
- **NVLink 4 (H100)**: 900 GB/s per GPU; **NVLink 5 (Blackwell)**: 1,800 GB/s.
- **PCIe-only systems (L40S, GB10)**: use P2P/PCIe; may need IOMMU passthrough.
- **InfiniBand vs RoCE vs Ethernet**: IB is native RDMA; RoCEv2 needs PFC/ECN for lossless; standard Ethernet needs TCP fallback.
- **GPUDirect RDMA / DMA-BUF**: direct GPU-to-NIC transfers; use DMA-BUF on modern kernels.

## Code pattern

```bash
# Debug NCCL
NCCL_DEBUG=INFO NCCL_DEBUG_SUBSYS=GRAPH,INIT python -m torch.distributed.run ...

# Force IB HCA on RoCE
NCCL_IB_HCA=rocep1s0f0,rocep2s0f0
NCCL_SOCKET_IFNAME=enp1s0f0np0
```

## Tuning notes

- Use `NCCL_P2P_DISABLE=1` only if P2P causes hangs (rare on modern systems).
- Set `NCCL_IB_DISABLE=0` and `NCCL_IB_GID_INDEX=3` for RoCEv2.
- For DGX Spark, use ConnectX-7 QSFP RoCE; no NVLink.

## Verification

1. Run `nccl-tests/all_reduce_perf` and confirm bandwidth matches expected (e.g., ~400-900 GB/s on NVLink, ~10-13 GB/s on PCIe).
2. Use `nvidia-smi topo -p2p` to inspect P2P connectivity.
3. Capture `NCCL_DEBUG=INFO` and check the chosen algorithm and transport.
''',
        "references": [
            "https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html",
            "https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/performance_and_tuning.html",
            "https://developer.nvidia.com/blog/understanding-nccl-tuning-to-accelerate-gpu-to-gpu-communication/",
            "https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-operator-rdma.html"
        ],
    },
    {
        "name": "jax-gpu-scientific",
        "title": "JAX on NVIDIA GPUs for Scientific ML",
        "description": "JAX `jit`, `vmap`, `shard_map`, device meshes, and XLA memory tuning on H100/H200/Blackwell/L40S.",
        "devin_body": '''
## When to use

You are writing scientific ML (PINNs, neural operators, molecular/weather models) in JAX and running on NVIDIA GPUs.

## Key concepts

- **Functional transformations**: `jax.jit`, `jax.grad`, `jax.vmap`, `jax.scan`.
- **Sharding**: `Mesh`, `PartitionSpec` (`P`), `NamedSharding`. JAX automatically generates SPMD XLA HLO.
- **XLA flags**: `XLA_PYTHON_CLIENT_PREALLOCATE`, `XLA_PYTHON_CLIENT_MEM_FRACTION`, `XLA_FLAGS`.
- **`jax.distributed`**: multi-node initialization; uses NCCL under the hood.

## Code pattern

```python
import jax
import jax.numpy as jnp
from jax.sharding import Mesh, NamedSharding, PartitionSpec as P

mesh = Mesh(jax.devices().reshape(2, 4), ('data', 'model'))
sharding = NamedSharding(mesh, P('data', 'model'))
x = jax.device_put(jnp.ones((1024, 1024)), sharding)
```

## Tuning notes

- `XLA_PYTHON_CLIENT_PREALLOCATE=false` helps on UMA/GB10 where GPU and CPU share memory.
- `jax_default_matmul_precision = 'bfloat16'` can speed training.
- On multi-node, set `NCCL_NVLS_ENABLE=1` for H100 NVLink4.

## Verification

1. `jax.devices()` shows the expected number of GPUs.
2. `jax.debug.visualize_array_sharding(x)` shows the intended layout.
3. Run a small `jax.jit(jnp.einsum)` and check XLA HLO for all-reduce.
''',
        "references": [
            "https://docs.jax.dev/en/latest/parallel.html",
            "https://docs.jax.dev/en/latest/jax.sharding.html",
            "https://docs.jax.dev/en/latest/multi_process.html",
            "https://docs.jax.dev/en/latest/gpu_memory_allocation.html"
        ],
    },
    {
        "name": "triton-cross-arch",
        "title": "Triton Cross-Architecture (Ampere/Hopper/Blackwell)",
        "description": "Writing and deploying Triton kernels across sm_80, sm_89, sm_90, sm_100, sm_120, and sm_121.",
        "devin_body": '''
## When to use

You write custom Triton kernels that must run on A100, L40S, H100, B200, RTX 50-series, or DGX Spark.

## Key concepts

- **Compute capability targeting**: Triton derives `ptxas` target from `cc` arg or env.
- **`TRITON_PTXAS_PATH`**: point to CUDA 13.0+ `ptxas` for sm_121 support.
- **`TRITON_OVERRIDE_ARCH`**: usually leave unset. Setting `sm_90` on Blackwell can produce silent wrong results.
- **No `sm_120a`**: consumer Blackwell has no `a` variant; Triton fix (PR #9734) removed `a` for sm_120.
- **Unified memory on GB10**: Triton may mis-handle `cudaMallocManaged` regions; use explicit `cudaMalloc`.

## Code pattern

```python
import triton
import triton.language as tl

@triton.jit
def add_kernel(x_ptr, y_ptr, out_ptr, n, BLOCK: tl.constexpr):
    pid = tl.program_id(0)
    offsets = pid * BLOCK + tl.arange(0, BLOCK)
    mask = offsets < n
    x = tl.load(x_ptr + offsets, mask=mask)
    y = tl.load(y_ptr + offsets, mask=mask)
    tl.store(out_ptr + offsets, x + y, mask=mask)
```

## Tuning notes

- `num_warps=4` is a good default; profile 2/4/8.
- `num_stages=3-4` for compute-bound GEMM; `2-3` for memory-bound.
- SMEM limits: 164 KB (A100), 228 KB (H100), 99 KB (sm_120/121), 228 KB (sm_100).

## Verification

1. Run the kernel on a small tensor and compare to PyTorch.
2. Clear Triton cache when switching architectures: `rm -rf ~/.triton/cache`.
3. On GB10: set `TRITON_PTXAS_PATH=/usr/local/cuda/bin/ptxas` and `TORCH_CUDA_ARCH_LIST="12.1+PTX"`.
''',
        "references": [
            "https://triton-lang.org/main/python-api/generated/triton.autotune.html",
            "https://github.com/triton-lang/triton/pull/9734",
            "https://github.com/triton-lang/triton/issues/10331",
            "https://github.com/triton-lang/kernels/blob/main/kernels/matmul.py"
        ],
    },
    {
        "name": "torch-compile-inductor",
        "title": "torch.compile and Inductor for NVIDIA GPUs",
        "description": "PyTorch 2.7+ `torch.compile`, Inductor autotune, custom operators, CuTeDSL/Gluon backends, and debug.",
        "devin_body": '''
## When to use

You want to accelerate PyTorch models on H100/Blackwell/L40S with `torch.compile` and need to tune or debug the generated kernels.

## Key concepts

- **Inductor modes**: `default`, `reduce-overhead` (CUDA Graphs), `max-autotune` (benchmarks kernels).
- **Backends**: ATen, Triton, CUTLASS, CuTeDSL, NVGEMM.
- **Custom operators**: `torch.library.custom_op`, `torch.library.register_kernel`.
- **Gluon / CuTeDSL**: explicit tile/warp/TMA programming as Inductor backends (experimental).
- **Blackwell template**: persistent matmul with TMA for Blackwell.

## Code pattern

```python
import torch

model = torch.compile(model, mode="max-autotune", fullgraph=False)

# Debug compile
import torch._inductor.config as cfg
cfg.debug = True
```

For a captured kernel source:

```python
src = torch.compiler.generate_kernel(fn, (x,))
```

## Tuning notes

- `max-autotune` can take minutes to compile but yields best throughput.
- Disable inductor for data-dependent shapes: `torch.compile(..., dynamic=False)`.
- For Blackwell, use CUDA 12.8+ nightly PyTorch wheels.

## Verification

1. Compare `torch.compile(model)` vs `model` on a benchmark batch.
2. Run `TORCH_COMPILE_DEBUG=1` and inspect generated Triton/C++ code.
3. Verify `torch.cuda.get_arch_list()` includes your target arch.
''',
        "references": [
            "https://pytorch.org/docs/stable/generated/torch.compile.html",
            "https://github.com/pytorch/pytorch/pull/162916",
            "https://github.com/pytorch/pytorch/pull/180953",
            "https://github.com/pytorch/pytorch/issues/188212"
        ],
    },
    {
        "name": "cuda-q-hybrid-quantum",
        "title": "CUDA-Q Hybrid Quantum-Classical Computing",
        "description": "CUDA-Q kernels, simulators, VQE/QAOA, PyTorch/JAX integration, and multi-GPU quantum workflows.",
        "devin_body": '''
## When to use

You are exploring hybrid quantum-classical algorithms or quantum machine learning on NVIDIA GPUs.

## Key concepts

- **CUDA-Q kernel**: `@cudaq.kernel` (Python) or `__qpu__` (C++).
- **Execution primitives**: `cudaq.sample`, `cudaq.observe`, `cudaq.get_state`.
- **Backends**: `nvidia` (GPU state vector), `tensornet` (multi-GPU tensor network), `qpp-cpu`.
- **VQE / QAOA**: variational circuits with parameter-shift gradients and built-in optimizers.
- **Hybrid workflows**: integrate quantum kernels with PyTorch or JAX loss functions.

## Code pattern

```python
import cudaq

@cudaq.kernel
def ansatz(theta: float):
    q = cudaq.qubit()
    rx(theta, q)

@cudaq.kernel
def hamiltonian():
    q = cudaq.qubit()
    mz(q)

res = cudaq.observe(ansatz, hamiltonian, 0.5)
```

## Tuning notes

- For 33+ qubits, use `tensornet` or multi-GPU state vector.
- `density-matrix-cpu` for noisy simulation.
- Installation: `pip install cudaq`; for multi-GPU, install with MPI.

## Verification

1. Run a 10-qubit GHZ circuit and compare `sample` counts to theoretical distribution.
2. Run a small VQE on a 2-qubit Hamiltonian and check convergence.
3. Verify GPU backend is active: `cudaq.set_target("nvidia")`.
''',
        "references": [
            "https://nvidia.github.io/cuda-quantum/latest/using/basics/kernel_intro.html",
            "https://nvidia.github.io/cuda-quantum/latest/using/backends/simulators.html",
            "https://nvidia.github.io/cuda-quantum/latest/applications/python/vqe_advanced.html",
            "https://nvidia.github.io/cuda-quantum/latest/applications/python/hybrid_quantum_neural_networks.html"
        ],
    },
    {
        "name": "protein-folding-gpu",
        "title": "Protein Structure Prediction on GPU",
        "description": "AlphaFold 3, ESM3, Boltz, BioNeMo Fold-CP, OpenFold, and high-throughput protein folding pipelines.",
        "devin_body": '''
## When to use

You are running or deploying protein structure prediction on H100/Blackwell and need to choose the right tool and optimize it.

## Key concepts

- **AlphaFold 3 / Boltz**: 3D structure from sequence and ligands. Boltz is an open AlphaFold3 reimplementation.
- **ESM3**: 98B multimodal protein language model (sequence, structure, function).
- **BioNeMo Fold-CP**: context parallelism for very large complexes (20,000+ tokens, 256 GPUs).
- **OpenFold-TRT / ColabFold**: optimized inference with TensorRT and MMseqs2-GPU.

## Code pattern

```python
# Example: Boltz inference
from boltz import Boltz1
model = Boltz1.load_from_checkpoint("boltz1.ckpt")
structure = model.predict("sequences.fasta")
```

For AlphaFold 3, set `XLA_PYTHON_CLIENT_MEM_FRACTION=0.95` on H100.

## Tuning notes

- For >5,120 tokens, use unified memory or Fold-CP context parallelism.
- H100 is ~1.8-2× faster than A100 for AlphaFold 3.
- Pre-compute MSAs with MMseqs2-GPU for throughput.

## Verification

1. Run a single-chain prediction and compare RMSD to a known PDB structure.
2. Run `alphafold3 --input ... --output ...` and check GPU utilization.
3. For Fold-CP, verify the complex fits in aggregate GPU memory.
''',
        "references": [
            "https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md",
            "https://github.com/jwohlwend/boltz",
            "https://www.evolutionaryscale.ai/blog/esm3-release",
            "https://developer.nvidia.com/blog/scaling-biomolecular-modeling-using-context-parallelism-in-nvidia-bionemo"
        ],
    },
    {
        "name": "molecular-ml-drug-discovery",
        "title": "Molecular ML and Drug Discovery on GPU",
        "description": "Equivariant GNNs, ML potentials, molecular docking (DiffDock), and generative molecule design on GPU.",
        "devin_body": '''
## When to use

You are training or deploying models for molecular property prediction, docking, or protein-ligand design on NVIDIA GPUs.

## Key concepts

- **Equivariant GNNs**: SchNet, DimeNet, GemNet, MACE, NequIP; preserve SE(3)/E(3) symmetry.
- **cuEquivariance**: NVIDIA library giving 10× end-to-end speedup for MACE.
- **ML potentials**: MACE, CHGNet, DeePMD-kit for large MD with learned forces.
- **DiffDock/GeoDiff**: diffusion for molecular docking and conformer generation.
- **RFDiffusion**: protein backbone design.

## Code pattern

```python
import cuequivariance as cue
# Use a built-in MACE kernel
from cuequivariance_tutorial import mace_layer
```

For MD with MLP:

```python
# LAMMPS input: pair_style neuroev, pair_coeff * * CHGNet.pt
```

## Tuning notes

- Use `bfloat16` or `fp32`; `fp16` can lose precision for energies/forces.
- cuEquivariance is preferred over e3nn for large GPU workloads.
- For MD, strong scaling peaks around 16-32 GPUs for ~15k atoms.

## Verification

1. Train SchNet on QM9 and check MAE per property.
2. Run DiffDock-L on a PDBBind split and compute top-1 RMSD<2Å.
3. Run a 1 ns MACE MD step and compare forces to DFT.
''',
        "references": [
            "https://developer.nvidia.com/cuequivariance",
            "https://github.com/ACEsuit/mace",
            "https://github.com/gcorso/DiffDock",
            "https://github.com/RosettaCommons/RFDiffusion"
        ],
    },
    {
        "name": "climate-weather-ml",
        "title": "AI Weather and Climate Forecasting on GPU",
        "description": "FourCastNet, GraphCast, Pangu-Weather, ClimaX, and ECMWF ai-models on GPU clusters.",
        "devin_body": '''
## When to use

You are training or running data-driven weather/climate models on GPU.

## Key concepts

- **FourCastNet**: AFNO transformer, global week-long forecasts in <2 seconds.
- **GraphCast**: graph neural network, state-of-the-art deterministic 10-day forecasts.
- **Pangu-Weather**: 3D Earth-specific transformer.
- **ClimaX**: foundation model trained on CMIP6 + ERA5.
- **ECMWF ai-models**: unified inference interface.

## Code pattern

```python
from ai_models import run_model
run_model("fourcastnet", input_file="era5_20200101.grb", output="out.nc")
```

For training ClimaX:

```python
from climax import ClimaX
model = ClimaX(img_size=(32, 64), patch_size=2)
```

## Tuning notes

- These models are large but inference is cheap; optimize I/O (NetCDF/Zarr) and batch size.
- FourCastNet scales to thousands of GPUs for ensemble generation.
- Use `bfloat16` for training; keep normalization in FP32.

## Verification

1. Run a 10-day deterministic forecast and compare RMSE to IFS.
2. Run `ai-models` CLI on a single ERA5 time step.
3. Profile with Nsight Systems to find I/O vs compute time.
''',
        "references": [
            "https://github.com/NVlabs/FourCastNet",
            "https://github.com/ecmwf-lab/ai-models",
            "https://github.com/google-deepmind/graphcast",
            "https://doi.org/10.1145/3592979.3593412"
        ],
    },
    {
        "name": "neural-operators-pinns",
        "title": "Neural Operators and Physics-Informed ML on GPU",
        "description": "Fourier Neural Operator, DeepONet, PINNs, and JAX/Diffrax/Exponax for PDEs on GPU.",
        "devin_body": '''
## When to use

You are solving parametric PDEs, surrogate modeling, or physics-constrained ML on GPU.

## Key concepts

- **FNO (Fourier Neural Operator)**: global convolutions in frequency space.
- **DeepONet**: branch-net + trunk-net for operator learning from function pairs.
- **PINNs**: add PDE residual to the loss; good for inverse problems.
- **PINO**: pre-train on coarse data, fine-tune with PDE constraints at higher resolution.
- **JAX tools**: Diffrax (ODE/SDE), Exponax (spectral PDEs), JAX-MD, JAX-FEM.

## Code pattern

```python
import jax
import jax.numpy as jnp
from diffrax import diffeqsolve, Tsit5

term = ...
sol = diffeqsolve(term, Tsit5(), t0=0, t1=1, dt0=0.01, y0=y0)
```

## Tuning notes

- PINNs can be hard to train; start with FNO if data is available.
- Use adaptive activations (tanh with learnable frequency) for multi-scale PDEs.
- JAX `jax.vmap` is powerful for batched parameter sweeps.

## Verification

1. Train FNO on Darcy flow and compare relative L2 to a spectral solver.
2. Solve a 1D Burgers equation with PINN and compare to finite-difference.
3. Run Diffrax ODE solve and compare to scipy.
''',
        "references": [
            "https://arxiv.org/abs/2111.03794v4",
            "https://docs.kidger.site/diffrax/",
            "https://github.com/ceyron/exponax",
            "https://github.com/jax-md/jax-md"
        ],
    },
    {
        "name": "materials-discovery-ml",
        "title": "Materials Discovery with Generative ML on GPU",
        "description": "MatterGen, GNoME, DiffCSP, CDVAE, and crystal structure generation on GPU.",
        "devin_body": '''
## When to use

You are generating or screening novel inorganic materials and crystal structures.

## Key concepts

- **MatterGen**: diffusion model for inorganic materials; 2× stable/novel rate over prior methods.
- **GNoME**: graph network for materials exploration; discovered 380k+ stable structures.
- **DiffCSP**: periodic E(3)-equivariant diffusion in fractional coordinates.
- **CDVAE**: SE(3)-invariant VAE for periodic structures.
- **Materials Project / CSD**: training data sources.

## Code pattern

```python
from mattergen import MatterGen
model = MatterGen.load_from_checkpoint("checkpoint/")
structures = model.generate(num_samples=100)
```

## Tuning notes

- Training requires large batches and stable E(3) equivariance; use `bfloat16` with care.
- GNoME models can be fine-tuned on local datasets.
- Validate generated structures with DFT (VASP, Quantum ESPRESSO) or a surrogate model.

## Verification

1. Generate 100 structures and compute validity / uniqueness / novelty.
2. Relax with a universal MLP (CHGNet, MACE) and check convex-hull distance.
3. Compare to known stable materials from Materials Project.
''',
        "references": [
            "https://github.com/microsoft/mattergen",
            "https://github.com/google-deepmind/materials_discovery",
            "https://github.com/jiaor17/DiffCSP",
            "https://github.com/txie-93/cdvae"
        ],
    },
    {
        "name": "scientific-data-formats",
        "title": "High-Performance Scientific Data Formats for GPU ML",
        "description": "Zarr, TensorStore, WebDataset, HDF5/NetCDF, KvikIO, and direct-to-GPU I/O pipelines.",
        "devin_body": '''
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
''',
        "references": [
            "https://zarr.dev/",
            "https://google.github.io/tensorstore/",
            "https://github.com/webdataset/webdataset",
            "https://xarray.dev/blog/gpu-pipeline"
        ],
    },
    {
        "name": "mamba-ssm-kernels",
        "title": "Mamba State-Space Model Kernels on GPU",
        "description": "Mamba-2/3 SSD kernels, fused selective scan, CuTe/Triton/TileLang backends, and chunk scheduling.",
        "devin_body": '''
## When to use

You are implementing or optimizing Mamba-style state-space models on GPU, especially for long-context or autoregressive inference.

## Key concepts

- **Mamba-2 SSD**: State-Space Duality; the five-kernel pipeline can be fused into one.
- **Selective scan**: linear-time recurrence with input-dependent state transitions.
- **Backends**: Triton (general), CuTe (`mamba3_step_fn`), TileLang (MIMO training).
- **Chunk scheduling**: chunk size impacts memory vs speed (e.g., static 128/256/512).

## Code pattern

```python
# PyTorch fused Mamba-2 SSD
from mamba_ssm import Mamba2
layer = Mamba2(d_model=1024, d_state=64, d_conv=4)
out = layer(x)
```

## Tuning notes

- Fused Triton SSD can be 1.5-2.5× faster than the unfused baseline.
- On Blackwell (sm_100), watch for `ptxas` register spilling; reduce `num_warps`.
- CuTe backend is best for low-latency autoregressive decode.

## Verification

1. Run `mamba2` forward and compare to a reference PyTorch selective scan.
2. Benchmark with different chunk sizes and plot latency vs memory.
3. On GB200, check for `ptxas C7907` and adjust autotune configs.
''',
        "references": [
            "https://pytorch.org/blog/accelerating-mamba2-with-kernel-fusion/",
            "https://github.com/state-spaces/mamba",
            "https://github.com/state-spaces/mamba/issues/904",
            "https://arxiv.org/abs/2604.10597v3"
        ],
    },
    {
        "name": "moe-grouped-gemm",
        "title": "MoE and Grouped GEMM on GPU",
        "description": "Grouped GEMM, MoE routing, cuBLAS/cuDNN/TransformerEngine/FlashInfer/vLLM backends.",
        "devin_body": '''
## When to use

You are implementing Mixture-of-Experts (MoE) layers or grouped GEMM for variable-size matrices.

## Key concepts

- **Grouped GEMM**: one kernel launch with multiple matrix shapes and per-matrix scaling.
- **MoE routing**: top-k gating, expert capacity, load balancing.
- **Backends**: cuBLASLt, CUTLASS, TransformerEngine, FlashInfer, vLLM `marlin`, TensorRT-LLM.
- **Blackwell**: TMA-based grouped GEMM with block-scaled FP4/FP8.

## Code pattern

```python
import torch
import triton

# vLLM MoE backend selection
# --moe-backend=marlin  # on GB10/sm_121
# --moe-backend=cutlass # on H100/B200
```

For cuBLAS grouped GEMM, see `cublasGemmGroupedBatchedEx`.

## Tuning notes

- On GB10, Marlin is currently the most reliable MoE backend.
- On B200, use FP4 grouped GEMM with TMA multicast.
- Load balancing losses prevent expert collapse.

## Verification

1. Run a small MoE layer and compare grouped GEMM to a loop of individual GEMMs.
2. Verify routing produces balanced expert assignment.
3. On B200, profile with Nsight Compute and check `tcgen05.mma` utilization.
''',
        "references": [
            "https://developer.nvidia.com/blog/introducing-grouped-gemm-apis-in-cublas-and-more-performance-updates/",
            "https://docs.nvidia.com/deeplearning/cudnn/latest/fe-oss-apis/gemm_fusions/grouped_gemm_quant_unified.html",
            "https://github.com/flashinfer-ai/flashinfer/pull/2725",
            "https://github.com/vllm-project/vllm/pull/43814"
        ],
    },
    {
        "name": "hopper-megatron-deepspeed",
        "title": "Megatron and DeepSpeed on Hopper",
        "description": "Large-model training with Megatron-Core, Megatron-FSDP, DeepSpeed ZeRO, and NVLink4 on H100/H200.",
        "devin_body": '''
## When to use

You are training or fine-tuning very large models (7B+) on H100/H200 clusters.

## Key concepts

- **Megatron-Core**: tensor, pipeline, and sequence parallelism.
- **Megatron-FSDP**: sharded data parallelism with optimizer state sharding.
- **DeepSpeed ZeRO**: ZeRO-1/2/3 and Offload++ for CPU/NVMe offloading.
- **NCCL user buffers**: overlap communication and compute.
- **NVLink 4**: 900 GB/s per GPU; NVSwitch Gen 3 for 8-GPU non-blocking all-reduce.

## Code pattern

```bash
# Megatron train command
torchrun --nproc_per_node=8 pretrain_gpt.py \
  --tensor-model-parallel-size 2 \
  --pipeline-model-parallel-size 2 \
  --use-flash-attn \
  --fp8-hybrid
```

## Tuning notes

- Set `CUDA_DEVICE_MAX_CONNECTIONS=1` to avoid stream bubbles on Hopper.
- Use BF16 or FP8 with Transformer Engine.
- For ZeRO-3, enable `contiguous_gradients` and `reduce_bucket_size` tuning.

## Verification

1. Run a small GPT 7B pretraining for 100 steps and check throughput (samples/s/GPU).
2. Verify no NCCL hangs in `NCCL_DEBUG=INFO`.
3. Compare Megatron-FSDP vs PyTorch FSDP memory and throughput.
''',
        "references": [
            "https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html",
            "https://docs.nvidia.com/megatron-core/developer-guide/latest/discussions/megatron-fsdp-user-guide/megatron-fsdp-user-guide.html",
            "https://github.com/microsoft/DeepSpeed/blob/master/blogs/deepspeed-offloadpp/README.md",
            "https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/"
        ],
    },
    {
        "name": "blackwell-dc-fp4-quantization",
        "title": "FP4/NVFP4/MXFP4 Quantization on Blackwell",
        "description": "Block-scaled 4-bit formats for training and inference on datacenter Blackwell.",
        "devin_body": '''
## When to use

You want to reduce memory and increase throughput using 4-bit formats on B200/GB200.

## Key concepts

- **NVFP4**: NVIDIA FP4 with hierarchical scaling. 16-element blocks with E4M3 scales + per-tensor FP32 scale.
- **MXFP4/MXFP8**: microscaling formats with 32-element blocks (MXFP8) or 16-element (MXFP4).
- **Block-scaled GEMM**: D = alpha * (SFA * A) * (SFB * B).
- **tcgen05.mma**: datacenter Blackwell path for FP4 GEMM.

## Code pattern

```python
# TransformerEngine FP8/NVFP4 linear
import transformer_engine.pytorch as te
linear = te.Linear(4096, 4096, params_dtype=torch.fp8)
```

For native PTX on sm_100, use `tcgen05.mma.kind::mxf4.block_scale`.

## Tuning notes

- NVFP4 can achieve 3.5× memory reduction vs FP16 with <1% accuracy loss.
- On consumer Blackwell (sm_120/121), native FP4 may be limited; use Marlin/MXFP4 fallback.
- Keep first and last layers in higher precision.

## Verification

1. Quantize a Llama-3-8B layer to NVFP4 and compare ppl to BF16.
2. Run a grouped GEMM with FP4 weights and FP32 accumulators.
3. Profile memory: KV cache should shrink 50% with FP4.
''',
        "references": [
            "https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/nvfp4/nvfp4.html",
            "https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/features/low_precision_training/mxfp8/mxfp8.html",
            "https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/",
            "https://github.com/NVIDIA/TensorRT-LLM/blob/main/tensorrt_llm/_torch/cute_dsl_kernels/blackwell/blockscaled_contiguous_grouped_gemm_swiglu_fusion.py"
        ],
    },
    {
        "name": "jax-pde-sciml",
        "title": "JAX for PDEs and Differentiable Scientific Computing",
        "description": "JAX-based SciML: Diffrax, Exponax, JAX-MD, neural operators, and differentiable simulations.",
        "devin_body": '''
## When to use

You are solving PDEs, ODEs, running differentiable MD, or implementing neural operators in JAX.

## Key concepts

- **Diffrax**: ODE/SDE/CDE solvers with JIT and AD support.
- **Exponax**: spectral PDE solvers for 46+ equations.
- **JAX-MD**: differentiable molecular dynamics.
- **JAX-FEM**: finite element analysis with AD.
- **Neural operators**: FNO, DeepONet, PINO.

## Code pattern

```python
import jax
import jax.numpy as jnp
from diffrax import Tsit5, ODETerm, diffeqsolve

def f(t, y, args):
    return -y

term = ODETerm(f)
sol = diffeqsolve(term, Tsit5(), t0=0, t1=1, dt0=0.1, y0=1.0)
```

## Tuning notes

- Use `jax.vmap` for batched trajectories.
- For long rollouts, use `jax.lax.scan` instead of Python loops.
- `jax.jit` can compile the whole solver; use `saveat` to avoid storing all intermediates.

## Verification

1. Solve a linear ODE and compare to analytic solution.
2. Train an FNO on 1D Burgers and compare to finite-difference.
3. Run JAX-MD energy minimization and compare to a reference MD package.
''',
        "references": [
            "https://docs.kidger.site/diffrax/",
            "https://github.com/ceyron/exponax",
            "https://github.com/jax-md/jax-md",
            "https://github.com/deepmodeling/jax-fem"
        ],
    },
    {
        "name": "distributed-launch-slurm-mpi",
        "title": "Distributed Launch: SLURM, torchrun, MPI, and UCX",
        "description": "Launching multi-node PyTorch/JAX training with SLURM, torchrun, MPI, CUDA-aware MPI, and UCX.",
        "devin_body": '''
## When to use

You are running distributed training on a cluster and need to choose/configure the launcher.

## Key concepts

- **torchrun**: PyTorch native; auto-sets RANK, WORLD_SIZE, LOCAL_RANK, MASTER_ADDR.
- **srun (SLURM)**: direct process spawning; set env vars manually.
- **mpirun (Open MPI / MVAPICH2)**: for HPC workloads.
- **CUDA-aware MPI**: pass GPU buffers directly without staging.
- **UCX**: transports `rc` (RDMA), `sm` (shared memory), `cuda_copy`, `cuda_ipc`, `gdr_copy`.

## Code pattern

```bash
# SLURM + torchrun
srun --nodes=2 --ntasks-per-node=8 --gpus-per-node=8 \
  torchrun --nnodes=2 --nproc_per_node=8 train.py
```

For MPI:

```bash
mpirun -np 16 -x LD_LIBRARY_PATH -x NCCL_DEBUG=INFO \
  -bind-to none -map-by ppr:8:node ./train_mpi
```

## Tuning notes

- Set `UCX_TLS=rc,sm,cuda_copy,cuda_ipc` for InfiniBand.
- For MNNVL/GB200: `UCX_CUDA_IPC_ENABLE_MNNVL=1`.
- Use `--gpu-bind=none` in SLURM unless you want explicit GPU binding.

## Verification

1. Run `nccl-tests/all_reduce_perf` with your launcher.
2. Check `NCCL_DEBUG=INFO` ranks and chosen transports.
3. Confirm each process sees the correct `LOCAL_RANK` and GPU.
''',
        "references": [
            "https://docs.pytorch.org/tutorials/intermediate/ddp_series_multinode.html",
            "https://docs.nersc.gov/machinelearning/launchers/",
            "https://developer.nvidia.com/blog/introduction-cuda-aware-mpi/",
            "https://docs.nvidia.com/multi-node-nvlink-systems/multi-node-tuning-guide/ucx.html"
        ],
    },
    {
        "name": "cuquantum-tensornet",
        "title": "cuQuantum cuStateVec and cuTensorNet Simulation",
        "description": "GPU-accelerated quantum simulation: state vector, tensor network, expectation values, and gradients.",
        "devin_body": '''
## When to use

You are simulating quantum circuits at scale (many qubits) or computing expectation values/gradients for VQE/QAOA.

## Key concepts

- **cuStateVec**: GPU state vector simulator with gate fusion and batched ops.
- **cuTensorNet**: tensor network contractions, exact and approximate (MPS) simulation.
- **Multi-GPU**: distributed state vector (`mgpu`) for 33+ qubits.
- **Expectation + gradients**: `cutensornetExpectationComputeWithGradientsBackward`.

## Code pattern

```python
import cuquantum
import cuquantum.cutensornet as cutn

# Create a tensor network state and compute an expectation value
handle = cutn.create()
# ... build state, add gates, compute
```

For Python high-level usage, use the `cudaq` `tensornet` target.

## Tuning notes

- cuTensorNet hyper-sampling finds good contraction paths.
- For Clifford circuits, use `stim` backend instead of state vector.
- Gate fusion reduces memory movement in cuStateVec.

## Verification

1. Run a 20-qubit GHZ and compare state vector to a CPU simulator.
2. Compute a 1D TFIM expectation value and compare to exact diagonalization.
3. For VQE, check gradient converges with parameter shift.
''',
        "references": [
            "https://docs.nvidia.com/cuda/cuquantum/latest/custatevec/overview/index.html",
            "https://docs.nvidia.com/cuda/cuquantum/latest/cutensornet/overview.html",
            "https://docs.nvidia.com/cuda/cuquantum/latest/cutensornet/examples/expectation-gradient.html",
            "https://developer.nvidia.com/cuquantum-sdk"
        ],
    },
]
