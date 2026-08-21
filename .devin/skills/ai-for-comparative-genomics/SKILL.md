# AI for Comparative Genomics

## Description

Use machine learning and phylogenomics to compare genomes across species and populations, infer orthology, detect selection and analyze pan-genomes.

## When to use

You are comparing genomes across species, strains, or populations to infer evolution, identify conserved regions, build phylogenies, or study pan-genomes.

## Usage

- **Infer orthology**: identify orthologs and paralogs across species with graph or tree methods.
- **Build alignments**: create whole-genome, synteny, and protein alignments.
- **Reconstruct phylogeny**: infer species and gene trees and reconcile them.
- **Detect selection**: scan for positive selection, introgression, and demographic history.
- **Analyze pan-genomes**: build graphs of core, shell, and accessory gene content.

## Steps

1. Select high-quality assemblies and annotate genes with consistent pipelines.
2. Build whole-genome or protein alignments and infer orthogroups with graph or tree methods.
3. Reconstruct phylogenies and reconcile gene and species trees.
4. Scan for selection, introgression, and structural variants across lineages.
5. Build a pan-genome graph or variation graph and quantify core/shell/accessory content.
6. Validate orthology and selection signals with synteny, reciprocal best hits, and experiments.

## Code pattern

```python
from Bio import AlignIO

alignment = AlignIO.read("genomes.aln", "fasta")
length = alignment.get_alignment_length()
variable = []
for i in range(length):
    column = [rec.seq[i] for rec in alignment]
    if len(set(column)) > 1:
        variable.append(i)
print("Variable sites:", len(variable))
```

## Tuning notes

- Use high-quality, chromosome-scale assemblies for whole-genome alignment.
- Account for incomplete lineage sorting and horizontal gene transfer.
- Choose substitution and indel models matched to data (codon, nucleotide, amino acid).
- Validate orthology with synteny and reciprocal best hits.

## Verification

1. Compare a phylogenetic tree to a published species tree or fossil record.
2. Test for selection with dN/dS or population genetics scans.
3. Map structural variants and check conservation in outgroup genomes.

## References

- https://doi.org/10.1016/j.ympev.2024.108066
- https://doi.org/10.1038/s41576-023-00636-3
- https://doi.org/10.1186/s13059-022-02735-6
- https://doi.org/10.3390/app14114837
