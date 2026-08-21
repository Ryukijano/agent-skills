# AI for Data Privacy

## Description

Protect sensitive data using differential privacy, anonymization, and federated learning.

## When to use

You train or serve ML models on personal, sensitive, or regulated data and need to protect privacy across the lifecycle.

## Usage

- Train models with differential privacy (Opacus, TensorFlow Privacy).
- Apply k-anonymity, l-diversity, and synthetic data generation.
- Run federated learning across institutions (NVIDIA FLARE, Flower).
- Audit re-identification risk and privacy budgets.
- De-identify free text with named-entity recognition.

## Steps

1. Classify sensitive attributes and privacy requirements.
2. Choose privacy mechanism (DP, federated, anonymization).
3. Implement training, aggregation, or synthesis.
4. Evaluate privacy-utility trade-off and budget.
5. Document privacy guarantees and audits.

## Code pattern

```python
import tensorflow_privacy as tfp
from tensorflow.keras import optimizers

# DP-SGD optimizer wrapper
optimizer = tfp.DPKerasSGDOptimizer(
    l2_norm_clip=1.0,
    noise_multiplier=0.5,
    num_microbatches=1,
    learning_rate=0.1,
)
```

## Tuning notes

- Trade off privacy budget against model utility on validation data.
- Account for composition across many queries or training steps.
- Validate that federated aggregation preserves privacy guarantees.

## Verification

1. Train a model with DP-SGD and report (epsilon, delta) privacy budget.
2. Run a membership inference attack and compare with and without DP.
3. Audit a synthetic or anonymized dataset for re-identification risk.

## References

- https://doi.org/10.1145/3440754
- https://doi.org/10.1145/3624010
- https://doi.org/10.1016/j.cose.2023.103605
- https://doi.org/10.3390/app16010277
