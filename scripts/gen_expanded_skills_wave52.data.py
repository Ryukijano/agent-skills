SKILLS = [
    {
        "name": "cudaq-algorithms",
        "title": "CUDA-Q Algorithms",
        "description": "Build and compose fault-tolerant quantum programs with the CUDA-Q Algorithms library: Pauli LCU, qubitization, QSVT, Trotter, state preparation, and quantum chemistry utilities.",
        "devin_body": r'''## When to use

You are designing or prototyping fault-tolerant quantum algorithms on CUDA-Q and need reusable, composable primitives rather than writing circuit construction from scratch.

## Usage

- **Block encodings**: encode a Hamiltonian as a unitary with `PauliLCU` or custom `BlockEncoding` objects.
- **Qubitization**: build a walk operator from an encoding and measure Chebyshev moments with `Walk`.
- **QSVT**: apply polynomial transformations to a block-encoded matrix.
- **Trotterization**: simulate time evolution of a Hamiltonian.
- **State preparation**: prepare Hartree–Fock or Givens-rotation Slater determinants inside a CUDA-Q kernel.
- **Quantum chemistry**: connect PySCF integrals to Jordan–Wigner Hamiltonians and ground-state workflows.

## Steps

1. Install `cudaq-algorithms` alongside `cudaq` (`pip install cudaq-algorithms`).
2. Import `PauliLCU`, `Walk`, `QSVT`, `Trotter`, and state-prep utilities.
3. Build a Hamiltonian from a Pauli dictionary or from PySCF molecular integrals.
4. Create a `BlockEncoding`, then compose it with `Walk` or `QSVT` inside a `@cudaq.kernel`.
5. Set a CUDA-Q target (`qpp-cpu`, `nvidia`, etc.) and run/verify against a classical reference.

## Code pattern

```python
import cudaq
import numpy as np
from cudaq_algorithms import PauliLCU, Walk

@cudaq.kernel
def main():
    q = cudaq.qvector(2)

# Block-encode a Pauli Hamiltonian
hamiltonian = {"ZZ": 0.5, "XI": 0.3, "IX": 0.3}
encoding = PauliLCU(hamiltonian)
walk = Walk(encoding)

state = np.array([1, 0, 0, 0], dtype=complex)
moments = walk.moments(state, 4)
print(moments)
```

## Tuning notes

- Choose the encoding (Pauli LCU vs. double factorization) to match your Hamiltonian sparsity and the target number of logical qubits.
- Use `qpp-cpu` for algorithm validation before moving to `nvidia` or physical backends.
- Capture large molecular integrals as numpy arrays and pass them into the CUDA-Q kernel with the `BlockEncoding` interface.

## Verification

1. Compare Chebyshev moments to a dense matrix calculation.
2. Verify ground-state energies against full configuration interaction for a small molecule.
3. Test the same workflow with two different block encodings to ensure they give consistent results.
''',
        "references": [
            "https://github.com/NVIDIA/cudaq-algorithms",
            "https://nvidia.github.io/cudaq-algorithms/",
            "https://nvidia.github.io/cuda-quantum/blogs/blog/2026/08/18/cudaq-algorithms-0.1/",
        ],
    },
    {
        "name": "pauli-lcu-encoding",
        "title": "Pauli LCU Block Encoding",
        "description": "Use the linear-combination-of-unitaries (LCU) block encoding for Pauli Hamiltonians in CUDA-Q Algorithms.",
        "devin_body": r'''## When to use

You need to block-encode a Hamiltonian expressed as a weighted sum of Pauli strings so it can be used by qubitization, QSVT, or other quantum signal-processing routines.

## Usage

- Encode a Pauli Hamiltonian dictionary into a unitary that acts on the system plus an ancilla register.
- Query the subnormalization factor `alpha` and the unitary list for manual inspection or custom kernels.
- Compose the encoding with `Walk` or `QSVT` primitives.

## Steps

1. Represent the Hamiltonian as a dictionary mapping Pauli strings to real coefficients, e.g. `{"ZZ": 0.5, "XI": 0.3}`.
2. Create `PauliLCU(hamiltonian)`.
3. Inspect `encoding.alpha` and `encoding.unitaries`.
4. Pass `encoding` to `Walk(encoding)` or a custom `BlockEncoding`-aware kernel.

## Code pattern

```python
from cudaq_algorithms import PauliLCU

hamiltonian = {"ZZ": 0.5, "XI": 0.3, "IX": 0.3}
encoding = PauliLCU(hamiltonian)
print("alpha =", encoding.alpha)
print("unitaries =", encoding.unitaries)
```

## Tuning notes

- Keep the number of Pauli terms and the subnormalization factor small to reduce ancilla and gate costs.
- Pauli LCU is convenient for spin/qubit Hamiltonians; for chemistry, consider double factorization for larger systems.

## Verification

1. Reconstruct the encoded Hamiltonian from the block encoding and compare to the input coefficients.
2. Verify the `alpha` matches the sum of absolute Pauli coefficients.
3. Compose with `Walk` and check that Chebyshev moments reproduce the Hamiltonian spectrum on a small system.
''',
        "references": [
            "https://nvidia.github.io/cudaq-algorithms/",
            "https://github.com/NVIDIA/cudaq-algorithms",
            "https://arxiv.org/abs/1511.02306",
        ],
    },
    {
        "name": "qubitization-walk",
        "title": "Qubitization and Walk Operators",
        "description": "Build qubitization walk operators from a block encoding and measure Chebyshev moments in CUDA-Q Algorithms.",
        "devin_body": r'''## When to use

You want to perform quantum signal processing on a block-encoded Hamiltonian, such as measuring Chebyshev moments for a Krylov eigensolver or preparing an approximate ground state.

## Usage

- Construct `Walk(encoding)` from any `BlockEncoding`.
- Compute `walk.moments(state, k)` to sample `<T_k(H/alpha)>`.
- Use the moments as input to a classical Krylov or filtering algorithm.

## Steps

1. Prepare or obtain a `BlockEncoding` (`PauliLCU`, custom, etc.).
2. Create `Walk(encoding)`.
3. Provide an initial state (numpy array or CUDA-Q kernel).
4. Measure the first `k` Chebyshev moments.
5. Post-process the moments classically (e.g., Lanczos/Krylov).

## Code pattern

```python
from cudaq_algorithms import PauliLCU, Walk
import numpy as np

encoding = PauliLCU({"ZZ": 0.5, "XI": 0.3, "IX": 0.3})
walk = Walk(encoding)
state = np.array([1, 0, 0, 0], dtype=complex)
moments = walk.moments(state, 4)
```

## Tuning notes

- Choose the moment order `k` to balance resolution of the spectrum with circuit depth.
- Ensure the initial state has overlap with the target eigenstate.

## Verification

1. Compare measured moments to dense linear-algebra Chebyshev moments for the same Hamiltonian.
2. Run on `qpp-cpu` and verify convergence as `k` increases.
3. Cross-check the ground-state energy from a Krylov solve against exact diagonalization.
''',
        "references": [
            "https://nvidia.github.io/cudaq-algorithms/",
            "https://github.com/NVIDIA/cudaq-algorithms",
            "https://arxiv.org/abs/1610.0653",
        ],
    },
    {
        "name": "quantum-singular-value-transformation",
        "title": "Quantum Singular Value Transformation",
        "description": "Apply polynomial transformations to block-encoded matrices with QSVT in CUDA-Q Algorithms.",
        "devin_body": r'''## When to use

You need to apply a polynomial function to a matrix (or its inverse, square root, filter, etc.) encoded as a block of a larger unitary.

## Usage

- Build a `QSVT` object from a `BlockEncoding` and a polynomial phase sequence.
- Embed the resulting kernel in a user-defined `@cudaq.kernel`.
- Use it for Hamiltonian simulation, matrix inversion, eigenstate filtering, or signal processing.

## Steps

1. Obtain a `BlockEncoding` for the target matrix.
2. Design a polynomial phase sequence (Chebyshev / Jacobi-Anger expansion) for the desired function.
3. Create `QSVT(encoding, phases)` and compose it with a state-preparation kernel.
4. Execute and post-select or measure the desired observable.

## Code pattern

```python
from cudaq_algorithms import QSVT, PauliLCU
import numpy as np

encoding = PauliLCU({"ZZ": 0.5, "XI": 0.3, "IX": 0.3})
phases = np.array([...])  # angles for target polynomial
qsvt = QSVT(encoding, phases)
```

## Tuning notes

- Degree and phase-angle precision dominate approximation error and circuit depth.
- For Hamiltonian simulation, use Jacobi-Anger expansion of the exponential.
- For eigenstate filtering, use a high-degree polynomial with sharp transition.

## Verification

1. Compare the transformed matrix to the target polynomial computed classically on a small instance.
2. Verify unitarity and the block structure of the constructed kernel.
3. Test that the output state overlaps with the expected filtered state.
''',
        "references": [
            "https://nvidia.github.io/cudaq-algorithms/",
            "https://arxiv.org/abs/2105.02859",
            "https://github.com/NVIDIA/cudaq-algorithms",
        ],
    },
    {
        "name": "trotterization-cudaq",
        "title": "Trotterization with CUDA-Q Algorithms",
        "description": "Simulate Hamiltonian time evolution using Trotter-Suzuki decomposition in CUDA-Q Algorithms.",
        "devin_body": r'''## When to use

You need a short-time or long-time evolution of a qubit or fermionic Hamiltonian and want a first- or higher-order Trotter circuit.

## Usage

- Decompose the Hamiltonian into local terms and build a Trotter circuit.
- Control the step size, order, and number of Trotter steps.
- Integrate state preparation into the same `@cudaq.kernel`.

## Steps

1. Define or import the Hamiltonian as Pauli strings or from a chemistry workflow.
2. Instantiate `Trotter(hamiltonian, order, trotter_steps)`.
3. Optionally prepare an initial state with a CUDA-Q kernel.
4. Set a CUDA-Q target and sample/expectation values at the final time.

## Code pattern

```python
from cudaq_algorithms import Trotter

hamiltonian = {"ZZ": 0.5, "XI": 0.3, "IX": 0.3}
unitary = Trotter(hamiltonian, order=1, trotter_steps=4, time=1.0)
```

## Tuning notes

- Reduce Trotter error by decreasing the step size or increasing the Suzuki order.
- For long-time evolution, combine Trotter with qubitization/QSP for better scaling.
- Match the gate set to the target QPU or simulator.

## Verification

1. Compare the final state or expectation value to a small-scale exact diagonalization.
2. Check convergence with decreasing step size.
3. Verify energy conservation for a closed system.
''',
        "references": [
            "https://nvidia.github.io/cudaq-algorithms/",
            "https://github.com/NVIDIA/cudaq-algorithms",
            "https://arxiv.org/abs/1612.09584",
        ],
    },
    {
        "name": "quantum-state-preparation-cudaq",
        "title": "Quantum State Preparation with CUDA-Q Algorithms",
        "description": "Prepare reference quantum states such as Hartree–Fock and Givens-rotation Slater determinants inside CUDA-Q kernels.",
        "devin_body": r'''## When to use

You need a clean, verifiable reference state (e.g., Hartree–Fock, Slater determinant) as input to a quantum chemistry or algorithm workflow.

## Usage

- Prepare a Hartree–Fock state from occupation numbers.
- Generate a Slater determinant from a Givens-rotation decomposition.
- Compose state preparation with `Walk`, `QSVT`, or `Trotter` in a single kernel.

## Steps

1. Define the number of qubits, occupied spin orbitals, and optional unitary parameterization.
2. Call the state-prep utility or write a `@cudaq.kernel` that applies the Givens rotations.
3. Pass the resulting kernel to `Walk.moments()` or another algorithm primitive.
4. Verify overlap with the classical state vector.

## Code pattern

```python
import cudaq
from cudaq_algorithms import hartree_fock_state, Walk

@cudaq.kernel
def hf_state(n_electrons: int):
    q = cudaq.qvector(4)
    for i in range(n_electrons):
        x(q[i])
```

## Tuning notes

- Use the smallest basis that captures the physics you need; extra virtual orbitals increase circuit depth.
- Givens-rotation circuits are more expressive but deeper than simple HF preparation.

## Verification

1. Compute the prepared state vector on `qpp-cpu` and compare to the classical HF/Slater vector.
2. Check that the state has the correct particle number and symmetry.
3. Combine with a Hamiltonian and verify the energy expectation.
''',
        "references": [
            "https://nvidia.github.io/cudaq-algorithms/",
            "https://github.com/NVIDIA/cudaq-algorithms",
            "https://arxiv.org/abs/1812.00954",
        ],
    },
    {
        "name": "fermion-to-qubit-cudaq",
        "title": "Fermion-to-Qubit Mappings in CUDA-Q",
        "description": "Map fermionic operators to qubit operators using Jordan–Wigner, Bravyi–Kitaev, and other schemes for quantum chemistry and materials.",
        "devin_body": r'''## When to use

You have fermionic creation/annihilation operators (from PySCF, molecular integrals, or a Hubbard model) and need a qubit Hamiltonian for a CUDA-Q algorithm.

## Usage

- Convert one- and two-electron integrals to Pauli strings with Jordan–Wigner or Bravyi–Kitaev.
- Use the Pauli Hamiltonian as input to `PauliLCU`, `Trotter`, or `Walk`.
- Compare mappings for qubit count, locality, and circuit depth trade-offs.

## Steps

1. Obtain molecular or model integrals (e.g., from PySCF `scf.get_hcore()` and `ao2mo`).
2. Choose a mapping (Jordan–Wigner, Bravyi–Kitaev, parity, etc.).
3. Generate the qubit Hamiltonian with `cudaq_algorithms.fermion_to_qubit` or equivalent.
4. Pass the Pauli dictionary to a block-encoding or time-evolution primitive.

## Code pattern

```python
from cudaq_algorithms import jordan_wigner

# h_pq and h_pqrs are numpy arrays of one-/two-electron integrals
qubit_hamiltonian = jordan_wigner(h_pq, h_pqrs)
print(qubit_hamiltonian)
```

## Tuning notes

- Jordan–Wigner is simple but has long Pauli strings.
- Bravyi–Kitaev balances locality and Pauli weight; use it for deeper circuits.
- Parity mapping can reduce qubit count by exploiting symmetries.

## Verification

1. Check that the qubit Hamiltonian reproduces the fermionic spectrum on a small basis.
2. Compare Jordan–Wigner and Bravyi–Kitaev energies for the same integrals.
3. Verify the operator algebra (number of particles, spin symmetries) is preserved.
''',
        "references": [
            "https://nvidia.github.io/cudaq-algorithms/",
            "https://github.com/NVIDIA/cudaq-algorithms",
            "https://arxiv.org/abs/1701.08213",
        ],
    },
    {
        "name": "quantum-chemistry-cudaq",
        "title": "Quantum Chemistry with CUDA-Q Algorithms",
        "description": "End-to-end quantum chemistry workflows from PySCF molecular integrals to CUDA-Q ground-state calculations.",
        "devin_body": r'''## When to use

You want to compute molecular ground-state energies or simulate electronic structure with a CUDA-Q algorithm using realistic chemistry inputs.

## Usage

- Run a PySCF mean-field calculation to obtain molecular integrals.
- Build a Jordan–Wigner or Bravyi–Kitaev Hamiltonian.
- Choose a block encoding and a solver (qubitization moments + Krylov, QSVT, Trotter).
- Verify the result against full configuration interaction for small molecules.

## Steps

1. Install PySCF and `cudaq-algorithms`.
2. Define a molecule and basis, then run PySCF RHF/UHF.
3. Extract one- and two-electron integrals.
4. Map fermion to qubit and create a `PauliLCU` (or double-factorized) encoding.
5. Build `Walk` or `QSVT` and compute ground-state energy.
6. Compare to FCI or experimental reference.

## Code pattern

```python
from pyscf import gto, scf
from cudaq_algorithms import jordan_wigner, PauliLCU, Walk

mol = gto.M(atom='H 0 0 0; H 0 0 0.74', basis='sto-3g')
mf = scf.RHF(mol).run()
hpq, hpqrs = mf.get_hcore(), mol.intor('int2e')
qubit_h = jordan_wigner(hpq, hpqrs)
encoding = PauliLCU(qubit_h)
walk = Walk(encoding)
```

## Tuning notes

- Use a minimal basis (`sto-3g`) for verification, then scale up.
- Double factorization reduces qubit/gate cost for larger active spaces.
- Active-space selection controls the number of correlated electrons and orbitals.

## Verification

1. Compare CUDA-Q ground-state energy to PySCF FCI for a small molecule.
2. Check that the mean-field energy from PySCF matches the Hartree–Fock reference.
3. Vary the active space and confirm convergence toward the full-basis limit.
''',
        "references": [
            "https://nvidia.github.io/cudaq-algorithms/",
            "https://pyscf.org/",
            "https://github.com/NVIDIA/cudaq-algorithms",
        ],
    },
    {
        "name": "double-factorization-cudaq",
        "title": "Double Factorization for CUDA-Q",
        "description": "Use double factorization block encodings to reduce the cost of quantum chemistry Hamiltonians in CUDA-Q Algorithms.",
        "devin_body": r'''## When to use

You are simulating a molecule or material with many orbitals and need a more compact block encoding than a naive Pauli LCU.

## Usage

- Decompose the two-electron tensor into auxiliary factors.
- Build a double-factorized block encoding.
- Swap the encoding into a `Walk` or `QSVT` workflow without changing downstream code.

## Steps

1. Compute one- and two-electron integrals from PySCF or a model Hamiltonian.
2. Run a double-factorization routine (e.g., ERI factorization).
3. Construct the `BlockEncoding` object from the factorized form.
4. Use it with `Walk` or `QSVT` exactly as you would with `PauliLCU`.

## Code pattern

```python
from cudaq_algorithms import DoubleFactorization, Walk

# factors and one-body terms obtained from factorization
encoding = DoubleFactorization(one_body, two_body_factors)
walk = Walk(encoding)
```

## Tuning notes

- Truncate small factors to balance accuracy and circuit depth.
- For large systems, combine with active-space truncation.
- Compare Pauli LCU and double-factorization resources for the same molecule.

## Verification

1. Confirm the factorized Hamiltonian reproduces the original two-electron integrals.
2. Compare ground-state energy from `Walk` with double factorization to FCI or Pauli-LCU results.
3. Track qubit and gate counts as a function of factorization rank.
''',
        "references": [
            "https://nvidia.github.io/cudaq-algorithms/",
            "https://github.com/NVIDIA/cudaq-algorithms",
            "https://arxiv.org/abs/2103.14750",
        ],
    },
    {
        "name": "custom-block-encodings-cudaq",
        "title": "Custom Block Encodings for CUDA-Q",
        "description": "Implement custom block encodings in CUDA-Q Algorithms and plug them into the common BlockEncoding interface.",
        "devin_body": r'''## When to use

You have a specialized Hamiltonian or matrix structure (tensor network, sparse, symmetry-adapted) and want to use it with `Walk`, `QSVT`, or `Trotter`.

## Usage

- Subclass or implement the `BlockEncoding` interface.
- Provide the unitary list, subnormalization factor, and data-capture logic.
- Pass the custom encoding to any primitive that accepts `BlockEncoding`.

## Steps

1. Implement the encoding unitary as a CUDA-Q kernel or a sequence of kernels.
2. Wrap it in a `BlockEncoding`-compatible object.
3. Test the block matrix by appending a controlled reflection and measuring the top-left block.
4. Compose with `Walk` or `QSVT` and run end-to-end.

## Code pattern

```python
from cudaq_algorithms import BlockEncoding, Walk

class MyEncoding(BlockEncoding):
    def __init__(self, data):
        self.data = data
        # define self.alpha and self.unitaries

encoding = MyEncoding(my_data)
walk = Walk(encoding)
```

## Tuning notes

- Keep the subnormalization factor as close to the spectral norm as possible.
- Reuse the built-in `Walk`/`QSVT` primitives so you only need to design the encoding.
- Document any assumptions on the input data format.

## Verification

1. Verify the encoding is unitary and the block structure is correct.
2. Compare Chebyshev moments or transformed matrix to a classical reference.
3. Test with both `qpp-cpu` and a target GPU/NVIDIA backend.
''',
        "references": [
            "https://nvidia.github.io/cudaq-algorithms/",
            "https://github.com/NVIDIA/cudaq-algorithms",
            "https://arxiv.org/abs/2105.02859",
        ],
    },
]
