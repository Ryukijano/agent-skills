# AI for Shopping

## Description

Product discovery, personalized recommendations, price comparison, review summarization, and AI buyer guides for consumer purchases.

## When to use

You want to discover products, compare prices, summarize reviews, or build a personalized buyer guide for a consumer purchase.

## Key concepts

- **Product search and ranking**: retrieve and score items by relevance, value, and constraints.
- **Review summarization and sentiment**: extract pros, cons, and recurring issues from user reviews.
- **Attribute extraction**: pull specs, dimensions, and compatibility from unstructured text.
- **Price monitoring and alerts**: track price history and forecast deals.
- **Trust and verification**: ground claims in real listings and flag uncertain information.

## Code pattern

```python
from transformers import pipeline

# Summarize customer reviews for a product
reviews = "Great battery. Screen is dim. Fast shipping. ..."
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
summary = summarizer(reviews, max_length=60, min_length=10, do_sample=False)
```

## Tuning notes

- Avoid hallucinated specs; always link back to source listings.
- Disclose commercial relationships or affiliate links.
- Update prices and availability frequently; stale data misleads buyers.
- Balance personalization with transparency and user control.

## Verification

1. Summarize 50 reviews for a product category and compare to a manual summary.
2. Build a price-alert pipeline and verify it detects a price drop.
3. Compare an LLM buyer guide to a review-and-spec-based ranking.

## References

- https://product.ai/research/trust-in-ai-commerce-report/
- https://openai.com/index/chatgpt-shopping-research/
- https://www.ipsos.com/sites/default/files/ct/publication/documents/2026-07/ipsos-views-shopping-with-AI.pdf
- https://www.pymnts.com/study_posts/the-50-million-consumer-migration-the-data-behind-retails-shift-toward-ai-discovery/
