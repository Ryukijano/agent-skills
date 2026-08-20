# AI for Heritage Tourism

## Description

Recommender systems, itinerary planning, visitor behavior modeling, and personalized cultural heritage experiences for sustainable tourism.

## When to use

You are building personalized heritage itineraries, recommending cultural sites, forecasting visitor flows, or balancing tourism with heritage preservation.

## Key concepts

- **Cultural recommender systems**: collaborative filtering, content-based, and hybrid recommendations for heritage sites.
- **Itinerary and path planning**: route optimization, time constraints, and content-adaptive path recommendation.
- **Visitor behavior modeling**: spatiotemporal forecasting, sequence modeling, and crowd-flow prediction.
- **Sustainable heritage tourism**: balancing visitor experience with site carrying capacity and conservation.

## Code pattern

```python
import pandas as pd
from sklearn.neighbors import NearestNeighbors

# Content-based recommendation of heritage sites by user profile features
knn = NearestNeighbors(n_neighbors=5, metric="cosine")
knn.fit(site_features)
_, indices = knn.kneighbors([user_profile])
recommended_sites = sites.iloc[indices[0]]
```

## Tuning notes

- Tourist preferences are diverse and context-dependent; incorporate time, weather, and accessibility.
- Avoid filter bubbles by mixing popular and lesser-known heritage assets.
- Evaluate recommendations with both offline metrics and on-site visitor satisfaction.

## Verification

1. Build a heritage-site recommender and measure hit rate on a held-out test set.
2. Generate an optimized day itinerary and check feasibility against travel times.
3. Forecast visitor arrivals and compare to actual gate counts for a heritage site.

## References

- https://www.mdpi.com/2504-2289/4/2/12
- https://doi.org/10.4018/ijitsa.402196
- https://research.unipg.it/handle/11391/1616242
- https://doi.org/10.1038/s41598-025-22592-0
- http://scholar.uoa.gr/gealexandri/publications/personalized-and-content-adaptive-cultural-heritage-path-recommendation
