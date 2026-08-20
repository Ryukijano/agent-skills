# Research Paper Ideation with AI

## Description

Use LLMs, citation networks, and structured brainstorming to generate and refine research questions, hypotheses, and project outlines.

## When to use

You are starting a new research project, exploring a new domain, or need to turn a broad interest into a focused, novel research question.

## Key concepts

- **Research question trees**: decompose a broad topic into nested, testable questions.
- **Literature gap analysis**: identify what has not been done by mapping existing work.
- **Hypothesis generation**: form falsifiable claims that connect methods, data, and outcomes.
- **Concept mapping**: visualize relationships between variables, mechanisms, and prior findings.
- **AI ideation agents**: use retrieval-augmented LLMs to propose, refine, and evaluate ideas against real papers.

## Code pattern

```python
import requests
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


def fetch_related_papers(paper_id, fields="title,abstract,year"):
    url = f"https://api.semanticscholar.org/graph/v1/paper/{paper_id}/references"
    params = {"fields": fields, "limit": 100}
    return requests.get(url, params=params, timeout=30).json()["data"]


def cluster_papers(papers, n=5):
    texts = [
        p["paper"]["title"] + " " + (p["paper"]["abstract"] or "")
        for p in papers
    ]
    X = TfidfVectorizer(stop_words="english", max_features=500).fit_transform(texts)
    labels = KMeans(n_clusters=n, random_state=42, n_init="auto").fit_predict(X)
    return pd.DataFrame(
        {"title": [p["paper"]["title"] for p in papers], "cluster": labels}
    )
```

## Tuning notes

- Always ground AI suggestions in real literature; verify citations exist and are relevant.
- Distinguish novelty from feasibility; a novel but infeasible idea is not a good project.
- Use multiple ideation rounds and diverse prompts to avoid anchoring on the first idea.
- Involve collaborators early to challenge assumptions and sharpen the question.

## Verification

1. Generate 5 candidate research questions for a target domain.
2. Map at least 30 related papers and cluster them to find gaps.
3. Pick one question and outline hypotheses, methods, and expected outcomes.

## References

- https://doi.org/10.1016/j.ijresmar.2023.10.002
- https://arxiv.org/html/2503.00946v3
- https://arxiv.org/pdf/2409.04109
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1013259
- https://openreview.net/forum?id=bIAFQ8asqi
