# AI for Type Theory

## Description

ML-guided tactic prediction, premise selection, and synthesis in dependent type theories and proof assistants.

## When to use

You are working in a dependently typed proof assistant (Coq, Lean, Agda, Idris) and want to automate tactic selection, lemma retrieval, or term synthesis.

## Key concepts

- **Dependent type theory**: Martin-Löf type theory, Calculus of Inductive Constructions, and homotopy/cubical type theory.
- **Tactic prediction**: train models to predict the next proof step from the proof state.
- **Premise selection**: rank library lemmas that are likely to be useful for a goal.
- **Lemma and term synthesis**: generate auxiliary lemmas or terms guided by types.

## Code pattern

```python
# Tactic prediction as a ranking problem
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Features encode goal/argument types and available tactics
X_train = np.array([[0, 1, 0, 1], [1, 0, 1, 0], ...])
y_train = np.array(["intro", "apply", "rewrite", ...])

clf = RandomForestClassifier(random_state=42).fit(X_train, y_train)
state_features = np.array([[0, 1, 0, 0]])
predicted_tactic = clf.predict(state_features)[0]
print("Next tactic:", predicted_tactic)
```

## Tuning notes

- Use tree-based models for fast interactive feedback in proof assistants.
- Augment tactic data with type-checker feedback and proof-state context.
- Validate synthesized terms by replaying them through the proof assistant kernel.

## Verification

1. Train a tactic predictor on a proof corpus and measure top-1 / top-5 accuracy.
2. Implement a premise-selection tool and check how often the human-used lemma is ranked first.
3. Synthesize a simple helper lemma and verify it with the proof assistant.

## References

- https://www.danielgratzer.com/papers/type-theory-book.pdf
- https://agda.readthedocs.io/en/latest/getting-started/what-is-agda.html
- https://doi.org/10.1145/3563306
- https://arxiv.org/html/2304.00994
- https://arxiv.org/html/2410.19605v1
