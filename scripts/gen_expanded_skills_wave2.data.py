SKILLS = [
    {
        "name": "dgx-spark-uma-tuning",
        "title": "DGX Spark UMA Memory and Thermal Tuning",
        "description": "Tuning DGX Spark's 128 GB unified LPDDR5X memory, page cache competition, thermal throttling, EC firmware, and CPU compilation flags.",
        "devin_body": '''
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
''',
        "references": [
            "https://docs.nvidia.com/dgx/dgx-spark-porting-guide/optimization.html",
            "https://nvidia.custhelp.com/app/answers/detail/a_id/5728",
            "https://forums.developer.nvidia.com/t/nvidia-dgx-spark-gb10-thermal-throttling-fan-curve-fix-via-ec-firmware-rollback/377069",
            "https://github.com/llvm/llvm-project/commit/84e54515bc4e9dd4938121f4df7cc27bb89a0a43"
        ],
    },
    {
        "name": "dgx-spark-multinode-roce",
        "title": "Multi-Node DGX Spark with RoCE",
        "description": "Connect 2-3 DGX Sparks over QSFP RoCE, NCCL configuration, Docker host networking, and no GPUDirect RDMA.",
        "devin_body": '''
## When to use

You want to run distributed training or inference across multiple DGX Spark systems.

## Key concepts

- **ConnectX-7**: each Spark has two QSFP56 ports, each with two logical partitions. Up to 200 Gbps per link.
- **No switch needed for 2-3 nodes**: direct QSFP cabling. 4+ nodes require a switch.
- **No GPUDirect RDMA on GB10**: UMA memory cannot be exposed for RDMA. Use `cudaHostAlloc` + `ib_reg_mr` fallback.
- **NCCL_IB_HCA is required**: otherwise NCCL may silently fall back to TCP.
- **Docker `--network=host`**: simplifies RoCE in containers.

## Code pattern

```bash
# Check RoCE interfaces
ip a show enp1s0f0np0
rdma link

# Set jumbo frames
sudo nmcli con modify cx7-cluster 802-3-ethernet.mtu 9000

# Launch container
export NCCL_SOCKET_IFNAME=enp1s0f0np0,enp1s0f1np1
export NCCL_IB_HCA=rocep1s0f0,rocep1s0f1
export NCCL_IB_GID_INDEX=3
export NCCL_IB_DISABLE=0
docker run -it --rm --gpus all --network=host --device=/dev/infiniband \
  --ulimit memlock=-1 $IMAGE
```

## Tuning notes

- Use one cable per link. Two cables do not double bandwidth.
- Keep cluster traffic on ConnectX-7 interfaces; management on 10GbE.
- For 3-node mesh, cable Port 0 of one to Port 1 of the next.

## Verification

1. `ping -M do -s 8972 <peer>` confirms jumbo frames.
2. Run `nccl-tests/all_reduce_perf` and check RDMA is used (not TCP).
3. Capture `NCCL_DEBUG=INFO` and verify `IB` transport and HCA selection.
''',
        "references": [
            "https://docs.nvidia.com/dgx/dgx-spark/spark-clustering.html",
            "https://docs.nvidia.com/sync/latest/cluster-assistant.html",
            "https://forums.developer.nvidia.com/t/two-dgx-sparks-over-the-connectx-7-direct-link-setup-notes/376298",
            "https://nvidia.custhelp.com/app/answers/detail/a_id/5780"
        ],
    },
    {
        "name": "flashattention-4-sm121",
        "title": "FlashAttention-4 on DGX Spark (SM121)",
        "description": "FlashAttention-4 consumer Blackwell support on sm_120/sm_121: paged KV, head_dim limits, FP8, and the CuTe DSL dispatch path.",
        "devin_body": '''
## When to use

You are running vLLM/SGLang on a DGX Spark or RTX 50-series and want to use the FlashAttention-4 CuTe DSL backend for attention.

## Key concepts

- **sm_120/121 path**: uses SM80-style `mma.sync.m16n8k16` with cp.async, no WGMMA, no tcgen05, no TMEM.
- **SMEM budget**: 99 KB per block (vs 163 KB on SM80, 228 KB on Hopper).
- **TMA**: single-CTA only, no multicast.
- **Paged KV**: implemented with in-kernel page table resolution (PR #2348).
- **FP8 KV cache decode**: supported for e4m3/e5m2, ~1.6-1.9× at GQA ratio ≤4.
- **FA4 in vLLM**: opt-in via `--attention-backend FLASH_ATTN_4`; `enforce_eager=True` required.

## Code pattern

```bash
# vLLM with FA4 on SM120/SM121
vllm serve model --attention-backend FLASH_ATTN_4 --enforce-eager
```

If using the downstream bundle:

```python
import flash_attn_4
out, _ = flash_attn_4.flash_attn_func(q, k_paged, v_paged, page_table=page_table, causal=True)
```

## Tuning notes

- `head_dim` 64 and 128 are best; 256 works but uses smaller tiles.
- `head_dim > head_dim_v` is routed to non-TMA to avoid hangs.
- Clear Triton cache when switching between FA versions: `rm -rf ~/.triton/cache`.

## Verification

1. Run `flash_attn_varlen_func` with a small paged KV tensor and compare to a reference attention.
2. Check vLLM logs that `FLASH_ATTN_4` backend is active.
3. Benchmark throughput vs `FLASHINFER` and vs `TRITON_ATTN`.
''',
        "references": [
            "https://github.com/Dao-AILab/flash-attention/pull/2634",
            "https://github.com/Dao-AILab/flash-attention/pull/2348",
            "https://huggingface.co/SecondNatureComputing/flash-attn-4-sm120",
            "https://github.com/vllm-project/vllm/pull/40110"
        ],
    },
    {
        "name": "llm-inference-gb10",
        "title": "LLM Inference on DGX Spark (GB10)",
        "description": "vLLM and TensorRT-LLM inference on GB10: FP8 KV, Marlin, MTP, MoE backend selection, and driver 580.x.",
        "devin_body": '''
## When to use

You are serving LLMs on a DGX Spark and need to choose quantization, attention backend, and MoE backend.

## Key concepts

- **FP8 KV cache**: safe and recommended; saves 50% KV memory.
- **NVFP4 not recommended on GB10**: native kernels are immature; Marlin/MXFP4 is more stable.
- **CUTLASS FP4 is broken on sm_121**: produces silent garbage (row-identical wrong values).
- **Marlin works**: set `VLLM_MARLIN_USE_ATOMIC_ADD=1` and `--moe-backend=marlin`.
- **MTP speculative decoding**: Qwen3.6/Gemma 4/Nemotron 3.5 Lightning; pair with FP8 KV.
- **Driver 580.x**: 590.x has CUDAGraph deadlock and UMA memory leak; pin it.

## Code pattern

```python
from vllm import LLM

llm = LLM(
    model="Qwen/Qwen3-35B-A3B",
    quantization="fp8",
    kv_cache_dtype="fp8",
    gpu_memory_utilization=0.85,
    attention_backend="TRITON_ATTN",
    moe_backend="marlin",
    enable_prefix_caching=True,
    enforce_eager=False,
)
```

## Tuning notes

- `max-cudagraph-capture-size=2048` is required for full throughput.
- `--attention-backend=TRITON_ATTN` is safer than FlashInfer on sm_121 for some FP8 paths.
- Use `mxfp4` only with gpt-oss pre-quantized checkpoints.

## Verification

1. Run a known-answer benchmark (e.g., OpenLLM leaderboard subset) and compare to BF16.
2. Check output for row-identical garbage (sign of CUTLASS FP4).
3. Monitor `nvidia-smi dmon` for thermal and power under sustained load.
''',
        "references": [
            "https://conselara.dev/notes/vllm-dgx-spark-sm121-gotchas/",
            "https://conselara.dev/notes/dgx-spark-gb10-hardware-reference/",
            "https://forums.developer.nvidia.com/t/guide-deepseek-v4-flash-on-2x-dgx-spark-gb10/374742",
            "https://github.com/vllm-project/vllm/pull/40923"
        ],
    },
    {
        "name": "ampere-a100-scientific",
        "title": "Ampere A100 for Scientific ML and HPC",
        "description": "A100 architecture, TF32, structured sparsity, MIG, FP64, and cuBLAS/cuDNN paths for scientific workloads.",
        "devin_body": '''
## When to use

You are running scientific ML or HPC on A100 (sm_80) or A6000/RTX 30-series (sm_86) and want to use TF32, sparsity, or MIG.

## Key concepts

- **A100 (sm_80)**: 3rd-gen Tensor Cores, HBM2e, MIG, 9.7 TFLOPS FP64.
- **TF32**: FP32 dynamic range with 10-bit mantissa. Enable in PyTorch with `torch.backends.cuda.matmul.allow_tf32 = True` and `torch.backends.cudnn.allow_tf32 = True`.
- **Structured sparsity**: 2:4 pattern in cuSPARSELt for 2× throughput.
- **MIG**: partition A100 into up to 7 isolated GPU instances.
- **sm_86 (A6000/RTX 3090)**: 100 KB SMEM, 48 warps/SM, no MIG, lower FP64.

## Code pattern

```python
import torch
# Enable TF32
 torch.backends.cuda.matmul.allow_tf32 = True
 torch.backends.cudnn.allow_tf32 = True

x = torch.randn(4096, 4096, device='cuda')
# cuBLAS will use TF32 Tensor Cores automatically
```

## Tuning notes

- TF32 is not appropriate for numerically sensitive scientific computing; disable with `torch.backends.cuda.matmul.allow_tf32 = False`.
- For MIG, choose profile based on workload (e.g., 20G MIG for GROMACS MD).
- NHWC layout is preferred for Tensor Core convolutions on Ampere.

## Verification

1. Run `nvidia-smi` and confirm GPU product name and compute capability.
2. Benchmark FP32 GEMM with and without TF32 and compare throughput.
3. If using MIG, verify the correct MIG instance is visible inside the container.
''',
        "references": [
            "https://www.nvidia.com/content/dam/en-zz/Solutions/Data-Center/nvidia-ampere-architecture-whitepaper.pdf",
            "https://developer.nvidia.com/blog/accelerating-ai-training-with-tf32-tensor-cores/",
            "https://docs.nvidia.com/cuda/cusparselt/",
            "https://docs.nvidia.com/datacenter/tesla/pdf/MIG_User_Guide.pdf"
        ],
    },
    {
        "name": "mixed-precision-training-gpu",
        "title": "Mixed Precision Training on NVIDIA GPUs",
        "description": "BF16, FP16, FP8, TF32, FP32 master weights, loss scaling, and when to use each on Ampere/Hopper/Blackwell.",
        "devin_body": '''
## When to use

You are training deep learning models and want to choose the right precision and scaling strategy for your GPU.

## Key concepts

- **BF16**: 8 exponent / 7 mantissa bits. FP32-like range, no loss scaling needed. Best on Ampere+.
- **FP16**: 5 exponent / 10 mantissa bits. Needs dynamic loss scaling to avoid underflow/overflow.
- **FP32 master weights**: store optimizer state in FP32; forward/backward in lower precision.
- **FP8**: E4M3 forward, E5M2 backward. Use Transformer Engine with current, delayed, or blockwise scaling.
- **TF32**: not a storage format; FP32 matmul uses Tensor Cores. Default on Ampere+.

## Code pattern

```python
import torch
from torch.amp import autocast, GradScaler

scaler = GradScaler()
for x, y in loader:
    with autocast(device_type='cuda', dtype=torch.bfloat16):
        loss = model(x, y)
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

## Tuning notes

- Keep softmax, LayerNorm, and first/last layers in FP32 for stability.
- Use BF16 on A100/H100/Blackwell; FP16 on V100/T4.
- For FP8, use Transformer Engine and enable blockwise scaling if accuracy regresses.

## Verification

1. Train a small ResNet/Transformer with each format and compare final loss and throughput.
2. Check no NaN/Inf in gradients when using FP16 with loss scaling.
3. Profile memory: lower precision should reduce activation and weight footprint.
''',
        "references": [
            "https://docs.nvidia.com/deeplearning/performance/mixed-precision-training/index.html",
            "https://pytorch.org/blog/what-every-user-should-know-about-mixed-precision-training-in-pytorch/",
            "https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/",
            "https://huggingface.co/docs/transformers/mixed_precision_training"
        ],
    },
    {
        "name": "nsight-profiling-gpu",
        "title": "Nsight Compute and Nsight Systems Profiling",
        "description": "Nsight Compute sections/metrics, Nsight Systems gap analysis, hardware CUDA trace, and Tile profiling for cuTile.",
        "devin_body": '''
## When to use

You need to profile GPU kernels and identify memory vs compute bottlenecks, occupancy, register pressure, or gaps in a CUDA graph.

## Key concepts

- **Nsight Compute**: section-based profiling. Key sections: ComputeWorkloadAnalysis, MemoryWorkloadAnalysis, Occupancy, InstructionStats.
- **Nsight Systems**: application-level tracing. Use `--trace=cuda-hw` on Blackwell for hardware event system trace.
- **Tile profiling**: Nsight Compute 2026.1+ has a Tile section for cuTile/CUDA Tile kernels.
- **Serialization**: Nsight Compute serializes kernel launches by default; use Range Replay for concurrent kernels.

## Code pattern

```bash
# Nsight Compute
ncu -o profile.ncu-rep --set full ./my_kernel

# Nsight Systems
nsys profile --trace=cuda-hw --cuda-graph-trace=graph -o profile.nsys-rep ./train.py

# Nsight Python
nsys profile --trace=cuda,nvtx,osrt,python -o profile.nsys-rep python train.py
```

## Tuning notes

- A memory-bound kernel has high `memory__bytes` relative to compute; increase data reuse or occupancy.
- A compute-bound kernel has high `sm__pipe_tensor_cycles_active`; check tensor core utilization.
- Register spilling shows up as `sass__inst_executed_register_spilling` in Nsight Compute 2026.1+.

## Verification

1. Profile a GEMM kernel and confirm tensor core utilization is >80%.
2. Run Nsight Systems on a training step and identify the largest GPU idle gap.
3. For cuTile, verify the Tile section appears in Nsight Compute with driver 580.126.09+.
''',
        "references": [
            "https://docs.nvidia.com/nsight-compute/ProfilingGuide/index.html",
            "https://docs.nvidia.com/nsight-systems/UserGuide/index.html",
            "https://docs.nvidia.com/nsight-compute/ReleaseNotes/topics/library-support-tile.html",
            "https://developer.nvidia.com/nsight-compute-2026_1-new-features"
        ],
    },
    {
        "name": "cutlass-persistent-kernels",
        "title": "CUTLASS Persistent and Warp-Specialized Kernels",
        "description": "CUTLASS 3.x persistent kernels, cooperative vs ping-pong schedule, warp specialization, and CollectiveBuilder for FP8/FP4.",
        "devin_body": '''
## When to use

You are writing high-performance GEMM kernels with CUTLASS 3.x/4.x and want to use persistent scheduling or block-scaled FP8/FP4.

## Key concepts

- **Cooperative schedule**: two consumer warpgroups work on the same output tile split along M. Cannot hide epilogue.
- **Ping-pong schedule**: two consumer warpgroups work on different tiles; can hide epilogue behind math.
- **Warp specialization**: producer warps load data (TMA/cp.async), consumer warps do MMA.
- **CollectiveBuilder**: composes mainloop and epilogue for block-scaled FP8/FP4.
- **SM100 vs SM120**: SM100 uses tcgen05/TMA multicast; SM120/121 uses `mma.sync` and cluster size 1.

## Code pattern

```cpp
// Ping-pong schedule on Hopper/Blackwell
using KernelSchedule = cutlass::gemm::KernelTmaWarpSpecializedPingpong;

// CollectiveBuilder for block-scaled FP8
using CollectiveMainloop = typename cutlass::gemm::collective::CollectiveBuilder<
    ArchTag, OperatorClass, ElementA, LayoutA, AlignmentA,
    ElementB, LayoutB, AlignmentB, ElementAccumulator,
    TileShape, ClusterShape, StageCount, KernelSchedule>::CollectiveOp;
```

## Tuning notes

- Persistent kernels amortize launch overhead and improve occupancy.
- SMEM limits: 164 KB (A100), 228 KB (H100), 99 KB (sm_120/121), 228 KB (sm_100).
- CUTLASS 4.4.0 adds SM121 support; CuTe DSL may need `sm_121a` patch.

## Verification

1. Build a CUTLASS example (e.g., `49_collective_builder`) and compare to cuBLAS.
2. Check Nsight Compute for high tensor core utilization and low launch overhead.
3. On GB10, verify the kernel does not use tcgen05/TMEM (will fail to load).
''',
        "references": [
            "https://docs.nvidia.com/cutlass/latest/media/docs/cpp/gemm_api_3x.html",
            "https://github.com/NVIDIA/cutlass/blob/main/examples/48_hopper_warp_specialized_gemm/48_hopper_warp_specialized_gemm.cu",
            "https://github.com/NVIDIA/cutlass/blob/main/examples/49_hopper_gemm_with_collective_builder/49_collective_builder.cu",
            "https://docs.nvidia.com/cutlass/4.4.0/CHANGELOG.html"
        ],
    },
    {
        "name": "molecular-dynamics-gpu",
        "title": "Molecular Dynamics with ML Potentials on GPU",
        "description": "MACE, CHGNet, DeePMD-kit, LAMMPS/GROMACS integration, and multi-GPU spatial decomposition for ML potentials.",
        "devin_body": '''
## When to use

You are running molecular dynamics with learned interatomic potentials on GPU.

## Key concepts

- **MACE**: higher-order equivariant message passing; supports cuEquivariance (3× speedup), LAMMPS MLIAP.
- **CHGNet**: charge-informed universal GNN potential; trained on Materials Project trajectories.
- **DeePMD-kit**: deep learning package for many-body potentials; interfaces with LAMMPS, GROMACS, OpenMM, AMBER.
- **cuEquivariance**: NVIDIA library for fast equivariant operations.
- **GROMACS-DeePMD**: domain-decomposed GPU inference; 66% strong scaling at 16 GPUs for 15k atoms.

## Code pattern

```python
# ASE + MACE
from mace.calculators import mace_mp
from ase import Atoms
atoms = Atoms(...)
calc = mace_mp(model="medium", device="cuda", default_dtype="float32")
atoms.calc = calc
```

LAMMPS input:

```
pair_style deepmd graph.pb
pair_coeff * * H O
```

## Tuning notes

- Use FP32 for energies/forces; FP16 can lose precision.
- MACE-MH-1 is a multi-head foundation model covering 89 elements.
- For multi-GPU MD, use spatial decomposition in LAMMPS with 1 MPI rank per GPU.

## Verification

1. Run a 1 ns MD of a small system and compare energy drift to a reference.
2. Compare MACE/CHGNet forces to DFT on a snapshot.
3. Benchmark strong scaling from 1 to 8 GPUs.
''',
        "references": [
            "https://github.com/ACEsuit/mace",
            "https://github.com/CederGroupHub/chgnet",
            "https://github.com/deepmodeling/deepmd-kit",
            "https://arxiv.org/abs/2602.02234",
            "https://github.com/tummfm/chemtrain-deploy"
        ],
    },
    {
        "name": "geospatial-remote-sensing-ml",
        "title": "Geospatial and Remote Sensing ML on GPU",
        "description": "Prithvi, SatMAE, TorchGeo, TerraTorch, segment-anything for Earth observation, and NVIDIA cuOpt.",
        "devin_body": '''
## When to use

You are training or deploying geospatial foundation models on GPU for satellite/aerial imagery.

## Key concepts

- **Prithvi**: NASA/IBM geospatial foundation model on HLS data; supports temporal and location embeddings.
- **SatMAE**: masked autoencoder on temporal Sentinel-2.
- **TorchGeo**: PyTorch domain library with 100+ CRS-aware datasets, multispectral transforms, pretrained weights.
- **TerraTorch**: fine-tuning framework built on TorchGeo + Lightning for GFMs.
- **SamGeo**: Segment Anything for GeoTIFF/TMS data.
- **cuOpt**: GPU VRP/TSP/PDPTW solver with RAPIDS cuDF.

## Code pattern

```python
import torchgeo
from torchgeo.trainers import SemanticSegmentationTask
from torchgeo.datasets import EuroSAT

# Use a pretrained Prithvi or DOFA backbone
```

For TerraTorch:

```bash
pip install terratorch
```

## Tuning notes

- Chunk size and I/O are usually the bottleneck; use Zarr/COG/Tar streaming and many DataLoader workers.
- Multispectral input may require 6/13 channels, not 3.
- Use `bfloat16` for fine-tuning; keep normalization in FP32.

## Verification

1. Run a small EuroSAT or So2Sat classification benchmark.
2. Fine-tune Prithvi on a flood/wildfire segmentation task and compare IoU.
3. Profile data loading vs compute with Nsight Systems.
''',
        "references": [
            "https://torchgeo.org/",
            "https://huggingface.co/ibm-nasa-geospatial/Prithvi-100M",
            "https://samgeo.gishub.org/",
            "https://docs.nvidia.com/cuopt/",
            "https://arxiv.org/abs/2412.02732v3"
        ],
    },
    {
        "name": "bioinformatics-genomics-ml",
        "title": "Bioinformatics and Genomics ML on GPU",
        "description": "DNABERT, Enformer, single-cell analysis with scVI/scGPT, and RAPIDS cuDF for genomics pipelines.",
        "devin_body": '''
## When to use

You are training or deploying genomics models on GPU, such as DNA sequence models, gene expression models, or single-cell analysis.

## Key concepts

- **DNABERT/DNABERT-2**: BERT on DNA k-mer/BPE tokens for promoter, splice site, TFBS prediction.
- **Enformer**: transformer for gene expression and chromatin states from DNA, 200 kb context.
- **scVI**: single-cell Variational Inference for scRNA-seq.
- **scGPT**: foundation model for single-cell multi-omics.
- **RAPIDS cuDF/cuML**: GPU-accelerated dataframes and ML for large genomics tables.

## Code pattern

```python
# scVI
import scvi
scvi.model.SCVI.setup_anndata(adata, layer="counts")
model = scvi.model.SCVI(adata)
model.train(accelerator="gpu", devices=1)
```

DNABERT:

```bash
python run_finetune.py --model_type dna --tokenizer_name dna6 \
  --model_name_or_path zhihan1996/DNABERT-2-117M
```

## Tuning notes

- Long-context genomics models can use FlashAttention for >2k sequences.
- Single-cell data is sparse; use highly variable gene selection and count layers.
- For RAPIDS, ensure `cudf` version matches CUDA.

## Verification

1. Fine-tune DNABERT-2 on a GUE benchmark and compare to reported metrics.
2. Run scVI on a 100k-cell dataset and compare latent structure to CPU.
3. Use cuDF to load a large Parquet genomics table and compare wall time to pandas.
''',
        "references": [
            "https://github.com/jerryji1993/DNABERT",
            "https://github.com/magics-lab/dnabert_2",
            "https://docs.scvi-tools.org/",
            "https://github.com/bowang-lab/scGPT",
            "https://developer.nvidia.com/blog/analyzing-the-rna-sequence-of-1-3m-mouse-brain-cells-with-rapids-on-nvidia-gpus/"
        ],
    },
    {
        "name": "cuda-tile-advanced-gb10",
        "title": "Advanced CUDA Tile / cuTile on GB10",
        "description": "cuTile Python/C++ advanced features: block-scaled `ct.mma_scaled`, Tile IR, persistent kernels, and Nsight Tile profiling.",
        "devin_body": '''
## When to use

You are writing or optimizing tile-based GPU programs with cuTile Python/CUDA Tile, especially block-scaled FP8/FP4 or persistent matmul.

## Key concepts

- **`@ct.kernel`**: entry point; `ct.load`, `ct.store`, `ct.mma`, `ct.mma_scaled`.
- **`ct.mma_scaled`**: block-scaled MMA. Scale block sizes: 16/32 for FP4, 32 for FP8.
- **Tile IR**: virtual ISA; source ↔ Tile IR ↔ SASS correlation in Nsight Compute (future).
- **Persistent kernels**: fewer tile blocks process multiple output tiles.
- **Nsight Tile profiling**: Tile section in Nsight Compute 2026.1+.

## Code pattern

```python
import cuda.tile as ct
import torch

@ct.kernel
def scaled_matmul(A, A_s, B, B_s, C, Ks: int):
    # load tiles, compute scaled MMA
    a = ct.load(A, ...)
    a_s = ct.load(A_s, ...)
    b = ct.load(B, ...)
    b_s = ct.load(B_s, ...)
    acc = ct.mma_scaled(a, a_s, b, b_s, ct.zeros(...))
    ct.store(C, acc)
```

## Tuning notes

- cuTile Python currently supports Ampere, Ada, Blackwell (sm_100 and sm_120/121).
- Match scale tensor layout to expected TMA swizzle (e.g., `Swizzle32x4x4`).
- For persistent kernels, choose tile shapes that fit SMEM (99 KB on sm_121).

## Verification

1. Compile and run the cuTile `MatMul.py` sample.
2. Compare a cuTile FP8 matmul to `torch.matmul` with FP8 weights.
3. Profile with Nsight Compute and inspect the Tile section.
''',
        "references": [
            "https://docs.nvidia.com/cuda/cutile-python/",
            "https://docs.nvidia.com/cuda/cutile-python/generated/cuda.tile.mma_scaled.html",
            "https://docs.nvidia.com/cuda/tile-ir/latest/",
            "https://developer.nvidia.com/blog/how-to-write-high-performance-matrix-multiply-in-nvidia-cuda-tile/"
        ],
    },
    {
        "name": "pytorch-blackwell-deployment",
        "title": "PyTorch Deployment on Blackwell",
        "description": "PyTorch nightly wheels, sm_100/sm_120 support, architecture detection, and common Blackwell-specific errors.",
        "devin_body": '''
## When to use

You are installing or debugging PyTorch on B200/GB200 (sm_100) or RTX 50-series/DGX Spark (sm_120/sm_121).

## Key concepts

- **PyTorch 2.7+ with CUDA 12.8+** is required for Blackwell.
- **Nightly wheels**: `pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/cu128`.
- **sm_100 vs sm_120**: datacenter vs consumer; binaries are not interchangeable.
- **No `sm_120a`**: consumer Blackwell has no `a` variant.
- **Common errors**: "sm_120 is not compatible" from old CUDA 12.1 binaries; DDP segfaults on sm_120; FP4 cast kernels missing.

## Code pattern

```bash
pip install --pre torch --index-url https://download.pytorch.org/whl/nightly/cu128
```

Check:

```python
import torch
print(torch.cuda.get_arch_list())
print(torch.cuda.get_device_properties(0))
```

## Tuning notes

- For `sm_120a` suffix stripping bug, set `TORCH_CUDA_ARCH_LIST="12.0a"`.
- `CUDA_FORCE_PTX_JIT=1` can test PTX compatibility.
- Use `torch.compile` with `max-autotune` for best Blackwell kernels.

## Verification

1. `torch.cuda.is_available()` and `get_arch_list()` show the target arch.
2. Run a small FP16 GEMM and compare to `torch._scaled_mm` with FP8.
3. Run `torch.compile` on a simple model and confirm it generates Triton/CuTeDSL kernels.
''',
        "references": [
            "https://discuss.pytorch.org/t/pytorch-support-for-sm120/216099",
            "https://github.com/pytorch/pytorch/issues/172807",
            "https://discuss.pytorch.org/t/solved-rtx-5090-sm-120-training-segfault-ddp-was-the-cause/224584",
            "https://docs.nvidia.com/cuda/blackwell-compatibility-guide/"
        ],
    },
    {
        "name": "quantization-backends-gpu",
        "title": "LLM Quantization Backends on NVIDIA GPUs",
        "description": "AWQ, GPTQ, AutoRound, Marlin, FP8, NVFP4, MXFP4, and backend selection for A100/H100/L40S/RTX50/GB10.",
        "devin_body": '''
## When to use

You are quantizing or serving LLMs with reduced precision and need to pick the right method and backend for the GPU.

## Key concepts

- **AWQ**: activation-aware, protects 1% salient weights, ~10 min for 8B.
- **GPTQ**: Hessian-based, slower, supports 2/3/4-bit.
- **AutoRound**: sign-gradient descent, minimal tuning, exports to GPTQ/AWQ/GGUF.
- **Marlin**: optimized FP16×INT4 kernel for Ampere+ (sm_80+).
- **FP8**: E4M3/E5M2, good for H100/Blackwell.
- **NVFP4**: NVIDIA native 4-bit with hierarchical scaling; best on B200/GB200.
- **MXFP4**: cross-platform microscaling 4-bit, works on AMD and NVIDIA.

## Code pattern

```python
# AutoRound
from transformers import AutoModelForCausalLM
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-2-7b",
    quantization_config=AutoRoundConfig(bits=4, group_size=128)
)

# vLLM Marlin
vllm serve model --quantization gptq_marlin --moe-backend marlin
```

## Tuning notes

- A100/H100: FP8/Marlin for memory-bound; INT4 for larger models.
- L40S: good for 7B-30B INT4/Marlin.
- RTX 50/GB10: Marlin is most reliable; NVFP4/MXFP4 need specific checkpoints.
- Backend priority: AutoRound selects Marlin > ExLLaMAV2 > Triton.

## Verification

1. Quantize a 7B model with AWQ and GPTQ and compare perplexity.
2. Serve with vLLM and measure throughput at batch 1 and 16.
3. Verify no garbage output with Marlin and no CUTLASS FP4 path on sm_121.
''',
        "references": [
            "https://huggingface.co/docs/transformers/en/quantization/selecting",
            "https://github.com/intel/auto-round",
            "https://github.com/IST-DASLab/marlin",
            "https://developer.nvidia.com/blog/introducing-nvfp4-for-efficient-and-accurate-low-precision-inference/",
            "https://arxiv.org/abs/2509.23202v3"
        ],
    },
]
