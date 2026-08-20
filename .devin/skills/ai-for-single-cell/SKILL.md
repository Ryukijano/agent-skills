# AI for Single-Cell Omics

## Description

Single-cell transcriptomics, epigenomics, proteomics, and multi-omics integration, cell type annotation, trajectory inference, and foundation models.

## When to use

You are working with single-cell genomics data (scRNA-seq, scATAC-seq, CITE-seq, or multi-omics) to annotate cell types, infer trajectories, integrate batches, or predict perturbation responses.

## Key concepts

- **scRNA-seq**: gene expression at single-cell resolution with dropout and high dimensionality.
- **scATAC and multi-omics**: chromatin accessibility and surface proteins in the same cells.
- **Batch correction and integration**: mapping new datasets to reference atlases.
- **Trajectory inference**: pseudotime, RNA velocity, and differentiation dynamics.
- **Foundation models**: scGPT, scBERT, and UCE for transfer learning and prediction.

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
