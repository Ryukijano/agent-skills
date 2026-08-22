# Qiskit Workflow Run

1. Confirm env: conda activate quantum_qiskit; check pinned versions.
2. Build circuit; use Estimator for energies, Sampler for distributions — no deprecated run syntax.
3. Transpile with optimization_level=3, seed_transpiler=42; log depth + count_ops before claiming NISQ feasibility.
4. VQE: JW mapping + SPSA (noisy) or L-BFGS (statevector); SQD: sample→project→diagonalize subspace.
5. Always report classical baseline (PySCF/DFT) next to quantum results; acceptance bar <5% alignment.
6. Save raw result JSONs + all seeds; plots from committed script.

Apply `qiskit-quantum-workflows`, `reproducibility`, `experiment-tracking`.
