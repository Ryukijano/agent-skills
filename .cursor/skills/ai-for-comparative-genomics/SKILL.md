# AI for Comparative Genomics

## Description

Cross-species and population genome comparison, orthology inference, phylogenomics, selection scans, and pan-genome analysis.

## When to use

You are comparing genomes across species, strains, or populations to infer evolution, identify conserved regions, build phylogenies, or study pan-genomes.

## Key concepts

- **Homology and orthology**: orthologous genes, paralogs, and orthogroups.
- **Genome alignment and synteny**: whole-genome and multiple alignments.
- **Phylogenetics and phylogenomics**: tree inference, gene trees, and species trees.
- **Population genomics**: selection, demographic history, and introgression.
- **Pan-genomes**: core, shell, and accessory gene content.

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
