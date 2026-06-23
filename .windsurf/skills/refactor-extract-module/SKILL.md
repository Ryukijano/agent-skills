---
name: refactor-extract-module
description: Safely extract a module or function from a monolithic file into its own module. Use when refactoring large files, reducing code coupling, or improving project structure.
---

## Refactor: Extract Module

1. Identify code to extract and its dependencies
2. Create new module file
3. Move code + add necessary imports + add docstring
4. Replace original code with import from new module
5. Run tests: `pytest tests/ -v -k "<relevant>"`
6. Write minimal test if none exist
7. Check for circular imports
8. Run linter on both files
9. Commit: `git commit -m "refactor: extract <name> into <module>"`
