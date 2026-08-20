# Advanced Prompt Engineering

## Description

Structured prompting, few-shot, chain-of-thought, role prompts, and prompt optimization for LLMs.

## When to use

You want to get more reliable, structured, or correct output from an LLM without fine-tuning.

## Key concepts

- **Few-shot prompting**: provide input-output examples in the context.
- **Role and style prompts**: frame the model as an expert in a domain.
- **Structured output**: request JSON, XML, or YAML with schemas.
- **Prompt templates**: separate instruction, examples, and user input.
- **Automatic prompt optimization**: e.g., DSPy, APE, OPRO.

## Code pattern

```python
prompt = f"""You are an expert Python reviewer. Given the code, output JSON with fields 'issues' and 'score'.

Code:
{code}

Output JSON only.
"""
```

## Tuning notes

- Use clear delimiters to separate instructions, examples, and input.
- Iterate with a small held-out set rather than one-off tuning.
- Optimize for the specific model and API; prompts may not transfer perfectly.

## Verification

1. Design a few-shot prompt for a classification task and measure F1.
2. Compare role prompts vs neutral prompts on a reasoning task.
3. Generate JSON outputs and validate schema compliance.

## References

- https://arxiv.org/abs/2307.11760
- https://arxiv.org/abs/2312.16171
- https://dspy-docs.vercel.app/
- https://github.com/keirp/automatic_prompt_engineer
