# AI for Crisis Communication

## Description

Use machine learning and NLP to extract verified information, detect rumors, translate and summarize crisis messages, and power public information chatbots.

## When to use

You must quickly extract, verify, and disseminate accurate information
during a disaster, emergency, or rapidly evolving public event.

## Usage

- Detect and classify crisis-related social media posts and events.
- Verify claims and score source credibility for rumor detection.
- Translate and summarize crisis briefs for diverse populations.
- Match needs and offers and power retrieval-grounded public chatbots.

## Steps

1. Collect crisis social media, official feeds, and fact-check data in multiple languages.
2. Train a classifier for information type and urgency.
3. Build a claim-verification pipeline that distinguishes confirmed from unverified reports.
4. Generate multilingual crisis briefs and evaluate clarity with experts.
5. Coordinate messaging through official channels and maintain uncertainty labels.

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
