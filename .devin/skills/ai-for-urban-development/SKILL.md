# AI for Urban Development

## Description

GeoAI, spatial modeling, generative urban design, and scenario simulation for sustainable, equitable, and data-driven urban development.

## When to use

You are planning urban growth, evaluating zoning or land-use scenarios, modeling housing and infrastructure needs, or assessing climate resilience.

## Usage

- **GeoAI and remote sensing**: classify urban fabric, monitor informality, and map green/gray infrastructure.
- **Scenario simulation**: use agent-based, cellular automata, and land-use change models.
- **Participatory planning**: synthesize public input and design options with LLMs.
- **Sustainable development metrics**: evaluate density, accessibility, emissions, and equity.

## Steps

1. Define planning objectives, boundaries, and stakeholder questions.
2. Integrate geospatial, demographic, economic, and mobility datasets.
3. Build or train spatial ML and generative models.
4. Run scenarios and quantify impacts across sustainability and equity metrics.
5. Co-design and iterate with planners and communities.

## Code pattern

```python
import geopandas as gpd
import rasterio
from sklearn.ensemble import RandomForestClassifier
import numpy as np

# Land-use/land-cover classification from satellite bands
X = np.stack([band.read(1).flatten() for band in bands], axis=1)
y = reference_classes.flatten()
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X, y)
```

## Tuning notes

- Validate spatially with out-of-bag or spatial cross-validation.
- Watch for data bias toward Global North cities.
- Couple models with governance and participatory review.

## Verification

1. Classify urban land cover and compare with ground-truth labels.
2. Run a scenario simulation and report key indicator changes.
3. Generate an LLM-assisted public-comment summary for a zoning proposal.

## References

- https://www.mdpi.com/2413-8851/10/3/148
- https://www.mdpi.com/2413-8851/9/12/508
- https://www.nature.com/articles/s44284-026-00492-2
- https://www.nature.com/articles/s43588-025-00846-1
- https://www.sciopen.com/article/10.1016/j.ese.2025.100526

## References

- https://www.mdpi.com/2413-8851/10/3/148
- https://www.mdpi.com/2413-8851/9/12/508
- https://www.nature.com/articles/s44284-026-00492-2
- https://www.nature.com/articles/s43588-025-00846-1
- https://www.sciopen.com/article/10.1016/j.ese.2025.100526
