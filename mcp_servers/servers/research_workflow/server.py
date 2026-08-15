#!/usr/bin/env python3
"""
Research Workflow MCP Server

ArXiv search, paper digestion, BibTeX management, experiment tracking,
and reproducibility bundling as MCP tools.

MCP mode:  python3 server.py
CLI mode:  python3 server.py --cli <tool_name> [--arg value ...]
"""
import sys
import os
import json
import re
import subprocess
import time
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import zipfile
import platform
import datetime
import hashlib
from typing import Annotated

import requests

from mcp.server import MCPServer

server = MCPServer("research-workflow", "1.0.0")

# Configurable paths
BIBTEX_FILE = os.environ.get("RESEARCH_BIBTEX", os.path.expanduser("~/research/papers.bib"))
EXPERIMENTS_ROOT = os.environ.get("RESEARCH_EXPERIMENTS_ROOT", os.path.expanduser("~/research/experiments"))

DEFAULT_USER_AGENT = "DGX-Spark-MCP/1.0 (research workflow; contact=aimsgroupuol@example.com)"
DEFAULT_HTTP_TIMEOUT = 10
HTTP_MAX_RETRIES = 2


def _http_get(url: str, headers: dict | None = None, timeout: int = DEFAULT_HTTP_TIMEOUT) -> dict:
    """Resilient HTTP GET with polite User-Agent, timeout, and exponential-backoff retries."""
    merged = {"User-Agent": DEFAULT_USER_AGENT}
    if headers:
        merged.update(headers)
    last_response = None
    for attempt in range(HTTP_MAX_RETRIES + 1):
        try:
            r = requests.get(url, headers=merged, timeout=timeout)
            last_response = r
            if r.status_code < 300:
                return {"status": r.status_code, "data": r.text}
            # Retry on transient / rate-limit status codes.
            if r.status_code in (429, 502, 503, 504) and attempt < HTTP_MAX_RETRIES:
                time.sleep(2 ** attempt)
                continue
            return {"status": r.status_code, "data": r.text}
        except requests.exceptions.RequestException as e:
            if attempt < HTTP_MAX_RETRIES:
                time.sleep(2 ** attempt)
                continue
            return {"status": 0, "data": f"{type(e).__name__}: {e}"}
    if last_response is not None:
        return {"status": last_response.status_code, "data": last_response.text}
    return {"status": 0, "data": "Unknown error after retries"}


# --- ArXiv Tools ---

@server.tool()
def search_arxiv(
    query: Annotated[str, "Search query (keywords, title, author)"],
    max_results: Annotated[int, "Maximum number of results"] = 10,
    sort_by: Annotated[str, "Sort by: relevance, submittedDate, lastUpdatedDate"] = "relevance",
) -> str:
    """Search arXiv for papers. Returns titles, authors, abstracts, and arXiv IDs."""
    base = "http://export.arxiv.org/api/query"
    params = urllib.parse.urlencode({
        "search_query": f"all:{query}",
        "max_results": str(max_results),
        "sortBy": sort_by,
        "sortOrder": "descending",
    })
    r = _http_get(f"{base}?{params}")
    if r["status"] != 200:
        return f"Error searching arXiv: {r['data']}"
    # Parse Atom XML (simple regex-based parsing for key fields)
    entries = re.findall(r"<entry>(.*?)</entry>", r["data"], re.DOTALL)
    if not entries:
        return f"No results found for '{query}'"
    results = [f"ArXiv search: '{query}' ({len(entries)} results)\n"]
    for i, entry in enumerate(entries[:max_results], 1):
        title = re.search(r"<title>(.*?)</title>", entry, re.DOTALL)
        arxiv_id = re.search(r"<id>http://arxiv.org/abs/(.*?)</id>", entry, re.DOTALL)
        published = re.search(r"<published>(.*?)</published>", entry)
        summary = re.search(r"<summary>(.*?)</summary>", entry, re.DOTALL)
        authors = re.findall(r"<name>(.*?)</name>", entry)
        title_text = title.group(1).strip() if title else "Unknown"
        arxiv_id_text = arxiv_id.group(1).strip() if arxiv_id else "Unknown"
        date_text = published.group(1)[:10] if published else "Unknown"
        summary_text = summary.group(1).strip()[:200] + "..." if summary else ""
        author_list = ", ".join(authors[:3])
        if len(authors) > 3:
            author_list += f" et al. ({len(authors)} authors)"
        results.append(f"{i}. [{arxiv_id_text}] {title_text}")
        results.append(f"   Authors: {author_list}")
        results.append(f"   Date: {date_text}")
        results.append(f"   Abstract: {summary_text}\n")
    return "\n".join(results)


