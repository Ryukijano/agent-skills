---
description: cuTile Python on GB10 workflow
---

# cuTile Python on GB10 Workflow

Skill: `.devin/skills/cutile-python-gb10/SKILL.md`

## Steps
1. Read the skill at `.devin/skills/cutile-python-gb10/SKILL.md`
2. Check driver version and create a venv with `cuda-tile[tileiras]` and `cupy-cuda13x`
3. Write the cuTile kernel in a real `.py` file (kernels need `inspect.getsource`)
4. Launch with `ct.launch()` and verify against CuPy/PyTorch reference
5. Report memory bandwidth (elementwise) or TFLOPS (GEMM)
