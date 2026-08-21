# AI for Biology

## Description

Use deep learning to analyze biological sequences, single-cell and spatial omics, microscopy images, and molecular structures.

## When to use

You are analyzing biological sequences, microscopy images, single-cell data, or molecular structures.

## Usage

- Embed DNA, RNA, and protein sequences with transformer or CNN models (e.g., ESM, HyenaDNA).
- Classify cell types and infer trajectories from single-cell RNA-seq or spatial transcriptomics.
- Quantify proteins and cell phenotypes from multiplexed imaging or mass spectrometry proteomics.
- Predict protein structures and interactions from sequences (e.g., AlphaFold, ESM embeddings).
- Build disease or perturbation classifiers from multi-omics and imaging data.

## Steps

1. Load and quality-control sequence, omics, or imaging data for the target organism and tissue.
2. Featurize biological inputs (k-mers, embeddings, expression matrices, image patches).
3. Train or fine-tune a sequence, graph, or vision model for the prediction task (e.g., cell type, binding, biomarker).
4. Integrate multiple modalities (genomics, transcriptomics, proteomics, imaging) to improve robustness.
5. Control for batch effects and biological confounders with integration and harmonization methods.
6. Validate predictions with held-out patients, datasets, or expert biological annotations.

## Code pattern

```python
from transformers import EsmModel, EsmTokenizer

model = EsmModel.from_pretrained("facebook/esm2_t6_8M_UR50D")
tokenizer = EsmTokenizer.from_pretrained("facebook/esm2_t6_8M_UR50D")
inputs = tokenizer("MKTLL", return_tensors="pt")
outputs = model(**inputs)
```

## Tuning notes

- Use organism- and tissue-appropriate train/test splits.
- Single-cell models can be confounded by batch effects; use integration methods.
- Be cautious about genomic data privacy and consent.

## Verification

1. Embed a set of protein sequences and cluster by function.
2. Fine-tune a small sequence model on a binding prediction task.
3. Evaluate a cell-type classifier on a held-out patient or dataset.

## References

- https://github.com/facebookresearch/esm
- https://www.nature.com/articles/s41586-021-03819-2
- https://arxiv.org/abs/2407.04446
- https://huggingface.co/
- https://www.biorxiv.org/content/10.1101/2023.01.11.523679
