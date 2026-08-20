# AI for Humanitarian Aid

## Description

AI across the crisis management cycle: needs assessment, resource allocation, routing, damage assessment, and early warning for disaster response.

## When to use

You are coordinating relief in natural or man-made crises and need faster needs assessment, logistics, or damage mapping.

## Key concepts

- **Crisis cycle AI**: early warning, preparedness, response, and recovery.
- **Multi-agent relief coordination**: LLM agents for task planning, routing, and information triage.
- **Post-disaster damage assessment**: use satellite, drone, or social-media imagery to classify building damage.
- **Beneficiary targeting**: integrate mobile, survey, and geospatial data to prioritize assistance.

## Code pattern

```python
import networkx as nx
import pandas as pd
from sklearn.cluster import KMeans

# Cluster affected zones by need and connect them to supply depots
need_points = df[["lat", "lon", "population", "severity"]]
clusters = KMeans(n_clusters=5, random_state=42, n_init="auto").fit(need_points)

G = nx.Graph()
# Add depot and demand nodes; solve a capacitated vehicle routing problem
```

## Tuning notes

- Balance speed and optimality during rapid-onset events; use heuristics when exact solvers are too slow.
- Keep human responders in the loop for life-safety and ethical decisions.
- Integrate offline mobile AI for connectivity-poor field settings.
- Map data biases from social-media or satellite sources to avoid undercounting rural areas.

## Verification

1. Run a simulated flood/earthquake response and compare AI-optimized routing to a baseline dispatch rule.
2. Classify post-disaster building damage on xBD or similar benchmark and report F1.
3. Test an LLM-based triage agent for correctness, safety, and escalation behavior.

## References

- https://doi.org/10.1016/j.technovation.2025.103415
- https://doi.org/10.3390/su18021014
- https://www.nature.com/articles/s41467-025-68216-z
- https://www.nature.com/articles/s41586-022-05422-504484-9
