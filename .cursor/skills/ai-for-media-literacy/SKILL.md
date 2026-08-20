# AI for Media Literacy

## Description

AI for detecting disinformation, prebunking, source credibility, and teaching critical thinking and digital literacy.

## When to use

You want to help users identify misinformation, understand manipulation tactics, evaluate sources, and develop resilience against online deception.

## Key concepts

- **Misinformation and disinformation detection**: classify false or misleading claims across text, images, and video.
- **Prebunking and inoculation**: expose users to weakened manipulation tactics before they encounter them.
- **Source and claim credibility**: assess website reliability, author expertise, and evidence quality.
- **Explainable AI for literacy**: make detection models transparent so users learn from them.
- **Generative AI awareness**: teach users how synthetic media is created and how to spot it.

## Code pattern

```python
from transformers import pipeline

# Zero-shot classification for manipulative tactics in a headline
classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
text = "Shocking secret they do not want you to see!"
labels = ["emotional manipulation", "conspiracy", "sensationalism", "legitimate news"]
result = classifier(text, labels)
for label, score in zip(result["labels"], result["scores"]):
    print(f"{label}: {score:.3f}")
```

## Tuning notes

- Frame tools as learning aids, not oracles; avoid undermining trust in genuine news.
- Include media-literacy explanations and interactive exercises, not just flags.
- Tailor interventions to age, language, and cultural context.
- Evaluate impact with pre/post tests and real-world believability measures.

## Verification

1. Test a misinformation detector on a labeled fact-check dataset and report AUC-PR.
2. Run a prebunking micro-intervention and compare pre/post quiz scores.
3. Have users rate the helpfulness and fairness of AI-generated explanations.

## References

- https://aclanthology.org/2026.acl-demo.48/
- https://cordis.europa.eu/article/id/464673-when-ai-also-becomes-a-disinformation-ally
- https://www.titanthinking.eu/
- https://www.fzi.de/en/project/discoboard/
