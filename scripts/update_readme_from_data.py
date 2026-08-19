#!/usr/bin/env python3
"""Update README.md from a skill data file.

Usage:
    python3 update_readme_from_data.py <data-file.py>

The data file must define a `SKILLS` list, where each skill is a dict with
`name` and `description` keys.
"""

import re
import sys
from pathlib import Path

BASE = Path("/home/aimsgroupuol/AIMSgeneral/Gyanateet/mpc_vla_diffusion_study/agent-skills")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: update_readme_from_data.py <data-file.py>", file=sys.stderr)
        sys.exit(1)

    data_file = Path(sys.argv[1])
    if not data_file.is_absolute():
        data_file = (BASE / data_file).resolve()

    spec = {"__file__": str(data_file)}
    with open(data_file, "r", encoding="utf-8") as f:
        exec(compile(f.read(), str(data_file), "exec"), spec, spec)

    skills = spec.get("SKILLS")
    if not isinstance(skills, list) or not skills:
        print("SKILLS list is empty or missing.", file=sys.stderr)
        sys.exit(1)

    new_skills = [(s["name"], s["description"]) for s in skills]
    new_skills.sort(key=lambda x: x[0])

    readme = BASE / "README.md"
    text = readme.read_text()

    missing_skills = [(n, d) for n, d in new_skills if f"| `{n}` |" not in text]
    missing_workflows = [(n, d) for n, d in new_skills if f"| `/{n}` |" not in text]
    add_count = len(missing_skills)

    if not add_count:
        print("README already up-to-date.")
        return

    # Bump counts
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

    skills_rows = "\n".join(f"| `{n}` | {d} |" for n, d in missing_skills)
    skills_pattern = r"(### Custom Research Skills \(\d+\)\n\n.*?\n\| Skill \| Description \|\n\|-------\|-------------\|\n)(.*?)(\n\n## Workflows|\n\n### Custom Research Workflows)"

    def repl_skills(m):
        existing = m.group(2).rstrip()
        return f"{m.group(1)}{existing}\n{skills_rows}{m.group(3)}"

    text, n_subs = re.subn(skills_pattern, repl_skills, text, flags=re.DOTALL)
    if n_subs == 0:
        print("ERROR: Could not find Custom Research Skills table", file=sys.stderr)
        sys.exit(1)

    workflows_rows = "\n".join(f"| `/{n}` | {d} |" for n, d in missing_workflows)
    workflows_pattern = r"(### Custom Research Workflows \(\d+\)\n\n\| Workflow \| Description \|\n\|----------\|-------------\|\n)(.*?)(\n\n## Usage)"

    def repl_workflows(m):
        existing = m.group(2).rstrip()
        return f"{m.group(1)}{existing}\n{workflows_rows}{m.group(3)}"

    text, n_subs = re.subn(workflows_pattern, repl_workflows, text, flags=re.DOTALL)
    if n_subs == 0:
        print("ERROR: Could not find Custom Research Workflows table", file=sys.stderr)
        sys.exit(1)

    readme.write_text(text)
    print(f"README updated with {add_count} new skills.")


if __name__ == "__main__":
    main()
