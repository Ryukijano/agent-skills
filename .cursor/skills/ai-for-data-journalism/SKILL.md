# AI for Data Journalism

## Description

Find, verify and visualize stories in public datasets, documents and real-time data streams to produce data-driven investigative reporting.

## When to use

You are investigating public datasets, leaked documents, FOIA releases, or real-time data streams and need to find and verify stories at speed.

## Usage

- **Algorithmically discover, monitor, and verify stories.**
- **Read CSV, JSON, PDF tables, and APIs with reproducible scripts.**
- **Identify people, organizations, and outliers in large corpora.**
- **Link every number, quote, and chart to the underlying source.**
- **Use full-text search, named-entity recognition, and cross-document linking.**

## Steps

1. Acquire public datasets, FOIA releases, or scraped documents and document the source and date.
2. Parse, clean, and join tables with reproducible scripts, tracking each transformation.
3. Use statistics, LLMs, or entity extraction to find anomalies, trends, and story leads.
4. Build charts and interactive graphics and ensure every value matches the source table.
5. Fact-check generated claims by locating the exact row, sentence, or document they came from.
6. Publish the methodology and data alongside the story for transparency and reproducibility.

## Code pattern

```python
import pandas as pd
import altair as alt

# Example: explore a dataset and export an interactive chart
df = pd.read_csv("public_spending.csv")
chart = alt.Chart(df).mark_bar().encode(
    x="department:N",
    y="amount:Q",
)
chart.save("spending_chart.html")
```

## Tuning notes

- Clean and document every data transformation; share the analysis notebook.
- Cross-check surprising findings with the source agency or a domain expert.
- Avoid ecological fallacy; report uncertainty and sample limits.
- Protect sources and personally identifiable information.

## Verification

1. Replicate a published data story from raw data and compare the headline numbers.
2. Generate a chart and manually verify a subset of values against the source table.
3. Fact-check a generated claim by locating the exact sentence or row it came from.

## References

- https://doi.org/10.48550/arxiv.2606.11176
- https://github.com/icij/datashare/
- https://datashare.icij.org/
- https://www.mdpi.com/2227-7080/10/3/68
- https://arxiv.org/abs/2409.07286
