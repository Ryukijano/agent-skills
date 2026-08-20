# AI for Political Science

## Description

Text-as-data for politics: manifesto scaling, sentiment and stance detection, legislative and voting analysis, and causal inference for political institutions.

## When to use

You are analyzing political texts, campaigns, legislatures, or public opinion and need to measure ideology, sentiment, stance, or institutional behavior from unstructured data.

## Key concepts

- **Text-as-data in politics**: scale party manifestos, speeches, and social media posts.
- **Stance and sentiment detection**: classify support or opposition toward candidates, issues, and policies.
- **Legislative roll-call and voting**: predict votes, measure polarization, and detect coalitions.
- **Causal inference for institutions**: estimate effects of reforms, campaigns, and policies.
- **Surveys and synthetic populations**: augment or benchmark measures with LLMs and polls.

## Code pattern

```python
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Supervised stance detection on political text
clf = make_pipeline(CountVectorizer(ngram_range=(1, 2)), MultinomialNB())
clf.fit(train["text"], train["stance"])
predictions = clf.predict(test["text"])
```

## Tuning notes

- Validate classifiers against expert or crowd-coded labels, not just accuracy.
- Account for temporal and partisan drift when deploying models on new election cycles.
- Be cautious about using LLM outputs as data without transparency and validation.
- Use out-of-time and cross-country tests to assess generalizability.

## Verification

1. Replicate a published manifesto scaling result and compare rankings.
2. Build a stance detector and evaluate F1 against expert annotations.
3. Predict roll-call votes and compare to a majority-class baseline.

## References

- https://doi.org/10.1017/psrm.2024.64
- https://www.cambridge.org/core/journals/political-science-research-and-methods/article/toward-a-framework-for-creating-trustworthy-measures-with-supervised-machine-learning-for-text/4DECB1072FB983F991BA84ADB01EAFC4
- https://www.cambridge.org/core/journals/political-science-research-and-methods/article/stance-detection-a-practical-guide-to-classifying-political-beliefs-in-text/E227E746BD7D9751526DA0EC2C378787
- https://www.cambridge.org/core/journals/ps-political-science-and-politics/article/applications-of-gpt-in-political-science-research-extracting-information-from-unstructured-text/7614D066F380A3751D298C2FF3C74F65
