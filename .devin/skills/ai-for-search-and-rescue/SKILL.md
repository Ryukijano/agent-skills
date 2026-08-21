# AI for Search and Rescue

## Description

Use machine learning and robotics to plan search coverage, detect victims from aerial and ground sensors, and coordinate human-robot teams in GNSS-denied or hazardous terrain.

## When to use

You are coordinating air, ground, or maritime search-and-rescue missions
in GNSS-denied, cluttered, or time-critical environments.

## Usage

- Plan coverage paths and information-theoretic search for air, ground, or maritime units.
- Detect victims from RGB, thermal, LiDAR, and acoustic sensors.
- Navigate autonomously and deliver payloads in rough terrain.
- Coordinate human-robot teaming with shared situational awareness.

## Steps

1. Fuse heterogeneous sensors and calibrate them for the environment.
2. Build a prior map of terrain, accessibility, and probability of detection.
3. Train a victim-detection or search-priority model on labeled aerial data.
4. Validate coverage and detection in a high-fidelity SAR simulator.
5. Run a field or simulation mission with human override for safety-critical calls.

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
- https://arxiv.org/abs/2503.02465v2
- https://arxiv.org/abs/2601.14973v2
- https://arxiv.org/abs/2306.02911
