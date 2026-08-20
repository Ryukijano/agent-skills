# AI for Evidence Synthesis

## Description

AI and LLMs for systematic review automation, risk-of-bias assessment, evidence mapping, and trustworthy synthesis of research findings.

## When to use

You need to synthesize a body of literature, produce a systematic review, evidence map, or summary of research findings, and want to use AI responsibly.

## Usage

- **Automated screening and extraction**: speed up systematic review production.
- **Risk-of-bias and quality assessment**: flag concerns and support appraisal.
- **Evidence maps and gap analysis**: categorize studies and identify research gaps.
- **Synthesis and manuscript support**: draft plain-language and technical summaries.

## Steps

1. Define the review question, scope, and search strategy in a registered protocol.
2. Run the search, deduplicate, and prepare title/abstract and full-text records.
3. Deploy AI-assisted screening and extraction with independent human checks.
4. Appraise risk of bias and synthesize findings narratively or quantitatively.
5. Verify claims against original sources and report AI contributions transparently.

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

## References

- https://www.cambridge.org/core/journals/research-synthesis-methods/article/generative-artificial-intelligence-use-in-evidence-synthesis/2DACF6D129AA6E46CB8A8740A03D0675
- https://www.ncbi.nlm.nih.gov/books/NBK620201/
- https://www.ncbi.nlm.nih.gov/pmc/articles/13035263
- https://www.cochranelibrary.com/cdsr/doi/10.1002/14651858.ED000178/full
- https://doi.org/10.1093/jamia/ocaf030
