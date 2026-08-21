# AI for Evidence Synthesis

## Description

Synthesize heterogeneous evidence, assess risk of bias, and generate decision-ready summaries.

## When to use

You need to synthesize a body of literature, produce a systematic review, evidence map, or summary of research findings, and want to use AI responsibly.

## Usage

- Automate risk-of-bias assessment with LLMs (ROBINS-I, ROB2).
- Combine direct and indirect comparisons in network meta-analysis.
- Generate evidence maps and interactive summaries.
- Grade certainty with GRADE and robot reviewers.
- Produce plain-language summaries for guidelines.

## Steps

1. Frame the synthesis question and inclusion criteria.
2. Extract data, effects, and risk-of-bias judgments.
3. Choose a synthesis model (pairwise, network, dose-response).
4. Assess heterogeneity, inconsistency, and certainty.
5. Summarize findings for clinical and policy audiences.

## Code pattern

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

# Title/abstract screening with TF-IDF and logistic regression
vect = TfidfVectorizer(stop_words="english", max_features=5000)
X = vect.fit_transform(records_df["abstract"])
y = records_df["included"]

clf = LogisticRegression(class_weight="balanced", max_iter=1000).fit(X, y)
records_df["screening_score"] = clf.predict_proba(X)[:, 1]
```

## Tuning notes

- Maintain human accountability for all inclusion and synthesis decisions.
- Validate LLM outputs against full-text sources to avoid hallucinations.
- Use structured protocols and reporting standards (PRISMA, ENTREQ, ROBIS).
- Update the living review regularly with new search results.

## Verification

1. Reproduce a small published systematic review with AI-assisted screening.
2. Compare LLM-generated risk-of-bias ratings to human ratings on a gold-standard set.
3. Cross-check every synthesized claim against its source publication.

## References

- https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis/2DACF6D129AA6E46CB8A8740A03D0675
- https://www.ncbi.nlm.nih.gov/books/NBK620201/
- https://www.ncbi.nlm.nih.gov/pmc/articles/13035263
- https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.ED000178/full
- https://doi.org/10.1093/jamia/ocaf030
