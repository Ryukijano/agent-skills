#!/usr/bin/env python3
"""Update agent-skills README counts and insert new skill/workflow rows.

Usage:
    python3 update_agent_skills_readme.py [path-to-repo]

If path is omitted, uses /home/aimsgroupuol/AIMSgeneral/Gyanateet/mpc_vla_diffusion_study/agent-skills.
"""

import re
import sys
from pathlib import Path

DEFAULT_BASE = "/home/aimsgroupuol/AIMSgeneral/Gyanateet/mpc_vla_diffusion_study/agent-skills"


def main():
    base = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(DEFAULT_BASE)
    if not base.is_dir():
        print(f"ERROR: {base} is not a directory", file=sys.stderr)
        sys.exit(1)

    readme = base / "README.md"
    if not readme.is_file():
        print(f"ERROR: {readme} not found", file=sys.stderr)
        sys.exit(1)

    new_skills = [
        ("tensor-core-fragment-layouts-gb10", "PTX mma.sync fragment layouts and lane-to-element mapping for GB10 Tensor Cores"),
        ("shared-memory-swizzling-gb10", "Bank-conflict-free shared memory layouts with XOR swizzling and padding tradeoffs on GB10"),
        ("blackwell-fp4-fp8-block-scaling-ptx-gb10", "FP8 and block-scaled FP4 (NVFP4) PTX MMA with scale factors on SM121"),
        ("cuda-occupancy-register-pressure-gb10", "Occupancy, register pressure, launch bounds, and SMEM tradeoffs on GB10"),
        ("cp-async-pipeline-gb10", "Multi-stage cp.async copy pipelines for GB10 GMEM->SMEM staging"),
        ("nsight-compute-tensor-cores-gb10", "Profile Tensor Core utilization and memory bottlenecks with Nsight Compute on GB10"),
        ("blackwell-sm121-targeting-gb10", "Correctly compile for GB10 (sm_121/121f/121a), PTX 9.1, and Triton ptxas setup"),
    ]
    new_skills.sort(key=lambda x: x[0])

    text = readme.read_text()

    # Determine which skills are actually new to this README
    missing_skills = [(n, d) for n, d in new_skills if f"| `{n}` |" not in text]
    missing_workflows = [(n, d) for n, d in new_skills if f"| `/{n}` |" not in text]
    add_count = len(missing_skills)

    def inc_counts(m):
        return f"{m.group(1)}{int(m.group(2)) + add_count}{m.group(3)}"

    # Top overview table
    if add_count:
        text = re.sub(
            r"(\| \*\*Devin\*\* \(`.devin/`\) \| )(\d+)( \| )(\d+)( workflows)",
            lambda m: f"{m.group(1)}{int(m.group(2)) + add_count}{m.group(3)}{int(m.group(4)) + add_count}{m.group(5)}",
            text,
        )
        text = re.sub(
            r"(\| \*\*Cursor\*\* \(`.cursor/`\) \| )(\d+)( \| )(\d+)( commands)",
            lambda m: f"{m.group(1)}{int(m.group(2)) + add_count}{m.group(3)}{int(m.group(4)) + add_count}{m.group(5)}",
            text,
        )

        # Update section counts and structure counts
        def bump_count(pattern, add):
            nonlocal text
            text = re.sub(pattern, lambda m: f"{m.group(1)}{int(m.group(2)) + add}{m.group(3)}", text)

        bump_count(r"(## Skills \()(\d+)(\))", add_count)
        bump_count(r"(## Workflows \()(\d+)(\))", add_count)
        bump_count(r"(### Custom Research Skills \()(\d+)(\))", add_count)
        bump_count(r"(### Custom Research Workflows \()(\d+)(\))", add_count)
        bump_count(r"(\.devin/skills/                    # )(\d+)", add_count)
        bump_count(r"(\.devin/workflows/                 # )(\d+)", add_count)
        bump_count(r"(\.cursor/skills/                    # )(\d+)", add_count)
        bump_count(r"(\.cursor/commands/                  # )(\d+)", add_count)

    # Insert skill rows into Custom Research Skills table
    skills_rows = "\n".join(f"| `{n}` | {d} |" for n, d in missing_skills)
    skills_pattern = r"(### Custom Research Skills \(\d+\)\n\n.*?\n\| Skill \| Description \|\n\|-------\|-------------\|\n)(.*?)(\n\n## Workflows|\n\n### Custom Research Workflows)"

    def repl_skills(m):
        existing = m.group(2).rstrip()
        if skills_rows:
            return f"{m.group(1)}{existing}\n{skills_rows}{m.group(3)}"
        return m.group(0)

    text_new, n_subs = re.subn(skills_pattern, repl_skills, text, flags=re.DOTALL)
    if n_subs == 0:
        print("ERROR: Could not find Custom Research Skills table", file=sys.stderr)
        sys.exit(1)
    text = text_new

    # Insert workflow rows into Custom Research Workflows table
    workflows_rows = "\n".join(f"| `/{n}` | {d} |" for n, d in missing_workflows)
    workflows_pattern = r"(### Custom Research Workflows \(\d+\)\n\n\| Workflow \| Description \|\n\|----------\|-------------\|\n)(.*?)(\n\n## Usage)"

    def repl_workflows(m):
        existing = m.group(2).rstrip()
        if workflows_rows:
            return f"{m.group(1)}{existing}\n{workflows_rows}{m.group(3)}"
        return m.group(0)

    text_new, n_subs = re.subn(workflows_pattern, repl_workflows, text, flags=re.DOTALL)
    if n_subs == 0:
        print("ERROR: Could not find Custom Research Workflows table", file=sys.stderr)
        sys.exit(1)
    text = text_new

    try:
        readme.write_text(text)
    except Exception as e:
        print(f"ERROR: failed to write {readme}: {e}", file=sys.stderr)
        sys.exit(1)

    print("README updated with", add_count, "new skills.")


if __name__ == "__main__":
    main()
