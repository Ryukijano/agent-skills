# AI for Human-Centered AI

## Description

Use human-AI interaction, explainability, and participatory design to keep people at the center of AI systems.

## When to use

You are building an AI system that people must understand, trust, and effectively collaborate with, and you want to center end-user needs, capabilities, and values in the design.

## Usage

- Design prompts and interfaces for effective human-AI collaboration.
- Provide feature attribution, counterfactuals, and model cards for explainability.
- Collect human feedback with active learning and interactive model refinement.
- Calibrate trust and avoid overreliance through appropriate reliance interfaces.
- Co-design with stakeholders and impacted communities.

## Steps

1. Identify user needs, mental models, and values for the target task or decision.
2. Design the interaction (prompts, displays, explanations) and collect user feedback.
3. Implement explainability methods matched to the user's level of expertise.
4. Run human-AI experiments and measure task success, trust, and overreliance.
5. Iterate on the interface and model based on user feedback.
6. Deploy with monitoring for fairness, accessibility, and sustained human control.

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
