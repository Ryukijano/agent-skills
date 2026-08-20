# AI for Mythology

## Description

Computational mythography, knowledge graphs of mythological figures, structural analysis of myths, and cross-cultural narrative comparison.

## When to use

You are modeling mythological narratives, building knowledge graphs of mythic figures, or comparing structural patterns across world mythologies.

## Key concepts

- **Mythological knowledge graphs**: structured representations of characters, events, objects, and relationships in myths.
- **Structural analysis**: Levi-Straussian transformations, narrative oppositions, and formal models of mythic variation.
- **Entity and allusion detection**: LLM-based annotation of mythological references in literary and historical texts.
- **Cross-cultural comparison**: schema induction and network analysis to compare creation myths and pantheons.

## Code pattern

```python
import networkx as nx

# Build and query a simple mythological knowledge graph
G = nx.DiGraph()
G.add_edge("Zeus", "Hera", relation="sibling_spouse")
G.add_edge("Zeus", "Athena", relation="parent_child")
print(list(nx.descendants(G, "Zeus")))
```

## Tuning notes

- Mythologies are interpretively rich; encode scholarly sources and uncertainty in the knowledge graph.
- Be cautious with LLM hallucinations when extracting rare or polysemous mythological entities.
- Validate structural models against domain experts and comparative mythology scholarship.

## Verification

1. Build a knowledge graph for a pantheon and query family and conflict relations.
2. Extract mythological allusions from a literary corpus and evaluate precision/recall.
3. Compare creation-myth schemas across cultures using a shared schema framework.

## References

- https://doi.org/10.5281/zenodo.20253116
- https://arxiv.org/abs/2601.15078v1
- https://doi.org/10.48550/arxiv.2412.18270
- https://kgeographer.org/glos_creation_schema.html
- https://doi.org/10.1177/20539517211037862