@server.tool()
def get_arxiv_paper(
    arxiv_id: Annotated[str, "ArXiv paper ID (e.g., '2401.12345' or '2401.12345v1')"],
    download_pdf: Annotated[bool, "Download the PDF to ~/research/papers/"] = False,
) -> str:
    """Get metadata for a specific arXiv paper by ID. Optionally download the PDF."""
    base = "http://export.arxiv.org/api/query"
    params = urllib.parse.urlencode({"id_list": arxiv_id})
    r = _http_get(f"{base}?{params}")
    if r["status"] != 200:
        # arXiv often returns an XML error entry for malformed/unknown IDs.
        try:
            root = ET.fromstring(r["data"])
            atom_ns = "http://www.w3.org/2005/Atom"
            entry = root.find(f".//{{{atom_ns}}}entry")
            if entry is not None:
                title = entry.find(f".//{{{atom_ns}}}title")
                if title is not None and title.text == "Error":
                    return f"Paper not found: {arxiv_id}"
        except ET.ParseError:
            pass
        return f"Error: {r['data']}"

    # Fast invalid-ID detection via opensearch:totalResults and entry presence.
    try:
        root = ET.fromstring(r["data"])
        ns = {"opensearch": "http://a9.com/-/spec/opensearch/1.1/"}
        total_results = root.find(".//opensearch:totalResults", ns)
        if total_results is not None and total_results.text == "0":
            return f"Paper not found: {arxiv_id}"
        atom_ns = "http://www.w3.org/2005/Atom"
        if not root.findall(f".//{{{atom_ns}}}entry"):
            return f"Paper not found: {arxiv_id}"
    except ET.ParseError:
        if re.search(r'<opensearch:totalResults[^>]*>0</opensearch:totalResults>', r["data"]):
            return f"Paper not found: {arxiv_id}"

    entry = re.search(r"<entry>(.*?)</entry>", r["data"], re.DOTALL)
    if not entry:
        return f"Paper not found: {arxiv_id}"
    entry = entry.group(1)
    title = re.search(r"<title>(.*?)</title>", entry, re.DOTALL)
    authors = re.findall(r"<name>(.*?)</name>", entry)
    published = re.search(r"<published>(.*?)</published>", entry)
    summary = re.search(r"<summary>(.*?)</summary>", entry, re.DOTALL)
    doi = re.search(r'<arxiv:doi[^>]*>(.*?)</arxiv:doi>', entry)
    categories = re.findall(r'<category term="(.*?)"', entry)
    result = f"ArXiv Paper: {arxiv_id}\n"
    result += f"Title: {title.group(1).strip() if title else 'Unknown'}\n"
    result += f"Authors: {', '.join(authors)}\n"
    result += f"Published: {published.group(1)[:10] if published else 'Unknown'}\n"
    result += f"Categories: {', '.join(categories)}\n"
    if doi:
        result += f"DOI: {doi.group(1)}\n"
    result += f"\nAbstract:\n{summary.group(1).strip() if summary else 'No abstract'}\n"
    if download_pdf:
        pdf_url = f"http://arxiv.org/pdf/{arxiv_id}.pdf"
        papers_dir = os.path.expanduser("~/research/papers")
        os.makedirs(papers_dir, exist_ok=True)
        pdf_path = os.path.join(papers_dir, f"{arxiv_id.replace('/', '_')}.pdf")
        try:
            urllib.request.urlretrieve(pdf_url, pdf_path)
            size_mb = os.path.getsize(pdf_path) / (1024 * 1024)
            result += f"\nPDF downloaded: {pdf_path} ({size_mb:.1f} MB)\n"
        except Exception as e:
            result += f"\nPDF download failed: {e}\n"
    return result


