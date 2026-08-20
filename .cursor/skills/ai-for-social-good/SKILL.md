# AI for Social Good

## Description

Education, poverty alleviation, agriculture, humanitarian response, accessibility, and community-driven AI for underserved populations.

## When to use

You are deploying AI to improve outcomes in education, health, agriculture, humanitarian aid, or economic inclusion, especially in low-resource or marginalized communities.

## Key concepts

- **Education and personalized tutoring**: adaptive learning, chat-based tutoring, and low-bandwidth delivery.
- **Poverty and development economics**: rigorous impact evaluation, cost-effectiveness, and scalable social programs.
- **Agriculture and food security**: crop-health monitoring, yield prediction, and extension services for smallholder farmers.
- **Humanitarian and crisis response**: information triage, needs assessment, and resource matching.
- **Participatory design and ethics**: co-design with communities, local language support, and harm prevention.

## Code pattern

```python
from transformers import pipeline

qa = pipeline(
    "question-answering",
    model="distilbert-base-uncased-distilled-squad"
)
answer = qa(question="What is crop rotation?", context=extension_text)
```

## Tuning notes

- Prioritize low-cost, low-bandwidth, and offline-capable deployments for last-mile users.
- Conduct randomized evaluations or quasi-experimental impact analysis when possible.
- Guard against paternalism and unintended consequences; center affected communities in design.

## Verification

1. Run a small RCT or A/B test of an AI tutoring or information tool and measure learning or adoption outcomes.
2. Build a farmer-facing crop-advisory prototype and validate recommendations with local experts.
3. Assess cost-effectiveness and equity impacts relative to non-AI alternatives.

## References

- https://www.povertyactionlab.org/sites/default/files/review-paper/J-PAL_AI_Evidence_Playbook_02.16.2026.pdf
- https://arxiv.org/pdf/2402.09809
- https://solve.mit.edu/solutions/21651
- https://documents1.worldbank.org/curated/en/099548105192529324/pdf/IDU-c09f40d8-9ff8-42dc-b315-591157499be7.pdf
- https://news.mit.edu/2026/new-j-pal-research-policy-initiative-to-test-scale-ai-innovations-fight-poverty-0212
