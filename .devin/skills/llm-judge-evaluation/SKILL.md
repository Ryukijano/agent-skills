# LLM-as-a-Judge Evaluation

## Description

Use strong language models to evaluate, score, and compare outputs from other models or pipelines.

## When to use

You need an automated, flexible evaluation metric for open-ended generation, chat, or instruction following.

## Key concepts

- **LLM-as-a-judge**: a capable model scores outputs against a rubric.
- **Pairwise vs pointwise**: compare two outputs or score one output.
- **Position bias**: the judge may prefer the first or last candidate.
- **Reference-free vs reference-based**: with or without a gold answer.

## Code pattern

```python
import openai

def judge(prediction, reference=None):
    prompt = f"Rate the following answer 1-5 for correctness and clarity.\n\nAnswer: {prediction}"
    if reference:
        prompt += f"\n\nReference: {reference}"
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

## Tuning notes

- Provide detailed rubrics and few-shot examples to reduce variance.
- Swap candidate order to detect and average out position bias.
- Calibrate judge scores with human annotations.

## Verification

1. Build a judge prompt for a summarization task.
2. Evaluate 20 model outputs and correlate with human ratings.
3. Measure inter-rater agreement between judge and human scores.

## References

- https://arxiv.org/abs/2306.05685
- https://arxiv.org/abs/2407.00449
- https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge
- https://huggingface.co/spaces/lm-sys/mt-bench