@server.tool()
def get_paper(
    arxiv_id: Annotated[str, "ArXiv paper ID (e.g., '2401.12345' or '2401.12345v1')"],
    download_pdf: Annotated[bool, "Download the PDF to ~/research/papers/"] = False,
) -> str:
    """Alias for get_arxiv_paper."""
    return get_arxiv_paper(arxiv_id, download_pdf)


# --- BibTeX Tools ---

@server.tool()
def add_to_bibtex(
    arxiv_id: Annotated[str, "ArXiv paper ID to add"],
    bibtex_file: Annotated[str, f"Path to BibTeX file (default: {BIBTEX_FILE})"] = BIBTEX_FILE,
) -> str:
    """Add an arXiv paper to your BibTeX file. Generates a proper BibTeX entry."""
    # Get paper metadata
    base = "http://export.arxiv.org/api/query"
    params = urllib.parse.urlencode({"id_list": arxiv_id})
    r = _http_get(f"{base}?{params}")
    if r["status"] != 200:
        return f"Error fetching paper: {r['data']}"
    entry = re.search(r"<entry>(.*?)</entry>", r["data"], re.DOTALL)
    if not entry:
        return f"Paper not found: {arxiv_id}"
    entry = entry.group(1)
    title = re.search(r"<title>(.*?)</title>", entry, re.DOTALL)
    authors = re.findall(r"<name>(.*?)</name>", entry)
    published = re.search(r"<published>(.*?)</published>", entry)
    # Generate BibTeX key (firstauthor + year + firstword)
    first_author = authors[0].split()[-1].lower() if authors else "unknown"
    year = published.group(1)[:4] if published else "2026"
    title_words = title.group(1).strip().split() if title else ["unknown"]
    first_word = re.sub(r'[^a-zA-Z]', '', title_words[0].lower())
    bib_key = f"{first_author}{year}{first_word}"
    # Build BibTeX entry
    author_str = " and ".join(authors)
    bib_entry = f"@article{{{bib_key},\n"
    bib_entry += f"  title = {{{title.group(1).strip() if title else ''}}},\n"
    bib_entry += f"  author = {{{author_str}}},\n"
    bib_entry += f"  journal = {{arXiv preprint arXiv:{arxiv_id}}},\n"
    bib_entry += f"  year = {{{year}}},\n"
    bib_entry += f"  eprint = {{{arxiv_id}}},\n"
    bib_entry += f"  archivePrefix = {{arXiv}}\n"
    bib_entry += "}\n"
    # Append to file
    os.makedirs(os.path.dirname(bibtex_file), exist_ok=True)
    with open(bibtex_file, "a") as f:
        f.write("\n" + bib_entry)
    return f"Added BibTeX entry '{bib_key}' to {bibtex_file}\n\n{bib_entry}"


@server.tool()
def search_bibtex(
    query: Annotated[str, "Search query (title, author, or key)"],
    bibtex_file: Annotated[str, f"Path to BibTeX file (default: {BIBTEX_FILE})"] = BIBTEX_FILE,
) -> str:
    """Search your BibTeX database for entries matching the query."""
    if not os.path.isfile(bibtex_file):
        return f"BibTeX file not found: {bibtex_file}"
    with open(bibtex_file) as f:
        content = f.read()
    # Simple search: find entries containing the query
    entries = re.findall(r'(@\w+\{[^}]+(?:\{[^}]*\}[^}]*)*\})', content, re.DOTALL)
    matches = []
    query_lower = query.lower()
    for entry in entries:
        if query_lower in entry.lower():
            matches.append(entry.strip())
    if not matches:
        return f"No BibTeX entries matching '{query}' in {bibtex_file}"
    return f"Found {len(matches)} matching entries:\n\n" + "\n\n---\n\n".join(matches[:10])


# --- Experiment Tracking Tools ---

