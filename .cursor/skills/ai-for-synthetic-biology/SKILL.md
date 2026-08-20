# AI for Synthetic Biology

## Description

Machine learning for genetic circuit design, promoter and RBS optimization, metabolic pathway engineering, and closed-loop Design-Build-Test-Learn biofoundry pipelines.

## When to use

You are engineering genetic circuits, optimizing promoters/RBSs, or automating a DBTL cycle for a synthetic biology project.

## Key concepts

- **Genetic parts**: promoters, ribosome binding sites (RBS), terminators, coding sequences, and their context dependence.
- **DBTL cycle**: Design, Build, Test, Learn closed-loop iteration.
- **Predictive part models**: regression and sequence models trained on part activity data.
- **Metabolic engineering**: pathway design, flux balance analysis, retro-biosynthesis.
- **Active learning / Bayesian optimization**: pick the next strain or part to test.
- **Biological constraints**: chassis dependency, toxicity, genetic load, and modularity limits.

## Code pattern

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import GradientBoostingRegressor

# One-hot encode promoter sequences (A,C,G,T)
def one_hot(seq):
    mapping = {'A': [1,0,0,0], 'C': [0,1,0,0], 'G': [0,0,1,0], 'T': [0,0,0,1], 'N': [0,0,0,0]}
    return np.array([mapping[s] for s in seq.upper()]).flatten()

df = pd.read_csv('promoters.csv')  # columns: sequence, expression
X = np.vstack(df['sequence'].apply(one_hot))
y = df['expression'].values

model = GradientBoostingRegressor(n_estimators=200, max_depth=4)
score = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
print('CV RMSE:', np.mean(-score) ** 0.5)

model.fit(X, y)
# Predict expression of a new promoter
new_seq = 'TTGACATGATAACAGTAA...'
print(model.predict(one_hot(new_seq).reshape(1, -1)))
```

## Tuning notes

- Match training data to the intended chassis (e.g., E. coli, S. cerevisiae, mammalian cells).
- One-hot encoding works for short parts; for longer sequences consider k-mer counts or language models.
- Watch for context effects and promoter crosstalk; use paired designs when possible.
- Active learning reduces the number of experimental builds needed by 2-5x.
- Always validate in the target biological system; in silico predictors are noisy.

## Verification

1. Train an expression predictor on synthetic promoter data and report cross-validated error.
2. Suggest a set of promoters that spans low, medium, and high predicted expression.
3. Compare predicted and measured activity for at least 5 designed constructs.

## References

- https://doi.org/10.1016/j.cobme.2024.100553
- https://doi.org/10.1021/acssynbio.4c00091
- https://github.com/JBEI/ART
- https://github.com/snap-stanford/BioDiscoveryAgent
- https://biocomplete.it/
