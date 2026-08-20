| name | quantum-error-correction-theory |
|------|------|
| description | Reference for quantum error correction (QEC) theory, fault-tolerant quantum computing, and quantum neural network foundations. Use when the user asks about qubit error correction, fusion-based quantum computation, trapped-ion quantum processors, equivariant quantum neural networks, or Krylov diagonalization on quantum hardware. |

# Quantum Error Correction & Fault-Tolerant Quantum Computing Theory

## Prerequisites

1. Familiarity with basic quantum computing (qubits, gates, stabilizer formalism) is assumed.
2. This skill is reference-only: it summarizes source papers stored in the Drive `Research_and_papers` folder and the `Quantum_error_correction` NotebookLM notebook. It does not execute code.

## Core Rules

- **[IMPORTANT] Cite sources**: When answering questions using this skill, reference the specific paper (by DOI suffix, e.g. `s41534-023-00753-1`) so the user can trace claims back to source material.
- **Do not fabricate results**: If a claim is not explicitly supported by one of the reference papers below, say so rather than inventing a number.
- **Prefer the NotebookLM notebook** (`Quantum_error_correction`) for deep-dive Q&A across these sources; this skill file is a lightweight index/router.

## Reference Papers Indexed

| Paper | Key Contribution |
|---|---|
| s41534-023-00753-1 (npj Quantum Information) | Core QEC theory: repetition codes, stabilizer formalism, CSS codes (Steane/Shor), transversal gates, Eastin-Knill theorem, magic state distillation |
| s41586-026-10676-4 | 98-qubit trapped-ion quantum computer with all-to-all connectivity — relevant to scalable QEC architectures |
| Theory for Equivariant Quantum Neural Networks | Group-theoretic framework for building symmetry-aware QNNs, relevant to quantum ML architecture design |
| s41567-025-02883-z (Nature Physics) | Shows quantum neural networks form Gaussian processes in certain limits — theoretical tool for understanding QNN expressivity/trainability |
| s41467-023-36493-1 (Nat. Comms) | Fusion-based quantum computation — an alternative measurement-based approach to fault tolerance |
| s41467-025-59716-z (Nat. Comms) | Krylov diagonalization of large many-body Hamiltonians on a quantum processor — near-term algorithm for simulating quantum systems |
| s41467-020-16930-1 (Nat. Comms) | Coherent control of rotational orientation states for gas-surface interaction modeling — quantum control benchmark |
| s41567-026-03298-0 (Nature Physics) | Quantum Fisher information in a strange metal — metrology/sensing angle on many-body quantum systems |
| s44196-025-00833-4 | Supplementary theoretical results (see Drive folder for full text) |

## Usage Pattern

When a user asks about QEC or fault-tolerant quantum computing:

1. Identify which reference paper(s) above are most relevant to the question.
2. Summarize the relevant finding in your own words (never reproduce more than a short quote verbatim, per copyright policy).
3. Point the user to the `Quantum_error_correction` NotebookLM notebook (or the Drive `Research_and_papers` folder) for the full source PDF if they want to go deeper.
4. If the question is about implementing QEC codes in code (e.g. Qiskit, Cirq), route to a code-execution skill/environment rather than trying to write untested quantum circuits from memory.

## Related Skills

- `quantum-ml-foundations` (equivariant QNNs, Gaussian process theory)
- `materials-science-database` (for solid-state/quantum materials papers)
