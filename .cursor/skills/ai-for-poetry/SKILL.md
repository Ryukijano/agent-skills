# AI for Poetry

## Description

Co-write poems under meter, rhyme, and style constraints with interactive language models that suggest lines and refine form.

## When to use

You want to generate or co-write poems under formal constraints such as meter, rhyme, syllable counts, or a specific literary style.

## Usage

- Generate poems under meter, rhyme scheme, syllable count, and stanza constraints.
- Emulate a specific poet, era, mood, or lexical register.
- Post-process with rule-based rhyme and meter checking.
- Curate and evaluate poems for novelty, emotion, and aesthetic quality.

## Steps

1. Choose a form (sonnet, haiku, villanelle) and its formal constraints.
2. Prompt the model with persona, mood, imagery, and a target rhyme scheme.
3. Generate multiple drafts and score them for form compliance.
4. Validate meter and rhyme with tools such as pronouncingpy or pyphen.
5. Select and edit the best poems in a blinded human-curation pass.

## Code pattern

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model_name = "openai-community/gpt2"
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
