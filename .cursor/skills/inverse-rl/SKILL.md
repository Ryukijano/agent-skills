# Inverse Reinforcement Learning

## Description

Recover reward functions from expert demonstrations using MaxEnt IRL, apprenticeship learning, and adversarial IRL.

## When to use

You need to infer the objective that an expert is optimizing, design a reward function from behavior, or understand intent in sequential tasks.

## Key concepts

- **Reward ambiguity / degeneracy**: many reward functions can explain the same optimal policy.
- **Feature expectations**: match expected feature counts between expert and learned policy.
- **Maximum Entropy / Maximum Causal Entropy IRL**: resolves ambiguity via a principled distribution over trajectories.
- **Apprenticeship learning**: learn a policy whose feature expectations match the expert.
- **Adversarial IRL (AIRL) and GAIL**: recover rewards via a discriminator that distinguishes expert from learner.

## Code pattern

```python
import numpy as np
from imitation.algorithms.mce_irl import MCEIRL
from imitation.rewards import reward_nets

reward_net = reward_nets.BasicRewardNet(
    env.observation_space,
    env.action_space,
    hid_sizes=[256],
)
mce_irl = MCEIRL(
    expert_demonstrations,
    env,
    reward_net,
    log_interval=250,
    optimizer_kwargs=dict(lr=0.01),
    rng=np.random.default_rng(0),
)
mce_irl.train()
```

## Tuning notes

- Feature/reward network design is critical; include state, action, and next-state features when relevant.
- Add regularization to avoid degenerate reward solutions.
- Use a strong RL algorithm to re-optimize the recovered reward.
- Ground-truth rewards, when available, are the best validation signal.

## Verification

1. Optimize a policy with the recovered reward and compare its return to the expert.
2. Measure feature-expectation distance between expert and learned policy.
3. Inspect the learned reward on a grid of representative states.

## References

- https://people.eecs.berkeley.edu/~russell/papers/ml00-irl.pdf
- https://www.cs.cmu.edu/~bziebart/publications/maximum-causal-entropy.pdf
- https://arxiv.org/abs/1710.11248
- https://arxiv.org/abs/1806.06877
