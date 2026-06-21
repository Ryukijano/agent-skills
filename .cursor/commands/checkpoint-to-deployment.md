# Checkpoint to Deployment

Extract a training checkpoint into deployment-ready weights (strip optimizer, EMA teacher, SSL heads).

1. Inspect `outputs/<run_name>/best.pth.tar` keys and step.
2. Strip training-only keys; save `deployment.pth` or encoder-only `encoder.pth`.
3. Load into a fresh model with `strict=False` diagnostics; run dummy inference.

Full procedure: `.windsurf/workflows/checkpoint-to-deployment.md`
