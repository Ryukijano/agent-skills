# Iterative Test Loop

Run change → test → diagnose → refine until green.

Apply skill: `iterative-test-loop`.

1. Make one focused edit aligned to the current hypothesis.
2. Run the narrowest test command that proves the change.
3. On failure: read full error, fix root cause, retry.
4. Exit only when tests pass and the user goal is satisfied.

For MOT projects: `pytest tests/test_mot_smoke.py -q` as minimum gate.
