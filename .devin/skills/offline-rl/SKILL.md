# Offline Reinforcement Learning

## Description

Learn from static logged datasets with CQL, IQL, TD3+BC, D4RL, and conservative/batch RL methods.

## When to use

You have a fixed, previously collected dataset and cannot or should not interact with the environment during training.

## Key concepts

- **Batch RL / offline RL**: learn a policy from a static set of transitions without new environment interaction.
- **Distributional shift**: the learned policy may visit out-of-distribution actions and states.
- **Conservative Q-Learning (CQL)**: regularizes Q-values to avoid overestimating OOD actions.
- **Implicit Q-Learning (IQL)**: learns a value function without querying OOD actions explicitly.
- **Decision Transformer and TD3+BC**: alternative offline methods using sequence modeling or behavior cloning regularization.

## Code pattern

```python
import d3rlpy
from d3rlpy.datasets import get_d4rl

dataset, env = get_d4rl('hopper-medium-v2')
cql = d3rlpy.algos.CQL(use_gpu=True)
cql.fit(dataset, n_steps=100000)
```

## Tuning notes

- The dataset quality and coverage heavily influence final performance.
- Conservative regularization should be strong enough to avoid OOD overestimation but not so strong that it paralyzes the policy.
- For continuous control, IQL is often a strong, easy-to-tune baseline.
- Use D4RL normalized scores for fair comparison.

## Verification

1. Train an offline algorithm on a D4RL dataset and report the normalized score.
2. Compare the offline policy to behavior cloning and online SAC baselines.
3. Evaluate on the real environment and check for OOD action selection.

## References

- https://doi.org/10.48550/arxiv.2006.04779
- https://arxiv.org/abs/2110.06169
- https://takuseno.github.io/d3rlpy/
- https://github.com/takuseno/d3rlpy
- https://github.com/Farama-Foundation/D4RL
