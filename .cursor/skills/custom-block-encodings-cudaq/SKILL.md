# Custom Block Encodings for CUDA-Q

## Description

Implement custom block encodings in CUDA-Q Algorithms and plug them into the common BlockEncoding interface.

## When to use

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

## References

- https://nvidia.github.io/cudaq-algorithms/
- https://github.com/NVIDIA/cudaq-algorithms
- https://arxiv.org/abs/2105.02859
