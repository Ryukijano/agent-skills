# AI for Spatial Omics

## Description

Spatially resolved transcriptomics and proteomics, cell segmentation, neighborhood analysis, and integration with imaging data.

## When to use

You are analyzing spatially resolved transcriptomics, proteomics, or multi-omics data and need to account for tissue context, neighborhood structure, and image features.

## Key concepts

- **Spatial transcriptomics**: Visium, Slide-seq, Xenium, MERFISH, Stereo-seq, and seqFISH.
- **Spatial proteomics**: imaging mass cytometry, CODEX, and MIBI-TOF.
- **Cell segmentation and deconvolution**: mapping spots or pixels to cell types.
- **Neighborhood and interaction**: spatial domains, cell-cell communication, and niches.
- **Spatially variable genes (SVGs)**: genes with expression patterns tied to location.

## Code pattern

```python
import scanpy as sc
import squidpy as sq

adata = sc.read_h5ad("visium.h5ad")
sq.gr.spatial_neighbors(adata, radius=1.5)
sq.gr.spatial_autocorr(adata, mode="moran", genes=adata.var_names[:100])
sq.gr.nhood_enrichment(adata, cluster_key="cell_type")
```

## Tuning notes

- Align H&E images and spatial coordinates carefully.
- Choose spot vs cell resolution based on the biological question.
- Use spatial-aware imputation when genes are lowly expressed.
- Compare to matched single-cell data for deconvolution quality.

## Verification

1. Identify spatially variable genes and compare to known tissue markers.
2. Validate cell-type deconvolution against matched scRNA-seq or IHC.
3. Inspect neighborhood enrichment results for biologically expected ligand-receptor pairs.

## References

- https://doi.org/10.1186/s13059-022-02653-7
- https://doi.org/10.1063/5.0091135
- https://doi.org/10.1093/bib/bbae719
- https://squidpy.readthedocs.io/en/stable/
