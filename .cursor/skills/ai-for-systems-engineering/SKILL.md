# AI for Systems Engineering

## Description

Apply AI to requirements, MBSE, and system reliability verification.

## When to use

You are architecting a complex system, managing requirements, running trade studies, building MBSE models, or planning verification and validation.

## Usage

- Parse requirements with NLP and flag inconsistencies.
- Build SysML/MBSE models in Cameo/MagicDraw with AI assist.
- Predict reliability and failure modes from digital threads.
- Optimize system architectures with multi-objective search.
- Verify and validate designs through simulation and digital twins.

## Steps

1. Elicit and structure requirements in DOORS or Jama.
2. Build or import SysML/UML models and system digital threads.
3. Train NLP or simulation models for risk and V&V.
4. Integrate predictions into MBSE and PLM workflows.
5. Update models as requirements and architectures evolve.

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
