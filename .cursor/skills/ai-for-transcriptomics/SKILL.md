# AI for Transcriptomics

## Description

Use machine learning and foundation models to quantify, normalize and interpret bulk and single-cell RNA-seq data for cell typing, differential expression and gene regulation.

## When to use

You need to quantify, normalize, cluster, or model gene expression from bulk RNA-seq or single-cell RNA-seq data for cell typing, differential expression, or gene regulation studies.

## Usage

- **Preprocess counts**: filter, normalize, and stabilize variance for bulk and single-cell RNA-seq.
- **Reduce dimensions**: run PCA, UMAP, or latent embeddings for visualization and analysis.
- **Detect differential expression**: identify genes across conditions or cell types with appropriate tests.
- **Apply foundation models**: use scBERT, scGPT, and scFoundation for representation and transfer learning.
- **Reconstruct trajectories**: infer pseudotime, RNA velocity, and lineage dynamics.

## Steps

1. Load raw counts and metadata, filter low-quality cells/genes, and normalize for library size.
2. Select highly variable genes and compute dimensionality reduction and embeddings.
3. Cluster cells or samples and annotate them with known marker genes or reference atlases.
4. Test for differential expression between conditions and validate with a second method.
5. Build or apply a foundation model for transfer learning, imputation, or perturbation prediction.
6. Compare results to reference atlases and orthogonal assays to assess biological consistency.

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
