# Ablation Study Workflow

1. Define the controlled axis (e.g. "LoRA rank 4/8/16, all else matched").
2. Create a WandB group name and tag all runs.
3. Prepare a matrix of configs or override lists (commit them).
4. Launch (or queue) the runs; record job IDs.
5. As runs finish, verify each with smoke eval + targeted metrics.
6. Pull results into a table (mAP@50, MOTA, key secondary).
7. Generate a bar chart or paper table (use professional styling: bold legend, error bars if multi-seed).
8. Write a short `experiments/<slug>/ablation-findings.md`.
9. Update paper draft discussion with the key takeaway + caveats.

Apply `ablation-study`, `experiment-tracking`, `reproducibility`.
