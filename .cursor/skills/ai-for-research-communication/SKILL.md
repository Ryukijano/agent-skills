# AI for Research Communication

## Description

Use LLMs to draft, refine and translate academic manuscripts, cover letters, responses to reviewers and interdisciplinary summaries while grounding every claim in verified sources.

## When to use

You are writing or refining academic manuscripts, abstracts, cover letters, response-to-reviewers, or interdisciplinary summaries of research findings.

## Usage

- **Draft and revise IMRaD sections, abstracts, and cover letters that follow journal guidelines.**
- **Adjust formality, clarity, and field-specific conventions for the target venue.**
- **Ground drafts in uploaded PDFs and verified bibliographies, not invented DOIs.**
- **Detect accidental plagiarism, AI-patterned phrasing, and citation errors before submission.**
- **Reframe findings for readers in adjacent fields and for broader impact statements.**

## Steps

1. Assemble source materials: paper, outline, reviewer comments, target journal guidelines, and reference library.
2. Generate a structured first draft of the section (abstract, cover letter, response to reviewers) using the sources as context.
3. Refine tone, length, and terminology to match the journal or correspondence style.
4. Verify every citation, DOI, statistic, and claim against the original sources.
5. Run integrity and style checks, then compare the draft to the original human version.
6. Finalize with author edits and maintain a record of AI involvement for transparency.

## Code pattern

```python
from transformers import pipeline

# Example: condense a long methods section into an abstract-sized summary
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
short = summarizer(long_methods, max_length=120, min_length=30, do_sample=False)
```

## Tuning notes

- Feed the model your own sources, outline, and reviewer comments to keep outputs grounded.
- Avoid asking the model to invent citations; verify every DOI and page number.
- Maintain author voice by editing generated drafts rather than publishing them raw.
- Use dedicated tools (e.g., Paperpal, Elicit, Semantic Scholar) for citation-aware writing.

## Verification

1. Draft an abstract from a full paper and compare it to the original for accuracy and style.
2. Run a reference check to confirm every generated citation exists and supports its claim.
3. Have a colleague compare an LLM-edited response-to-reviewers to a human-only version.

## References

- https://peelback.ai/
- https://paperpal.com/
- https://sciencecast.org/
- https://github.com/microsoft/ResearchStudio
- https://aclanthology.org/2025.aisd-main.4.pdf
