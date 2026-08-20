# AI for Open Science

## Description

Reproducible research agents, open-source workbenches, provenance tracking, and computational reproducibility with AI.

## When to use

You want to make a research project open, reproducible, and auditable by automating literature review, code execution, provenance tracking, and FAIR data packaging.

## Key concepts

- **Open science principles**: open data, code, protocols, preprints, and transparent methods.
- **Reproducibility and replication packages**: containerized, documented, and versioned artifacts.
- **Provenance and RO-Crate**: record the origin and transformation of every dataset, figure, and model.
- **AI research workbenches**: agents that search literature, run experiments, and write reports with traceability.
- **FAIR and knowledge graphs**: make data Findable, Accessible, Interoperable, and Reusable.

## Code pattern

```python
import hashlib

# Example: create a content hash to track data provenance
with open("data.csv", "rb") as f:
    digest = hashlib.sha256(f.read()).hexdigest()
print("data.csv sha256:", digest)
```

## Tuning notes

- Prefer open-weight or local models when handling sensitive research data.
- Version data, code, and environment definitions together.
- Document every assumption, parameter, and random seed.
- Have an independent run attempt to reproduce the key results.

## Verification

1. Hand the project to a colleague and ask them to reproduce the main result from the README.
2. Compare AI-generated analysis outputs to the original data and code.
3. Check that every figure can be traced back to the script and dataset that produced it.

## References

- https://arxiv.org/html/2412.17859
- https://github.com/synthetic-sciences/openscience
- https://github.com/opencodon/opencodon
- https://reproai.org/
- https://arxiv.org/html/2409.11363
