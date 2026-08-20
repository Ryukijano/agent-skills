# Event-Driven Architecture

## Description

Events, event brokers, event sourcing, CQRS, and event-driven microservices for scalable, decoupled systems.

## When to use

You have multiple services or subsystems that need to react to state changes asynchronously, with loose coupling and auditability.

## Key concepts

- **Events and event brokers**: producers, consumers, topics, partitions, delivery semantics.
- **Event-driven microservices**: services communicate via events, not direct calls.
- **Event sourcing**: store state as a sequence of events; replay to reconstruct state.
- **CQRS**: separate read and write models, often materialized from events.
- **Patterns**: saga, outbox, event collaboration, stream-table joins.
- **Brokers**: Kafka, Pulsar, RabbitMQ, NATS, cloud event services.

## Code pattern

```python
from kafka import KafkaProducer, KafkaConsumer
import json

producer = KafkaProducer(
    bootstrap_servers=["localhost:9092"],
    value_serializer=lambda v: json.dumps(v).encode("utf-8"),
)

producer.send("orders", {"order_id": "123", "event": "OrderCreated", "amount": 99.0})

consumer = KafkaConsumer(
    "orders",
    bootstrap_servers=["localhost:9092"],
    value_deserializer=lambda v: json.loads(v.decode("utf-8")),
    group_id="inventory-service",
    auto_offset_reset="earliest",
)

for msg in consumer:
    print(msg.value)
    # trigger downstream action
```

## Tuning notes

- Design events as facts (e.g., OrderCreated), not commands or internal state dumps.
- Choose delivery semantics based on correctness needs; exactly-once is expensive.
- Use schemas (Avro/Protobuf/JSON Schema) with a registry for compatibility.
- Plan for consumer lag, replay, and event retention.

## Verification

1. Build a producer/consumer pair with Kafka or RabbitMQ.
2. Implement event sourcing with an aggregate that replays events to rebuild state.
3. Design a saga or outbox pattern to maintain consistency across services.

## References

- https://kafka.apache.org/documentation/
- https://martinfowler.com/eaaDev/EventSourcing.html
- https://www.oreilly.com/library/view/designing-event-driven-systems/9781492038252/titlepage01.html
- https://www.rabbitmq.com/docs
- https://developer.confluent.io/courses/microservices/event-driven-architecture/
