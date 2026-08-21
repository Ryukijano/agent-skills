# AI for Cognitive Science

## Description

Use AI to build or evaluate computational models of human cognition, compare AI behavior to human data, or use AI as a model organism for cognitive theory.

## When to use

You want to build or evaluate computational models of human cognition, compare AI behavior to human data, or use AI as a model organism for cognitive theory.

## Usage

- Build computational models of perception, memory, or reasoning.
- Compare AI behavior to human data.
- Probe LLM next-token predictions against human cloze.
- Evaluate symbolic vs. subsymbolic representations.

## Steps

1. Build computational models of perception, memory, or reasoning.
2. Compare AI behavior to human data.
3. Probe LLM next-token predictions against human cloze.
4. Evaluate symbolic vs. subsymbolic representations.
5. Validate with reaction time and error-pattern metrics.
6. Validate on local devices, clinical measurements, and diverse populations before embedding into EHR or public-health workflows (ChatEHR-style).

## Code pattern

```python
import torch
from transformers import AutoModel, AutoTokenizer

# Compare LLM next-token probabilities to human cloze responses
tokenizer = AutoTokenizer.from_pretrained("openai-community/gpt2")
model = AutoModel.from_pretrained("openai-community/gpt2", output_hidden_states=True)
inputs = tokenizer("The cat sat on the ___", return_tensors="pt")
outputs = model(**inputs)
```

## Tuning notes

- Match training scale and stimuli to human experience for valid comparisons.
- Use likelihood, reaction time, and error-pattern metrics, not just accuracy.
- Distinguish performance from competence and test out-of-distribution generalization.
- Combine top-down theory with bottom-up model fits.

## Verification

1. Fit a cognitive model to a choice-reaction-time dataset and recover parameters.
2. Compare LLM and human predictions on a semantic reasoning task.
3. Probe a neural network for symbolic compositionality and report failure modes.

## References

- https://doi.org/10.1146/annurev-psych-030625-040748
- https://www.nature.com/articles/s41593-018-0210-5
- https://doi.org/10.15212/bioi-2025-0199
- https://www.cambridge.org/core/books/cambridge-handbook-of-computational-cognitive-sciences/2713AC0C8AC0B0F2B9E97DB010813883
