# AI for UX Design

## Description

Use AI to design interaction patterns, prototype AI features, synthesize user research, and build human-centered AI experiences.

## When to use

You are designing AI-powered products, chatbots, agent interfaces, recommendation surfaces, or generative tools where user trust and control are critical.

## Usage

- Prototype chat, agent, and recommendation interfaces with user control.
- Synthesize user interviews, usability tests, and analytics.
- Apply AI UX patterns such as explainability, progressive disclosure, and graceful failure.
- Test trust, comprehension, and accessibility with diverse users.

## Steps

1. Define the user task, mental model, and trust expectations.
2. Create low-fidelity wireframes and a clickable prototype.
3. Design feedback, correction, and escalation paths into the UI.
4. Run a usability test with 5+ users and measure task success.
5. Iterate on trust, comprehension, and failure handling based on results.

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
