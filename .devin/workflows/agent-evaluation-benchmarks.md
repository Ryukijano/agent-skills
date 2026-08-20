# /agent-evaluation-benchmarks

Measure agent capability on coding, web, tool use, and open-ended reasoning benchmarks.

## Trigger

When the user is working on or asking about `agent evaluation benchmarks`.

## Steps

1. Load the `agent-evaluation-benchmarks` skill for the full reference.
2. Ask the user what architecture / framework / dataset they are using (Ampere, Hopper, Ada, Blackwell, GB10, JAX, CUDA-Q, etc.).
3. Propose the smallest verification or code snippet they can run next.
4. Point them at the references and any relevant `cuda-blackwell-labs` or `agent-skills` examples.

## Output

A focused, architecture-aware next action and a short code path to test it.
