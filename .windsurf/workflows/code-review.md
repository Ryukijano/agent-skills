---
description: Systematic code review checklist for ML research code
---

## Code Review

Perform a systematic review of the changes in the current branch or PR.

1. Get the diff to review:
   ```bash
   git diff main...HEAD --stat
   git diff main...HEAD
   ```

2. Review each file systematically, checking for:

   **Correctness**
   - [ ] No off-by-one errors in indexing
   - [ ] Tensor shapes match between operations (add assertions for critical reshapes)
   - [ ] Loss functions handle edge cases (empty targets, NaN inputs)
   - [ ] Model forward pass produces correct output shapes
   - [ ] Optimizer is stepping (not just computing gradients)
   - [ ] EMA / teacher updates are inside `torch.no_grad()` or `@torch.no_grad()`

   **Performance**
   - [ ] No unnecessary CPU-GPU syncs (`.item()`, `.cpu()`, `print(tensor)`)
   - [ ] DataLoader uses `num_workers > 0`, `pin_memory=True`
   - [ ] No memory leaks (tensors not detached in logging)
   - [ ] Mixed precision used where appropriate

   **Safety**
   - [ ] No hardcoded paths (use config or environment variables)
   - [ ] No API keys or credentials in code
   - [ ] Gradient clipping enabled for training
   - [ ] Checkpoint saving includes optimizer state for resumption
   - [ ] No `os.system()` or shell injection vectors

   **Style**
   - [ ] No debug print statements left in production code
   - [ ] Functions have type hints where practical
   - [ ] Config parameters have defaults and are documented
   - [ ] No commented-out code blocks

3. For each issue found, either:
   - Fix it directly if it's a clear bug
   - Add a comment in the PR if it needs discussion

4. Run tests if they exist:
   ```bash
   python -m pytest tests/ -x -q
   ```

5. Summarize findings as:
   - **Critical bugs** (must fix before merge)
   - **Improvements** (should fix, not blocking)
   - **Suggestions** (nice to have, future work)
