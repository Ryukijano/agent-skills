# AI for NLP

## Description

Large language models, text classification, machine translation, question answering, information extraction, and prompt engineering.

## When to use

You are processing, generating, or understanding text for chatbots, search, translation, summarization, or information extraction.

## Key concepts

- **Transformer language models**: BERT, GPT, T5, and LLaMA.
- **Prompting and in-context learning**: zero and few-shot, chain-of-thought, and RAG.
- **Fine-tuning and alignment**: instruction tuning, RLHF, and DPO.
- **Information extraction and semantic parsing**: NER, relation extraction, and parsing.
- **Evaluation and safety**: perplexity, BLEU, ROUGE, toxicity, and bias.

## Code pattern

```python
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-hf")
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-hf")

inputs = tokenizer("Summarize the following:", return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Tuning notes

- Use instruction and chat templates for dialog models.
- Combine retrieval augmentation to reduce hallucination.
- Balance context length, batch size, and learning rate for fine-tuning.
- Evaluate on task-specific benchmarks and human judgments.

## Verification

1. Fine-tune an LLM on a domain QA dataset and measure exact match and F1.
2. Build a RAG pipeline and compare answer accuracy to a pure LLM.
3. Run a prompt-engineering ablation and track performance across prompts.

## References

- https://doi.org/10.48550/arxiv.2405.12819
- https://arxiv.org/abs/2402.06196
- https://arxiv.org/abs/2501.04040
- https://arxiv.org/abs/2503.06072
