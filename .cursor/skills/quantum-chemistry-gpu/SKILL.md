# Quantum Chemistry and Quantum ML on GPU

## Description

GPU-accelerated DFT, Hartree-Fock, coupled cluster with PySCF/GPU4PySCF, and hybrid quantum-classical ML.

## When to use

You are running electronic structure calculations or hybrid quantum-classical ML on GPU.

## Key concepts

- **GPU4PySCF**: CUDA plugin for PySCF; 1000× speedup on A100 for DFT with density fitting.
- **Methods**: SCF, DFT, MP2, CCSD, geometry optimization, frequency analysis.
- **Quantum ML**: VQE, QAOA, quantum kernels, PennyLane, Qiskit.
- **Datasets**: QM9, MD17, GMTKN55, Materials Project.
- **Hybrid**: PySCF active space + Qiskit Nature VQE.

## Code pattern

```python
from gpu4pyscf.scf import RHF

mol = pyscf.M(atom='H 0 0 0; H 0 0 0.74', basis='def2-tzvp')
mf = RHF(mol)
mf.kernel()
```

Quantum ML:

```python
import pennylane as qml
dev = qml.device("default.qubit", wires=2)
@qml.qnode(dev, interface="torch")
def circuit(params):
    qml.RX(params[0], wires=0)
    qml.CNOT(wires=[0, 1])
    return qml.expval(qml.PauliZ(1))
```

## Tuning notes

- Use density fitting for large systems to reduce ERI cost.
- GPU4PySCF supports SCF/DFT and some post-HF; coupled cluster may still be CPU.
- Quantum ML on classical simulators is limited to <50 qubits without tensor network tricks.

## Verification

1. Run a DFT single point and compare energy to CPU PySCF.
2. Optimize a small molecule and compare bond lengths to experimental data.
3. Run a small VQE on H2 and compare exact ground-state energy.

## References

- https://pyscf.org/user/gpu.html
- https://pennylane.ai/
- https://qiskit.org/ecosystem/nature/
- https://doi.org/10.48550/arxiv.2602.02234
