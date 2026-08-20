# Feature Stores

## Description

Feast, Tecton, and Hopsworks for centralized feature definition, versioning, and online/offline serving.

## When to use

You need consistent, low-latency features shared across training and inference, with point-in-time correctness and versioning.

## Key concepts

- **Offline store**: historical feature data for training (data warehouse / lakehouse).
- **Online store**: low-latency key-value store for inference (Redis, DynamoDB, Bigtable).
- **Feature view**: a declarative group of features computed from data sources.
- **Point-in-time joins**: retrieve feature values as of each training example's timestamp.
- **Feast / Tecton / Hopsworks**: open-source and managed feature store platforms.

## Code pattern

```python
from feast import FeatureStore

store = FeatureStore(repo_path="feature_repo")

training_df = store.get_historical_features(
    entity_df=entities,
    features=["user_stats:daily_transactions", "user_stats:ltv"]
).to_df()
```

## Tuning notes

- Define clear entities, feature views, and feature services.
- Materialize features to the online store before serving.
- Monitor train/serve skew with freshness and distribution checks.

## Verification

1. Set up a feature repo with an offline and online store.
2. Materialize features and serve a sample online request.
3. Compare training-serving feature values for the same entity and timestamp.

## References

- https://feast.dev/
- https://docs.feast.dev/
- https://resources.tecton.ai/hubfs/Choosing-Feature-Solution-Feast-or-Tecton.pdf
- https://mlopsplatforms.com/posts/feature-store-comparison-2026/
