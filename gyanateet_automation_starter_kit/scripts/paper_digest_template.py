#!/usr/bin/env python3
"""Skeleton for a paper digest generator.

Wire this to arXiv/Semantic Scholar/Zotero in n8n, then pass exported JSON here.
This offline script deduplicates and renders Markdown.
"""
import json
from pathlib import Path
import argparse


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--input', required=True)
    ap.add_argument('--output', default='paper_digest.md')
    args = ap.parse_args()
    papers = json.loads(Path(args.input).read_text())
    seen = set()
    lines = ['# Paper Digest', '']
    for p in papers:
        key = (p.get('title') or '').lower().strip()
        if not key or key in seen:
            continue
        seen.add(key)
        lines.extend([
            f"## {p.get('title', 'Untitled')}",
            f"- Authors: {p.get('authors', 'Unknown')}",
            f"- Link: {p.get('url', '')}",
            f"- Tags: {', '.join(p.get('tags', [])) if isinstance(p.get('tags'), list) else p.get('tags', '')}",
            f"- Why it may matter: {p.get('why_it_matters', 'TODO')}",
            ''
        ])
    Path(args.output).write_text('
'.join(lines))

if __name__ == '__main__':
    main()
