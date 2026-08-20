# AI for Research Communication

## Description

Drafting manuscripts, abstracts, cover letters, response-to-reviewers, and translating findings across disciplines with LLMs.

## When to use

You are writing or refining academic manuscripts, abstracts, cover letters, response-to-reviewers, or interdisciplinary summaries of research findings.

## Key concepts

- **Structured scientific writing**: follow IMRaD, abstract structures, and journal-specific guidelines.
- **Academic tone and style**: use LLMs to adjust formality, clarity, and field-specific conventions.
- **Citation and reference management**: ground drafts in uploaded PDFs and verified bibliographies.
- **Integrity checks**: detect accidental plagiarism, AI-patterned text, and citation errors.
- **Cross-disciplinary translation**: reframe findings for readers in adjacent fields.

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
