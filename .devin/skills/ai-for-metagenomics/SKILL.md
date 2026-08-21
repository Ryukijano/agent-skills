# AI for Metagenomics

## Description

Use machine learning on 16S rRNA and shotgun metagenomic data to profile microbial communities, infer functions, assemble metagenome-assembled genomes and link the microbiome to host phenotypes.

## When to use

You are profiling microbial communities from 16S rRNA or shotgun metagenomic data to classify taxa, infer function, assemble MAGs, or link the microbiome to host phenotypes.

## Usage

- **Profile taxonomy**: classify 16S amplicon or shotgun reads into taxonomic and functional profiles.
- **Assemble MAGs**: bin contigs into metagenome-assembled genomes and assess quality.
- **Handle composition**: apply CLR, ILR, or other transformations to relative-abundance data.
- **Model host associations**: link taxonomic and functional features to phenotype or intervention.
- **Validate generalization**: test microbiome associations in independent cohorts.

## Steps

1. Quality-filter and trim reads, remove contaminants, and account for negative controls.
2. Profile taxonomy from 16S or shotgun data, or assemble and bin MAGs from metagenomes.
3. Infer functional content with gene catalogs and pathway databases.
4. Apply compositional transformations and batch correction before statistical testing.
5. Train classification or regression models linking microbiome features to host phenotypes.
6. Validate associations in independent cohorts and confirm with targeted experiments.

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
