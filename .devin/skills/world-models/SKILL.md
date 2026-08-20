# World Models

## Description

Latent dynamics models, recurrent state-space models, Dreamer, PlaNet, and agents that plan in imagination.

## When to use

You need to learn an environment model from high-dimensional observations and use it for planning, credit assignment, or transferring policies from simulated rollouts.

## Key concepts

- **Recurrent state-space model (RSSM)**: combines deterministic and stochastic latent states.
- **Encoder/decoder**: compress observations into latents and reconstruct observations.
- **Latent imagination**: plan and optimize policies entirely in the learned latent space.
- **Dreamer**: actor-critic agent trained on imagined trajectories with long-term gradients.
- **MuZero and PlaNet**: model-based planning without reconstructing observations.

## Code pattern

```python
import torch
import torch.nn as nn

class WorldModel(nn.Module):
    def __init__(self, obs_dim, act_dim, hid=256):
        super().__init__()
        self.encoder = nn.Linear(obs_dim, hid)
        self.dynamics = nn.GRUCell(act_dim + hid, hid)
        self.decoder = nn.Linear(hid, obs_dim)
        self.reward = nn.Linear(hid, 1)

    def forward(self, obs, action, hidden):
        e = self.encoder(obs)
        h = self.dynamics(torch.cat([action, e], -1), hidden)
        return self.decoder(h), self.reward(h), h
```

## Tuning notes

- Balance reconstruction, reward, and dynamics losses.
- Stochastic latent states help capture partial observability and multi-modal futures.
- Use straight-through or REINFORCE estimators for discrete latent variables.
- Regularize the latent space (e.g., KL loss) to prevent overfitting to idiosyncrasies.

## Verification

1. Roll out the learned model and compare imagined vs. real trajectories.
2. Train a policy inside the world model and transfer it to the real environment.
3. Measure long-horizon reward prediction error and sample-efficiency gains.

## References

- https://arxiv.org/abs/1803.10122
- https://worldmodels.github.io/
- https://github.com/danijar/dreamerv3
- https://arxiv.org/abs/1912.01603
