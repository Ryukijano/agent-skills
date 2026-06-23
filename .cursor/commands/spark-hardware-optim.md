# Spark / L40S Optimization Pass

1. Profile current run (util, memory timeline).
2. Try expandable_segments + bfloat16 autocast.
3. Reduce T or backbone size as controlled experiment.
4. Increase workers / prefetch if CPU bound.
5. For multi-GPU: confirm NCCL settings and barriers.
6. Re-measure and record the delta (throughput or max batch).

Apply `spark-hardware-optim`, `debug-pytorch-gpu`.
