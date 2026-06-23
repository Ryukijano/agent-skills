---
name: dgx-spark-cosmos3
description: Running and developing with NVIDIA Cosmos3 (video/world model generation and action forward dynamics) on DGX Spark (GB10 Grace Blackwell) under AIMSgeneral. Covers venvs, launchers, and common workflows.
---

## DGX Spark + Cosmos3

### Key paths (from AGENTS.md + DGX_SPARK_SETUP)
- Base: `/home/aimsgroupuol/AIMSgeneral`
- Venv: `venv/cosmos3` (separate from nemotron)
- Scripts: `scripts/run_cosmos3_actions_spark.sh`, `run_cosmos3_t2v_spark.py`, verify + bootstrap.
- Outputs: `outputs/omni_actions/...`, `outputs/cosmos3_spark_test.mp4` etc.

### Separation
Never mix nemotron and cosmos3 in the same venv. Use `venv/nemotron` for agentic/document work; `venv/cosmos3` for video/world-model.

### Common commands
- Verify: `/cosmos-verify` or `scripts/verify_cosmos3_spark.sh`
- ESD forward dynamics: `scripts/run_cosmos3_actions_spark.sh forward_esd`
- T2V / other: see `workflows/devin/*.devin.md` and AIMSgeneral .cursor/commands

### Tips
- NATTEN / custom kernels may be required for some action models — run kernel bootstrap first if indicated.
- Large model weights (~28GB for Nano) live in HF cache.
- Monitor disk (2.9T+ free reported historically).

Related: AGENTS.md, `cosmos-spark-esd` rule, endosight-3d, agentic-loop-lifeline.
