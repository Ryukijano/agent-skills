# AI for Social Services

## Description

Matches clients to benefits and services by triaging eligibility, risk, and available community resources.

## When to use

You are supporting social service delivery, eligibility determination, case prioritization, or benefit navigation.

## Usage

- **Eligibility pre-screening**: triage applicants for benefits and services.
- **Case prioritization**: rank cases by risk, urgency, and complexity.
- **Resource matching**: connect clients to housing, food, health, and employment programs.
- **Caseworker support**: summarize case notes, suggest next steps, and check policy.

## Steps

1. Map programs, eligibility rules, and referral pathways.
2. Collect client, program, and service data with consent and data minimization.
3. Build rule-based and ML triage models with explainable outputs.
4. Provide human review for high-stakes benefit and placement decisions.
5. Track outcomes, wait times, and access disparities across groups.

## Code pattern

```python
from sklearn.ensemble import GradientBoostingClassifier

# Risk triage for case prioritization
X = df[["age", "household_size", "income", "prior_interactions"]]
y = df["high_need"]
model = GradientBoostingClassifier(random_state=42).fit(X, y)
df["risk_score"] = model.predict_proba(X)[:, 1]
```

## Tuning notes

- Prioritize equity, consent, and data minimization.
- Keep humans in the loop for benefit and placement decisions.
- Monitor for disparate impact on protected groups.

## Verification

1. Compare triage model outcomes to expert social-worker rankings.
2. Build an eligibility screener and test against known cases.
3. Measure reduction in time-to-service and access gaps.

## References

- https://sage.cnpereading.com/doi/10.1177/10497315251350933
- https://www.mathematica.org/publications/navigating-genai-in-child-welfare-quick-start-guide-for-agency-leaders
- https://digitalgovernmenthub.org/publications/ai-powered-rules-as-code-experiments-with-public-benefits-policy/
- https://doi.org/10.1145/3491102.3517439
