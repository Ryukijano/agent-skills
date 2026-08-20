# AI for Embedded AI

## Description

TinyML, on-device inference, quantization, neural architecture search, and co-optimization for microcontrollers and DSPs.

## When to use

You are deploying ML on microcontrollers, DSPs, or low-power SoCs and need to meet latency, memory, and energy budgets.

## Key concepts

- **TinyML**: sub-1 mW inference on Cortex-M, RISC-V, or custom DSP cores.
- **Quantization and pruning**: int8/int16, unstructured/structured pruning, and mixed-precision search.
- **Neural architecture search (NAS)**: TinyNAS co-designs networks and inference engines for a target MCU.
- **Hardware-software co-design**: matching operator support, memory hierarchy, and on-device training.

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