@server.tool()
def list_experiments() -> str:
    """List experiment directories with timestamps and status."""
    if not os.path.isdir(EXPERIMENTS_ROOT):
        return f"Experiments directory not found: {EXPERIMENTS_ROOT}"
    entries = sorted(os.listdir(EXPERIMENTS_ROOT))
    if not entries:
        return f"No experiments in {EXPERIMENTS_ROOT}"
    results = ["Experiments:"]
    for entry in entries:
        path = os.path.join(EXPERIMENTS_ROOT, entry)
        if not os.path.isdir(path):
            continue
        # Check for metadata
        meta_path = os.path.join(path, "metadata.json")
        if os.path.isfile(meta_path):
            with open(meta_path) as f:
                meta = json.load(f)
            status = meta.get("status", "unknown")
            desc = meta.get("description", "")
            results.append(f"  {entry:40} [{status}] {desc}")
        else:
            # Infer from contents
            has_log = os.path.isfile(os.path.join(path, "log.md"))
            has_results = os.path.isdir(os.path.join(path, "results"))
            has_code = os.path.isdir(os.path.join(path, "code"))
            status_parts = []
            if has_code: status_parts.append("code")
            if has_log: status_parts.append("log")
            if has_results: status_parts.append("results")
            results.append(f"  {entry:40} [{', '.join(status_parts) or 'empty'}]")
    return "\n".join(results)


@server.tool()
def create_experiment(
    name: Annotated[str, "Experiment name (will be directory name)"],
    description: Annotated[str, "Short description of the experiment"] = "",
    hypothesis: Annotated[str, "Hypothesis being tested"] = "",
    tags: Annotated[str, "Comma-separated tags"] = "",
) -> str:
    """Create a new experiment directory with metadata, log, and subdirectories."""
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    exp_dir = os.path.join(EXPERIMENTS_ROOT, f"{timestamp}_{name}")
    os.makedirs(exp_dir, exist_ok=True)
    os.makedirs(os.path.join(exp_dir, "code"), exist_ok=True)
    os.makedirs(os.path.join(exp_dir, "data"), exist_ok=True)
    os.makedirs(os.path.join(exp_dir, "results"), exist_ok=True)
    # Write metadata
    meta = {
        "name": name,
        "description": description,
        "hypothesis": hypothesis,
        "tags": [t.strip() for t in tags.split(",") if t.strip()],
        "created": timestamp,
        "status": "created",
    }
    with open(os.path.join(exp_dir, "metadata.json"), "w") as f:
        json.dump(meta, f, indent=2)
    # Write initial log
    with open(os.path.join(exp_dir, "log.md"), "w") as f:
        f.write(f"# Experiment: {name}\n\n")
        f.write(f"**Created:** {timestamp}\n")
        f.write(f"**Description:** {description}\n")
        f.write(f"**Hypothesis:** {hypothesis}\n\n")
        f.write("## Log\n\n")
    return f"Experiment created: {exp_dir}"


@server.tool()
def log_experiment(
    experiment: Annotated[str, "Experiment directory name or timestamp prefix"],
    message: Annotated[str, "Log message to append"],
) -> str:
    """Append a timestamped entry to an experiment's log file."""
    # Find the experiment directory
    candidates = [d for d in os.listdir(EXPERIMENTS_ROOT) if d.endswith(experiment) or d.startswith(experiment) or experiment == d]
    if not candidates:
        return f"Experiment not found: {experiment}"
    exp_dir = os.path.join(EXPERIMENTS_ROOT, candidates[0])
    log_path = os.path.join(exp_dir, "log.md")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(log_path, "a") as f:
        f.write(f"### {timestamp}\n\n{message}\n\n")
    return f"Logged to {log_path}"


# --- Reproducibility Bundling ---

