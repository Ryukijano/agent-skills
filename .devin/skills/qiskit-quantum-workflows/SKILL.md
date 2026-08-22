---
name: qiskit-quantum-workflows
description: Qiskit 2.x quantum simulation workflows — circuits, Estimator/Sampler primitives, VQE/SQD chemistry patterns, Aer noise models, and transpilation discipline.
---

## Qiskit Quantum Workflows

Distilled from the NQCC 2025 hackathon (H2-on-Ni SQD/VQE vs DFT). Conda env `quantum_qiskit`.

### Primitives (Qiskit 2.x — not the old run syntax)
```python
from qiskit.primitives import StatevectorEstimator, StatevectorSampler
estimator = StatevectorEstimator()          # expectation values
sampler  = StatevectorSampler()             # measurement samples
job = estimator.run([(qc, obs)])
```
- Use `Estimator` for energies/gradients; `Sampler` for distributions (SQD sample loops).
- For hardware-realistic noise: `qiskit_aer.noise.NoiseModel.from_backend(fake_backend)`.

### Chemistry patterns
- **VQE**: `qiskit_nature.second_q` drivers → `JordanWignerMapper`; optimize with SPSA (noise-robust) or L-BFGS (statevector only).
- **SQD**: sample bitstrings from a chemically-motivated ansatz, project + diagonalize in the selected subspace; compare against PySCF/DFT baseline (<5% alignment was our acceptance bar).
- Always report against the classical reference: DFT/FCI numbers next to every quantum result.

### Transpilation discipline
- `transpile(qc, backend, optimization_level=3, seed_transpiler=42)` — fix the seed for reproducibility.
- Check `qc.count_ops()` depth before claiming NISQ feasibility; log circuit depth per experiment.

### Reproducibility & reporting
- Pin versions (`qiskit`, `qiskit-aer`, `qiskit-nature`) in env lock.
- Save raw result objects (`result.json`) + seeds; plots regenerate via committed script.
- Depth-analysis scripts live beside notebooks (see Team_15 repo pattern).

Related: `reproducibility`, `experiment-tracking`.
