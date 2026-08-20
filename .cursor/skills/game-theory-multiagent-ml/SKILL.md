# Game Theory and Multi-Agent Learning

## Description

Nash equilibria, mean-field games, mechanism design, and deep multi-agent reinforcement learning.

## When to use

You are modeling strategic interactions among multiple agents or designing incentives.

## Key concepts

- **Nash equilibrium**: no agent can benefit by unilateral deviation.
- **Mean-field games**: approximate large N games with infinite-population limit.
- **Mechanism design**: design rules to achieve desired equilibria.
- **Multi-agent RL**: independent learners, opponent shaping, population-based training.

## Code pattern

```python
import nashpy as nash

A = [[3, 1], [0, 2]]
B = [[2, 1], [0, 3]]
game = nash.Game(A, B)
for eq in game.support_enumeration():
    print(eq)
```

## Tuning notes

- Equilibrium computation is hard; use approximations for large games.
- Mean-field games reduce complexity from O(N²) to O(N).
- Multi-agent training can be unstable; use curriculum or self-play.

## Verification

1. Compute Nash equilibria for a 2x2 matrix game.
2. Implement a mean-field game solver and compare to N-agent simulation.
3. Train two agents in a simple game and check convergence.

## References

- https://nashpy.readthedocs.io/
- https://doi.org/10.48550/arxiv.2510.21442
- https://proceedings.mlr.press/v202/yardim23a.html
- https://jmlr.org/papers/v24/21-0505.html
