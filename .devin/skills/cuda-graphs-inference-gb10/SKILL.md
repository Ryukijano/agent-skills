---
name: cuda-graphs-inference-gb10
description: >-
  Capture and replay CUDA graphs for low-latency inference pipelines on GB10. Covers stream capture, graph instantiation, launch, and kernel node parameter updates.
---

# CUDA Graphs for Inference on GB10 DGX Spark

## Overview

CUDA graphs remove most host launch overhead by recording a sequence of kernels/memcpy once and replaying it. This is critical for small-batch inference where kernel execution time is short.

## Capture pattern

```cpp
cudaGraph_t graph;
cudaGraphExec_t execGraph;
cudaStream_t capStream;
cudaStreamCreate(&capStream);

cudaStreamBeginCapture(capStream, cudaStreamCaptureModeGlobal);
scale_kernel<<<blocks, threads, 0, capStream>>>(d_in, d_tmp, scale, n);
add_bias_kernel<<<blocks, threads, 0, capStream>>>(d_tmp, d_out, d_bias, n);
relu_kernel<<<blocks, threads, 0, capStream>>>(d_out, d_tmp, n);
cudaMemcpyAsync(d_out, d_tmp, n * sizeof(float), cudaMemcpyDeviceToDevice, capStream);
cudaStreamEndCapture(capStream, &graph);

cudaGraphInstantiate(&execGraph, graph, nullptr, nullptr, 0);
cudaGraphLaunch(execGraph, 0);
cudaDeviceSynchronize();
```

## Update node params without rebuild

```cpp
cudaKernelNodeParams params;
cudaGraphExecKernelNodeGetParams(execGraph, scaleNode, &params);
params.kernelParams = new_args;
cudaGraphExecKernelNodeSetParams(execGraph, scaleNode, &params);
```

## When graphs help

- Small N / small batch where launch overhead dominates.
- Static topologies (same sequence of ops every step).
- Not a win for single huge kernels or dynamic control flow.

## Verification

Run the same pipeline without a graph and compare the output elementwise.

## Reference

- `cuda-blackwell-labs/projects/39_cuda_graphs_inference/`
- https://docs.nvidia.com/cuda/cuda-c-programming-guide/index.html#cuda-graphs

