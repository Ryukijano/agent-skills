# MCP Servers and Tools Masterplan

Build custom MCP servers and CLI tools that work both as direct terminal commands AND as MCP tools for AI agents (Cursor, Devin, Claude, Windsurf). Stop pasting the same commands and output into every conversation.

---

## Architecture: Dual CLI + MCP Interface

Every MCP server in this plan has two interfaces:

1. **CLI mode** — you run `python server.py --cli <tool> <args>` from the terminal
2. **MCP mode** — AI agents call the same tools via the Model Context Protocol

Same code, same logic, dual interface. This means:
- You can use tools directly when you know what you want
- Agents can call the same tools when you're working through them
- No duplicated logic

### Technology Stack

| Component | Choice | Why |
|-----------|--------|-----|
| Language | Python 3.13 | Already installed, mcp SDK works, your scripts are Python |
| MCP SDK | `mcp` 2.0.0 (official) | Already installed, has `MCPServer` with `@tool()` decorator |
| Transport | stdio | Simplest for local tools, works with all agents |
| Package manager | `uv` | Already installed, fast, handles venvs |
| Testing | MCP Inspector | `npx @modelcontextprotocol/inspector` |

### Directory Structure

```
mcp-tools/
├── MASTERPLAN.md              # This file
├── README.md                  # Setup and usage guide
├── install_all.sh             # Register all servers with all agents
├── servers/
│   ├── cuda_profiling/        # MCP 1: nsys/ncu/compute-sanitizer wrappers
│   │   ├── server.py
│   │   ├── tools.py
│   │   └── README.md
│   ├── dgx_monitor/           # MCP 2: GPU/memory/Docker/conda monitoring
│   │   ├── server.py
│   │   ├── tools.py
│   │   └── README.md
│   ├── endosight_pipeline/    # MCP 3: Endosight 3D pipeline operations
│   │   ├── server.py
│   │   ├── tools.py
│   │   └── README.md
│   └── research_workflow/     # MCP 4: arxiv/papers/bibtex/experiments
│       ├── server.py
│       ├── tools.py
│       └── README.md
└── configs/                   # MCP config JSON for each agent
    ├── cursor.json
    ├── windsurf.json
    ├── claude.json
    └── devin.json
```

---

## MCP 1: CUDA Profiling Server

Wrap nsys, ncu, and compute-sanitizer as MCP tools so any agent can profile kernels without you writing the commands each time.

### Tools

| Tool | What it does | CLI equivalent |
|------|-------------|----------------|
| `profile_nsys` | Run Nsight Systems profile, return report path | `nsys profile -o report <cmd>` |
| `profile_ncu` | Run Nsight Compute profile with metric sets | `ncu --set full -o report <cmd>` |
| `memcheck` | Run compute-sanitizer memcheck | `compute-sanitizer --tool memcheck <cmd>` |
| `racecheck` | Run compute-sanitizer racecheck | `compute-sanitizer --tool racecheck <cmd>` |
| `initcheck` | Run compute-sanitizer initcheck | `compute-sanitizer --tool initcheck <cmd>` |
| `parse_ncu_report` | Parse ncu report, extract key metrics | `ncu --import report --csv` |
| `parse_nsys_report` | Parse nsys report, extract timeline summary | `nsys stats report` |
| `gpu_info` | Get GPU compute capability, memory, SM count | `nvidia-smi --query-gpu=...` |
| `compile_kernel` | Compile .cu with nvcc, correct flags for SM121 | `nvcc -arch=sm_121 -lineinfo ...` |
| `dump_sass` | Dump SASS for a compiled binary | `cuobjdump --dump-sass` |
| `dump_ptx` | Dump PTX for a compiled binary | `cuobjdump --dump-ptx` |

### Why You Need This

Every time you or an agent wants to profile a kernel, you write:
```bash
ncu --set full --target-processes all -o /tmp/profile python my_script.py
ncu --import /tmp/profile --csv --page details | head -100
```

With this MCP, the agent just calls `profile_ncu` with the command and gets back parsed metrics. You can also run it directly:
```bash
python servers/cuda_profiling/server.py --cli profile_ncu --cmd "python my_script.py"
```

---

## MCP 2: DGX Spark Monitor Server

