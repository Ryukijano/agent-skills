# Debugging and Error Recovery

## Stop-the-Line Rule
Stop. Understand before fixing. Fix root cause, not symptom.

## Triage Checklist
1. **Reproduce**: Minimal reproduction case
2. **Localize**: Binary search to find failing component
3. **Reduce**: Strip unrelated code, isolate bug
4. **Fix Root Cause**: Understand WHY, not just WHAT
5. **Guard Recurrence**: Write regression test
6. **Verify End-to-End**: Full test suite + original scenario

## Error-Specific Patterns
- Test Failure: check assertion, run single test -v
- Build Failure: full error output, check deps
- Runtime Error: full stack trace, check inputs/state
