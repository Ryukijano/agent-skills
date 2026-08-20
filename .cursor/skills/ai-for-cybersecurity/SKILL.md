# AI for Cybersecurity

## Description

Network intrusion detection, malware and phishing classification, vulnerability discovery, adversarial ML, and SOC automation.

## When to use

You are defending networks, endpoints, or cloud environments against
intrusions, malware, phishing, or adversarial ML attacks.

## Key concepts

- **AI-driven intrusion detection**: anomaly and signature detection on
  network and host telemetry.
- **Malware and phishing classification**: static/dynamic analysis and
  URL or email content models.
- **Vulnerability discovery**: ML-assisted fuzzing, static analysis, and
  patch prioritization.
- **Adversarial ML**: evasion, poisoning, model extraction, and
  hardening defenses.
- **SOC automation**: triage, correlation, and response playbooks with
  LLM agents.

## Code pattern

```python
from sklearn.ensemble import IsolationForest

# Anomaly detector on network-flow features
model = IsolationForest(contamination=0.01, random_state=42)
model.fit(X_train)
scores = model.decision_function(X_test)
```

## Tuning notes

- Use chronological train/test splits to prevent label leakage in logs.
- Balance extreme class imbalance with cost-sensitive learning.
- Validate against adversarial evasion on a holdout attack set.
- Combine rule-based and ML detectors for auditable alerts.

## Verification

1. Train a network-IDS model and report precision-recall at the top 1%.
2. Build a phishing URL classifier and evaluate on a time-separated test.
3. Run an adversarial-evasion test against a trained malware detector.

## References

- https://www.mdpi.com/1424-8220/26/5/1518
- https://arxiv.org/abs/2405.04760
- https://arxiv.org/abs/2601.05293
- https://attack.mitre.org/
