# AI for Humanitarian Aid

## Description

Use AI across the crisis management cycle for needs assessment, resource allocation, damage mapping, and early warning.

## When to use

You are coordinating relief in natural or man-made crises and need faster needs assessment, logistics, or damage mapping.

## Usage

- Support early warning, preparedness, response, and recovery with AI.
- Coordinate multi-agent relief planning, routing, and information triage.
- Classify post-disaster building damage from satellite, drone, or social-media imagery.
- Integrate mobile, survey, and geospatial data for beneficiary targeting.

## Steps

1. Identify the crisis phase and assemble relevant data (imagery, needs reports, logistics).
2. Train or configure models for damage classification, routing, or needs triage.
3. Use heuristics or solvers for rapid-onset logistics where exact methods are too slow.
4. Keep human responders in the loop for life-safety and ethical decisions.
5. Map data biases from social media or satellite sources to avoid undercounting.
6. Run simulated responses and iterate with frontline feedback.

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
