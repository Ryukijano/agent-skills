# JAX on NVIDIA GPUs for Scientific ML

## Description

JAX `jit`, `vmap`, `shard_map`, device meshes, and XLA memory tuning on H100/H200/Blackwell/L40S.

## When to use

You are writing scientific ML (PINNs, neural operators, molecular/weather models) in JAX and running on NVIDIA GPUs.

## Key concepts

- **Functional transformations**: `jax.jit`, `jax.grad`, `jax.vmap`, `jax.scan`.
- **Sharding**: `Mesh`, `PartitionSpec` (`P`), `NamedSharding`. JAX automatically generates SPMD XLA HLO.
- **XLA flags**: `XLA_PYTHON_CLIENT_PREALLOCATE`, `XLA_PYTHON_CLIENT_MEM_FRACTION`, `XLA_FLAGS`.
- **`jax.distributed`**: multi-node initialization; uses NCCL under the hood.

## Code pattern

```python
import jax
import jax.numpy as jnp
from jax.sharding import Mesh, NamedSharding, PartitionSpec as P

mesh = Mesh(jax.devices().reshape(2, 4), ('data', 'model'))
sharding = NamedSharding(mesh, P('data', 'model'))
x = jax.device_put(jnp.ones((1024, 1024)), sharding)
```

## Tuning notes

- `XLA_PYTHON_CLIENT_PREALLOCATE=false` helps on UMA/GB10 where GPU and CPU share memory.
- `jax_default_matmul_precision = 'bfloat16'` can speed training.
- On multi-node, set `NCCL_NVLS_ENABLE=1` for H100 NVLink4.

## Verification

1. `jax.devices()` shows the expected number of GPUs.
2. `jax.debug.visualize_array_sharding(x)` shows the intended layout.
3. Run a small `jax.jit(jnp.einsum)` and check XLA HLO for all-reduce.

## References

- https://docs.jax.dev/en/latest/parallel.html
- https://docs.jax.dev/en/latest/jax.sharding.html
- https://docs.jax.dev/en/latest/multi_process.html
- https://docs.jax.dev/en/latest/gpu_memory_allocation.html