@server.tool()
def create_repro_bundle(
    source_dir: Annotated[str, "Directory to bundle into a reproducibility archive"],
    output_path: Annotated[str, "Path to output zip (default: ~/research/repro-bundles/<name>.zip)"] = "",
) -> str:
    """Create a zip of a target directory plus a manifest with git status, env snapshot, and file list."""
    source = os.path.abspath(os.path.expanduser(source_dir))
    if not os.path.isdir(source):
        return f"Source directory not found: {source_dir}"

    name = os.path.basename(source)
    if not output_path:
        output = os.path.join(os.path.expanduser("~/research/repro-bundles"), f"{name}.zip")
    else:
        output = os.path.abspath(os.path.expanduser(output_path))
    out_dir = os.path.dirname(output)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)

    manifest = {
        "created": datetime.datetime.now().isoformat(),
        "source_dir": source,
        "output_path": output,
        "name": name,
        "git_status": None,
        "git_log": None,
        "env_snapshot": None,
        "file_list": [],
    }

    # Git snapshot
    try:
        is_git = subprocess.run(
            ["git", "-C", source, "rev-parse", "--is-inside-work-tree"],
            capture_output=True, text=True, timeout=10
        )
        if is_git.returncode == 0 and is_git.stdout.strip() == "true":
            status = subprocess.run(
                ["git", "-C", source, "status", "--porcelain"],
                capture_output=True, text=True, timeout=10
            )
            if status.returncode == 0:
                manifest["git_status"] = status.stdout.strip()
            log = subprocess.run(
                ["git", "-C", source, "log", "-1"],
                capture_output=True, text=True, timeout=10
            )
            if log.returncode == 0:
                manifest["git_log"] = log.stdout.strip()
    except Exception as e:
        manifest["git_status"] = f"git capture failed: {e}"

    # Environment snapshot
    python_version = platform.python_version()
    if os.path.isfile(os.path.join(source, "requirements.txt")):
        try:
            pip = subprocess.run(
                [sys.executable, "-m", "pip", "list"],
                capture_output=True, text=True, timeout=30
            )
            if pip.returncode == 0:
                manifest["env_snapshot"] = {
                    "python_version": python_version,
                    "pip_packages": pip.stdout.strip(),
                }
            else:
                manifest["env_snapshot"] = {
                    "python_version": python_version,
                    "pip_error": pip.stderr.strip(),
                }
        except Exception as e:
            manifest["env_snapshot"] = {"python_version": python_version, "pip_error": str(e)}
    else:
        manifest["env_snapshot"] = {"python_version": python_version}

    file_list = []
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(source):
            # Skip VCS and cache directories
            dirs[:] = [d for d in dirs if d not in (".git", "__pycache__")]
            for file in files:
                if file.endswith(".pyc"):
                    continue
                full = os.path.join(root, file)
                arcname = os.path.relpath(full, source)
                try:
                    zf.write(full, arcname)
                    file_list.append({"path": arcname, "size_bytes": os.path.getsize(full)})
                except Exception as e:
                    file_list.append({"path": arcname, "error": str(e)})

        file_list.append({"path": "manifest.json", "note": "bundle manifest"})
        manifest["file_list"] = file_list
        zf.writestr("manifest.json", json.dumps(manifest, indent=2))

    return (
        f"Repro bundle created: {output}\n"
        f"Files archived: {len(file_list)}\n"
        f"Git status lines: {len(manifest['git_status'].splitlines()) if manifest['git_status'] else 0}\n"
        f"Env snapshot: {manifest['env_snapshot']}"
    )


# --- Semantic Scholar Tools ---

@server.tool()
def search_semantic_scholar(
    query: Annotated[str, "Search query"],
    max_results: Annotated[int, "Maximum results"] = 10,
    fields: Annotated[str, "Comma-separated fields to return"] = "title,authors,year,abstract,citationCount,externalIds",
) -> str:
    """Search Semantic Scholar for papers. Returns titles, authors, citation counts."""
    base = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = urllib.parse.urlencode({
        "query": query,
        "limit": str(max_results),
        "fields": fields,
    })
    headers = {}
    s2_key = os.environ.get("S2_API_KEY")
    if s2_key:
        headers["x-api-key"] = s2_key
    r = _http_get(f"{base}?{params}", headers=headers, timeout=10)
    if r["status"] != 200:
        return f"Error: {r['data']}"
    data = json.loads(r["data"])
    papers = data.get("data", [])
    if not papers:
        return f"No results for '{query}'"
    results = [f"Semantic Scholar: '{query}' ({data.get('total', len(papers))} total, showing {len(papers)})\n"]
    for i, paper in enumerate(papers[:max_results], 1):
        title = paper.get("title", "Unknown")
        year = paper.get("year", "?")
        citations = paper.get("citationCount", 0)
        authors = [a.get("name", "?") for a in paper.get("authors", [])[:3]]
        author_str = ", ".join(authors)
        if len(paper.get("authors", [])) > 3:
            author_str += " et al."
        arxiv_id = paper.get("externalIds", {}).get("ArXiv", "")
        doi = paper.get("externalIds", {}).get("DOI", "")
        results.append(f"{i}. {title} ({year})")
        results.append(f"   Authors: {author_str}")
        results.append(f"   Citations: {citations}")
        if arxiv_id:
            results.append(f"   ArXiv: {arxiv_id}")
        if doi:
            results.append(f"   DOI: {doi}")
        results.append("")
    return "\n".join(results)


