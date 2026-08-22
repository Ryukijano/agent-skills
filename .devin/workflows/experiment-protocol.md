# Experiment Protocol Run

1. Design: hypothesis, variables, metrics, sample sizes — written before running.
2. Controls: baselines matched on data/seeds/optimizer; ablation matrix defined.
3. Pre-registration checklist complete (predictions, kill criteria).
4. Environment manifest captured (versions, seeds, hardware, data hashes).
5. Execute in order: baseline first → verify metric pipeline on known subset → treatment conditions documented.
6. Log every run: config hash, start/end time, output paths, exit status.

Apply `experiment-protocol`, `reproducibility`.
