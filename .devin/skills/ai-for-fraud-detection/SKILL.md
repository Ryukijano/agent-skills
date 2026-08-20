# AI for Fraud Detection

## Description

Transaction fraud, anti-money laundering, anomaly detection, graph-based fraud networks, and concept-drift monitoring.

## When to use

You need to detect fraudulent payments, accounts, claims, or transactions in real time while minimizing false positives.

## Key concepts

- **Supervised fraud classification**: tree ensembles and neural nets on labeled fraud cases.
- **Anomaly detection**: isolation forests, autoencoders, and one-class methods for unknown fraud patterns.
- **Graph-based detection**: GNNs to exploit account, device, and merchant networks.
- **Concept drift and adversaries**: fraud patterns evolve; monitor model performance and adversarial behavior.

## Code pattern

```python
from sklearn.ensemble import IsolationForest
from sklearn.model_selection import train_test_split

X = df.drop("is_fraud", axis=1)
clf = IsolationForest(contamination=0.01, random_state=42)
clf.fit(X)
df["anomaly_score"] = clf.decision_function(X)
```

## Tuning notes

- Fraud data is extremely imbalanced; use stratified sampling, class weights, or cost-sensitive loss.
- Use time-based splits and chronological validation to avoid leakage.
- Combine graph structure with behavioral features for network-based fraud.

## Verification

1. Train a fraud classifier and report precision-recall at the top-decile.
2. Build a graph feature extractor and measure lift over tabular features.
3. Deploy a drift monitor and simulate an adversarial shift.

## References

- https://arxiv.org/html/2307.05633
- https://doi.org/10.3390/app16041931
- https://www.mdpi.com/1911-8074/19/1/14
- https://ar5iv.labs.arxiv.org/html/2411.05815
