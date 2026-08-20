# Model-Based Reinforcement Learning

## Description

Learn environment dynamics for sample-efficient planning and policy optimization with PETS, MBPO, PlaNet, and MuZero.

## When to use

Environment interactions are expensive, slow, or risky, and you want a policy that is more sample-efficient than model-free methods.

## Key concepts

- **Learned transition and reward models**: train a neural network from real transitions.
- **Probabilistic ensembles**: capture epistemic uncertainty and avoid compounding errors.
- **Trajectory optimization / shooting**: CEM, MPPI, or cross-entropy planning in the learned model.
- **Model-based policy optimization (MBPO)**: use a learned model to generate synthetic training data.
- **PETS and PlaNet**: well-known probabilistic and latent model-based methods.

## Code pattern

```python
import mbrl.util.common as mutil
import mbrl.planning as planning
import gymnasium as gym

env = gym.make('CartPole-v1')
obs_shape = env.observation_space.shape
act_shape = env.action_space.shape

# Requires an OmegaConf-style config
dynamics_model = mutil.create_one_dim_tr_model(cfg, obs_shape, act_shape)
agent = planning.create_trajectory_optim_agent_for_model(model_env, cfg.algorithm.agent)
```

## Tuning notes

- Longer planning horizons amplify model bias; start short and increase gradually.
- Ensemble disagreement is a useful signal for exploration and uncertainty.
- Replan at every step or use a learned action sequence for real-time control.
- Use early termination and reward shaping to keep model rollouts stable.

## Verification

1. Compare sample efficiency (environment steps to target return) with model-free baselines.
2. Measure model prediction error on a holdout real transition set.
3. Verify that planning in the learned model transfers to the real environment.

## References

- https://doi.org/10.1561/2200000086
- https://github.com/facebookresearch/mbrl-lib
- https://arxiv.org/abs/2104.10159
- https://arxiv.org/abs/1805.12114
