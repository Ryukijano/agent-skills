# AI for Site Selection

## Description

Rank retail and facility locations using mobility, demographic, and competitor data to maximize customer capture.

## When to use

You are choosing locations for stores, warehouses, facilities, or services based on demographics, competition, transport, and imagery.

## Usage

- **Location analytics**: integrate POI, mobility, satellite, and census data.
- **Revenue and footfall forecasting**: predict site performance by catchment and trade area.
- **Graph and spatial modeling**: capture neighborhood effects and cannibalization across a portfolio.
- **Multi-criteria decision**: balance revenue, cost, accessibility, and risk.

## Steps

1. Define site type, catchment, and success metric (revenue, footfall, ROI).
2. Assemble geospatial, mobility, demographic, and competitor data from CARTO, Kalibrate, or StreetLight.
3. Build features and train spatial or graph models.
4. Score and rank candidate sites.
5. Validate with actual site performance.

## Code pattern

```python
import networkx as nx
import torch

# Build a site-neighborhood graph from a transport network
G = nx.read_graphml('transport.graphml')
# Convert to PyTorch Geometric and train a GCN for site attractiveness
```

## Tuning notes

- Use spatial cross-validation to avoid leakage.
- Combine model scores with domain knowledge and zoning.
- Update models as new sites open and competitors move.

## Verification

1. Predict sales or footfall for a set of retail sites.
2. Compare GCN scores to a baseline XGBoost location model.
3. Generate an explainable site report for stakeholders.

## References

- https://dl.acm.org/doi/10.1145/3372406
- https://doi.org/10.1108/mscra-03-2019-0010
- https://mdpi-res.com/d_attachment/remotesensing/remotesensing-14-03579/article_deploy/remotesensing-14-03579-v2.pdf?version=1659596819
- https://fi.ee.tsinghua.edu.cn/~dingjingtao/papers/KnowSite-Sigspatial23.pdf
- https://onlinelibrary.wiley.com/doi/10.1111/tgis.12553
