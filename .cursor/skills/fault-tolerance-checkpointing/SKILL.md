# Fault Tolerance and Checkpointing at Scale

## Description

PyTorch DCP, DeepSpeed elastic training, asynchronous checkpointing, and multi-tier checkpoint storage.

## When to use

You are running long or large-scale distributed training and need to recover from failures.

## Key concepts

- **PyTorch DCP**: Distributed Checkpoint, `torch.distributed.checkpoint`, async checkpointing.
- **Elastic training**: `torchrun` with `--rdzv_id`, `--max_restarts`.
- **DeepSpeed**: DSElasticAgent, universal checkpoints, ZeRO optimizer state.
- **Checkpoint content**: model, optimizer, scheduler, RNG, step.
- **Storage tiers**: local NVMe/PMEM → `$SCRATCH` → permanent object storage.

## Code pattern

```python
import torch.distributed.checkpoint as dcp

dcp.save(state_dict, checkpoint_id=f"checkpoint/{step}")
```

DeepSpeed:

```bash
deepspeed --num_gpus 8 train.py --deepspeed ds_config.json
```

## Tuning notes

- Checkpoint frequency balances lost work vs overhead.
- Use async checkpointing to avoid blocking training.
- Store RNG state for exact reproducibility.

## Verification

1. Kill a training job mid-run and resume; confirm loss matches no-interruption curve.
2. Measure checkpoint write bandwidth to `$SCRATCH` vs object storage.
3. Run an elastic training job and simulate a worker failure.

## References

- https://pytorch.org/docs/stable/distributed.checkpoint.html
- https://www.deepspeed.ai/
- https://pytorch.org/docs/stable/elastic/run.html
- https://docs.mila.quebec/examples/good_practices/checkpointing/