@server.tool()
def get_citations(
    arxiv_id: Annotated[str, "ArXiv paper ID"],
    limit: Annotated[int, "Maximum number of citations to return"] = 10,
) -> str:
    """Get citations for an arXiv paper from Semantic Scholar."""
    headers = {}
    s2_key = os.environ.get("S2_API_KEY")
    if s2_key:
        headers["x-api-key"] = s2_key
    url = (
        f"https://api.semanticscholar.org/graph/v1/paper/ARXIV:{arxiv_id}/citations"
        f"?fields=title,authors,year&limit={limit}"
    )
    r = _http_get(url, headers=headers, timeout=10)
    if r["status"] != 200:
        return f"Error fetching citations for {arxiv_id}: {r['data']}"
    data = json.loads(r["data"])
    papers = data.get("data", [])
    if not papers:
        return f"No citations found for {arxiv_id}"
    results = [f"Citations for arXiv:{arxiv_id} (showing {len(papers)}):\n"]
    for i, citation in enumerate(papers, 1):
        paper = citation.get("citingPaper", {})
        title = paper.get("title", "Unknown")
        year = paper.get("year", "?")
        authors = [a.get("name", "?") for a in paper.get("authors", [])[:3]]
        author_str = ", ".join(authors) if authors else "?"
        if len(paper.get("authors", [])) > 3:
            author_str += " et al."
        results.append(f"{i}. {title} ({year}) - {author_str}")
    return "\n".join(results)


# --- CLI Mode ---

TOOLS = {
    "search_arxiv": search_arxiv,
    "get_arxiv_paper": get_arxiv_paper,
    "get_paper": get_paper,
    "add_to_bibtex": add_to_bibtex,
    "search_bibtex": search_bibtex,
    "list_experiments": list_experiments,
    "create_experiment": create_experiment,
    "log_experiment": log_experiment,
    "search_semantic_scholar": search_semantic_scholar,
    "get_citations": get_citations,
    "create_repro_bundle": create_repro_bundle,
}


def cli_mode():
    if len(sys.argv) < 3:
        print("Usage: python3 server.py --cli <tool_name> [--arg value ...]")
        print("\nAvailable tools:")
        for name, func in TOOLS.items():
            doc = func.__doc__ or ""
            print(f"  {name:25} - {doc.split(chr(10))[0]}")
        sys.exit(1)
    tool_name = sys.argv[2]
    if tool_name not in TOOLS:
        print(f"Unknown tool: {tool_name}")
        print(f"Available: {', '.join(TOOLS.keys())}")
        sys.exit(1)
    kwargs = {}
    args = sys.argv[3:]
    i = 0
    while i < len(args):
        if args[i].startswith("--"):
            key = args[i][2:]
            if i + 1 < len(args) and not args[i + 1].startswith("--"):
                val = args[i + 1]
                if val.lower() in ("true", "false"):
                    kwargs[key] = val.lower() == "true"
                else:
                    try:
                        kwargs[key] = int(val)
                    except ValueError:
                        kwargs[key] = val
                i += 2
            else:
                kwargs[key] = True
                i += 1
        else:
            i += 1
    result = TOOLS[tool_name](**kwargs)
    print(result)


if __name__ == "__main__":
    if "--cli" in sys.argv:
        cli_mode()
    else:
        import asyncio
        asyncio.run(server.run_stdio_async())
