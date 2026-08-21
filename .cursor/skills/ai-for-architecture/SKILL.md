# AI for Architecture

## Description

Use AI for Architecture to generate massing, floorplans and style variations from text or sketches.

## When to use

You are in early architectural concept design and want to generate massing, floorplans, spatial layouts, or style variations from text, sketches, or adjacency constraints.


## Usage


- **Language-driven layout generation**: Prompt large language models to produce structured floorplan descriptions and adjacency graphs.
- **3D architectural synthesis**: Autoregressive or diffusion models for building forms and interiors.
- **Sketch-to-architecture**: Convert freehand sketches into 3D massing or floorplan renderings.
- **Graph and constraint-based layout**: Encode room adjacencies and area constraints as optimization problems.
- **Space syntax and typology conditioning**: Guide generation with circulation, daylight, and program rules.

## Steps

1. Collect and prepare design briefs, sketches, adjacency graphs and constraints.
2. In early architectural concept design and want to generate massing.
3. Floorplans.
4. Spatial layouts.
5. Validate by generating 100 layouts from text prompts and check valid room adjacencies.
6. Deploy into the target workflow and monitor performance, drift, and outcomes.

## Code pattern

```python
import numpy as np
import networkx as nx

rooms = ["living", "kitchen", "bed1", "bed2", "bath"]
adj = np.array([
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 0, 1],
    [0, 0, 1, 1, 0],
])

G = nx.from_numpy_array(adj)
G = nx.relabel_nodes(G, {i: rooms[i] for i in range(len(rooms))})
pos = nx.spring_layout(G, seed=42)
# pos gives an initial spatial topology for refinement into a floorplan
```


## Tuning notes

- Use adjacency, area, and aspect-ratio constraints to filter invalid layouts.
- Fine-tune language models on domain-specific floorplan text or synthetic bubble diagrams.
- Combine parametric geometry (e.g., shapely, Rhino/Grasshopper) with generative models.
- Evaluate both design diversity and hard-constraint satisfaction, not just visual realism.


## Verification

1. Generate 100 layouts from text prompts and check valid room adjacencies.
2. Run a relevance or usefulness study with architects on generated concepts.
3. Compare generated floorplans to code-compliant area and accessibility guidelines.

## References

- https://arxiv.org/abs/2303.07519
- https://arxiv.org/abs/2412.17957
- https://arxiv.org/abs/2403.20186
- https://arxiv.org/abs/2405.09997
