# Competitive Analysis with AI

## Description

Map industry structure, benchmark competitors, and identify strategic positioning using Porter's Five Forces, SWOT, and data.

## When to use

You are entering a new market, launching a product, writing an industry background section, or planning a strategic pivot.

## Key concepts

- **Porter's Five Forces**: rivalry, new entrants, substitutes, buyer power, supplier power.
- **SWOT**: Strengths, Weaknesses, Opportunities, Threats.
- **SCP framework**: Structure-Conduct-Performance and industry attractiveness.
- **Competitor profiling**: products, pricing, positioning, and capabilities.
- **Strategic positioning**: where to play and how to win.

## Code pattern

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def five_forces_radar(scores):
    categories = list(scores.keys())
    values = list(scores.values())
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    values += values[:1]
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    ax.plot(angles, values, "o-", linewidth=2)
    ax.fill(angles, values, alpha=0.25)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_ylim(0, 5)
    plt.title("Five Forces Scorecard")
    plt.savefig("five_forces_radar.png", dpi=300)


five_forces_radar({
    "rivalry": 4,
    "new_entrants": 2,
    "substitutes": 3,
    "buyer_power": 3,
    "supplier_power": 2,
})
```

## Tuning notes

- Ground scores in public data and primary sources, not intuition alone.
- Update the analysis regularly; competitive landscapes shift quickly.
- Distinguish facts from inference and label assumptions clearly.
- Pair Five Forces with a SWOT to capture internal and external factors.

## Verification

1. Build a Five Forces scorecard and a SWOT grid for a target market.
2. Compare your analysis with a published industry report.
3. Present it to stakeholders and test whether it informs decisions.

## References

- https://hbr.org/1979/03/how-competitive-forces-shape-strategy
- https://hbr.org/2008/01/the-five-competitive-forces-that-shape-strategy
- https://hbr.org/2021/02/are-you-doing-the-swot-analysis-backwards
- https://www.coursera.org/articles/competitor-analysis
- https://www.sba.gov/business-guide/plan-your-business/market-research-competitive-analysis
