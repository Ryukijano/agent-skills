# Biodiversity and eDNA Analysis with ML

## Description

Environmental DNA, species distribution modeling, zero-shot taxonomic assignment, and biodiversity monitoring on GPU.

## When to use

You are using eDNA or camera-trap data to monitor biodiversity and species distributions.

## Key concepts

- **eDNA metabarcoding**: classify short reads to taxonomy.
- **Zero-shot annotation**: embedding-based assignment for unknown species.
- **Species distribution models (SDM)**: DeepSDM, attention U-Net.
- **Camera traps**: MegaDetector, SpeciesNet for automated classification.

## Code pattern

```python
# eDNA classifier
import torch
from metanode import MetAnoDe

model = MetAnoDe(...)
model = model.to('cuda')
```

## Tuning notes

- Reference databases are incomplete; use alignment-free methods and embeddings.
- Combine eDNA with environmental covariates (climate, soil).
- Handle class imbalance due to rare species.

## Verification

1. Classify eDNA samples and compare to known mock communities.
2. Run a species distribution model and evaluate AUC on held-out species.
3. Compare ML taxonomic assignment to BLAST/qiime2.

## References

- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013776
- https://github.com/KLKua/DeepSDM
- https://github.com/chiras/MetAnoDe
