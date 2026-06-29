---
name: tdd-workflow
description: >-
  Test-driven development workflow: write failing test, implement minimum code
  to pass, refactor. Use when the user wants to follow TDD practices or needs
  guidance on structured testing.
---

# TDD Workflow

## The Red-Green-Refactor Cycle
1. RED: Write a failing test that describes the desired behavior
2. GREEN: Write the minimum code to make the test pass
3. REFACTOR: Improve code quality while keeping tests green

## Step-by-Step Process

### 1. Write the Test First
```python
def test_addition():
    assert add(2, 3) == 5
```

### 2. Run and Watch It Fail
```bash
pytest test_math.py -v
# Expected: NameError or AssertionError
```

### 3. Write Minimum Implementation
```python
def add(a, b):
    return a + b
```

### 4. Run and Watch It Pass
```bash
pytest test_math.py -v
# Expected: PASSED
```

### 5. Refactor
- Extract functions, remove duplication, improve naming
- Tests should still pass after refactoring

## Best Practices
- One assertion per test (ideally)
- Test names describe behavior: `test_empty_list_returns_zero`
- Arrange-Act-Assert pattern
- Test edge cases: empty input, None, boundary values
- Use fixtures for setup/teardown

## Common Pitfalls
- Testing implementation instead of behavior
- Too many mocks — test the real integration
- Flaky tests — avoid time-dependent or order-dependent tests
