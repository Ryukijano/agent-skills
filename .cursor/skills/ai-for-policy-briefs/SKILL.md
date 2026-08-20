# AI for Policy Briefs

## Description

Converting scientific evidence and legislative text into concise, actionable policy briefs and impact analyses.

## When to use

You need to turn a scientific paper, a body of evidence, or a legislative document into a short, decision-ready policy brief for government, agencies, or advocacy groups.

## Key concepts

- **Policy brief structure**: problem, evidence, policy options, recommendations, and implications.
- **Science-to-policy translation**: reframe technical findings into actionable, audience-specific guidance.
- **Stakeholder and impact analysis**: map who is affected, how, and what trade-offs exist.
- **Evidence synthesis**: combine multiple studies while tracking source credibility and recency.
- **Hallucination control**: policy briefs must not invent statistics, legal clauses, or citations.

## Code pattern

```python
from sklearn.feature_extraction.text import TfidfVectorizer

# Example: identify key themes across a set of policy documents
vectorizer = TfidfVectorizer(max_features=20, stop_words="english")
X = vectorizer.fit_transform(policy_docs)
print(vectorizer.get_feature_names_out())
```

## Tuning notes

- Tailor length and tone to the specific decision-maker and meeting context.
- Use verified sources (peer-reviewed research, official legislation, government data).
- Lead with the recommendation; support it with concise evidence and trade-offs.
- Have a policy expert review the brief before it reaches decision-makers.

## Verification

1. Generate a one-page brief from a scientific paper and compare it to a human-written brief.
2. Verify that every statistic and citation in the brief exists and is accurately represented.
3. Ask a policy professional to rate clarity, relevance, and actionability.

## References

- https://doi.org/10.48550/arxiv.2509.21493
- https://openreview.net/forum?id=S6gJESWNSX
- https://doi.org/10.1038/d41586-023-02999-3
- https://algorithms.dk/responsible-use-of-ai-in-scientific-advice/
