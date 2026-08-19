# Transformers and Foundation Models for Science

## Description

Transformers for protein, genomics, weather, chemistry, math, and symbolic regression; ESM, AlphaFold, Prithvi, DNABERT, AI-Descartes.

## When to use

You want to apply large transformer-based foundation models to scientific data or use transformers for symbolic and mathematical discovery.

## Key concepts

- **Protein**: ESM-2, ESMFold, AlphaFold, Boltz.
- **Genomics**: DNABERT/DNABERT-2, Enformer, Nucleotide Transformer.
- **Weather/climate**: Prithvi, ClimaX, FourCastNet, GraphCast.
- **Chemistry**: ChemBERTa, MolFormer, GPT for chemistry.
- **Math/symbolic**: LLM-SR, AI-Descartes, formal provers (Lean, Isabelle).

## Code pattern

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("facebook/esm2_t33_650M_UR50D")
model = AutoModel.from_pretrained("facebook/esm2_t33_650M_UR50D").to("cuda")
inputs = tokenizer("MKTAYIAKQRQISFVK", return_tensors="pt").to("cuda")
outputs = model(**inputs)
```

## Tuning notes

- Use FlashAttention for long sequences (genomics, weather).
- Fine-tune with LoRA/QLoRA for limited data.
- For symbolic regression, combine LLM-generated hypotheses with constrained fitting.

## Verification

1. Extract ESM-2 embeddings and train a small head for a protein task.
2. Fine-tune DNABERT-2 on a GUE benchmark and compare to baseline.
3. Use AI-Descartes/LLM-SR to rediscover a known physical law from data.

## References

- https://github.com/facebookresearch/esm
- https://github.com/magics-lab/dnabert_2
- https://huggingface.co/ibm-nasa-geospatial
- https://www.nature.com/articles/s41467-023-37236-y
