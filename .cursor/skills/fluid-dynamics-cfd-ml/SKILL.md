# Fluid Dynamics and CFD ML on GPU

## Description

Neural operators, PhysicsNeMo (Modulus), JAX-Fluids, PhiFlow, and surrogate CFD on GPU.

## When to use

You want to build surrogate models for fluid dynamics or accelerate CFD with ML and GPUs.

## Key concepts

- **Neural operators**: FNO, DeepONet, GraphCast, L-ESHyRA.
- **Differentiable CFD**: JAX-Fluids, PhiFlow, PhysicsNeMo (Modulus).
- **Turbulence modeling**: LES, RANS closures, PINNs for turbulence.
- **Surrogate CFD**: train on simulation data, deploy for fast inference.
- **Datasets**: Darcy flow, 2D turbulence, DrivAerML, ERA5.

## Code pattern

```python
import jaxfluids

# JAX-Fluids fully-differentiable compressible Navier-Stokes
```

For FNO:

```python
from neuralop.models import FNO

fno = FNO(n_modes=(16, 16), hidden_channels=64, in_channels=1, out_channels=1)
fno = fno.to('cuda')
```

## Tuning notes

- FNO works best on regular grids; use GNNs or point-cloud methods for unstructured meshes.
- Physics-informed loss can improve generalization but increases training cost.
- For production, deploy with TensorRT/TorchScript for low-latency inference.

## Verification

1. Train FNO on 2D Navier-Stokes and compare to reference solver at test time.
2. Run a JAX-Fluids simulation and verify conservation properties.
3. Profile surrogate vs CFD wall time for the same geometry.

## References

- https://github.com/tumaer/jaxfluids
- https://tum-pbs.github.io/PhiFlow/
- https://developer.nvidia.com/PhysicsNeMo
- https://github.com/neuraloperator/neuraloperator
