# AI for Market Research

## Description

Design surveys, segment customers, analyze open-ended responses, and forecast market trends with AI-driven tools.

## When to use

You need to assess product-market fit, customer preferences, pricing sensitivity, or competitive positioning for a product or research spin-out.

## Key concepts

- **Survey design**: clear questions, response scales, sampling, and bias control.
- **Conjoint and MaxDiff**: measure feature and price preferences.
- **Synthetic panels and LLM responses**: fast, low-cost but require validation.
- **Text analysis of open-ends**: topic modeling, sentiment, and theme extraction.
- **Trend forecasting**: time-series models and leading-indicator tracking.

## Code pattern

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF


def analyze_open_ends(responses, n_topics=5):
    vectorizer = TfidfVectorizer(stop_words="english", max_features=500)
    X = vectorizer.fit_transform(responses)
    nmf = NMF(n_components=n_topics, random_state=42, max_iter=500)
    W = nmf.fit_transform(X)
    terms = vectorizer.get_feature_names_out()
    topics = [
        [terms[i] for i in topic.argsort()[-5:]]
        for topic in nmf.components_
    ]
    scores = pd.DataFrame(
        W, columns=[f"topic_{i}" for i in range(n_topics)]
    )
    return scores, topics
```

## Tuning notes

- Pre-test survey questions to avoid ambiguity and leading wording.
- Validate synthetic or LLM-generated responses against a small real panel.
- Protect respondent privacy and comply with data-use agreements.
- Combine quantitative scores with qualitative quotes for richer insight.

## Verification

1. Design a short survey for a product concept.
2. Collect or simulate 50+ responses and analyze the open-ended answers.
3. Compare AI-derived themes with a manual coding of a subset.

## References

- https://www.qualtrics.com/articles/strategy-research/agentic-ai-market-research/
- https://www.hbs.edu/ris/Publication%20Files/23-062_1f58623a-ee21-44b9-a262-276047bc5543.pdf
- https://www.surveymonkey.com/use-cases/market-research/
- https://esocorpwebsitestg.blob.core.windows.net/strapi-uploads/uploads/cltn6755401khqe3v0od2y6ut_esomar_20_questions_to_help_buyers_of_ai_based_services_0277e1b5eb.pdf
