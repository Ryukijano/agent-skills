# /triton-cross-arch

Writing and deploying Triton kernels across sm_80, sm_89, sm_90, sm_100, sm_120, and sm_121.

## Trigger

When the user is working on or asking about `triton cross arch`.

## Steps

1. Load the `triton-cross-arch` skill for the full reference.
2. Ask the user what architecture / framework / dataset they are using (Ampere, Hopper, Ada, Blackwell, GB10, JAX, CUDA-Q, etc.).
3. Propose the smallest verification or code snippet they can run next.
4. Point them at the references and any relevant `cuda-blackwell-labs` or `agent-skills` examples.

## Output

A focused, architecture-aware next action and a short code path to test it.
