# AI for Embedded AI

## Description

Use machine learning and co-optimization to deploy tiny models on microcontrollers, DSPs, and low-power SoCs.

## When to use

You are deploying ML on microcontrollers, DSPs, or low-power SoCs and need to meet latency, memory, and energy budgets.

## Usage

- Run sub-milliwatt inference on Cortex-M, RISC-V, or custom DSP cores.
- Quantize and prune models to int8/int16 with mixed precision.
- Co-design neural architectures and inference engines for a target MCU.
- Match operators, memory hierarchy, and on-device training to the hardware.

## Steps

1. Profile the target MCU for SRAM, Flash, and MAC limits.
2. Select or search a TinyML network with NAS and quantization.
3. Convert to TFLite Micro or CMSIS-NN with per-layer quantization.
4. Validate on the actual device, not just the simulator.
5. Measure latency and energy with MLPerf Tiny or board-level benchmarks.
6. Iterate on the network, operator support, and memory allocation.

## Code pattern

```python
import tensorflow as tf

# Convert a trained model to a quantized TFLite Micro model
converter = tf.lite.TFLiteConverter.from_saved_model("model")
converter.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model = converter.convert()
```

## Tuning notes

- Profile peak SRAM and Flash usage against the target device limits.
- Use per-layer quantization to preserve accuracy for sensitive layers.
- Validate on the actual embedded target, not just the host simulator, to catch timing and cache effects.

## Verification

1. Deploy a keyword-spotting model on a Cortex-M4 and measure latency/energy with MLPerf Tiny.
2. Run a TinyNAS search for an MCU and compare accuracy to a hand-tuned MobileNet.
3. Perform on-device inference on a held-out test set and confirm bit-exact outputs with the reference.

## References

- https://hanlab.mit.edu/projects/mcunet
- https://github.com/ARM-software/CMSIS-NN
- https://github.com/tensorflow/tflite-micro
- https://www.arm.com/resources/guide/machine-learning-on-cortex-m
