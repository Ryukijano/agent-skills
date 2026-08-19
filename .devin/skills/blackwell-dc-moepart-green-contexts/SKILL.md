# MLOPart, Green Contexts, and Disaggregated Serving on Blackwell

## Description

Resource partitioning (MLOPart, Green Contexts, MPS) and disaggregated prefill/decode serving for datacenter Blackwell.

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

## References

- https://developer.nvidia.com/blog/boost-gpu-memory-performance-with-no-code-changes-using-nvidia-cuda-mps/
- https://developer.nvidia.com/blog/nvidia-cuda-13-1-powers-next-gen-gpu-programming-with-nvidia-cuda-tile-and-performance-gains/
- https://docs.nvidia.com/cuda/cuda-programming-guide/04-special-topics/green-contexts.html
- https://developer.nvidia.com/blog/how-nvidia-gb200-nvl72-and-nvidia-dynamo-boost-inference-performance-for-moe-models/
