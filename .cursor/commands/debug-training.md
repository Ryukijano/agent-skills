# Debug Training

Diagnose training failures: loss=NaN, CUDA OOM, DDP hangs, poor convergence, wrong shapes.

Apply skills: `debug-pytorch-gpu`, `systematic-debug`, `iterative-test-loop`.

1. Identify failure mode from logs.
2. Follow the step-by-step tree in `.windsurf/workflows/debug-training.md`.
3. For MOT on Spark: `conda activate surgi_track`, `export XFORMERS_DISABLED=1`.
4. Verify fix with a short smoke train step before full resume.
