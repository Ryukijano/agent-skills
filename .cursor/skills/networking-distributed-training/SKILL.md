# Networking for Distributed Training

## Description

InfiniBand, RoCE, NCCL tuning, AWS EFA, and diagnosing multi-node network issues.

## When to use

You are running multi-node distributed training and need to optimize the interconnect.

## Key concepts

- **InfiniBand**: lowest latency, highest bandwidth, RDMA; needs Subnet Manager.
- **RoCEv2**: RDMA over Ethernet; needs PFC/ECN for lossless.
- **NCCL tuning**: `NCCL_IB_HCA`, `NCCL_SOCKET_IFNAME`, `NCCL_BUFFSIZE`.
- **AWS EFA**: `aws-ofi-nccl` plugin, `FI_EFA_USE_DEVICE_RDMA=1`.
- **Diagnostics**: `ibstat`, `ibstatus`, `ethtool`, `nccl-tests`.

## Code pattern

```bash
# NCCL with IB
export NCCL_IB_HCA=mlx5_0,mlx5_1
export NCCL_IB_GID_INDEX=3
export NCCL_SOCKET_IFNAME=eth0
mpirun -np 8 python train.py
```

## Tuning notes

- Use `NCCL_DEBUG=INFO` to verify transport.
- For AWS EFA, use the `aws-ofi-nccl` plugin.
- MTU 9000 for RoCE; check with `ping -M do -s 8972`.

## Verification

1. Run `nccl-tests/all_reduce_perf` and confirm bandwidth.
2. `NCCL_DEBUG=INFO` shows `IB` or `NET/IB` being used.
3. `ibstat` or `rdma link` shows link up.

## References

- https://docs.nvidia.com/deeplearning/nccl/user-guide/docs/troubleshooting/networking_troubleshooting.html
- https://github.com/aws/aws-ofi-nccl
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa-start-nccl.html
- https://github.com/NVIDIA/nccl-tests
