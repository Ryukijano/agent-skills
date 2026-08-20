# AI for Surveillance Ethics

## Description

Fairness, privacy, proportionality, and algorithmic accountability for AI surveillance and facial recognition.

## When to use

You are designing, deploying, or auditing surveillance or biometric
systems where privacy, human rights, and societal trust are at stake.

## Key concepts

- **Proportionality and necessity**: balancing security gains against
  individual rights and freedoms.
- **Algorithmic fairness**: auditing demographic disparities in
  detection and recognition rates.
- **Privacy by design**: data minimization, retention limits, and
  anonymization.
- **Transparency and accountability**: explainability, audit trails,
  and redress mechanisms.
- **Regulatory compliance**: AI Act, biometric data rules, and sector
  guidelines.

## Code pattern

```python
from sklearn.metrics import classification_report

# Audit subgroup performance for a recognition or detection model
print(classification_report(y_true, y_pred, target_names=groups))
```

## Tuning notes

- Conduct independent audits before and after deployment.
- Document the purpose, data sources, and decision logic for oversight.
- Implement human-in-the-loop review for high-stakes identifications.
- Apply the least intrusive means to achieve a legitimate security goal.

## Verification

1. Audit a facial-recognition model for equalized odds across groups.
2. Write a proportionality assessment for a proposed surveillance use.
3. Verify that audit logs and deletion policies meet the stated policy.

## References

- https://arxiv.org/html/2402.05731
- https://dl.acm.org/doi/10.1145/3375627.3375820
- https://arxiv.org/html/2503.04866v1
- https://arxiv.org/html/2606.07628v1
- https://www.frontiersin.org/articles/10.3389/fdata.2024.1337465
