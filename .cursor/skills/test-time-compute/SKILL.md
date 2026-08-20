# Test-Time Compute Scaling

## Description

Improve LLM output quality by increasing inference-time computation: search, verification, and reward models.

## When to use

You want better answers from a fixed model by allowing it to think longer or verify candidates at inference.

## Key concepts

- **Compute-optimal inference**: allocate inference compute to maximize pass@k.
- **Process reward models (PRM)**: score each reasoning step.
- **Outcome reward models (ORM)**: score the final answer.
- **Monte Carlo tree search / beam search** over reasoning paths.
- **Verifier ensembles**: multiple verifiers judge a candidate answer.

## Code pattern

```python
def best_of_n(prompt, n=8):
    candidates = [model.generate(prompt) for _ in range(n)]
    scores = [verifier(c) for c in candidates]
    return candidates[argmax(scores)]
```

## Tuning notes

- More samples helps most on hard reasoning tasks with reliable verifiers.
- A weak verifier can hurt performance; calibrate on a dev set.
- Balance sampling budget against latency and cost.

## Verification

1. Implement best-of-N sampling on a math word-problem set.
2. Train or use a small verifier and compare RM selection to majority vote.
3. Plot pass@k and compute-optimal pass rate versus N.

## References

- https://arxiv.org/abs/2408.03314
- https://arxiv.org/abs/2409.01903
- https://openai.com/index/learning-to-reason-with-llms/
- https://arxiv.org/abs/2402.06178
