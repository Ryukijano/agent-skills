# AI for Public Policy

## Description

Use AI for Public Policy to evaluate programs, predict service demand and audit equitable allocation.

## When to use

You are designing, implementing, or evaluating public programs and need evidence on what works, for whom, and under what conditions.


## Usage


- **Causal machine learning for policy**: Heterogeneous treatment effects, causal forests, and double/debiased ML.
- **Counterfactual policy evaluation**: Synthetic controls, difference-in-differences, and interrupted time series.
- **Predictive analytics for public services**: Risk modeling, demand forecasting, and resource allocation.
- **Regulatory and legislative text analysis**: Parse rulemaking comments, statutes, and contracts.
- **Equity and accountability**: Audit for disparate impact and ensure explainability.

## Steps

1. Collect and prepare program, administrative and survey data.
2. Design.
3. Implemente.
4. Evaluate public programs and need evidence on what works.
5. Validate by replicating a published policy evaluation with a causal ML estimator.
6. Deploy into the target workflow and monitor performance, drift, and outcomes.

## Code pattern

```python
from econml.dml import LinearDML
from sklearn.ensemble import GradientBoostingRegressor

# Estimate the effect of a job-training program on earnings
est = LinearDML(
    model_y=GradientBoostingRegressor(random_state=42),
    model_t=GradientBoostingRegressor(random_state=42),
)
est.fit(Y, T, X=covariates)
print("ATE:", est.ate_)
print("CATE:", est.cate(X=covariates[:5]))
```


## Tuning notes

- Use cross-fitting and out-of-fold nuisance predictions to avoid overfitting.
- Validate causal claims with placebo tests, pre-trend checks, and sensitivity analysis.
- Consider external validity and transportability across jurisdictions.
- Balance predictive accuracy with fairness and transparency for high-stakes decisions.


## Verification

1. Replicate a published policy evaluation with a causal ML estimator.
2. Run a placebo test and confirm no effect before the treatment date.
3. Compare model recommendations to a status-quo allocation on held-out cases.

## References

- https://www.oecd.org/en/publications/governing-with-artificial-intelligence_795de142-en/full-report/ai-in-policy-evaluation_c88cc2fd.html
- https://www.cambridge.org/core/journals/data-and-policy/article/transparency-challenges-in-policy-evaluation-with-causal-machine-learning-improving-usability-and-accountability/DA780C002E4D4309655CB0DEEC88BC79
- https://www.cambridge.org/core/journals/data-and-policy/article/explainable-machine-learning-for-public-policy-use-cases-gaps-and-research-directions/B5B66B3C3B16196482984E878D795161
- https://www.frontiersin.org/journals/public-health/articles/10.3389/fpubh.2025.1502599/full
