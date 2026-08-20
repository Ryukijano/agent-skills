# Data Stream Processing for Machine Learning

## Description

Apache Kafka and Flink pipelines, event-time semantics, exactly-once delivery, online feature engineering, and real-time model updates.

## When to use

You need to ingest, transform, and act on high-velocity event data rather than processing everything in static batches.

## Key concepts

- **Data streams**: unbounded, time-ordered sequences of events.
- **Stream processing engines**: Apache Flink, Kafka Streams, Spark Structured Streaming, ksqlDB.
- **Event time vs. processing time**: windows and watermarks for out-of-order data.
- **Delivery guarantees**: at-most-once, at-least-once, exactly-once.
- **Online feature engineering**: real-time aggregations, joins, and point-in-time lookups.

## Code pattern

```python
from kafka import KafkaProducer, KafkaConsumer
import json

producer = KafkaProducer(
    bootstrap_servers='kafka:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Produce events
for record in event_source:
    producer.send('user-events', record)

# Consume and score events in real time
consumer = KafkaConsumer(
    'user-events',
    bootstrap_servers='kafka:9092',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

for msg in consumer:
    features = extract_online_features(msg.value)
    score = online_model.predict(features)
    if score > threshold:
        trigger_action(msg.value)
```

## Tuning notes

- Use keyed partitioning to keep related events on the same stream partition.
- Tune checkpointing, watermarks, and state backend for Flink jobs.
- Avoid training-inference skew by using the same feature transformation logic in both paths.
- Back-pressure and autoscaling are critical during traffic spikes.

## Verification

1. Deploy a Flink or Kafka Streams job and verify exactly-once output under failures.
2. Compare event-time windows to processing-time windows on out-of-order data.
3. Build a real-time feature pipeline and validate features against batch equivalents.

## References

- https://arxiv.org/abs/2410.15533
- https://arxiv.org/abs/1802.05872
- https://arxiv.org/abs/2211.10280
- https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/datastream/kafka/
- https://www.kai-waehner.de/blog/2024/10/01/real-time-model-inference-with-apache-kafka-and-flink-for-predictive-ai-and-genai/
