# AI for Drones

## Description

AI for UAV perception, navigation, obstacle avoidance, mission planning, multi-drone coordination, and vision-language drone control.

## When to use

You are building autonomous drones for inspection, delivery, search and rescue, mapping, or natural-language-guided navigation.

## Key concepts

- **Vision-based drone navigation**: VIO, visual SLAM, and object detection on embedded GPUs.
- **Foundation models for drones**: vision-language navigation, LLM mission planners, and neural policies.
- **Swarm and multi-UAV coordination**: task allocation, collision avoidance, and communication-constrained control.
- **Sim-to-real**: AirSim, Gazebo, and photorealistic simulators with domain transfer.

## Code pattern

```python
from ultralytics import YOLO
import cv2

# Detect objects from a drone camera feed for inspection
model = YOLO("yolov8n.pt")
frame = cv2.imread("drone_frame.jpg")
results = model(frame)
```

## Tuning notes

- Drones are resource-constrained; use lightweight models and TensorRT/ONNX for inference.
- Safety critical: enforce geofencing, fail-safe, and low-latency obstacle avoidance.
- Outdoor flight needs robustness to wind, lighting, and GNSS-denied conditions.

## Verification

1. Run a real-time object detector on a drone video feed and report FPS/accuracy.
2. Implement vision-based navigation in a simulator and test waypoint following.
3. Deploy a multi-drone task-allocation algorithm in a simulated swarm scenario.

## References

- https://doi.org/10.1016/j.array.2024.100361
- https://arxiv.org/html/2606.12142
- https://arxiv.org/html/2509.18610
- https://doi.org/10.13111/2066-8201.2026.18.2.9
