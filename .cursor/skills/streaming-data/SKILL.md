# Streaming Data

## Description

Real-time data ingestion and processing with stream processors, message brokers, and event-time semantics.

## When to use

You have continuous, unbounded data (logs, events, sensors, clickstreams) and need low-latency ingestion, processing, or serving.

## Key concepts

- **Message brokers**: Kafka, RabbitMQ, Pulsar, NATS.
- **Stream processing**: Flink, Kafka Streams, Spark Structured Streaming, ksqldb.
- **Event time vs processing time**: watermarks, windows, late data handling.
- **Delivery semantics**: at-most-once, at-least-once, exactly-once.
- **State and checkpointing**: durable state, failure recovery, idempotent sinks.

## Code pattern

```python
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.table import StreamTableEnvironment

env = StreamExecutionEnvironment.get_execution_environment()
t_env = StreamTableEnvironment.create(env)

t_env.execute_sql("""
    CREATE TABLE events (
        event_id STRING,
        event_time TIMESTAMP(3),
        WATERMARK FOR event_time AS event_time - INTERVAL '5' SECOND
    ) WITH (
        'connector' = 'kafka',
        'topic' = 'events',
        'properties.bootstrap.servers' = 'localhost:9092',
        'format' = 'json'
    )
""")

t_env.execute_sql("""
    SELECT
        TUMBLE_START(event_time, INTERVAL '1' MINUTE) AS window_start,
        COUNT(*) AS cnt
    FROM events
    GROUP BY TUMBLE(event_time, INTERVAL '1' MINUTE)
""").print()
```

## Tuning notes

- Use event time with watermarks for out-of-order data.
- Tune buffer and parallelism to match throughput and latency targets.
- Choose at-least-once by default; exactly-once only where needed and supported.
- Store offsets and checkpoints externally for recoverability.

## Verification

1. Ingest a Kafka stream and compute windowed aggregates with Flink or Spark.
2. Simulate late records and verify watermark behavior.
3. Restart a job from a checkpoint and confirm no data loss or duplicates.

## References

- https://kafka.apache.org/documentation/
- https://nightlies.apache.org/flink/flink-docs-release-1.20/
- https://spark.apache.org/docs/latest/structured-streaming-programming-guide
- https://www.rabbitmq.com/docs
- https://www.confluent.io/resources/white-paper/event-driven-microservices/
