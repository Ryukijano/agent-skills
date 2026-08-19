# Molecular ML and Drug Discovery on GPU

## Description

Equivariant GNNs, ML potentials, molecular docking (DiffDock), and generative molecule design on GPU.

## When to use

You are training or deploying models for molecular property prediction, docking, or protein-ligand design on NVIDIA GPUs.

## Key concepts

- **Equivariant GNNs**: SchNet, DimeNet, GemNet, MACE, NequIP; preserve SE(3)/E(3) symmetry.
- **cuEquivariance**: NVIDIA library giving 10× end-to-end speedup for MACE.
- **ML potentials**: MACE, CHGNet, DeePMD-kit for large MD with learned forces.
- **DiffDock/GeoDiff**: diffusion for molecular docking and conformer generation.
- **RFDiffusion**: protein backbone design.

## Code pattern

```python
import cuequivariance as cue
# Use a built-in MACE kernel
from cuequivariance_tutorial import mace_layer
```

For MD with MLP:

```python
# LAMMPS input: pair_style neuroev, pair_coeff * * CHGNet.pt
```

## Tuning notes

- Use `bfloat16` or `fp32`; `fp16` can lose precision for energies/forces.
- cuEquivariance is preferred over e3nn for large GPU workloads.
- For MD, strong scaling peaks around 16-32 GPUs for ~15k atoms.

## Verification

1. Train SchNet on QM9 and check MAE per property.
2. Run DiffDock-L on a PDBBind split and compute top-1 RMSD<2Å.
3. Run a 1 ns MACE MD step and compare forces to DFT.

## References

- https://developer.nvidia.com/cuequivariance
- https://github.com/ACEsuit/mace
- https://github.com/gcorso/DiffDock
- https://github.com/RosettaCommons/RFDiffusion
