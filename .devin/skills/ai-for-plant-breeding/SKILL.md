# AI for Plant Breeding

## Description

Genomic selection, phenotype prediction, multi-environment trial analysis, and marker-assisted breeding with machine and deep learning.

## When to use

You are selecting parents, predicting progeny performance, analysing genotype-by-environment interactions, or optimising crossing schemes in a crop or forage breeding programme.

## Usage

- **Genomic prediction**: predict quantitative traits from dense marker data using ML or statistical learning methods.
- **Multi-environment trial analysis**: model genotype x environment (GxE) interactions and stability across locations and years.
- **High-throughput phenotyping integration**: fuse remote sensing, spectral, and drone-derived traits with genotypes.
- **Parent selection and genetic diversity**: use prediction and diversity metrics to design optimal crosses.

## Steps

1. Collect high-quality genotype (e.g., SNP array, resequencing) and phenotype data across multiple environments.
2. Quality-control markers and phenotypes; account for population structure and kinship.
3. Train and validate prediction models for target traits (yield, quality, stress tolerance).
4. Evaluate prediction accuracy in independent environments and examine GxE patterns.
5. Integrate predictions into crossing plans and selection decisions, updating as new data arrive.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import cross_val_predict

X = df[genomic_markers]
y = df["yield_kg_ha"]

y_pred = cross_val_predict(
    GradientBoostingRegressor(random_state=42), X, y, cv=5
)
```

## Tuning notes

- Include pedigree or kinship to borrow information across related lines; regularise when p >> n.
- Use environment-specific models and covariance structures to capture GxE.
- Combine genomic, transcriptomic, and phenomic data with multimodal fusion.
- Track linkage disequilibrium and marker density effects on prediction stability.

## Verification

1. Compare genomic prediction accuracy to a pedigree-BLUP or GBLUP baseline.
2. Run leave-one-environment-out cross-validation to assess GxE generalisation.
3. Estimate expected genetic gain from the predicted selection index.

## References

- https://www.sciencedirect.com/science/article/pii/S1360138524003455
- https://doi.org/10.1093/genetics/iyae161
- https://link.springer.com/article/10.1186/s12864-020-07319-x
- https://www.sciencedirect.com/science/article/pii/S1674205224000807
