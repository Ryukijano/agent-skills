---
name: performance-optimization
description: >-
  Systematic performance optimization: profile, identify bottlenecks, optimize,
  measure. Use when speeding up code or reducing memory usage.
---

# Performance Optimization

## The Cycle
1. Profile → 2. Analyze → 3. Optimize → 4. Measure → 5. Repeat

## Profiling Tools
- Python: cProfile, line_profiler, memory_profiler, py-spy
- PyTorch: torch.profiler, torch.cuda.Event
- System: perf, valgrind

## Common Optimizations
- Algorithmic: O(n^2) → O(n log n) — biggest wins
- Caching/memoization
- Vectorization (NumPy/torch ops vs Python loops)
- Batching, lazy loading, parallelism

## PyTorch-Specific
- torch.compile(), mixed precision (amp), DataLoader workers
- Gradient checkpointing, cudnn.benchmark=True

## Anti-Patterns
- Optimizing without profiling
- Premature optimization
- Micro-optimizing when algorithmic improvements exist
