# AI for Digital Organism

## Description

Computational models, simulations, and multiscale foundation models of living systems as AI-driven digital organisms.

## When to use

You want to simulate evolution, cellular behavior, or multiscale biological systems in silico as an alternative to risky or expensive wet-lab experiments.

## Key concepts

- **Digital organisms**: self-replicating programs or agents that evolve in a virtual environment.
- **Artificial life (ALife)**: simulation of living systems and open-ended evolution.
- **Multiscale foundation models**: AIDO-style integration from molecules to organisms.
- **Agent-based models**: individuals interact, compete, and reproduce.
- **Genotype-phenotype maps**: how genotypic changes translate to phenotypes.
- **Evolutionary dynamics**: selection, mutation, drift, robustness, evolvability.

## Code pattern

```python
import numpy as np

# Conceptual grid-based digital ecosystem with four species
grid = np.random.randint(0, 4, (64, 64))

def propose_updates(grid, n_species=4):
    # Each species proposes a growth score for every cell
    return [np.random.rand(*grid.shape) + 0.1 * (grid == sp) for sp in range(n_species)]

def compete(proposals, grid):
    scores = np.stack(proposals)
    winner = scores.argmax(axis=0)
    # Keep current cell if its score is the highest
    return np.where(scores.max(axis=0) > 0.5, winner, grid)

for step in range(100):
    proposals = propose_updates(grid)
    grid = compete(proposals, grid)
    if step % 10 == 0:
        print('Step', step, 'dominant species:', np.bincount(grid.flat).argmax())
```

## Tuning notes

- Match simulation complexity to the question; simpler is better for hypothesis testing.
- Track phylogenies and fitness landscapes to understand evolvability.
- Reproducibility is critical; fix random seeds and log parameters.
- Use Parquet/standard formats for long-running simulation outputs.
- Compare digital-evolution results to known biological theory when possible.

## Verification

1. Evolve a population of digital organisms and plot diversity over time.
2. Reproduce a known evolutionary dynamics pattern (e.g., Muller plot, clonal interference).
3. Connect a digital-organism prediction to a wet-lab validation experiment.

## References

- https://www.nature.com/articles/s41591-026-04595-0
- https://doi.org/10.48550/arxiv.2412.06993
- https://evochora.org/
- https://github.com/mauriceling/dose
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005414
