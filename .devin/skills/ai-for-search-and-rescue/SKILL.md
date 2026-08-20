# AI for Search and Rescue

## Description

UAV and robot search planning, victim detection from imagery and sensors, and SAR mission coordination with AI.

## When to use

You are coordinating air, ground, or maritime search-and-rescue missions
in GNSS-denied, cluttered, or time-critical environments.

## Key concepts

- **Search planning**: coverage path planning, information-theoretic
  search, and multi-UAV task allocation.
- **Victim detection**: vision, thermal, and acoustic detection of
  persons and distress signals.
- **Rescue robotics**: autonomous navigation, manipulation, and
  payload delivery in rough terrain.
- **Human-robot teaming**: shared situational awareness and safe
  proximity navigation.

## Code pattern

```python
import numpy as np

# Score grid cells by probability of detection and accessibility
prior = np.ones_like(terrain_map) / terrain_map.size
likelihood = detectability_map * prior
best_cell = np.unravel_index(likelihood.argmax(), likelihood.shape)
```

## Tuning notes

- Integrate heterogeneous sensors (RGB, thermal, LiDAR, sound) with
  care for calibration and time synchronization.
- Plan for limited battery, communication range, and weather constraints.
- Use simulation environments to stress-test before field deployment.
- Include human override for safety-critical decisions.

## Verification

1. Run a coverage planner in a high-fidelity SAR simulation.
2. Evaluate victim-detection accuracy on a held-out aerial image set.
3. Compare a learned task-allocation policy to a greedy baseline.

## References

- https://arxiv.org/abs/2502.20326
- https://arxiv.org/html/2503.02465v2
- https://arxiv.org/html/2601.14973v2
- https://arxiv.org/abs/2306.02911
