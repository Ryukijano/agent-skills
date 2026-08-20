# AI for Metagenomics

## Description

16S rRNA and shotgun microbial community profiling, taxonomic and functional prediction, MAG binning, and microbiome-host association modeling.

## When to use

You are profiling microbial communities from 16S rRNA or shotgun metagenomic data to classify taxa, infer function, assemble MAGs, or link the microbiome to host phenotypes.

## Key concepts

- **Amplicon vs shotgun**: 16S rRNA profiling versus whole-genome metagenomics.
- **Taxonomic and functional profiling**: read classification, gene catalogues, and pathway inference.
- **Metagenome-assembled genomes (MAGs)**: binning contigs into draft microbial genomes.
- **Compositional data**: relative abundance, sparsity, and library size effects.
- **Host-microbiome models**: classification, time-series, and causal inference.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold

X = pd.read_csv("feature_table.tsv", sep="\t", index_col=0).T
y = pd.read_csv("metadata.tsv", sep="\t", index_col=0)["status"]
model = RandomForestClassifier(n_estimators=1000, random_state=42)
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
```

## Tuning notes

- Rarefy or use compositional transformations (CLR, ILR) with care.
- Remove contaminants and batch effects by including negative controls.
- Combine taxonomic and functional features for phenotype prediction.
- Validate on independent cohorts because microbiome associations rarely generalize.

## Verification

1. Reproduce alpha and beta diversity ordination.
2. Compare Random Forest, LASSO, and a compositional model on the same data.
3. Validate biomarkers in a geographically independent cohort.

## References

- https://doi.org/10.1128/msystems.01642-24
- https://doi.org/10.1099/mgen.0.001231
- https://doi.org/10.3389/fmicb.2024.1516667
- https://doi.org/10.3389/fmicb.2023.1261889
- https://doi.org/10.3390/ijms26189206
