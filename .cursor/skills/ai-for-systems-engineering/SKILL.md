# AI for Systems Engineering

## Description

AI for architecting complex systems, model-based systems engineering (MBSE), requirements analysis, trade studies, and verification.

## When to use

You are architecting a complex system, managing requirements, running trade studies, building MBSE models, or planning verification and validation.

## Usage

- **Model-based systems engineering (MBSE)**: SysML models and AI-augmented authoring.
- **Requirements engineering**: extraction, consistency checking, and traceability.
- **Trade studies and design-space exploration**: multi-objective optimization and digital threads.
- **Verification and validation (V&V)**: test planning, simulation-based validation, assurance cases.
- **Digital twins and digital threads**: linking lifecycle data to system models.

## Steps

1. Collect requirements, MBSE models, trade-study data, and test plans.
2. Structure data into traceable requirements and architecture elements.
3. Train a requirements/traceability/optimization model with human review.
4. Validate against system simulations and stakeholder review.
5. Maintain model provenance as the design evolves.

## Code pattern

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans

# Cluster system requirements by topic
docs = df["requirement_text"].fillna("")
X = TfidfVectorizer(stop_words="english").fit_transform(docs)
df["cluster"] = KMeans(n_clusters=5, random_state=42, n_init="auto").fit_predict(X)
```

## Tuning notes

- Integrate AI with SysML/MBSE tools and versioned repositories.
- Use human-in-the-loop for safety-critical and mission-critical systems.
- Maintain traceability between generated artifacts and source requirements.

## Verification

1. Extract requirements from a document and measure coverage vs. a gold set.
2. Run a trade-study optimizer and compare to a baseline architecture.
3. Verify an MBSE model consistency against a set of rules.

## References

- https://doi.org/10.1017/pds.2025.10058
- https://doi.org/10.48550/arxiv.2606.06727
- https://www.mdpi.com/2079-8954/13/7/584
- https://doi.org/10.23919/JSEE.2024.000066
