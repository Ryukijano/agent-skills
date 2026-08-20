# AI for Data Privacy

## Description

Differential privacy, federated learning, homomorphic encryption, PETs, and privacy-preserving ML for sensitive data.

## When to use

You train or serve ML models on personal, sensitive, or regulated data and need to protect privacy across the lifecycle.

## Usage

- **Differential privacy**: add calibrated noise to queries, gradients, or outputs.
- **Federated and split learning**: keep raw data at the edge while training shared models.
- **Homomorphic encryption and secure multiparty computation**: compute on encrypted data.
- **Anonymization and pseudonymization**: de-identify datasets and evaluate re-identification risk.
- **Privacy auditing**: run membership inference and model inversion tests.

## Steps

1. Classify data sensitivity and identify privacy requirements.
2. Choose PETs (DP, FL, SMPC, HE) appropriate to the threat model.
3. Implement privacy mechanisms and tune privacy budgets or noise.
4. Audit models with attack simulations and privacy metrics.
5. Document privacy controls and compliance evidence.

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
