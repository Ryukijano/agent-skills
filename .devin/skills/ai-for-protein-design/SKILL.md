# AI for Protein Design

## Description

Inverse folding, generative backbone design, and binder engineering with ProteinMPNN, RFdiffusion, structure predictors, and Rosetta validation.

## When to use

You need a protein sequence for a fixed backbone, a de novo protein binder, or a new scaffold with specified structure or function.

## Key concepts

- **Inverse folding**: predict an amino-acid sequence that folds into a target backbone.
- **ProteinMPNN**: message-passing neural network for sequence design.
- **RFdiffusion**: diffusion model for generating protein backbones and binders.
- **Structure prediction**: AlphaFold2, ESMFold, or OpenFold to validate designs.
- **Interface metrics**: pLDDT, pAE, interface RMSD, binding energy.
- **Mutagenesis**: design focused libraries and assess stability.

## Code pattern

```python
import subprocess

# 1. Generate a backbone with RFdiffusion (requires installed environment)
subprocess.run([
    'python', 'scripts/run_inference.py',
    'inference.output_prefix=outputs/binder',
    'inference.num_designs=10',
    'contigmap.contigs=[150-150]',
], check=True)

# 2. Design sequences with ProteinMPNN
subprocess.run([
    'python', 'proteinmpnn_run.py',
    '--pdb_path', 'outputs/binder_0.pdb',
    '--out_folder', 'mpnn_outputs',
    '--num_seq_per_target', '8',
], check=True)

# 3. Validate with a structure predictor (ESMFold, AlphaFold2, or OpenFold)
# Fold the top sequences and inspect pLDDT plus interface residues.
```

## Tuning notes

- Start with a high-quality backbone; RFdiffusion works best with clear design objectives.
- Use `num_seq_per_target` >= 8 to explore sequence space.
- Filter designs by pLDDT > 80 and low pAE at the binding interface.
- For binders, check shape complementarity and hotspot residues.
- Experimental validation (yeast display, BLI, SPR) is the ground truth.

## Verification

1. Design 10 sequences for a fixed backbone and run them through ESMFold/AlphaFold2.
2. Compare predicted structures to the target backbone (RMSD < 2 A for monomers).
3. Design a binder to a target, dock/validate it, and rank by interface pLDDT.

## References

- https://github.com/dauparas/ProteinMPNN
- https://doi.org/10.1126/science.add2187
- https://github.com/RosettaCommons/RFdiffusion
- https://doi.org/10.1038/s41586-023-06415-8
- https://doi.org/10.1038/s41467-023-38328-5
