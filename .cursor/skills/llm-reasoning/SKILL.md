# LLM Reasoning and Chain-of-Thought

## Description

Chain-of-thought, self-consistency, tree-of-thoughts, and reasoning-optimized prompting for large language models.

## When to use

You want to improve a language model's performance on multi-step math, logic, code, or planning problems.

## Key concepts

- **Chain-of-thought (CoT)**: prompt the model to emit intermediate reasoning steps.
- **Self-consistency**: sample multiple CoT answers and vote on the final result.
- **Tree-of-thoughts (ToT)**: search over partial reasoning chains and backtrack.
- **Zero-shot CoT**: append "Let's think step by step" or similar to elicit reasoning.
- **Reasoning models**: scaling test-time compute and process-supervised reward models.

## Code pattern

```python
import openai

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Solve: if 3x+2=14, what is x? Let's think step by step."}
    ]
)
print(response.choices[0].message.content)
```

## Tuning notes

- CoT helps most when the task requires explicit intermediate steps.
- Self-consistency increases accuracy at the cost of extra sampling.
- ToT is powerful but requires a way to evaluate partial solutions and a search budget.

## Verification

1. Solve a small arithmetic dataset with and without CoT.
2. Run self-consistency with 5 samples and compare majority vote to greedy decode.
3. Implement a two-step ToT search and verify it finds a better answer on a planning puzzle.

## References

- https://arxiv.org/abs/2201.11903
- https://arxiv.org/abs/2203.11171
- https://arxiv.org/abs/2305.10601
- https://openai.com/index/learning-to-reason-with-llms/
