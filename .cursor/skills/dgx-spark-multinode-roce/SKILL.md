# Multi-Node DGX Spark with RoCE

## Description

Connect 2-3 DGX Sparks over QSFP RoCE, NCCL configuration, Docker host networking, and no GPUDirect RDMA.

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
docker run -it --rm --gpus all --network=host --device=/dev/infiniband   --ulimit memlock=-1 $IMAGE
```

## Tuning notes

- Use one cable per link. Two cables do not double bandwidth.
- Keep cluster traffic on ConnectX-7 interfaces; management on 10GbE.
- For 3-node mesh, cable Port 0 of one to Port 1 of the next.

## Verification

1. `ping -M do -s 8972 <peer>` confirms jumbo frames.
2. Run `nccl-tests/all_reduce_perf` and check RDMA is used (not TCP).
3. Capture `NCCL_DEBUG=INFO` and verify `IB` transport and HCA selection.

## References

- https://docs.nvidia.com/dgx/dgx-spark/spark-clustering.html
- https://docs.nvidia.com/sync/latest/cluster-assistant.html
- https://forums.developer.nvidia.com/t/two-dgx-sparks-over-the-connectx-7-direct-link-setup-notes/376298
- https://nvidia.custhelp.com/app/answers/detail/a_id/5780
