# AI for Science Communication

## Description

Use generative AI to turn scientific findings into clear, audience-tailored public communications—such as plain-language summaries and multimedia explainers—while preserving accuracy.

## When to use

You need to translate technical scientific findings into accessible, engaging formats for the public, patients, educators, or policymakers while preserving accuracy.

## Usage

- **Rewrite abstracts and papers into plain-language summaries for non-expert, patient, and public reading levels.**
- **Tune tone, length, and examples for policymakers, journalists, educators, patients, and social media.**
- **Use story structure, metaphors, and relatable examples while preserving uncertainty and avoiding overclaiming.**
- **Combine text, audio, slides, and visuals into accessible, multimodal explainers.**
- **Make every generated claim traceable to the source paper and disclose AI assistance.**

## Steps

1. Identify the target audience, channel, and reading level for the science message.
2. Extract and verify key claims, uncertainties, and source evidence from the original paper or dataset.
3. Generate a plain-language or narrative draft with an LLM prompted for the specific audience and format.
4. Enrich the draft with analogies, visuals, or multimedia while preserving scientific nuance.
5. Fact-check every claim against the source, cite evidence, and disclose AI assistance.
6. Pilot test with a sample audience and refine for comprehension, trust, and accessibility.

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
