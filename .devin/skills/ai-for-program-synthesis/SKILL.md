# AI for Program Synthesis

## Description

Generate executable programs from natural-language descriptions or input-output examples for non-expert users and new APIs.

## When to use

You want to generate programs from examples, partial sketches, or natural language, or combine symbolic search with neural models for reliable code generation.

## Usage

- Synthesize programs consistent with input-output examples using programming by example (PBE).
- Generate code from natural-language specifications or partial sketches with transformer models.
- Combine symbolic search, constraint solving, and neural priors for reliable synthesis.
- Fill holes in user-provided program templates while satisfying types and constraints.

## Steps

1. Collect input-output examples, sketches, or natural-language specifications for the target program.
2. Choose a synthesis approach: enumerative search, constraint solving, LLM generation, or neurosymbolic search.
3. Train or prompt the model with few-shot examples and constrain output with a grammar or type system.
4. Filter candidates by executing tests and, where possible, verifying them with a symbolic checker.
5. Measure pass@k and compare the synthesizer to a human-written or symbolic baseline.
6. Integrate the synthesis loop into an IDE, API, or code-generation assistant.

## Code pattern

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("codellama/CodeLlama-7b-hf")
tokenizer = AutoTokenizer.from_pretrained("codellama/CodeLlama-7b-hf")

prompt = "# Python function that returns the sum of even numbers in a list\ndef sum_evens(lst):\n    "
inputs = tokenizer(prompt, return_tensors="pt")
outputs = model.generate(**inputs, max_new_tokens=64)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

## Tuning notes

- Constrain generation with a grammar or type system to improve correctness.
- Filter candidates with test-case execution and a symbolic verifier.
- Use few-shot examples that match the target domain and style.

## Verification

1. Synthesize a program from a small set of input-output examples and run it on hidden tests.
2. Compare a neural synthesizer against an enumerative synthesizer on the same benchmark.
3. Measure pass@k on a program-synthesis dataset (e.g., HumanEval, APPS, SyGuS).

## References

- https://www.cs.utexas.edu/~swarat/pubs/ns-handbook-2025.pdf
- https://doi.org/10.1117/12.3011627
- https://www.mdpi.com/2078-2489/16/5/401
- https://doi.org/10.1007/978-3-642-11931-6_3
- https://www.mdpi.com/2076-3417/15/22/12150
