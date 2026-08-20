# AI for Chemistry

## Description

Molecular property prediction, generative chemistry, reaction prediction, and cheminformatics with deep learning.

## When to use

You are predicting molecular properties, designing new molecules, or forecasting chemical reactions.

## Key concepts

- **Molecular fingerprints / SMILES / SELFIES**: text or vector representations of molecules.
- **Graph neural networks for molecules**: GNNs operate on atom-bond graphs.
- **Generative chemistry**: VAE, diffusion, or flow models for molecule design.
- **Reaction prediction**: models that predict products from reactants and reagents.
- **Datasets**: QM9, ZINC, ChEMBL, PubChem.

## Code pattern

```python
import deepchem as dc
from deepchem.feat import ConvMolFeaturizer
from deepchem.models import GraphConvModel

featurizer = ConvMolFeaturizer()
loader = dc.data.CSVLoader(tasks=["task"], feature_field="smiles", featurizer=featurizer)
dataset = loader.create_dataset("data.csv")
model = GraphConvModel(n_tasks=1, mode="regression")
model.fit(dataset)
```

## Tuning notes

- Use scaffold splits for realistic generalization estimates.
- Validate generated molecules for chemical plausibility and synthesizability.
- For reaction prediction, keep atom-mapping and reaction templates in mind.

## Verification

1. Train a GNN to predict a molecular property from SMILES.
2. Generate a set of candidate molecules and filter with RDKit.
3. Predict a small reaction product and compare to known outcome.

## References

- https://deepchem.io/
- https://www.rdkit.org/
- https://arxiv.org/abs/2401.14876
- https://doi.org/10.1038/s41586-023-06197-z
