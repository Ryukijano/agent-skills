# AI for Fraud Detection

## Description

Use AI for Fraud Detection to detect transaction fraud, money laundering and graph-based fraud rings.

## When to use

You need to detect fraudulent payments, accounts, claims, or transactions in real time while minimizing false positives.


## Usage


- **Supervised fraud classification**: Tree ensembles and neural nets on labeled fraud cases.
- **Anomaly detection**: Isolation forests, autoencoders, and one-class methods for unknown fraud patterns.
- **Graph-based detection**: GNNs to exploit account, device, and merchant networks.
- **Concept drift and adversaries**: Fraud patterns evolve; monitor model performance and adversarial behavior.

## Steps

1. Collect and prepare transaction, account, device and merchant data.
2. Detect fraudulent payments.
3. Accounts.
4. Claims.
5. Validate by training a fraud classifier and report precision-recall at the top-decile.
6. Deploy into the target workflow and monitor performance, drift, and outcomes.

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

- https://arxiv.org/abs/2307.05633
- https://doi.org/10.3390/app16041931
- https://www.mdpi.com/1911-8074/19/1/14
- https://arxiv.org/abs/2411.05815
