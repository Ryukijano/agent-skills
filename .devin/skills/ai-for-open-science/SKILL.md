# AI for Open Science

## Description

Make research reproducible and auditable by automating literature review, code execution, provenance tracking and FAIR data packaging with AI agents.

## When to use

You want to make a research project open, reproducible, and auditable by automating literature review, code execution, provenance tracking, and FAIR data packaging.

## Usage

- **Share open data, code, protocols, preprints, and transparent methods.**
- **Build containerized, documented, and versioned replication packages.**
- **Record the origin and transformation of every dataset, figure, and model.**
- **Deploy agents that search literature, run experiments, and write reports with traceability.**
- **Make data Findable, Accessible, Interoperable, and Reusable.**

## Steps

1. Organize the project with versioned data, code, environment files, and a clear README.
2. Use an agent or script to search literature, extract methods, and draft reproducible analysis notebooks.
3. Track provenance with content hashes, container definitions, and RO-Crate or PROV-O metadata.
4. Run the analysis end-to-end and compare outputs to expected values and original data.
5. Package results as a replication archive with figures linked to the scripts that produced them.
6. Share the package under an open license and attempt an independent reproduction by a colleague.

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

- https://arxiv.org/abs/2412.17859
- https://github.com/synthetic-sciences/openscience
- https://github.com/opencodon/opencodon
- https://reproai.org/
- https://arxiv.org/abs/2409.11363
