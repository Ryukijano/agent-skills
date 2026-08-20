# AI for Architecture

## Description

AI for generative spatial layouts, floorplan synthesis, style exploration, and text/sketch-driven conceptual design.

## When to use

You are in early architectural concept design and want to generate massing, floorplans, spatial layouts, or style variations from text, sketches, or adjacency constraints.

## Key concepts

- **Language-driven layout generation**: prompt large language models to produce structured floorplan descriptions and adjacency graphs.
- **3D architectural synthesis**: autoregressive or diffusion models for building forms and interiors.
- **Sketch-to-architecture**: convert freehand sketches into 3D massing or floorplan renderings.
- **Graph and constraint-based layout**: encode room adjacencies and area constraints as optimization problems.
- **Space syntax and typology conditioning**: guide generation with circulation, daylight, and program rules.

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
