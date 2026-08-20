# AI for Poetry

## Description

Meter, rhyme, and stylistic constraints for AI-generated poetry, with evaluation and human-AI curation.

## When to use

You want to generate or co-write poems under formal constraints such as meter, rhyme, syllable counts, or a specific literary style.

## Key concepts

- **Formal constraints**: meter, rhyme scheme, syllable counts, stanza forms, and refrain patterns.
- **Poetic style prompting**: persona, era, mood, imagery, alliteration, and lexical register.
- **Controllable generation**: constrained decoding, iterative refinement, and rule-based post-processing for rhyme and meter.
- **Evaluation**: automatic metrics, LLM-as-judge, and human evaluation for novelty, emotion, and aesthetic quality.
- **Ethics and attribution**: respect public-domain or licensed training data and credit human curators.

## Code pattern

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "gpt2"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

prompt = """Write a Shakespearean sonnet about autumn.
Use iambic pentameter and an ABAB CDCD EFEF GG rhyme scheme:

"""

inputs = tokenizer(prompt, return_tensors="pt")
output = model.generate(
    **inputs,
    max_new_tokens=200,
    temperature=0.9,
    do_sample=True,
)
poem = tokenizer.decode(output[0], skip_special_tokens=True)
print(poem)
```

## Tuning notes

- Use constrained decoding or post-hoc rhyme checking to satisfy form.
- Fine-tune on poetry corpora for stronger stylistic control.
- Balance novelty with readability; avoid cliches.
- Validate meter and rhyme with dedicated tools such as `pronouncingpy` or `pyphen`.

## Verification

1. Generate 10 sonnets and check rhyme and meter compliance automatically.
2. Compare human vs. AI poems in a small blinded preference test.
3. Evaluate diversity and novelty across a themed set of poems.

## References

- https://doi.org/10.1613/jair.1.20584
- https://aclanthology.org/W17-3502/
- https://aclanthology.org/2024.emnlp-main.1097/
- https://computationalcreativity.net/iccc24/papers/ICCC24_paper_164.pdf
