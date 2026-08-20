#!/usr/bin/env python3
"""Audit ai-for-* skills and workflows for low-quality / 'slop' patterns."""

import re
import sys
import json
from pathlib import Path
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_SECTIONS = ["When to use", "Code pattern", "Tuning notes", "Verification", "References"]
PREFERRED_SECTIONS = ["Usage", "Steps"]


def parse_markdown_headings(text):
    return [m.strip() for m in re.findall(r"^## (.+)$", text, re.MULTILINE)]


def find_code_blocks(text):
    """Return all fenced code blocks."""
    return re.findall(r"```(?:\w+)?\n(.*?)```", text, re.DOTALL)


def code_block_has_syntax_error(code, language=""):
    """Heuristic: check for common slop patterns in code snippets."""
    issues = []
    # Mismatched quotes around strings, e.g. from_pretrained("dennisjooo/"deepfake-vs-real")
    # Look for a quote immediately followed by non-separator text and another quote (unescaped inner quotes)
    if re.search(r'(?<![\\])["\'](?:(?![\\])["\']).*?(?<![\\])["\']', code):
        issues.append("suspicious nested quotes")
    # Unclosed parens/brackets (simple)
    for open_c, close_c in [("(", ")"), ("[", "]"), ("{", "}")]:
        if code.count(open_c) != code.count(close_c):
            issues.append(f"unbalanced {open_c}{close_c}")
            break
    # Invalid escape sequences in non-raw strings
    if re.search(r'(?<!\\)\\[a-zA-Z]', code):
        # this is very broad; just count as potential issue
        issues.append("possible invalid escape")
    # Placeholder / todo comments
    if re.search(r'(<INSERT|TODO|FIXME|\[INSERT|\{\{.*\}\})', code, re.IGNORECASE):
        issues.append("placeholder")
    # Missing imports in python? Too strict.
    return issues


def heading_score(headings):
    missing = [s for s in REQUIRED_SECTIONS if s not in headings]
    has_key_concepts = "Key concepts" in headings
    has_usage = "Usage" in headings
    has_steps = "Steps" in headings
    return {
        "missing_required": missing,
        "has_key_concepts": has_key_concepts,
        "has_usage_steps": has_usage and has_steps,
    }


def description_quality(text):
    """Simple heuristics for description fluff."""
    desc_match = re.search(r"## Description\n\n(.+?)\n\n", text, re.DOTALL)
    if not desc_match:
        return {"score": 0, "issues": ["no description"]}
    desc = desc_match.group(1)
    issues = []
    # Just a comma-separated list of nouns?
    if len(re.findall(r", ", desc)) >= 4 and len(desc.split(". ")) <= 1:
        issues.append("description is a comma list")
    # Vague verbs repeated
    vague = ["using", "with", "and", "or", "for", "in"]
    words = desc.lower().split()
    if sum(1 for w in words if w in vague) / max(len(words), 1) > 0.5:
        issues.append("description is mostly filler words")
    # Too short
    if len(desc) < 60:
        issues.append("description is very short")
    # Starts with "Machine learning for" then a list
    if desc.lower().startswith("machine learning for") and "," in desc:
        issues.append("generic 'Machine learning for X, Y, Z' formula")
    return {"length": len(desc), "issues": issues}


def audit_skills():
    results = []
    all_headings = Counter()
    all_issues = Counter()

    for platform in ("devin", "cursor"):
        skills_dir = ROOT / f".{platform}" / "skills"
        for d in skills_dir.glob("ai-for-*/"):
            f = d / "SKILL.md"
            if not f.exists():
                continue
            text = f.read_text()
            headings = parse_markdown_headings(text)
            hs = heading_score(headings)
            dq = description_quality(text)

            code_issues = []
            for code in find_code_blocks(text):
                issues = code_block_has_syntax_error(code)
                if issues:
                    code_issues.append(issues)

            # References count
            refs = re.findall(r"^## References$", text, re.MULTILINE)
            ref_count = len(re.findall(r"^\s*- (https?://|/)", text, re.MULTILINE))

            issues = []
            if hs["missing_required"]:
                issues.append(f"missing {hs['missing_required']}")
            if hs["has_key_concepts"] and not hs["has_usage_steps"]:
                issues.append("uses 'Key concepts' instead of 'Usage'/'Steps'")
            if dq["issues"]:
                issues.extend(dq["issues"])
            if code_issues:
                issues.append(f"code pattern issues: {code_issues[:2]}")
            if ref_count == 0:
                issues.append("no references")
            elif ref_count < 3:
                issues.append("few references")

            results.append({
                "platform": platform,
                "skill": d.name,
                "path": str(f),
                "headings": headings,
                "description": dq,
                "issues": issues,
            })

            for h in headings:
                all_headings[h] += 1
            for issue in issues:
                # bucket issue type
                key = issue.split(":")[0]
                all_issues[key] += 1

    return results, all_headings, all_issues


def main():
    results, all_headings, all_issues = audit_skills()

    print(f"Audited {len(results)} ai-for-* skills")
    print("\nHeading distribution:")
    for h, c in all_headings.most_common():
        print(f"  {h}: {c}")

    print("\nCommon issue types:")
    for issue, c in all_issues.most_common():
        print(f"  {issue}: {c}")

    flagged = [r for r in results if r["issues"]]
    print(f"\nFlagged {len(flagged)} skills with one or more issues")

    out = ROOT / "scripts" / "ai_for_slop_report.json"
    out.write_text(json.dumps({
        "total": len(results),
        "flagged_count": len(flagged),
        "heading_counts": dict(all_headings),
        "issue_counts": dict(all_issues),
        "flagged": flagged,
    }, indent=2))
    print(f"\nWrote {out}")


if __name__ == "__main__":
    main()
