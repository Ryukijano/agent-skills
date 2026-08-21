# AI for Chemistry

## Description

Use deep learning to predict molecular properties, design novel molecules, and forecast chemical reactions and retrosynthetic routes.

## When to use

You are predicting molecular properties, designing new molecules, or forecasting chemical reactions.

## Usage

- Predict molecular properties (solubility, toxicity, binding affinity) from SMILES, SELFIES, or molecular graphs.
- Generate and optimize drug or material candidates with VAE, diffusion, or flow models.
- Propose retrosynthetic routes and reaction conditions to shorten the DMTA cycle.
- Represent molecules with SMILES, SELFIES, fingerprints, or atom-bond graphs for model input.
- Filter generated structures for chemical plausibility and synthesizability with cheminformatics tools.
- Benchmark and validate models on datasets like QM9, ZINC, ChEMBL, and PubChem.

## Steps

1. Featurize molecules (SMILES/SELFIES, fingerprints, or graph) from a chemical dataset.
2. Train or fine-tune a GNN or transformer to predict a target molecular property.
3. Generate candidate molecules with a generative or diffusion model against a desired property profile.
4. Filter candidates for chemical plausibility, synthesizability, and patentability using RDKit and retrosynthesis tools.
5. Predict reaction products or retrosynthetic routes for the most promising candidates.
6. Validate shortlisted compounds with experimental or high-fidelity computational assays.

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
- https://github.com/rdkit/rdkit
- https://arxiv.org/abs/2401.14876
- https://doi.org/10.1038/s41586-023-06197-z
