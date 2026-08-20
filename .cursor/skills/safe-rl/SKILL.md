# Safe Reinforcement Learning

## Description

Constrained Markov Decision Processes, CPO, P3O, Lagrangian methods, and safety-gym benchmarks for constrained RL.

## When to use

The task has explicit safety limits (velocity, collision, power) and the agent must maximize reward while keeping expected costs below a threshold.

## Key concepts

- **Constrained MDP (CMDP)**: maximize return subject to constraints on expected cumulative cost.
- **Constrained Policy Optimization (CPO)**: trust-region policy search with near-constraint satisfaction.
- **Primal-dual / Lagrangian methods**: PPO-Lagrangian, P3O, and TRPO-Lagrangian update a cost multiplier online.
- **Chance constraints and shielding**: ensure safety with high probability or via explicit safety filters.
- **Safety-Gymnasium**: standardized benchmark for constrained RL in navigation and locomotion.

## Code pattern

```python
import safety_gymnasium

env = safety_gymnasium.make('SafetyPointGoal1-v0')
obs, info = env.reset()
for _ in range(1000):
    action = env.action_space.sample()
    obs, reward, cost, terminated, truncated, info = env.step(action)
```

## Tuning notes

- Start with a strict cost limit and relax it as the policy converges.
- Primal-dual methods can oscillate; tune the Lagrange multiplier learning rate and projection.
- CPO is more conservative but expensive; Lagrangian methods scale better.
- Separate cost and value critics to avoid interference.

## Verification

1. Train with a cost limit and plot cumulative cost vs. training episodes.
2. Compare constrained return to an unconstrained baseline.
3. Test zero-shot constraint satisfaction on held-out cost limits.

## References

- https://arxiv.org/abs/1705.10528
- https://github.com/PKU-Alignment/safety-gymnasium
- https://safety-gymnasium.readthedocs.io/en/latest/
- https://proceedings.mlr.press/v162/liu22b.html
- https://arxiv.org/abs/2205.11814
