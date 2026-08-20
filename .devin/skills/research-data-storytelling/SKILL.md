# Research Data Storytelling

## Description

Turn complex scientific results into narrative visualizations and stories that resonate with specialists and the public.

## When to use

You are preparing figures, a press release, a public talk, a grant impact section, or any communication where the story behind the data matters.

## Key concepts

- **Narrative arc**: setup, tension, resolution, and call to action.
- **Audience-centric design**: match the message to the reader's background.
- **Data-ink ratio and chart junk**: remove non-essential marks.
- **Annotations and callouts**: guide attention to the key data point.
- **Ethical representation**: show uncertainty, avoid misleading axes, and credit sources.

## Code pattern

```python
import matplotlib.pyplot as plt


def story_chart(years, values, highlight_year, message):
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.plot(years, values, marker="o", color="steelblue")

    idx = years.index(highlight_year)
    ax.annotate(
        message,
        xy=(highlight_year, values[idx]),
        xytext=(highlight_year + 1, values[idx] + 0.5),
        arrowprops=dict(facecolor="black", shrink=0.05, width=1, headwidth=6),
    )
    ax.set_title(message, fontsize=14, weight="bold")
    ax.set_ylabel("Measured value")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    fig.tight_layout()
    fig.savefig("story_figure.png", dpi=300)


story_chart(
    years=[2020, 2021, 2022, 2023, 2024],
    values=[12, 15, 18, 22, 35],
    highlight_year=2024,
    message="Treatment effect doubled after 2023",
)
```

## Tuning notes

- Identify one clear message for each visual and build around it.
- Use plain language titles; avoid jargon in public-facing graphics.
- Include error bars, confidence intervals, or sample sizes where relevant.
- Test visuals with a non-expert to ensure the story is clear.

## Verification

1. Design a figure that tells a specific story from your data.
2. Gather feedback from both a specialist and a non-specialist.
3. Check accessibility: color-blind safe palette, alt text, and readable labels.

## References

- https://doi.org/10.1109/tvcg.2010.179
- https://doi.org/10.1371/journal.pcbi.1003833
- https://help.tableau.com/current/pro/desktop/en-gb/story_best_practices.htm
- https://www.storytellingwithdata.com/books
- https://books.google.com/books/about/Storytelling_with_Data.html?id=rRSRCgAAQBAJ
