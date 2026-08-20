# AI for Biology

## Description

Deep learning for genomics, transcriptomics, proteomics, cell imaging, and biological sequence modeling.

## When to use

You are analyzing biological sequences, microscopy images, single-cell data, or molecular structures.

## Key concepts

- **Sequence models for DNA/RNA/protein**: CNNs, transformers, and k-mer embeddings.
- **Foundation models for biology**: ESM, AlphaFold, scBERT, HyenaDNA.
- **Single-cell analysis**: cell type classification, perturbation prediction, trajectory inference.
- **Biomedical image analysis**: segmentation, classification, and phenotyping.

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
