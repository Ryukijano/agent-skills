# Reinforcement Learning for Scientific Control

## Description

RL for tokamak plasma control, drug design, experiment design, and autonomous scientific systems.

## When to use

You are using RL to control a scientific system or optimize a design process.

## Key concepts

- **Algorithms**: PPO, SAC, DQN, model-based RL, offline RL.
- **Plasma control**: real-time tokamak shape/position tracking with deep RL at kHz rates.
- **Drug design**: ReLeaSE, AlphaDrug, ClickGen — RL agents in chemical space.
- **Experiment design**: RL for automated lab protocols.
- **Sim-to-real**: domain randomization, privileged information, simulators like NSFsim.

## Code pattern

```python
import torch
import gymnasium as gym

# Stable-Baselines3 PPO on a custom env
from stable_baselines3 import PPO
env = gym.make("Pendulum-v1")
model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100000)
```

For scientific envs, define state (observations), action, reward, and simulator.

## Tuning notes

- Sample efficiency matters; use model-based or offline RL for expensive simulators.
- Reward shaping should encode domain knowledge.
- Plasma control needs 4 kHz inference; use a small MLP/CNN and TensorRT.

## Verification

1. Train PPO on a toy control task and confirm policy converges.
2. Test in simulator before real hardware.
3. Measure inference latency on target deployment hardware.

## References

- https://www.nature.com/articles/s41586-021-04301-9
- https://www.science.org/doi/10.1126/sciadv.aap7885
- https://github.com/DLR-RM/stable-baselines3
- https://doi.org/10.1088/1741-4326/ae34c6
