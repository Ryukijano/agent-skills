# AI for Software Engineering

## Description

Use AI to generate, review, and test code across the software lifecycle.

## When to use

You are building, maintaining, or reviewing software and want to use AI to generate, test, debug, or document code.

## Usage

- Complete and refactor code with GitHub Copilot or Cody.
- Run static analysis with SonarQube and ESLint.
- Generate unit tests and property-based checks.
- Predict bug-prone files and triage CI failures.
- Summarize code and documentation with LLMs.

## Steps

1. Index repositories and set up code-quality baselines.
2. Fine-tune or prompt LLMs on internal style and APIs.
3. Automate generation, review, and test coverage checks in CI.
4. Track bug-proneness and build-failure trends.
5. Measure impact on cycle time and defect escape rate.

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
