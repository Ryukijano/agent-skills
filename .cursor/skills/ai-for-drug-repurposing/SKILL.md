# AI for Drug Repurposing

## Description

Graph ML, knowledge graphs, LLMs, and transcriptomics for identifying new indications for existing drugs.

## When to use

You want to find a new therapeutic use for an existing drug, rank candidates for a disease, or explain mechanistic rationale for off-label use.

## Key concepts

- **Drug repurposing (repositioning)**: finding new indications for approved drugs.
- **Knowledge graphs**: nodes for drugs, diseases, genes, pathways; edges for known relations.
- **Graph neural networks**: TxGNN and similar models for zero-shot indication prediction.
- **Signature matching**: match disease and drug transcriptomic signatures (e.g., LINCS, CMap).
- **Mechanistic grounding**: pathways, targets, and literature support.
- **Contraindications**: predicting when a repurposed drug is unsafe.

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
