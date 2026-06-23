---
description: Safely extract a module or function from a monolithic file into its own module
---

## Refactor: Extract Module

1. Identify the code to extract. Read the source file and note:
   - The function/class to extract
   - Its dependencies (imports, other functions it calls)
   - What depends on it (callers)

2. Create the new module file:
   ```bash
   touch core_app/<module_name>.py
   ```

3. Move the code to the new module:
   - Copy the function/class to the new file
   - Add all necessary imports to the new file
   - Add a docstring explaining the module's purpose

4. In the original file, replace the code with an import:
   ```python
   from core_app.<module_name> import <ExtractedClass>
   ```

5. Run existing tests to verify nothing broke:
   ```bash
   pytest tests/ -v -k "<relevant_test>"
   ```

6. If no tests exist, write a minimal test for the extracted module:
   ```python
   # tests/test_<module_name>.py
   def test_import():
       from core_app.<module_name> import <ExtractedClass>
       assert <ExtractedClass> is not None
   ```

7. Check for circular imports:
   ```bash
   python -c "from core_app.<module_name> import <ExtractedClass>; print('OK')"
   python -c "from core_app.<original_module> import <OriginalClass>; print('OK')"
   ```

8. Run linter on both files:
   ```bash
   ruff check core_app/<module_name>.py core_app/<original_module>.py
   ```

9. Commit with descriptive message:
   ```bash
   git add -A
   git commit -m "refactor: extract <name> into core_app/<module_name>.py"
   ```

10. Summarize: what was extracted, why, and any import changes needed by downstream code.
