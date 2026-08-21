# AI for Risk Management

## Description

Use AI to quantify credit, market, operational, or emerging risks; building early-warning systems; or stress-testing portfolios and operations.

## When to use

You are quantifying credit, market, operational, or emerging risks; building early-warning systems; or stress-testing portfolios and operations.

## Usage

- Calibrate probability and loss models.
- Detect anomalies and tail risks.
- Run stress and scenario tests.
- Separate model development and governance.

## Steps

1. Calibrate probability and loss models.
2. Detect anomalies and tail risks.
3. Run stress and scenario tests.
4. Separate model development and governance.
5. Monitor for distribution shift and adversarial behavior.
6. Deploy in client engagements, capture requirements from discovery calls, and measure time-to-insight and decision quality (Task-GenAI Fit-style).

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
- https://arxiv.org/abs/2310.17721
