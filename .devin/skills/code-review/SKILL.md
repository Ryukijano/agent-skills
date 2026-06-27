---
name: code-review
description: Perform systematic ML-focused code review checking correctness, performance, safety, and style. Use when reviewing PRs, auditing code quality, or preparing code for release.
---

## Code Review Checklist

### Correctness
- [ ] No off-by-one errors in indexing
- [ ] Tensor shapes match between operations
- [ ] Loss functions handle edge cases (empty targets, NaN)
- [ ] Optimizer is stepping (not just computing gradients)
- [ ] EMA/teacher updates inside `torch.no_grad()`

### Performance
- [ ] No CPU-GPU syncs (`.item()`, `.cpu()`, print in loop)
- [ ] DataLoader uses `num_workers > 0`, `pin_memory=True`
- [ ] No memory leaks (tensors not detached in logging)
- [ ] Mixed precision used where appropriate

### Safety
- [ ] No hardcoded paths
- [ ] No API keys in code
- [ ] Gradient clipping enabled
- [ ] Checkpoint includes optimizer state

### Style
- [ ] No debug prints
- [ ] Type hints on public functions
- [ ] Config params have defaults
- [ ] No commented-out code
