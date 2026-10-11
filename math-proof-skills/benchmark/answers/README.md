# SCORER-ONLY: agents under test must not read this directory

These files hold the answer keys. Keep them out of the tested agent's context:

- Give the agent only `run/inputs/<id>/` (built by `../setup.sh`): no corpus clone, no repo checkout, no `answers/`, no `history.md`, no `reasoning_traces/`, no `lean/docs/`.
- If the agent works inside a checkout of this repo, delete `math-proof-skills/benchmark/answers/` from that copy first, or score in a separate step after the agent's output is frozen.
- Agents reading the skill pack: do not open this folder.
