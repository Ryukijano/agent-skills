# /ai-for-tutoring

Use AI to build or augment a one-on-one digital tutor that diagnoses misconceptions and gives step-by-step guidance without giving away the answer.

## Trigger

When the user is working on or asking about `ai for tutoring`.

## Steps

1. Load the `ai-for-tutoring` skill for the full reference.
2. Ask the user what architecture / framework / dataset they are using (Ampere, Hopper, Ada, Blackwell, GB10, JAX, CUDA-Q, etc.).
3. Propose the smallest verification or code snippet they can run next.
4. Point them at the references and any relevant `cuda-blackwell-labs` or `agent-skills` examples.

## Output

A focused, architecture-aware next action and a short code path to test it.
