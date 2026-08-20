# Federated Learning

## Description

Decentralized model training across clients, handling non-IID data, aggregation, and personalization.

## When to use

You need to train a model on data that is distributed across devices, hospitals, or institutions.

## Key concepts

- **Horizontal vs vertical FL**: same features across clients vs different feature sets.
- **FedAvg**: average client model updates weighted by data size.
- **Non-IID challenges**: client drift, pathological data distributions.
- **Personalization**: per-client or cluster-specific model heads.

## Code pattern

```python
import flower as fl

# Define a simple FedAvg server
strategy = fl.server.strategy.FedAvg(
    fraction_fit=0.5,
    min_available_clients=5,
)
fl.server.start_server(server_address="0.0.0.0:8080", strategy=strategy)
```

## Tuning notes

- Use secure aggregation for privacy-sensitive gradients.
- Adjust local epochs and learning rate to control client drift.
- Monitor per-client metrics, not just global loss.

## Verification

1. Partition a dataset into non-IID clients and run FedAvg.
2. Compare centralized and federated test accuracy.
3. Evaluate a personalized FL method on a heterogeneous client set.

## References

- https://arxiv.org/abs/2511.22616
- https://flower.ai/
- https://github.com/google-research/federated
- https://arxiv.org/abs/2507.15796
