# /grant-proposal-writing

Structure Specific Aims, research strategy, budget, and broader impact sections for NIH/NSF/ERC-style proposals with AI drafting support.

## Trigger

When the user is working on or asking about `grant proposal writing`.

## Steps

1. Load the `grant-proposal-writing` skill for the full reference.
2. Ask the user what architecture / framework / dataset they are using (Ampere, Hopper, Ada, Blackwell, GB10, JAX, CUDA-Q, etc.).
3. Propose the smallest verification or code snippet they can run next.
4. Point them at the references and any relevant `cuda-blackwell-labs` or `agent-skills` examples.

## Output

A focused, architecture-aware next action and a short code path to test it.
