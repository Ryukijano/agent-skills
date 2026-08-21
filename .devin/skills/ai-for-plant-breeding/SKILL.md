# AI for Plant Breeding

## Description

Accelerate crop improvement by predicting trait performance, genomic breeding values, and envirotype effects.

## When to use

You are selecting parents, predicting progeny performance, analysing genotype-by-environment interactions, or optimising crossing schemes in a crop or forage breeding programme.

## Usage

- Run genomic prediction with rrBLUP, BOLT-LMM, or AutoGP.
- Optimize training populations and cross designs.
- Integrate enviromic covariates and multi-environment trials.
- Predict genotype-by-environment interaction.
- Select parents and lines with multi-trait indices.

## Steps

1. Collect genotypic, phenotypic, and environmental data.
2. Impute and filter markers; build kinship or genomic relationship matrices.
3. Train genomic prediction or GWAS models.
4. Predict breeding values across environments.
5. Validate with cross-validation and independent trials.

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
