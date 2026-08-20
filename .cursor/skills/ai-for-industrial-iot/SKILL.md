# AI for Industrial IoT

## Description

Industrial Internet of Things, edge-fog-cloud architectures, and AI for real-time monitoring, predictive maintenance, and secure shop-floor connectivity.

## When to use

You are connecting machines, sensors, and actuators across a plant or supply chain and need scalable, low-latency data pipelines for AI-driven operations.

## Usage

- **IIoT architecture**: design sensor, edge gateway, fog node, cloud, and digital thread layers.
- **Protocols**: use OPC UA, MQTT, Modbus, DDS, and Time-Sensitive Networking.
- **Edge AI and TinyML**: process data locally to reduce bandwidth and latency.
- **Time-series and streaming analytics**: use Kafka, InfluxDB, and anomaly detection on streams.
- **Security and data sovereignty**: implement encryption, device identity, and on-premise inference.

## Steps

1. Define the asset model, data sources, and latency/privacy requirements.
2. Deploy sensors, gateways, and a message broker or historian.
3. Ingest and time-align telemetry; build a streaming or batch analytics pipeline.
4. Train and deploy edge or cloud ML models for monitoring and prediction.
5. Secure devices, manage OTA updates, and monitor end-to-end data quality.

## Code pattern

```python
import paho.mqtt.client as mqtt
import json

# Subscribe to a machine telemetry topic
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload)
    # stream into InfluxDB or run anomaly detector
    print(payload)

client = mqtt.Client()
client.on_message = on_message
client.connect("edge-broker.local")
client.subscribe("factory/line1/press/telemetry")
client.loop_forever()
```

## Tuning notes

- Choose edge vs. cloud based on latency, bandwidth, and privacy requirements.
- Handle missing, delayed, and out-of-sequence sensor messages with robust buffering.
- Plan device management, OTA updates, and model versioning from the start.

## Verification

1. Ingest telemetry from at least one machine and verify end-to-end latency.
2. Deploy an edge anomaly detector and compare its recall to a cloud-based model.
3. Test security by validating device certificates and encrypted transport.

## References

- https://doi.org/10.1109/jsyst.2022.3193200
- https://dl.acm.org/doi/10.1145/3732287
- https://doi.org/10.3390/s25247636
- https://www.mdpi.com/1424-8220/24/24/7918
- https://ieeexplore.ieee.org/document/9784867
