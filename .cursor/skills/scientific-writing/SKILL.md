# Scientific Writing with AI

## Description

Improve clarity, structure, and style for manuscripts, theses, and reports using AI drafting and editing tools.

## When to use

You are drafting a manuscript, revising for a journal, or trying to make complex research accessible to a broader audience.

## Key concepts

- **IMRAD structure**: Introduction, Methods, Results, And Discussion.
- **C-C-C scheme**: Context-Content-Conclusion at the paragraph level.
- **Active voice and parallel structure**: improve readability and momentum.
- **Readability metrics**: Flesch-Kincaid grade, sentence length, word complexity.
- **Central contribution**: every section should reinforce the paper's main message.

## Code pattern

```python
import textstat
import re


def analyze_readability(text):
    sentences = [s for s in re.split(r"(?<=[.!?])\s+", text) if s.strip()]
    word_counts = [len(s.split()) for s in sentences]
    return {
        "flesch_kincaid_grade": textstat.flesch_kincaid_grade(text),
        "avg_sentence_length": sum(word_counts) / len(word_counts),
        "word_count": len(text.split()),
        "sentence_count": len(sentences),
    }


# Example: load a draft and flag overly long sentences
with open("draft.txt") as f:
    report = analyze_readability(f.read())
print(report)
```

## Tuning notes

- Put the central contribution in the title, abstract, and first paragraph.
- Write for flesh-and-blood readers who do not already know your work.
- Use AI for revision, not for fabricating citations or results.
- Verify that every claim in the introduction is supported in the results.

## Verification

1. Analyze a draft for readability and sentence length.
2. Restructure one section using the C-C-C scheme.
3. Compare the before and after versions with a co-author or reader.

## References

- https://doi.org/10.1371/journal.pcbi.1003453
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619
- https://www.gatsby.ucl.ac.uk/~pel/misc/gopen_swan.pdf
- https://www.coursera.org/learn/sciwrite
