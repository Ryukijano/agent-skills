# Bioinformatics and Genomics ML on GPU

## Description

DNABERT, Enformer, single-cell analysis with scVI/scGPT, and RAPIDS cuDF for genomics pipelines.

## When to use

You are training or deploying genomics models on GPU, such as DNA sequence models, gene expression models, or single-cell analysis.

## Key concepts

- **DNABERT/DNABERT-2**: BERT on DNA k-mer/BPE tokens for promoter, splice site, TFBS prediction.
- **Enformer**: transformer for gene expression and chromatin states from DNA, 200 kb context.
- **scVI**: single-cell Variational Inference for scRNA-seq.
- **scGPT**: foundation model for single-cell multi-omics.
- **RAPIDS cuDF/cuML**: GPU-accelerated dataframes and ML for large genomics tables.

## Code pattern

```python
# scVI
import scvi
scvi.model.SCVI.setup_anndata(adata, layer="counts")
model = scvi.model.SCVI(adata)
model.train(accelerator="gpu", devices=1)
```

DNABERT:

```bash
python run_finetune.py --model_type dna --tokenizer_name dna6   --model_name_or_path zhihan1996/DNABERT-2-117M
```

## Tuning notes

- Long-context genomics models can use FlashAttention for >2k sequences.
- Single-cell data is sparse; use highly variable gene selection and count layers.
- For RAPIDS, ensure `cudf` version matches CUDA.

## Verification

1. Fine-tune DNABERT-2 on a GUE benchmark and compare to reported metrics.
2. Run scVI on a 100k-cell dataset and compare latent structure to CPU.
3. Use cuDF to load a large Parquet genomics table and compare wall time to pandas.

## References

- https://github.com/jerryji1993/DNABERT
- https://github.com/magics-lab/dnabert_2
- https://docs.scvi-tools.org/
- https://github.com/bowang-lab/scGPT
- https://developer.nvidia.com/blog/analyzing-the-rna-sequence-of-1-3m-mouse-brain-cells-with-rapids-on-nvidia-gpus/
