# AI for Finance

## Description

Machine learning for time-series forecasting, risk modeling, algorithmic trading, and financial NLP.

## When to use

You are building predictive models for markets, credit, fraud, or financial documents.

## Key concepts

- **Time-series forecasting**: ARIMA, Prophet, deep state-space, transformers.
- **Risk modeling**: Value-at-Risk, stress testing, default prediction.
- **Fraud detection**: anomaly detection, imbalanced classification.
- **Financial NLP**: sentiment, earnings calls, filings, FinBERT.
- **Backtesting**: avoid lookahead bias and overfitting.

## Code pattern

```python
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Example: classify next-day direction from features
X, y = load_features_and_labels()
model = RandomForestClassifier(n_estimators=200, class_weight="balanced")
model.fit(X_train, y_train)
```

## Tuning notes

- Avoid data leakage: do not train on future information.
- Use proper temporal cross-validation.
- Transaction costs and slippage can erase paper profits.

## Verification

1. Build a time-series forecast and evaluate with temporal CV.
2. Run a backtest with realistic costs and report Sharpe ratio.
3. Classify financial news sentiment and compare to a baseline.

## References

- https://arxiv.org/abs/2402.03740
- https://github.com/yixuanqiao/FinRobot
- https://huggingface.co/ProsusAI/finbert
- https://pyfolio-reloaded.readthedocs.io/
