# AI for Heritage Tourism

## Description

Use AI to build personalized heritage itineraries, recommend cultural sites, forecast visitor flows, or balance tourism with heritage preservation.

## When to use

You are building personalized heritage itineraries, recommending cultural sites, forecasting visitor flows, or balancing tourism with heritage preservation.

## Usage

- Build multimodal heritage site experiences.
- Personalize tours by interest, mobility, and language.
- Generate AR/VR reconstructions.
- Balance tourism access with conservation limits.

## Steps

1. Build multimodal heritage site experiences.
2. Personalize tours by interest, mobility, and language.
3. Generate AR/VR reconstructions.
4. Balance tourism access with conservation limits.
5. Evaluate visitor learning and satisfaction.
6. Validate digital outputs with heritage experts, source communities, and authority files before publication or physical intervention (Heritage Digital Twin-style).

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
