# AI for Risk Management

## Description

Credit, market, operational, and emerging risk modeling with ML and scenario analysis.

## When to use

You are quantifying credit, market, operational, or emerging risks; building early-warning systems; or stress-testing portfolios and operations.

## Key concepts

- **Risk modeling**: probability of default, loss distribution, and value-at-risk estimation.
- **Anomaly and tail-risk detection**: spot rare events and emerging vulnerabilities.
- **Scenario and stress testing**: evaluate sensitivity to shocks and regime changes.
- **Model risk management**: validate, monitor, and govern AI risk models.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingClassifier

# Credit-risk probability of default from borrower features
X = df[["income", "debt_to_income", "credit_history", "collateral"]]
y = df["defaulted"]
model = GradientBoostingClassifier(n_estimators=300, random_state=42).fit(X, y)
```

## Tuning notes

- Calibrate predicted probabilities so they reflect true likelihoods.
- Use time-based splits and out-of-time validation to avoid leakage.
- Separate model development from model-risk governance roles.
- Monitor for distribution shift and adversarial behavior in production.

## Verification

1. Build a default model and report AUC-ROC and calibration curves.
2. Run a stress scenario and quantify tail losses vs a baseline.
3. Deploy a drift monitor and simulate a regime shift.

## References

- https://doi.org/10.48550/arxiv.2502.06656
- https://pmc.ncbi.nlm.nih.gov/articles/PMC12032382/
- https://www.msci.com/downloads/web/msci-com/research-and-insights/paper/ai-portfolio-insights-and-the-future-of-risk-management/AI-Portfolio-Insights-and-the-Future-of-Risk-Management.pdf
- https://arxiv.org/html/2310.17721
