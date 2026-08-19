# Ray for Distributed ML

## Description

Ray Train, Ray Tune, Ray Serve, Ray Data, and Ray clusters for scaling training, tuning, serving, and data processing.

## When to use

You want to scale PyTorch/TensorFlow/HF training, hyperparameter search, or serving across a Ray cluster.

## Key concepts

- **Ray Train**: `TorchTrainer`, `ScalingConfig`, distributed data-parallel training.
- **Ray Tune**: distributed HPO with ASHA/Hyperband, integrates with Ray Train.
- **Ray Serve**: model composition, dynamic batching, multi-GPU inference.
- **Ray Data**: scalable data loading and preprocessing with GPU actors.
- **Ray Clusters**: `ray start --head`, `ray submit`, autoscaling.

## Code pattern

```python
import ray
from ray.train.torch import TorchTrainer
from ray.train import ScalingConfig

ray.init()

def train_func(config):
    # training loop
    pass

trainer = TorchTrainer(
    train_loop_per_worker=train_func,
    scaling_config=ScalingConfig(num_workers=4, use_gpu=True)
)
result = trainer.fit()
```

## Tuning notes

- Use `RAY_TRAIN_V2_ENABLED=1` for the new Ray Train V2 API.
- Tune with `ASHAScheduler` for early stopping.
- `ray.init(address="auto")` on a cluster; `ray.init()` for local testing.

## Verification

1. Start a local Ray cluster and run a `TorchTrainer` with 2 workers.
2. Run a small Tune search and confirm multiple trials execute in parallel.
3. Check `ray status` shows expected GPU usage.

## References

- https://docs.ray.io/en/latest/train/train.html
- https://docs.ray.io/en/latest/tune/index.html
- https://docs.ray.io/en/latest/serve/index.html
- https://docs.ray.io/en/latest/data/data.html
