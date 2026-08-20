# AI for Autonomous Vehicles

## Description

Perception, prediction, planning, and simulation for self-driving cars and mobile robots.

## When to use

You are working on perception, motion forecasting, path planning, or end-to-end driving for autonomous vehicles.

## Key concepts

- **Perception**: 3D object detection, tracking, lane detection, segmentation.
- **Prediction**: trajectory forecasting for agents in a scene.
- **Planning**: rule-based, sampling-based, or learned planners.
- **Simulation**: CARLA, nuPlan, Waymo Open, nuScenes.
- **Safety and redundancy**: functional safety, ODD, scenario coverage.

## Code pattern

```python
import av2

# Load a NuScenes-like scene and run a simple 3D detector
from nuscenes.nuscenes import NuScenes
nusc = NuScenes(version='v1.0-mini', dataroot='/data/nuscenes', verbose=False)
```

## Tuning notes

- Pay attention to class imbalance and rare objects (e.g., pedestrians, cyclists).
- Test under diverse weather, lighting, and geographic conditions.
- Use closed-loop simulation to evaluate planning, not just open-loop.

## Verification

1. Train a 2D or BEV object detector on a public AV dataset.
2. Run a simple motion-prediction baseline on nuScenes.
3. Evaluate a planner in closed-loop simulation (e.g., nuPlan).

## References

- https://www.nuscenes.org/
- https://www.nuscenes.org/nuplan
- https://carla.org/
- https://arxiv.org/abs/2306.07962
