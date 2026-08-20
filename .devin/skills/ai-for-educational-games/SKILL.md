# AI for Educational Games

## Description

Game-based learning, adaptive difficulty, intelligent NPCs, scaffolding, and learning analytics embedded in playful environments.

## When to use

You are building or adapting games that teach concepts through interactive, adaptive, and engaging play.

## Key concepts

- **Digital game-based learning (DGBL)**: use games to motivate and support learning.
- **Adaptive difficulty and player modeling**: adjust challenge to maintain flow.
- **Intelligent NPCs**: AI characters that scaffold, coach, or converse with players.
- **Procedural content generation**: create varied levels, puzzles, and scenarios.

## Code pattern

```python
# Simple adaptive difficulty based on recent player performance
recent = [1, 1, 0, 1, 1]  # 1 = success, 0 = failure
success_rate = sum(recent) / len(recent)

if success_rate > 0.8:
    next_level = current_level + 1
elif success_rate < 0.4:
    next_level = max(1, current_level - 1)
else:
    next_level = current_level
```

## Tuning notes

- Balance learning objectives with player enjoyment and autonomy.
- Avoid excessive scaffolding that removes productive struggle.
- Collect learning evidence and validate against a non-game baseline.

## Verification

1. Design a short learning game around a specific concept.
2. Implement adaptive difficulty and test retention on repeated play.
3. Measure learning gains and motivation compared to a traditional lesson.

## References

- https://journals.sagepub.com/doi/10.1177/07356331251396354
- https://eric.ed.gov/?id=EJ1445818
- https://link.springer.com/article/10.1007/s10639-025-13624-3
- https://ojs.aaai.org/index.php/AAAI/article/view/30354
