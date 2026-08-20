# Code Simplification

## Five Principles
1. Preserve Behavior Exactly (tests pass before/after)
2. Follow Project Conventions
3. Prefer Clarity Over Cleverness
4. Maintain Balance
5. Scope to What Changed

## Process
1. **Understand Before Touching** (Chesterton's Fence): don't remove what you don't understand
2. **Identify Opportunities**: duplication, deep nesting, long functions, complex conditionals
3. **Apply Incrementally**: one change at a time, test after each
4. **Verify**: tests pass, behavior unchanged, more readable

## Language Tips
- Python: comprehensions, dataclasses, pathlib, early returns
- JS/TS: optional chaining, destructuring
- React: extract components, hooks properly
