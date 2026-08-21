# AI for Synthetic Biology

## Description

AI accelerates closed-loop Design-Build-Test-Learn cycles by predicting and optimizing genetic parts, pathways, and strains before they are built.

## When to use

You are engineering genetic circuits, optimizing promoters/RBSs, or automating a DBTL cycle for a synthetic biology project.

## Usage

- **Genetic-part prediction**: use regression and sequence models to score promoter, RBS, terminator, and coding-sequence activity in a chosen chassis.
- **DBTL acceleration**: close the Design-Build-Test-Learn loop by feeding assay data back into design models.
- **Pathway and strain optimization**: pick the next construct to build with active learning or Bayesian optimization.
- **Biological-constraint modeling**: account for chassis dependency, toxicity, genetic load, and context effects.
- **Assay interpretation**: apply ML to plate-reader, flow-cytometry, and proteomics outputs for phenotype calling.
- **Closed-loop biofoundry execution**: integrate predictions with robotic build and test workflows.

## Steps

1. Define the target function, host chassis, and constraints (titer, toxicity, genetic load).
2. Curate and encode genetic parts and historical part-activity data for that chassis.
3. Train predictive models for part activity, pathway flux, or strain phenotype.
4. Use active learning or Bayesian optimization to propose the next set of constructs.
5. Build and assay the proposed designs, then feed the measurements back into the model.
6. Validate top performers and transfer the best design to scaled production.

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
