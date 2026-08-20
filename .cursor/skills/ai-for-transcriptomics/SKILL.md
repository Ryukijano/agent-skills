# AI for Transcriptomics

## Description

Bulk and single-cell RNA-seq analysis, normalization, clustering, differential expression, splicing, and foundation models for gene expression.

## When to use

You need to quantify, normalize, cluster, or model gene expression from bulk RNA-seq or single-cell RNA-seq data for cell typing, differential expression, or gene regulation studies.

## Key concepts

- **Bulk vs single-cell RNA-seq**: population average versus cell-resolution expression.
- **Count normalization**: library size correction, log1p, and variance stabilization.
- **Dimensionality reduction**: PCA, UMAP, and latent embeddings for visualization and analysis.
- **Differential expression**: edgeR, DESeq2, or model-based tests across conditions or cell types.
- **Foundation models**: scBERT, scGPT, and scFoundation for cell representation and transfer learning.

## Code pattern

```python
import scanpy as sc

adata = sc.read_h5ad("scRNA.h5ad")
sc.pp.filter_cells(adata, min_genes=200)
sc.pp.filter_genes(adata, min_cells=3)
sc.pp.normalize_total(adata, target_sum=1e4)
sc.pp.log1p(adata)
sc.pp.highly_variable_genes(adata, n_top_genes=2000)
sc.tl.pca(adata)
```

## Tuning notes

- Filter low-quality cells and doublets before clustering.
- Choose a batch correction strategy (Harmony, scVI, Scanorama) when integrating datasets.
- Avoid overclustering by testing multiple resolution parameters.
- Use pseudotime and RNA velocity to interpret differentiation trajectories.

## Verification

1. Cluster the data and confirm known marker-gene expression.
2. Reproduce differential expression results with a second method (e.g., DESeq2 or MAST).
3. Project query cells onto a reference atlas and check annotation consistency.

## References

- https://doi.org/10.1038/s41592-024-02353-z
- https://doi.org/10.1016/j.gpb.2022.11.011
- https://doi.org/10.1261/rna.080889.125
- https://doi.org/10.1038/s41592-019-0537-1
- https://doi.org/10.1038/s41592-024-02331-5
