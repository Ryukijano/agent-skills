# AI for Human-Centered AI

## Description

Human-AI interaction, explainability, trust, feedback loops, participatory design, and human-in-the-loop ML to keep people at the center of AI systems.

## When to use

You are building an AI system that people must understand, trust, and effectively collaborate with, and you want to center end-user needs, capabilities, and values in the design.

## Key concepts

- **Human-AI interaction (HAII)**: designing prompts, interfaces, and interaction modes for collaboration.
- **Explainability and transparency**: feature attribution, counterfactuals, and model cards.
- **Human-in-the-loop ML**: active learning, feedback, and interactive model refinement.
- **Trust and overreliance**: calibrated trust, appropriate reliance, and cognitive load.
- **Participatory and value-sensitive design**: co-design with stakeholders and impacted communities.

## Code pattern

```python
import shap
from sklearn.inspection import permutation_importance

# Explain a model to a human reviewer
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X_test.iloc[:100])

# Identify which features most affect predictions
importance = permutation_importance(model, X_test, y_test, n_repeats=5)
feature_rank = dict(zip(X_test.columns, importance.importances_mean))
```

## Tuning notes

- Explainability should match the user's mental model, not just the model internals.
- Avoid over-automation; keep meaningful human control and graceful failure.
- Test with diverse user groups; trust and utility are context- and population-dependent.
- Measure task outcomes, not just model accuracy, in human-AI experiments.

## Verification

1. Run a human-AI co-creation study and compare idea quality and ownership across interaction modes.
2. Evaluate an explanation interface with a think-aloud protocol and task success.
3. Monitor for overreliance in a deployed decision-support tool and adjust confidence displays.

## References

- https://arxiv.org/abs/2601.11812
- https://dl.acm.org/doi/10.1145/3544548.3580959
- https://arxiv.org/abs/2310.07127
- https://arxiv.org/abs/2105.05424
