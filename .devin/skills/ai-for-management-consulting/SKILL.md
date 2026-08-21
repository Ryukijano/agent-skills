# AI for Management Consulting

## Description

Use AI to build AI-augmented consulting workflows for market analysis, synthesis of client data, hypothesis generation, or executive-ready deliverables.

## When to use

You are building AI-augmented consulting workflows for market analysis, synthesis of client data, hypothesis generation, or executive-ready deliverables.

## Usage

- Map tasks to GenAI fit (automate, augment, or avoid).
- Synthesize client documents and prior proposals.
- Draft proposals, status reports, and deliverables.
- Ground claims to sources and cite evidence.

## Steps

1. Map tasks to GenAI fit (automate, augment, or avoid).
2. Synthesize client documents and prior proposals.
3. Draft proposals, status reports, and deliverables.
4. Ground claims to sources and cite evidence.
5. Audit for hallucinations and epistemic risk.
6. Deploy in client engagements, capture requirements from discovery calls, and measure time-to-insight and decision quality (Task-GenAI Fit-style).

## Code pattern

```python
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Cluster similar client documents or interview transcripts
vec = TfidfVectorizer(stop_words="english", ngram_range=(1, 2))
X = vec.fit_transform(documents)
sim = cosine_similarity(X)
```

## Tuning notes

- Keep human consultants in the loop for ambiguous, high-stakes judgments.
- Trace every AI-generated claim to a source document or dataset.
- Calibrate outputs to client style, confidentiality, and ethical standards.
- Monitor for hallucinations and over-reliance on generic benchmarks.

## Verification

1. Build a document-synthesis pipeline and compare output to a manually written summary.
2. Run a market-sizing model and verify inputs against published data.
3. Audit a sample of GenAI outputs for factual accuracy and source attribution.

## References

- https://doi.org/10.1007/s12599-026-00992-4
- https://www.wi.uni-muenster.de/research/publications/193019598
- https://doi.org/10.1016/j.infoandorg.2025.100559
- https://arxiv.org/abs/2409.06643
