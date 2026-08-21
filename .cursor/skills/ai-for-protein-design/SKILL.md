# AI for Protein Design

## Description

Generate de novo binders and enzymes from target structures or reactions using inverse folding and diffusion models.

## When to use

You need a protein sequence for a fixed backbone, a de novo protein binder, or a new scaffold with specified structure or function.

## Usage

- **Inverse folding**: use ProteinMPNN or similar models to predict sequences for a fixed backbone.
- **Backbone generation**: design de novo scaffolds or binders around a target motif with RFdiffusion.
- **In silico validation**: refold designed sequences with AlphaFold2, ESMFold, or OpenFold and compute pLDDT/pAE/scRMSD.
- **Interface filtering**: rank candidates by interface pLDDT, pAE, shape complementarity, and hotspot residues.
- **Focused mutagenesis**: build stability or affinity libraries around promising designs.
- **Experimental triage**: move high-confidence binders to expression and biophysical assays (BLI, SPR, yeast display).

## Steps

1. Specify the target structure, epitope, or binding hotspot and the desired binder length/constraints.
2. Generate candidate backbones with RFdiffusion conditioned on the target motif or interface.
3. Design amino-acid sequences for each backbone using ProteinMPNN.
4. Refold designed sequences and compute self-consistency metrics (pLDDT, pAE, scRMSD, scTM).
5. Rank candidates by interface quality, hotspot coverage, and predicted expressability.
6. Express and validate top candidates with binding or activity assays (BLI, SPR, crystallography).

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
