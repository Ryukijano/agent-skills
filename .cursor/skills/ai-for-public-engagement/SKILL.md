# AI for Public Engagement

## Description

Conversational agents, citizen science, public consultations, and participatory science supported by LLMs and interactive AI.

## When to use

You are running public consultations, citizen-science projects, science-festival chatbots, or community outreach and want to make engagement more inclusive and scalable.

## Key concepts

- **Bidirectional science communication**: collect, analyze, and respond to public questions and concerns.
- **Conversational AI**: chatbots and voice agents that answer science questions and guide participation.
- **Citizen science and data quality**: LLMs help onboard volunteers, validate submissions, and provide feedback.
- **Deliberative and participatory design**: AI can support but not replace community voice and agency.
- **Transparency and accessibility**: disclose AI involvement, support multiple languages, and protect privacy.

## Code pattern

```python
from collections import Counter

# Example: simple theme extraction from public consultation comments
def extract_theme(comment):
    # In practice, use an NER or topic model
    return comment.split(":")[0]

themes = [extract_theme(c) for c in comments]
print(Counter(themes).most_common(10))
```

## Tuning notes

- Co-design prompts with community stakeholders, not just technical staff.
- Use retrieval-augmented generation to ground chatbot answers in vetted FAQs and sources.
- Monitor for bias, misinformation, and over-reliance on AI in sensitive discussions.
- Ensure data ownership and consent, especially for youth and marginalized groups.

## Verification

1. Deploy a chatbot at a public event and log question types, answer accuracy, and escalation rates.
2. Analyze a corpus of consultation comments and compare AI-extracted themes to human coding.
3. Measure changes in volunteer retention and data quality when adding an LLM onboarding assistant.

## References

- https://doi.org/10.1057/s41599-026-06594-5
- https://publichealth.jmir.org/2025/1/e65699
- https://doi.org/10.1038/s41893-024-01489-2
- https://doi.org/10.5334/cstp.812
