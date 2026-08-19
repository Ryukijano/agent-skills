# Megatron and DeepSpeed on Hopper

## Description

Large-model training with Megatron-Core, Megatron-FSDP, DeepSpeed ZeRO, and NVLink4 on H100/H200.

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
torchrun --nproc_per_node=8 pretrain_gpt.py   --tensor-model-parallel-size 2   --pipeline-model-parallel-size 2   --use-flash-attn   --fp8-hybrid
```

## Tuning notes

- Set `CUDA_DEVICE_MAX_CONNECTIONS=1` to avoid stream bubbles on Hopper.
- Use BF16 or FP8 with Transformer Engine.
- For ZeRO-3, enable `contiguous_gradients` and `reduce_bucket_size` tuning.

## Verification

1. Run a small GPT 7B pretraining for 100 steps and check throughput (samples/s/GPU).
2. Verify no NCCL hangs in `NCCL_DEBUG=INFO`.
3. Compare Megatron-FSDP vs PyTorch FSDP memory and throughput.

## References

- https://docs.nvidia.com/megatron-core/developer-guide/latest/user-guide/parallelism-guide.html
- https://docs.nvidia.com/megatron-core/developer-guide/latest/discussions/megatron-fsdp-user-guide/megatron-fsdp-user-guide.html
- https://github.com/microsoft/DeepSpeed/blob/master/blogs/deepspeed-offloadpp/README.md
- https://docs.nvidia.com/deeplearning/transformer-engine/user-guide/
