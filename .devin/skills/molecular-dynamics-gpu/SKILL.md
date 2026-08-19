# Molecular Dynamics with ML Potentials on GPU

## Description

MACE, CHGNet, DeePMD-kit, LAMMPS/GROMACS integration, and multi-GPU spatial decomposition for ML potentials.

## When to use

You are running molecular dynamics with learned interatomic potentials on GPU.

## Key concepts

- **MACE**: higher-order equivariant message passing; supports cuEquivariance (3× speedup), LAMMPS MLIAP.
- **CHGNet**: charge-informed universal GNN potential; trained on Materials Project trajectories.
- **DeePMD-kit**: deep learning package for many-body potentials; interfaces with LAMMPS, GROMACS, OpenMM, AMBER.
- **cuEquivariance**: NVIDIA library for fast equivariant operations.
- **GROMACS-DeePMD**: domain-decomposed GPU inference; 66% strong scaling at 16 GPUs for 15k atoms.

## Code pattern

```python
# ASE + MACE
from mace.calculators import mace_mp
from ase import Atoms
atoms = Atoms(...)
calc = mace_mp(model="medium", device="cuda", default_dtype="float32")
atoms.calc = calc
```

LAMMPS input:

```
pair_style deepmd graph.pb
pair_coeff * * H O
```

## Tuning notes

- Use FP32 for energies/forces; FP16 can lose precision.
- MACE-MH-1 is a multi-head foundation model covering 89 elements.
- For multi-GPU MD, use spatial decomposition in LAMMPS with 1 MPI rank per GPU.

## Verification

1. Run a 1 ns MD of a small system and compare energy drift to a reference.
2. Compare MACE/CHGNet forces to DFT on a snapshot.
3. Benchmark strong scaling from 1 to 8 GPUs.

## References

- https://github.com/ACEsuit/mace
- https://github.com/CederGroupHub/chgnet
- https://github.com/deepmodeling/deepmd-kit
- https://arxiv.org/html/2602.02234
- https://github.com/tummfm/chemtrain-deploy
