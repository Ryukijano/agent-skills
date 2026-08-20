# User Interview Synthesis

## Description

Turn interview transcripts into themes, insights, and personas using thematic analysis, affinity mapping, and AI coding.

## When to use

You have completed qualitative user or stakeholder interviews and need to extract actionable themes, insights, and design implications.

## Key concepts

- **Thematic analysis**: identify, analyze, and report patterns across data.
- **Open and axial coding**: label quotes and group codes into themes.
- **Affinity diagramming**: cluster observations collaboratively on sticky notes or digital boards.
- **Personas and empathy maps**: synthesize user needs and contexts.
- **Saturation**: stop sampling when new interviews add no new themes.

## Code pattern

```python
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF


def code_transcripts(csv_path, n_themes=5):
    df = pd.read_csv(csv_path)
    quotes = df["quote"].dropna().astype(str)
    vectorizer = TfidfVectorizer(
        stop_words="english", ngram_range=(1, 2), max_features=500
    )
    X = vectorizer.fit_transform(quotes)
    nmf = NMF(n_components=n_themes, random_state=42, max_iter=500)
    W = nmf.fit_transform(X)
    df["dominant_theme"] = W.argmax(axis=1)
    terms = vectorizer.get_feature_names_out()
    themes = [
        [terms[i] for i in comp.argsort()[-5:]]
        for comp in nmf.components_
    ]
    return df, themes


df, themes = code_transcripts("interview_quotes.csv")
print(themes)
```

## Tuning notes

- Start synthesis with clear research questions, not the algorithm.
- Avoid confirmation bias; seek disconfirming evidence and edge cases.
- Involve the team; interpretation benefits from multiple perspectives.
- Triangulate interview findings with surveys, analytics, or prototypes.

## Verification

1. Synthesize 3-5 transcripts and produce a theme report.
2. Build an affinity diagram and compare it to the algorithmic output.
3. Compare theme assignments with an independent rater and compute agreement.

## References

- https://www.nngroup.com/articles/affinity-diagram/
- https://www.userinterviews.com/blog/affinity-mapping-ux-research-data-synthesis
- https://dovetail.com/research/research-synthesis/
- https://handbook.gitlab.com/handbook/upstream-studios/experience-research/analyzing-research-data/
- https://www2.uwe.ac.uk/services/Marketing/students/Newstudents/HAS/Using%20thematic%20analysis%20in%20psychology.pdf
