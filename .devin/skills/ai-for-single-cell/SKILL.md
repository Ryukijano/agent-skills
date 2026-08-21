# AI for Single-Cell Omics

## Description

Use single-cell and multi-omics foundation models to annotate cell types, integrate batches, infer trajectories and predict perturbation responses.

## When to use

You are working with single-cell genomics data (scRNA-seq, scATAC-seq, CITE-seq, or multi-omics) to annotate cell types, infer trajectories, integrate batches, or predict perturbation responses.

## Usage

- **Preprocess data**: normalize scRNA-seq, scATAC-seq, CITE-seq, or multi-omics profiles.
- **Remove artifacts**: filter ambient RNA, doublets, and low-quality cells before analysis.
- **Annotate cells**: identify types and novel subpopulations with marker genes and foundation models.
- **Integrate batches**: correct batch effects or map query data to reference atlases.
- **Model dynamics**: infer trajectories, RNA velocity, and perturbation responses with scGPT or scFoundation.

## Steps

1. Load single-cell data, filter low-quality cells and doublets, and normalize counts.
2. Select features and compute dimensionality reduction, neighbors, and embeddings.
3. Cluster cells and annotate them with marker genes or reference atlases.
4. Integrate multiple batches or project query data onto a reference while preserving biology.
5. Infer trajectories and velocity, or predict perturbation responses with foundation models.
6. Validate cell types and dynamics with orthogonal experiments or lineage-tracing data.

## Code pattern

```python
import scanpy as sc

adata = sc.read_h5ad("scMultiome.h5ad")
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, n_top_genes=3000)
sc.tl.pca(adata)
sc.pp.neighbors(adata)
sc.tl.umap(adata)
```

## Tuning notes

- Remove ambient RNA and doublets before clustering.
- Choose integration method based on whether you need batch correction or atlas projection.
- Resolve subpopulations by testing marker genes and multiple resolutions.
- Use perturbation and time-series models to interpret dynamics.

## Verification

1. Assign cell types and compare to a reference atlas or known markers.
2. Project held-out batches and evaluate mixing vs biological conservation.
3. Validate trajectory ordering with time-course or lineage-tracing data.

## References

- https://doi.org/10.1016/j.coisb.2021.04.006
- https://doi.org/10.1093/bioinformatics/btae374
- https://doi.org/10.1038/s41592-024-02353-z
- https://doi.org/10.1038/s41592-025-02856-3
