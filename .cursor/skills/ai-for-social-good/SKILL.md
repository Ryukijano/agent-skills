# AI for Social Good

## Description

Optimize vaccination outreach and agricultural advice for low-resource communities to improve health and livelihood outcomes.

## When to use

You are deploying AI to improve outcomes in education, health, agriculture, humanitarian aid, or economic inclusion, especially in low-resource or marginalized communities.

## Usage

- Deliver personalized, low-bandwidth tutoring and educational support with adaptive learning systems.
- Evaluate impact with randomized or quasi-experimental designs and cost-effectiveness analysis.
- Support smallholder agriculture with crop-health monitoring, yield prediction, and extension chatbots.
- Triage information, assess needs, and match resources in humanitarian and crisis response.

## Steps

1. Engage affected communities and domain partners to define the problem, outcomes, and ethical constraints.
2. Co-design a low-cost, low-bandwidth, and accessible AI solution (chatbot, advisory app, monitoring tool).
3. Collect local data and train or adapt models, ensuring local language and cultural relevance.
4. Run a pilot with an RCT, A/B test, or quasi-experimental design to measure learning, adoption, or welfare outcomes.
5. Assess cost-effectiveness, equity, and unintended consequences compared to non-AI alternatives.
6. Iterate with community feedback, scale responsibly, and monitor for harm and drift.

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