Real-time monitoring of your DGX Spark's GPU, memory, Docker containers, and conda environments.

### Tools

| Tool | What it does | CLI equivalent |
|------|-------------|----------------|
| `gpu_status` | Current GPU utilization, memory, temperature | `nvidia-smi` |
| `gpu_memory_detail` | Per-process GPU memory breakdown | `nvidia-smi --query-compute-apps=...` |
| `system_memory` | System RAM usage (unified memory!) | `free -h` + `/proc/meminfo` |
| `disk_usage` | Disk space on key partitions | `df -h` |
| `docker_ps` | Running containers with GPU assignments | `docker ps --format ...` |
| `docker_gpu_stats` | Per-container GPU usage | `nvidia-smi` + `docker inspect` |
| `conda_envs` | List conda environments with sizes | `conda env list` + du |
| `conda_packages` | List packages in an environment | `conda list -n <env>` |
| `nvdec_status` | NVDEC engine utilization | `nvidia-smi --query-gpu=encoder.stats...` |
| `top_gpu_processes` | Top processes by GPU memory | `nvidia-smi` + `ps` |
| `kill_gpu_process` | Kill a process using GPU memory | `kill -9 <pid>` |
| `bandwidth_test` | Quick memory bandwidth test | Custom CUDA script |

### Why You Need This

Agents constantly ask "what's using GPU memory?" or "is the GPU free?". Instead of running nvidia-smi and pasting output, the agent calls `gpu_status` and gets structured data back.

---

## MCP 3: Endosight Pipeline Server

Expose Endosight 3D pipeline operations as MCP tools so agents can trigger and monitor pipeline runs directly.

### Tools

| Tool | What it does |
|------|-------------|
| `run_reconstruction` | Start a 3D reconstruction job |
| `run_crop` | Run polyp crop extraction |
| `run_qa` | Run QA checks on a reconstruction |
| `run_video_export` | Export reconstruction as video |
| `pipeline_status` | Check status of running pipeline jobs |
| `pipeline_logs` | Get logs from a pipeline job |
| `list_clips` | List available endoscopy clips |
| `list_reconstructions` | List completed reconstructions |
| `validate_reconstruction` | Run validation checks on a reconstruction |
| `get_reconstruction_stats` | Get point count, mesh stats, file sizes |

### Why You Need This

Your `endosight_project` has many scripts. Instead of agents figuring out which script to run and with what arguments, they call the MCP tool with a clean interface.

---

## MCP 4: Research Workflow Server

ArXiv search, paper digestion, BibTeX management, experiment tracking, and reproducibility bundling.

### Tools

| Tool | What it does |
|------|-------------|
| `search_arxiv` | Search arXiv by keywords, return titles/abstracts |
| `get_paper` | Download paper PDF + metadata by arXiv ID |
| `add_to_bibtex` | Add a paper to your BibTeX file |
| `search_bibtex` | Search your BibTeX database |
| `list_experiments` | List experiment directories with timestamps |
| `create_experiment` | Create a new experiment directory with metadata |
| `log_experiment` | Append to an experiment's log file |
| `create_repro_bundle` | Package code + data manifest + env for reproducibility |
| `search_semantic_scholar` | Search Semantic Scholar API |
| `get_citations` | Get citation count and citing papers |

### Why You Need This

You already have skills for `digest-paper`, `explore-sota`, `repro-bundle`, etc. This MCP exposes the underlying operations as tools that any agent can call, not just the skill-enabled ones.

---

## NVIDIA's Existing MCP Servers (Install First)

### 1. NVIDIA CUDA MCP Server (Hosted)

Gives AI agents access to up-to-date CUDA documentation and code examples. One-line setup:

```bash
# For Claude Code
claude mcp add --scope user --transport http nvidia-cuda-docs https://api.copilot.nsight.ngc.nvidia.com/mcp/cuda-docs

# For other agents, add to their mcp config:
{
  "mcpServers": {
    "nvidia-cuda-docs": {
      "url": "https://api.copilot.nsight.ngc.nvidia.com/mcp/cuda-docs"
    }
  }
}
```

Requires NVIDIA Developer account (free). Sign in on first connection.

### 2. Nsight Copilot Blueprint (Self-Hosted on DGX Spark)

