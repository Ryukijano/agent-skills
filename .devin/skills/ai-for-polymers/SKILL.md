# AI for Polymers

## Description

Use ML to predict polymer properties, generate novel structures, and optimize process-structure-property relationships for sustainable materials.

## When to use

You are discovering or optimizing polymeric materials for mechanical, thermal, electronic, or sustainable applications and need to navigate the vast polymer chemical and morphological space.

## Usage

- Represent polymers with SMILES, BigSMILES, fingerprints, graph neural networks, or polyBERT-style embeddings.
- Predict glass transition, viscosity, modulus, permeability, and degradation from structure.
- Generate novel polymer structures with VAEs, GANs, diffusion models, or reinforcement learning.
- Link synthesis, molecular weight, and morphology to performance for sustainable and recyclable design.

## Steps

1. Curate polymer structures and property data, choosing repeat-unit, oligomer, or bulk representations as appropriate.
2. Train property-prediction models for target properties (Tg, modulus, permeability, bandgap) with transfer learning.
3. Generate candidate polymers using a generative model and filter for synthetic accessibility and target property windows.
4. Incorporate process, molecular weight, crystallinity, and polydispersity descriptors into structure-property models.
5. Evaluate candidates for biodegradability, recyclability, or circularity with sustainability scoring.
6. Validate top candidates by synthesis and measurement, and retrain the models with new data.

## Code pattern

```python
from transformers import AutoTokenizer, AutoModel

tokenizer = AutoTokenizer.from_pretrained("kuelumbus/polyBERT")
model = AutoModel.from_pretrained("kuelumbus/polyBERT")
inputs = tokenizer("[*]CC(C)C[*]", return_tensors="pt")
emb = model(**inputs).pooler_output
```

## Tuning notes

- Polymer data are sparse and highly heterogeneous; use transfer learning and multitask models where possible.
- Distinguish between repeat-unit, oligomer, and bulk-property predictions; the same SMILES can map to very different materials.
- Pay attention to polydispersity, crystallinity, and processing history when building descriptors.

## Verification

1. Train a polymer Tg or bandgap predictor and evaluate on a held-out test set.
2. Generate novel polymer candidates with a VAE and filter for synthesizability.
3. Predict rheological or permeability behavior and compare to experimental measurements.

## References

- https://doi.org/10.1002/masy.202400185
- https://www.mdpi.com/2073-4360/17/12/1667
- https://pubs.acs.org/doi/abs/10.1021/accountsmr.3c00288
- https://doi.org/10.66640/ujp-2026-5-00001
