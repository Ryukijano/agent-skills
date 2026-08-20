# Real-Time Machine Learning and Low-Latency Inference

## Description

Streaming inference, online learning, low-latency GPU serving, event-time semantics, and service-level objectives for real-time ML systems.

## When to use

You must serve predictions or update models on continuously arriving data with strict latency and freshness requirements.

## Key concepts

- **Stream processing**: Kafka, Flink, ksqlDB, and cloud-managed streaming services.
- **Online learning**: incremental model updates from data streams.
- **Exactly-once / at-least-once**: delivery guarantees and idempotent consumers.
- **Event time vs. processing time**: handling out-of-order and late-arriving events.
- **SLOs and tail latency**: p50, p99 latency, throughput, and freshness windows.

## Code pattern

```python
from kafka import KafkaConsumer
import onnxruntime as ort
import json

consumer = KafkaConsumer(
    'events',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

session = ort.InferenceSession('model.onnx', providers=['CUDAExecutionProvider'])
input_name = session.get_inputs()[0].name

for msg in consumer:
    features = preprocess(msg.value)
    pred = session.run(None, {input_name: features})[0]
    emit(pred)
```

## Tuning notes

- Precompute and cache features to avoid repeated transformations at inference time.
- Use hardware-specific runtimes (TensorRT, ONNX Runtime) and batching for throughput.
- Set autoscaling based on queue depth and p99 latency, not just CPU.
- Monitor data drift continuously; stale models hurt real-time accuracy.

## Verification

1. Build a streaming inference pipeline and measure p50/p99 latency over 1M events.
2. Compare batch and online learning performance on a concept-drift benchmark.
3. Validate exactly-once semantics by replaying a small event log and checking outputs.

## References

- https://arxiv.org/abs/2410.15533
- https://arxiv.org/abs/2211.10280
- https://proceedings.neurips.cc/paper_files/paper/2023/file/7526508f11bbe0a123af62b9dab1fbe1-Paper-Conference.pdf
- https://developer.nvidia.com/blog/achieving-single-digit-microsecond-latency-inference-for-capital-markets/
- https://www.usenix.org/system/files/atc25-yu.pdf
