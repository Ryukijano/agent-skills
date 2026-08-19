# cuTile Python on GB10

Use NVIDIA cuTile Python (cuda.tile) for tile-based GPU programming on GB10 / sm_121. Covers installation, tile load/store, vector add, matrix multiplication with ct.mma, and environment setup for the tileiras compiler.

Skill: `.cursor/skills/cutile-python-gb10/SKILL.md`

## Workflow
1. Read `.cursor/skills/cutile-python-gb10/SKILL.md`
2. Check driver version and create a venv with `cuda-tile[tileiras]` and `cupy-cuda13x`
3. Write the cuTile kernel in a real `.py` file
4. Launch with `ct.launch()` and verify against CuPy/PyTorch reference
5. Report memory bandwidth or TFLOPS
