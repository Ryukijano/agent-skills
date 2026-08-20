# Imitation Learning

## Description

Behavioral cloning, DAgger, GAIL, and learning policies from expert demonstrations with or without a reward function.

## When to use

Expert demonstrations are available but a reward function is hard to design, or you want a good warm-start policy before RL fine-tuning.

## Key concepts

- **Behavioral cloning (BC)**: supervised learning of actions from state-action expert demonstrations.
- **DAgger**: iterative dataset aggregation that queries an expert on states visited by the learned policy.
- **Generative Adversarial Imitation Learning (GAIL)**: adversarially matches the state-action distribution of the expert.
- **SQIL**: soft Q imitation learning that assigns positive rewards to expert transitions.
- **DAgger with noisy rollouts**: improves robustness by collecting data under the learner's own state distribution.

## Code pattern

```python
from imitation.algorithms.bc import BC
from imitation.data import rollout

transitions = rollout.flatten_trajectories(expert_trajectories)
bc_trainer = BC(
    observation_space=env.observation_space,
    action_space=env.action_space,
    demonstrations=transitions,
)
bc_trainer.train(n_epochs=50)
```

## Tuning notes

- Demonstration coverage and quality dominate BC performance.
- Use DAgger when the test-time state distribution differs from the expert data.
- For GAIL, carefully tune the discriminator and use a strong policy optimizer.
- Add entropy regularization and early stopping to avoid overfitting.

## Verification

1. Evaluate the learned policy on the task and compare return to the expert.
2. For BC, report action MSE or classification accuracy on a held-out expert set.
3. For DAgger, show that test-time rollouts improve over multiple iterations.

## References

- https://arxiv.org/abs/1606.03476
- https://arxiv.org/abs/1011.0686
- https://imitation.readthedocs.io/en/stable/
- https://github.com/humancompatibleai/imitation
