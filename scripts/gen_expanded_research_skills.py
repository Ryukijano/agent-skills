#!/usr/bin/env python3
"""Generate a batch of expanded research/ML skills for agent-skills.

Each skill gets the standard 4-file treatment:
  .devin/skills/<name>/SKILL.md
  .devin/workflows/<name>.md
  .cursor/skills/<name>/SKILL.md
  .cursor/commands/<name>.md

Usage:
    python3 gen_expanded_research_skills.py [path-to-agent-skills-repo] [data-file.py]
"""

import os
import re
import sys
from pathlib import Path

DEFAULT_BASE = "/home/aimsgroupuol/AIMSgeneral/Gyanateet/mpc_vla_diffusion_study/agent-skills"


def _get_data_file(argv: list) -> Path:
    if len(argv) > 2:
        return Path(argv[2])
    script = Path(__file__).resolve()
    return script.with_suffix(".data.py")


def _make_workflow_body(skill: dict) -> str:
    name = skill["name"]
    desc = skill["description"]
    return f"""# /{name}

{desc}

## Trigger

When the user is working on or asking about `{name.replace('-', ' ')}`.

## Steps

1. Load the `{name}` skill for the full reference.
2. Ask the user what architecture / framework / dataset they are using (Ampere, Hopper, Ada, Blackwell, GB10, JAX, CUDA-Q, etc.).
3. Propose the smallest verification or code snippet they can run next.
4. Point them at the references and any relevant `cuda-blackwell-labs` or `agent-skills` examples.

## Output

A focused, architecture-aware next action and a short code path to test it.
"""


def _make_command_body(skill: dict) -> str:
    name = skill["name"]
    return f"""# {name}

Quick reference for `{name.replace('-', ' ')}`.

- Architecture / framework: ask first.
- Key command / env vars: see the full skill.
- Verification: run the smallest failing test first.
"""


def _make_devin_skill(skill: dict) -> str:
    body = skill["devin_body"].strip()
    # Avoid double References sections if the raw body already ends with one.
    body = re.sub(r"\n+## References\n+.*", "", body, flags=re.DOTALL).strip()
    return f"""# {skill['title']}

## Description

{skill['description']}

{body}

## References

{chr(10).join('- ' + r for r in skill['references'])}
"""


def main() -> None:
    data_file = _get_data_file(sys.argv)
    if not data_file.exists():
        print(f"Data file not found: {data_file}", file=sys.stderr)
        sys.exit(1)

    spec = {"__file__": str(data_file)}
    with open(data_file, "r", encoding="utf-8") as f:
        exec(compile(f.read(), str(data_file), "exec"), spec, spec)

    SKILLS = spec.get("SKILLS")
    if not isinstance(SKILLS, list) or not SKILLS:
        print("SKILLS list is empty or missing in data file.", file=sys.stderr)
        sys.exit(1)

    base = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(DEFAULT_BASE)
    if not base.is_dir():
        print(f"Base path not found: {base}", file=sys.stderr)
        sys.exit(1)

    for s in SKILLS:
        name = s["name"]
        (base / ".devin" / "skills" / name).mkdir(parents=True, exist_ok=True)
        (base / ".cursor" / "skills" / name).mkdir(parents=True, exist_ok=True)
        (base / ".devin" / "workflows").mkdir(parents=True, exist_ok=True)
        (base / ".cursor" / "commands").mkdir(parents=True, exist_ok=True)

        devin_skill = _make_devin_skill(s)
        workflow = _make_workflow_body(s)
        command = _make_command_body(s)

        (base / ".devin" / "skills" / name / "SKILL.md").write_text(devin_skill, encoding="utf-8")
        (base / ".cursor" / "skills" / name / "SKILL.md").write_text(devin_skill, encoding="utf-8")
        (base / ".devin" / "workflows" / f"{name}.md").write_text(workflow, encoding="utf-8")
        (base / ".cursor" / "commands" / f"{name}.md").write_text(command, encoding="utf-8")

        print(f"Created {name}")

    print(f"Done. {len(SKILLS)} skill families created.")


if __name__ == "__main__":
    main()
