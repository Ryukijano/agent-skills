# Model Serving on GPU

## Description

Triton Inference Server, TensorRT-LLM, vLLM, TorchServe, FastAPI, and BentoML for production inference.

## When to use

You need to deploy a trained model for low-latency, high-throughput inference on GPU.

## Key concepts

- **Triton Inference Server**: multi-backend, batched, multi-GPU. Supports vLLM and TensorRT-LLM backends.
- **TensorRT-LLM**: compile and serve LLMs with inflight batching, paged attention, FP8/FP4.
- **vLLM**: PagedAttention, continuous batching, easy OpenAI-compatible API.
- **TorchServe**: PyTorch-native serving with model archiving and A/B testing.
- **BentoML**: full ML serving platform with packaging and monitoring.

## Code pattern

```bash
# vLLM serve
vllm serve meta-llama/Llama-2-7b --tensor-parallel-size 1

# Triton with TensorRT-LLM backend
python TensorRT-LLM/triton_backend/scripts/launch_triton_server.py   --model_repo=TensorRT-LLM/triton_backend/all_models/llmapi/
```

## Tuning notes

- TensorRT-LLM gives 20-40% higher throughput after compile time; vLLM is faster to deploy.
- Use `--gpu-memory-utilization` carefully on UMA systems.
- For mixed model serving, Triton can host multiple backends in one server.

## Verification

1. Send a sample request to the server and measure latency at batch 1 and 16.
2. Verify throughput (tokens/s) matches expected for the GPU.
3. Check `nvidia-smi` for GPU utilization and memory.

## References

- https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/vllm_backend/README.html
- https://docs.nvidia.com/deeplearning/triton-inference-server/user-guide/docs/tensorrtllm_backend/README.html
- https://docs.vllm.ai/
- https://pytorch.org/serve/
