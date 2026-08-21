# AI for Spatial Omics

## Description

Use machine learning on spatially resolved transcriptomics and proteomics to segment cells, analyze neighborhoods, integrate imaging and map tissue microenvironments.

## When to use

You are analyzing spatially resolved transcriptomics, proteomics, or multi-omics data and need to account for tissue context, neighborhood structure, and image features.

## Usage

- **Process platforms**: analyze Visium, Slide-seq, Xenium, MERFISH, Stereo-seq, and seqFISH data.
- **Segment or deconvolve**: map spots or pixels to cell types using single-cell references.
- **Find spatial patterns**: identify spatially variable genes and tissue domains.
- **Model neighborhoods**: compute cell-cell communication, niches, and enrichment.
- **Integrate modalities**: combine with H&E images and matched single-cell data.

## Steps

1. Load spatial data and align coordinates with tissue images or H&E sections.
2. Preprocess expression, select spatially variable genes, and perform normalization.
3. Segment cells or deconvolve spots into cell-type proportions using single-cell references.
4. Build spatial neighbor graphs and compute spatial autocorrelation and domain detection.
5. Infer cell-cell communication, niches, and interactions in spatial neighborhoods.
6. Validate deconvolution and spatial patterns with IHC, smFISH, or matched scRNA-seq.

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
