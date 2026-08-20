# AI for Science Communication

## Description

Plain-language summaries, research storytelling, audience adaptation, and ethical, evidence-based use of generative AI for public-facing science.

## When to use

You need to translate technical scientific findings into accessible, engaging formats for the public, patients, educators, or policymakers while preserving accuracy.

## Key concepts

- **Plain-language summaries**: rewrite abstracts and papers for non-expert reading levels.
- **Audience adaptation**: tune tone, length, and examples for patients, teachers, journalists, or legislators.
- **Narrative and framing**: use story structure, metaphors, and relatable examples without overclaiming.
- **Multimodal science communication**: combine text, audio, slides, and visuals for broader reach.
- **Hallucination and fact-checking**: every generated claim must be traceable to the source paper.

## Code pattern

```python
import textstat

# Example: post-process a plain-language summary for target reading level
summary = "CRISPR edits DNA to treat disease."
print("Flesch-Kincaid grade:", textstat.flesch_kincaid_grade(summary))
```

## Tuning notes

- Target a specific reading level (e.g., Flesch-Kincaid 8-10 for general public).
- Preserve hedges and uncertainty (e.g., "suggests," "may," "in this sample").
- Always have a domain expert review AI-generated summaries before publication.
- Disclose AI assistance and maintain transparency about the source material.

## Verification

1. Generate a plain-language summary from a paper and compare its reading level to a human-written version.
2. Fact-check every generated claim against the original source.
3. Pilot the summary with a small non-expert audience and collect comprehension and trust metrics.

## References

- https://doi.org/10.1177/10755470251411176
- https://doi.org/10.1093/pnasnexus/pgae387
- https://doi.org/10.48550/arxiv.2308.16377
- https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0342852
