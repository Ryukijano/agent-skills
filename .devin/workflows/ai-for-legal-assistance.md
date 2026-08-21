# /ai-for-legal-assistance

Use NLP to triage legal questions, summarize contracts, flag risky clauses, and help non-experts fill forms and find the right jurisdiction.

## Trigger

When the user is working on or asking about `ai for legal assistance`.

## Steps

1. Load the `ai-for-legal-assistance` skill for the full reference.
2. Ask the user what architecture / framework / dataset they are using (Ampere, Hopper, Ada, Blackwell, GB10, JAX, CUDA-Q, etc.).
3. Propose the smallest verification or code snippet they can run next.
4. Point them at the references and any relevant `cuda-blackwell-labs` or `agent-skills` examples.

## Output

A focused, architecture-aware next action and a short code path to test it.
