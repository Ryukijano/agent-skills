# AI for Journalism

## Description

Algorithmic journalism, automated reporting, fact-checking, news recommendation, and AI-assisted investigative data reporting.

## When to use

You are producing, verifying, or distributing news and want to automate routine reporting, find leads in data, or assist reporters with research and drafting.

## Key concepts

- **Robot and automated journalism**: generate data-driven stories from structured feeds.
- **Computational news discovery**: detect anomalies, trends, and leads in public datasets.
- **Fact-checking and verification**: identify claims, source evidence, and detect misinformation.
- **News summarization and personalization**: adapt stories for platforms and audiences.
- **Editorial oversight and provenance**: log decisions, keep humans in the loop, and cite sources.

## Code pattern

```python
import pandas as pd
from jinja2 import Template

# Generate a simple data-driven news brief from a structured dataset
template = Template("{{ n }} incidents were reported in {{ city }} in {{ month }}, up {{ pct }}% from last year.")
row = {"n": 42, "city": "Springfield", "month": "March", "pct": 12}
print(template.render(**row))
```

## Tuning notes

- Human editorial judgment remains responsible for publication decisions and framing.
- Avoid hallucination by grounding generated text in verified source data.
- Monitor for bias in story selection, source diversity, and recommendation algorithms.
- Ensure transparent disclosure when content is automated or AI-assisted.

## Verification

1. Generate a batch of briefs from a public dataset and have a reporter review them.
2. Build a claim-detection pipeline and evaluate precision on a fact-check corpus.
3. Compare an AI-written summary to the original article for factual consistency.

## References

- https://arxiv.org/abs/2409.03462v1
- https://arxiv.org/abs/2603.13232
- https://aclanthology.org/2026.findings-acl.1816/
- https://workflow.ap.org/ai/
