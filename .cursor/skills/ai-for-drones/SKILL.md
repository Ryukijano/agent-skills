# AI for Drones

## Description

Assess earthquake and flood damage from UAV imagery in real time to prioritize rescue routes and distribute aid.

## When to use

You are building autonomous drones for inspection, delivery, search and rescue, mapping, or natural-language-guided navigation.

## Usage

- Run visual-inertial odometry, SLAM, and object detection on embedded GPUs.
- Plan missions and allocate tasks across multi-UAV swarms.
- Use vision-language models and LLM planners for language-guided flight.
- Bridge photorealistic simulation to real flight with domain transfer.

## Steps

1. Select a lightweight model and TensorRT/ONNX runtime for the onboard computer.
2. Train perception and navigation networks on simulated and real flight data.
3. Implement geofencing, fail-safe, and low-latency obstacle avoidance.
4. Test in simulation for wind, lighting, and GNSS-denied scenarios.
5. Fly limited real-world missions and log metrics for retraining.

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
- https://arxiv.org/abs/2606.12142
- https://arxiv.org/abs/2509.18610
- https://doi.org/10.13111/2066-8201.2026.18.2.9
