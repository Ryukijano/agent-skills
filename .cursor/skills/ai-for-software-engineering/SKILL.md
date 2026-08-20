# AI for Software Engineering

## Description

AI for code generation, testing, debugging, program repair, code review, and design assistance.

## When to use

You are building, maintaining, or reviewing software and want to use AI to generate, test, debug, or document code.

## Usage

- **Code generation and completion**: large language models and code-specific foundation models.
- **Automated testing and fuzzing**: generating test cases and oracles.
- **Bug detection and program repair**: static analysis, code review, and patch generation.
- **Requirements and design**: natural-language-to-code, architecture suggestion.
- **Software verification and security**: formal methods, vulnerability detection.

## Steps

1. Collect code repositories, issue trackers, test suites, and documentation.
2. Preprocess and chunk code, add retrieval context, and build prompts.
3. Fine-tune or prompt a code model for generation, test, or repair tasks.
4. Validate generated outputs with compilers, linters, and CI tests.
5. Iterate with developer feedback and versioned benchmarks.

## Code pattern

```python
from transformers import pipeline

# Generate code from a docstring
generator = pipeline("text-generation", model="codellama/CodeLlama-7b-hf")
output = generator("def is_palindrome(s: str) -> bool:")
```

## Tuning notes

- Use retrieval and RAG for large, proprietary codebases.
- Validate generated code with compilers, linters, and test suites.
- Watch for hallucinated APIs, license issues, and security vulnerabilities.

## Verification

1. Generate tests for a set of functions and measure line/branch coverage.
2. Run a bug-localization model and compare to issue labels.
3. Review generated patches in a real pull request setting.

## References

- https://link.springer.com/article/10.1007/s11432-025-4670-0
- https://link.springer.com/article/10.1007/s11432-025-4632-8
- https://www.frontiersin.org/journals/computer-science/articles/10.3389/fcomp.2025.1655469/full
- https://proceedings.mlr.press/v267/lu25f.html
