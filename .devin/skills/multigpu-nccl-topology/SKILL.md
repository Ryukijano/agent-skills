# Multi-GPU Topology and NCCL Tuning

## Description

NCCL, NVLink/NVSwitch, PCIe, InfiniBand/RoCE, GPUDirect, and common topology hang fixes.

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

## References

- https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/env.html
- https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/performance_and_tuning.html
- https://developer.nvidia.com/blog/understanding-nccl-tuning-to-accelerate-gpu-to-gpu-communication/
- https://docs.nvidia.com/datacenter/cloud-native/gpu-operator/latest/gpu-operator-rdma.html
