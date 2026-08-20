# Hierarchical Reinforcement Learning

## Description

Options, feudal networks, and goal-conditioned hierarchies for long-horizon, sparse-reward tasks.

## When to use

Tasks are long-horizon, rewards are sparse or delayed, and you need temporal abstraction or reusable sub-skills.

## Key concepts

- **Options framework**: high-level actions are closed-loop sub-policies with initiation, execution, and termination conditions.
- **Semi-Markov Decision Process (SMDP)**: formalizes actions that take variable time.
- **Feudal networks**: manager sets abstract goals and worker selects primitive actions.
- **Goal-conditioned HRL**: high-level policy proposes subgoals; low-level policy reaches them (HIRO, HRO).
- **Option-critic**: joint learning of options and their policies end-to-end.

## Code pattern

```python
import torch
import torch.nn as nn

class HierarchicalAgent(nn.Module):
    def __init__(self, state_dim, action_dim, goal_dim):
        super().__init__()
        self.high_level = nn.Linear(state_dim, goal_dim)     # subgoal generator
        self.low_level = nn.Linear(state_dim + goal_dim, action_dim)

    def forward(self, state, goal):
        return self.low_level(torch.cat([state, goal], -1))
```

## Tuning notes

- Non-stationarity between high-level and low-level policies is the main challenge; use off-policy correction or fixed low-level pretraining.
- Choose subgoal spaces that are learnable but expressive.
- Control the time scale of each level; common values range from 10 to 100 steps.
- Reward the low-level with intrinsic goal-reaching rewards.

## Verification

1. Solve a maze or long-horizon navigation task and compare to a flat RL baseline.
2. Measure success rate and sample efficiency across difficulty levels.
3. Analyze option/subgoal usage to confirm meaningful temporal abstraction.

## References

- https://doi.org/10.3390/make4010009
- https://arxiv.org/abs/1609.05140
- https://arxiv.org/abs/1709.02374
- https://arxiv.org/abs/1805.08296
- https://github.com/tensorflow/models/tree/master/research/efficient-hrl
