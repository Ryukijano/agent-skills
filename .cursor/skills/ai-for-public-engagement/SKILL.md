# AI for Public Engagement

## Description

Use conversational AI and citizen-science chatbots to make public consultations, science festivals and participatory research more inclusive and scalable.

## When to use

You are running public consultations, citizen-science projects, science-festival chatbots, or community outreach and want to make engagement more inclusive and scalable.

## Usage

- **Collect, analyze, and respond to public questions, concerns, and ideas.**
- **Deploy chatbots and voice agents that answer science questions and guide participation.**
- **Onboard volunteers, validate submissions, and provide real-time feedback in citizen-science projects.**
- **Support community voice and agency without replacing human decision-making.**
- **Disclose AI involvement, support multilingual interactions, and protect privacy.**

## Steps

1. Co-design engagement goals, prompts, and fallback rules with community stakeholders.
2. Build a retrieval-augmented chatbot grounded in vetted FAQs, papers, and institutional sources.
3. Deploy the agent on accessible channels (web, SMS, voice, event kiosks) in relevant languages.
4. Collect questions and feedback, then extract themes using topic modeling or LLM summarization.
5. Validate chatbot answers against sources and monitor for bias, misinformation, and escalation needs.
6. Iterate with participants and report how input influenced research or policy outcomes.

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
- https://theoryandpractice.citizenscienceassociation.org/articles/10.5334/cstp.812
