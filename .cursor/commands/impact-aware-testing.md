# Impact-Aware Testing

Find and run tests related to changed source files.

Apply skill: `impact-aware-testing`.

1. `git diff --name-only` for changed files.
2. Map imports and module names to test paths.
3. Run the narrowest pytest/npm/cargo subset that covers the diff.
4. Report commands run and pass/fail evidence.

MOT default: `pytest tests/test_mot_smoke.py -q` plus any module-specific tests found.