A self-hosted CUDA AI backend that runs locally on your DGX Spark. No prompts or code sent to external services.

**Requirements:**
- DGX Spark (you have this) — the reference setup
- Docker with Compose v2
- NVIDIA Container Toolkit
- 200 GB free disk space
- NGC API key

**Setup:**
```bash
git clone https://github.com/NVIDIA-AI-Blueprints/nsight-copilot
cd nsight-copilot
# Follow docs/deploy-docker-self-hosted.md
```

Provides:
- CUDA-aware chat in VS Code and Nsight Compute
- Code generation for optimized CUDA kernels
- Interactive guidance on memory access patterns
- RAG over authoritative CUDA documentation
- All running locally on your GB10

### 3. Anaconda MCP Server (Optional)

Exposes conda environment management to AI agents:

```bash
pip install anaconda-mcp
anaconda login
anaconda mcp terms accept
anaconda mcp setup  # auto-detects clients
```

---

## How to Build an MCP Server (Quick Reference)

### Minimal Server (15 lines)

```python
#!/usr/bin/env python3
"""Minimal MCP server with CLI mode."""
import sys
from mcp.server import MCPServer

server = MCPServer("my-server", "1.0.0")

@server.tool()
def add(a: int, b: int) -> int:
    """Add two numbers."""
    return a + b

if __name__ == "__main__":
    if "--cli" in sys.argv:
        # CLI mode: python server.py --cli add 3 5
        tool_name = sys.argv[sys.argv.index("--cli") + 1]
        args = sys.argv[sys.argv.index("--cli") + 2:]
        # Dispatch to tool function
        ...
    else:
        # MCP mode: stdio transport for agents
        import asyncio
        from mcp.server.stdio import stdio_server
        asyncio.run(server.run_stdio_async())
```

### Register with Agents

Add to each agent's MCP config:

```json
{
  "mcpServers": {
    "my-server": {
      "command": "python3",
      "args": ["/absolute/path/to/server.py"]
    }
  }
}
```

**Agent config file locations:**

| Agent | Config file |
|-------|------------|
| Cursor | `~/.cursor/mcp.json` |
| Windsurf | `~/.codeium/windsurf/mcp_config.json` |
| Claude Code | `~/.claude/mcp.json` |
| Devin | `~/.config/devin/mcp_config.json` |
| Gemini | `~/.gemini/config/mcp_config.json` |

### Test with MCP Inspector

```bash
npx @modelcontextprotocol/inspector python3 /path/to/server.py
```

Opens a web UI where you can call tools and see responses.

---

## Implementation Order

1. **NVIDIA CUDA MCP Server** — one-line setup, immediate value
2. **DGX Spark Monitor MCP** — simplest to build, most useful day-to-day
3. **CUDA Profiling MCP** — wraps nsys/ncu, needed for Blackwell labs
4. **Endosight Pipeline MCP** — requires understanding your pipeline scripts
5. **Research Workflow MCP** — wraps existing skills' operations
6. **Nsight Copilot Blueprint** — deploy on DGX Spark (heavier setup)

---

## Resources

- [MCP Specification](https://modelcontextprotocol.io/docs/learn/architecture) — protocol overview
- [Python SDK](https://github.com/modelcontextprotocol/python-sdk) — official Python SDK
- [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk) — official TypeScript SDK
- [MCP Inspector](https://github.com/modelcontextprotocol/inspector) — testing tool
- [PulseMCP Directory](https://www.pulsemcp.com/servers/) — 22,000+ MCP servers
- [MCP Toplist](https://mcptoplist.com/) — ranked server list
- [NVIDIA CUDA MCP Server](https://developer.nvidia.com/nsight-ai) — hosted CUDA docs
- [Nsight Copilot Blueprint](https://github.com/NVIDIA-AI-Blueprints/nsight-copilot) — self-hosted CUDA AI
- [Anaconda MCP](https://github.com/anaconda/anaconda-mcp) — conda environment management
- [FastMCP tutorial](https://blog.jztan.com/how-to-build-an-mcp-server-in-python-step-by-step/) — real server in 100 lines
- [MCP server quickstart](https://github.com/modelcontextprotocol/typescript-sdk/blob/main/docs/server-quickstart.md) — official quickstart
