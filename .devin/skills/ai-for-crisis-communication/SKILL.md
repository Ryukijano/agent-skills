# AI for Crisis Communication

## Description

Automated situational awareness, rumor detection, multilingual crisis summarization, and public information chatbots.

## When to use

You must quickly extract, verify, and disseminate accurate information
during a disaster, emergency, or rapidly evolving public event.

## Key concepts

- **Situational awareness from social media**: event detection,
  classification, and geolocation.
- **Rumor and misinformation detection**: claim verification and source
  credibility scoring.
- **Multilingual and cross-cultural communication**: machine
  translation and summarization for diverse populations.
- **Chatbots and public alerts**: LLM-driven, retrieval-grounded
  response systems.
- **Needs-offers matching**: connecting requests and resources during
  a crisis.

## Code pattern

```python
from transformers import pipeline

# Classify crisis-related social media posts by information type
classifier = pipeline(
    "text-classification",
    model="your-crisis-bert",
)
labels = classifier(posts)
```

## Tuning notes

- Integrate uncertainty signals; distinguish confirmed reports from
  unverified claims.
- Ground LLM responses in approved sources to prevent hallucination.
- Support low-connectivity and low-literacy audiences with simple
  formats and multiple languages.
- Coordinate messaging with official channels to avoid confusion.

## Verification

1. Classify social media posts into situational categories and report
   F1 per class.
2. Detect a rumor outbreak and compare against fact-checked reports.
3. Generate multilingual crisis briefs and evaluate clarity with
   domain experts.

## References

- https://arxiv.org/abs/2605.00829
- https://arxiv.org/pdf/2504.00046
- https://arxiv.org/abs/2402.10908
- https://arxiv.org/abs/2405.11897
- https://ojs.iscram.org/index.php/Proceedings/article/view/152
