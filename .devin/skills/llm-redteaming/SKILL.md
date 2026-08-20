# LLM Red Teaming and Safety

## Description

Systematically probe LLMs for harmful outputs, jailbreaks, privacy leaks, and misalignment.

## When to use

You are deploying or fine-tuning an LLM and need to find and mitigate failure modes before release.

## Key concepts

- **Red teaming**: adversarial probing to elicit undesirable behavior.
- **Jailbreaks and prompt injection**: user-level attacks that bypass safety filters.
- **Privacy extraction**: training data or secrets leakage.
- **Safety evals**: toxicity, bias, harmful instructions, misinformation.

## Code pattern

```python
# Probe with a set of adversarial prompts
for prompt in adversarial_prompts:
    response = model.generate(prompt)
    flagged = safety_classifier(response)
    print(prompt, flagged, response[:200])
```

## Tuning notes

- Combine automated probes with human review.
- Use a broad taxonomy of harms, not just a single safety metric.
- Retest after mitigation to ensure over-refusal does not spike.

## Verification

1. Run a small jailbreak probe set and record success rate.
2. Test a classifier on a balanced harmful/harmless test set.
3. Document a failure mode and a mitigating guardrail.

## References

- https://arxiv.org/abs/2402.09300
- https://www.anthropic.com/news/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned
- https://arxiv.org/abs/2312.07401
- https://github.com/llm-attacks/llm-attacks
