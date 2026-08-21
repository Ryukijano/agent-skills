# AI for Drug Repurposing

## Description

Predict new indications for existing drugs by reasoning over biomedical knowledge graphs and transcriptomic signatures.

## When to use

You want to find a new therapeutic use for an existing drug, rank candidates for a disease, or explain mechanistic rationale for off-label use.

## Usage

- **Knowledge-graph reasoning**: use GNNs (e.g., TxGNN) to rank drug-disease indications and contraindications.
- **Transcriptomic signature matching**: match drug-perturbation and disease expression profiles (LINCS, CMap).
- **Real-world evidence integration**: combine in silico predictions with EHR, claims, or trial data.
- **Mechanistic explanation**: generate multi-hop graph paths or literature rationales for a prediction.
- **Safety filtering**: flag contraindications, adverse events, and pharmacokinetic concerns.
- **Candidate triage**: prioritize approved drugs with known human safety for faster experimental validation.

## Steps

1. Build or load a biomedical knowledge graph (diseases, drugs, genes, pathways) and/or a transcriptomic compendium.
2. Train or apply a graph/Siamese model to embed drugs and diseases (e.g., TxGNN, RPath, CellAwareGNN).
3. For a query disease, retrieve top drug candidates and compute indication and contraindication scores.
4. Cross-check candidates against opposing transcriptomic signatures and supporting literature.
5. Generate multi-hop mechanistic explanations and prioritize by safety and contraindication profiles.
6. Validate in cell or animal models, retrospective EHR, or clinical-trial registries.

## Code pattern

```python
from txgnn import TxData, TxGNN, TxEval

# Load the TxGNN knowledge graph
tx_data = TxData('./data/')
txg = TxGNN(model='.', data=tx_data, weight_bias_save='./weights/')

# Predict indication for a disease
txg.predict(indications=True, drug='DRUG_NAME', disease='DISEASE_NAME')

# Generate a mechanistic explanation for the prediction
txg.explain('DRUG_NAME', 'DISEASE_NAME')
```

## Tuning notes

- Zero-shot models need diseases not seen during training for a fair test.
- Combine in silico predictions with real-world evidence (claims, EHR, trial data).
- Use graph explainability to build a mechanistic case for experimental follow-up.
- Filter by safety, contraindications, and pharmacokinetics.
- Prioritize drugs with known human safety data to de-risk trials.

## Verification

1. Run TxGNN or DrugKLM for a query disease and inspect top-ranked drugs.
2. Check whether top candidates have supporting literature in PubMed.
3. Compare GNN predictions to signature-matching results for the same disease.

## References

- https://github.com/mims-harvard/TxGNN
- https://doi.org/10.1038/s41591-024-03233-x
- https://github.com/ncbi-nlp/DrugKLM
- https://doi.org/10.48550/arxiv.2604.19815
- https://github.com/SynDRep/SynDRep
