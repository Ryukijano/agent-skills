# Meta-Learning

## Description

Learn-to-learn methods such as MAML, metric learning, and neural processes for fast adaptation.

## When to use

You need a model that adapts to new tasks with only a few examples.

## Key concepts

- **Optimization-based**: MAML, iMAML, Reptile.
- **Metric-based**: Prototypical Networks, Matching Networks, Siamese networks.
- **Model-based**: Neural Turing Machines, LSTM meta-learners, Neural Processes.
- **Task distribution**: meta-train and meta-test on separate tasks.

## Code pattern

```python
import learn2learn as l2l

maml = l2l.algorithms.MAML(model, lr=0.01, first_order=False)
for task in tasks:
    # Inner loop adaptation
    learner = maml.clone()
    for _ in range(5):
        train_error = loss(learner(X_train), y_train)
        learner.adapt(train_error)
```

## Tuning notes

- Meta-learning can overfit to the meta-train task distribution.
- Second-order MAML is expensive; first-order methods are common.
- Use proper task sampling to ensure diversity.

## Verification

1. Train MAML on a few-shot image classification benchmark.
2. Adapt the model to a held-out class with 5 examples.
3. Compare meta-learned initialization to pretrained + fine-tuning.

## References

- https://arxiv.org/abs/2402.03017
- https://github.com/learn2learn/
- https://arxiv.org/abs/1703.03400
- https://arxiv.org/abs/1707.03141
