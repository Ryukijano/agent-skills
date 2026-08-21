# AI for Factory Automation

## Description

Runs ML inference on PLCs, edge devices, and robot controllers for low-latency motion and quality control.

## When to use

You are deploying AI directly into automation systems: PLCs, edge devices, robot controllers, and SCADA to make control decisions with low latency and high reliability.

## Usage

- **PLC-based ML**: execute regression, classification, or neural networks on IEC 61131-3 controllers.
- **Industrial edge computing**: run ONNX or TensorFlow Lite models close to sensors and actuators.
- **AI motion control**: use reinforcement learning for path planning, positioning, and energy/force optimization.
- **OPC UA and MQTT**: standard protocols for real-time data exchange between controllers and AI.
- **Safety and determinism**: respect real-time cycles, guard limits, and fail-safe behavior.

## Steps

1. Profile latency, memory, and cycle-time constraints of the target controller.
2. Select and quantize a model suitable for PLC or edge execution.
3. Implement data exchange through OPC UA, MQTT, or shared memory.
4. Validate control behavior in simulation and with safe operating limits.
5. Deploy, monitor inference latency, and log all AI-driven actions.

## Code pattern

```python
import onnxruntime as ort

# Run an ONNX model on an industrial edge device
session = ort.InferenceSession("defect_classifier.onnx", providers=["CPUExecutionProvider"])
input_name = session.get_inputs()[0].name
outputs = session.run(None, {input_name: image_batch})
```

## Tuning notes

- Quantize and prune models to meet PLC or edge latency and memory budgets.
- Co-ordinate inference with control scan cycles; output jitter can destabilize control.
- Keep human oversight for safety-critical decisions and log all AI-driven actions.

## Verification

1. Deploy a lightweight model on a PLC or edge gateway and measure inference latency.
2. Compare an AI-optimized motion profile to a classical controller on cycle time and energy.
3. Test fail-safe behavior when the AI model returns an out-of-distribution prediction.

## References

- https://doi.org/10.1109/ETFA61755.2024.10710938
- https://www.mdpi.com/1424-8220/24/3/843
- https://doi.org/10.1007/978-3-030-99108-1_34
- https://doi.org/10.3390/computers13070172
- https://www.mdpi.com/2075-1702/13/12/1140
