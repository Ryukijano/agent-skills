# Curriculum Reinforcement Learning

## Description

Task sequencing, automatic curriculum generation, and progressive difficulty for sample-efficient RL.

## When to use

The target task is too hard to learn from scratch, and you can generate a sequence of easier tasks or starting states that gradually build skills.

## Key concepts

- **Curriculum learning**: present tasks from easy to hard according to the learner's current ability.
- **Teacher-student curriculum (TSCL)**: a teacher selects subtasks where the student makes the fastest progress.
- **Reverse curriculum generation**: start near the goal and sample increasingly distant initial states.
- **Prioritized level replay (PLR) and domain randomization**: adapt task difficulty via learning progress or regret.
- **Reward/constraint curricula**: gradually introduce terms or increase strictness.

## Code pattern

```python
import gymnasium as gym

def make_env(level=0):
    # difficulty increases with level
    return gym.make('FrozenLake-v1', map_name=["4x4", "8x8", "12x12"][level], is_slippery=True)

curriculum = [make_env(level=i) for i in range(3)]
# train agent sequentially on each level before advancing
```

## Tuning notes

- Choose a difficulty measure aligned with true learning progress (not just episodic return).
- Keep easier tasks in the mix to avoid catastrophic forgetting.
- Advance the curriculum only when the current level reaches a threshold.
- Monitor transfer from curriculum tasks to the target task.

## Verification

1. Compare final performance and sample complexity with and without the curriculum.
2. Track success rate at each curriculum stage over time.
3. Ablate curriculum pacing and measure robustness on the target task.

## References

- https://arxiv.org/abs/2003.04960
- https://arxiv.org/abs/1707.00183
- https://proceedings.mlr.press/v78/florensa17a.html
- https://proceedings.mlr.press/v70/graves17a.html
