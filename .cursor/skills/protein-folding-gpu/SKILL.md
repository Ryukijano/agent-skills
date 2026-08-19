# Protein Structure Prediction on GPU

## Description

AlphaFold 3, ESM3, Boltz, BioNeMo Fold-CP, OpenFold, and high-throughput protein folding pipelines.

## When to use

You are running or deploying protein structure prediction on H100/Blackwell and need to choose the right tool and optimize it.

## Key concepts

- **AlphaFold 3 / Boltz**: 3D structure from sequence and ligands. Boltz is an open AlphaFold3 reimplementation.
- **ESM3**: 98B multimodal protein language model (sequence, structure, function).
- **BioNeMo Fold-CP**: context parallelism for very large complexes (20,000+ tokens, 256 GPUs).
- **OpenFold-TRT / ColabFold**: optimized inference with TensorRT and MMseqs2-GPU.

## Code pattern

```python
# Example: Boltz inference
from boltz import Boltz1
model = Boltz1.load_from_checkpoint("boltz1.ckpt")
structure = model.predict("sequences.fasta")
```

For AlphaFold 3, set `XLA_PYTHON_CLIENT_MEM_FRACTION=0.95` on H100.

## Tuning notes

- For >5,120 tokens, use unified memory or Fold-CP context parallelism.
- H100 is ~1.8-2× faster than A100 for AlphaFold 3.
- Pre-compute MSAs with MMseqs2-GPU for throughput.

## Verification

1. Run a single-chain prediction and compare RMSD to a known PDB structure.
2. Run `alphafold3 --input ... --output ...` and check GPU utilization.
3. For Fold-CP, verify the complex fits in aggregate GPU memory.

## References

- https://github.com/google-deepmind/alphafold3/blob/main/docs/performance.md
- https://github.com/jwohlwend/boltz
- https://www.evolutionaryscale.ai/blog/esm3-release
- https://developer.nvidia.com/blog/scaling-biomolecular-modeling-using-context-parallelism-in-nvidia-bionemo
