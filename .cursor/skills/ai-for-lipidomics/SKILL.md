# AI for Lipidomics

## Description

LC-MS/MS lipid species quantification, structural isomer resolution, lipid class normalization, and predictive modeling of lipid phenotypes.

## When to use

You are quantifying or classifying lipid species from LC-MS/MS or shotgun lipidomics data and need to annotate lipid classes, correct for technical variation, or link lipid profiles to phenotypes.

## Key concepts

- **Lipid classes**: fatty acyls, glycerolipids, glycerophospholipids, sphingolipids, and sterols.
- **LC-MS/MS lipidomics**: separation and fragmentation for species and isomer resolution.
- **Epilipidomics**: post-translationally modified lipids and oxidation products.
- **LipidMaps**: curated lipid nomenclature and classification database.
- **Statistical modeling**: univariate tests, multivariate PCA, and supervised classifiers.

## Code pattern

```python
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_csv("lipidomics.csv")
X = df[lipid_columns]
X_scaled = StandardScaler().fit_transform(X)
pcs = PCA(n_components=2).fit_transform(X_scaled)
```

## Tuning notes

- Normalize by total lipid class sum or internal standards.
- Handle structural isomers and annotation confidence levels.
- Correct for instrument batch and column drift.
- Be cautious of correlated lipid species in multivariate models.

## Verification

1. Inspect lipid class distributions for biological plausibility.
2. Replicate sample correlation and coefficient of variation across replicates.
3. Compare class separation in PCA to a priori group labels.

## References

- https://doi.org/10.1007/s00216-023-04991-2
- https://doi.org/10.3390/biom11030473
- https://doi.org/10.1016/j.bbalip.2017.05.006
- https://doi.org/10.1021/acs.analchem.2c04406
