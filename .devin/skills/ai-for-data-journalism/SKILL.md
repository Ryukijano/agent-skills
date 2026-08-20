# AI for Data Journalism

## Description

Using AI to find stories in datasets, fact-check claims, generate visualizations, and produce data-driven reporting.

## When to use

You are investigating public datasets, leaked documents, FOIA releases, or real-time data streams and need to find and verify stories at speed.

## Key concepts

- **Computational journalism**: algorithmic story discovery, monitoring, and verification.
- **Structured data parsing**: read CSV, JSON, PDF tables, and APIs with reproducible scripts.
- **Entity and anomaly detection**: identify people, organizations, and outliers in large corpora.
- **Verifiable claims**: every number, quote, and chart must link to the underlying source.
- **Document intelligence**: full-text search, named-entity recognition, and cross-document linking.

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
