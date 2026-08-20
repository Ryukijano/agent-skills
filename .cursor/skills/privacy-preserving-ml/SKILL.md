# Privacy-Preserving Machine Learning

## Description

Differential privacy, federated learning, homomorphic encryption, and secure multi-party computation for ML.

## When to use

You are training or deploying models on sensitive data and must protect individual privacy.

## Key concepts

- **Differential privacy**: randomized mechanisms with formal privacy budgets.
- **Federated learning**: train across decentralized data without centralization.
- **Homomorphic encryption / MPC**: compute on encrypted data.
- **Synthetic data**: generate privacy-safe training data.

## Code pattern

```python
import tensorflow_privacy as tfp
from tensorflow_privacy.privacy.optimizers.dp_optimizer import DPKerasSGDOptimizer

optimizer = DPKerasSGDOptimizer(
    l2_norm_clip=1.0,
    noise_multiplier=0.8,
    num_microbatches=1,
    learning_rate=0.01
)
```

## Tuning notes

- Balance privacy budget with model utility; smaller epsilon, larger noise.
- Federated learning protects data in transit but does not guarantee privacy alone.
- Consider threat models and linkability attacks.

## Verification

1. Train a model with DP-SGD and report (epsilon, delta) for a fixed accuracy.
2. Run a membership-inference attack on a standard and a private model.
3. Implement a federated averaging loop on a partitioned dataset.

## References

- https://arxiv.org/abs/2508.13730
- https://www.oecd.org/publications/sharing-trustworthy-ai-models-with-privacy-enhancing-technologies_5df6fd05
- https://www.tensorflow.org/responsible_ai/privacy
- https://opacus.ai/
