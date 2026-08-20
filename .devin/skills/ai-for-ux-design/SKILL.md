# AI for UX Design

## Description

Interaction design, user research, prototyping, and AI UX patterns for human-centered AI products.

## When to use

You are designing AI-powered products, chatbots, agent interfaces, recommendation surfaces, or generative tools where user trust and control are critical.

## Key concepts

- **Human-centered AI UX**: user needs, mental models, and trust calibration.
- **AI UX patterns**: contextual assistance, progressive disclosure, explainability, and graceful failure.
- **Conversational and agent interfaces**: turn-taking, intent, escalation, and feedback.
- **UX research with AI**: synthesis of interviews, usability testing, and analytics.
- **Accessibility and ethics**: inclusive design, privacy, safety, and transparency.

## Code pattern

```python
import gradio as gr

# A simple chat UI with user feedback

def chat(message, history):
    response = model.respond(message, history)
    return response

demo = gr.ChatInterface(chat)
demo.launch()
```

## Tuning notes

- Set clear expectations for AI capabilities and confidence.
- Provide easy correction, undo, and escalation paths.
- Show why the AI made a recommendation when feasible.
- Test with diverse users under realistic failure conditions.

## Verification

1. Prototype an AI feature in a low-fidelity clickable mock.
2. Run a usability test with 5 users and measure task success.
3. Evaluate trust and comprehension with a post-task survey.

## References

- https://www.aiuxdesign.guide/patterns
- https://ai-interaction.com/
- https://doi.org/10.1561/1100000106
- https://web.dev/learn/ai/ux-patterns
