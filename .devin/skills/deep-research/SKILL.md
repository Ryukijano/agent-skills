---
name: deep-research
description: Systematic web research and deep reasoning for complex technical questions. Use when investigating unfamiliar APIs, debugging obscure errors, comparing libraries/frameworks, understanding research papers, or making architectural decisions that benefit from external evidence. Covers search strategy, source evaluation, iterative refinement, and synthesis with citations.
---

## Deep Research and Reasoning

### Core principle

**Search is a control loop, not a pipeline.** Don't search once and generate. Formulate → search → evaluate → refine → synthesize. The first query reflects only what you knew before searching; each round surfaces evidence that reshapes what's worth asking next.

### When to search vs. when to reason internally

| Situation | Action |
|-----------|--------|
| Unfamiliar API, library, or framework | **Search** — training data may be stale |
| Obscure error message or crash | **Search** — someone likely hit it before |
| Comparing libraries/approaches | **Search** — need current feature matrices |
| Research paper or method | **Search** — find original + follow-up work |
| Architecture decision with trade-offs | **Search + reason** — gather evidence, then think |
| Code in the repo | **Don't search** — use `code_search` / `grep_search` |
| User preferences or project facts | **Don't search** — check memory DB |
| Simple factual question | **Reason internally** — don't waste tokens on search |
| Subjective or contested topic | **Search cautiously** — more sources can amplify disagreement |

### The search loop

```
1. DECOMPOSE  — Split complex questions into independent sub-queries
2. SEARCH     — Issue queries (broad-to-narrow strategy)
3. EVALUATE   — Filter results: is this source authoritative? relevant? current?
4. IDENTIFY GAPS — What's still unknown? What conflicts with what we have?
5. REFINE     — Reformulate queries targeting specific gaps (not minor variations)
6. REPEAT     — Until gaps are closed or budget is hit
7. SYNTHESIZE — Combine findings with source attribution; flag conflicts
```

### Query formulation strategies

- **Decomposition**: "How do I fix NCCL SIGSEGV on L40S?" → sub-queries: "NCCL SIGSEGV PCIe GPU", "NCCL_P2P_DISABLE L40S", "PyTorch NCCL init_process_group crash", "NCCL version mismatch LD_PRELOAD"
- **Broad-to-narrow**: Start with "DINOv2 surgical video domain adaptation" → narrow to "DINOv2 fine-tuning surgical" → "progressive unfreezing ViT domain adaptation"
- **Gap-driven**: After initial results, target what's missing — "L2-SP regularization vs vanilla fine-tuning catastrophic forgetting"
- **Avoid query lock-in**: Don't rephrase the same query 3 times. If results are poor, reformulate with different terminology or perspective.

### Source evaluation hierarchy

| Source quality | Examples | Trust level |
|----------------|----------|-------------|
| **Official docs** | docs.python.org, pytorch.org, developer.nvidia.com | High — use as ground truth |
| **GitHub issues/PRs** | github.com/pytorch/pytorch/issues | High — real bugs, real fixes |
| **Peer-reviewed papers** | arxiv.org, openreview.net | High for methods, verify recency |
| **Engineering blogs** | engineering blogs from major companies | Medium — well-tested practices |
| **Stack Overflow** |stackoverflow.com | Medium — check upvotes and recency |
| **Random blogs/tutorials** | personal blogs, medium.com | Low — verify against official docs |
| **AI-generated content** | AI summary sites | Very low — verify everything |

### Reading depth: when to fetch full content

- **Snippets are not content** — search results give titles + snippets, not answers
- **Always fetch the top result** before quoting or acting on it
- **Fetch 2-3 sources** for comparisons or contested topics
- **Stop fetching when** you have 3+ consistent authoritative sources agreeing
- **Break-even for delegation**: ~3 fetches. Beyond that, summarize what you have and reason internally.

### Deep thinking protocol

After gathering evidence, before generating code or recommendations:

1. **Restate the problem** in your own words — confirm understanding
2. **List known constraints** — what must be true? what can't change?
3. **Enumerate options** — don't jump to the first solution
4. **Evaluate each option** against evidence gathered — pros, cons, risks
5. **Check for failure modes** — what breaks? what are edge cases?
6. **Decide and justify** — pick the best option, explain why
7. **Identify verification** — how will we know it worked?

### Anti-patterns

| Anti-pattern | Why it fails | Fix |
|--------------|-------------|-----|
| Search once, generate immediately | Misses context, stale info | Use the loop: search → evaluate → refine |
| Fetch 10 pages into main context | Context bloat, loses thread | Summarize after 2-3 fetches; delegate if more needed |
| Quote snippets as facts | Snippets mislead | Fetch the actual page before quoting |
| Over-search simple questions | Wastes tokens and time | Reason internally for known facts |
| Ignore conflicting evidence | Confirmation bias | Flag conflicts explicitly; investigate the discrepancy |
| Query lock-in | Same query rephrased 3x = stagnation | Reformulate with different terminology |
| Overthinking simple code changes | Long CoT hurts simple tasks (SEER paper) | Match reasoning depth to problem complexity |

### Budget management

- **Hard cap**: Set max iterations (3-5 for most tasks, 10+ for deep research)
- **Quality signal**: Stop when gaps are closed, not when budget is exhausted
- **Stagnation detection**: Repeated queries or diminishing result quality = stop
- **Cost awareness**: Multi-agent research uses ~15x tokens of single-turn chat
- **Task-shape matters**: Sequential reasoning tasks degrade with too many parallel searches; parallelizable research tasks benefit from breadth

### Synthesis and output

When presenting research findings:

1. **Lead with the answer** — don't bury the conclusion
2. **Cite sources** — URL + source type (official docs, paper, blog)
3. **Flag uncertainty** — "This is from a 2024 blog, may be outdated" vs "This is from current official docs"
4. **Note conflicts** — "Source A says X, Source B says Y. I trust Source A because..."
5. **Provide actionable next steps** — not just "here's what I found" but "here's what to do"
6. **Distinguish facts from opinions** — "PyTorch 2.7 requires NCCL 2.20+" (fact) vs "L2-SP is better than vanilla fine-tuning" (opinion, needs evidence)

### Integration with coding workflow

Research should feed directly into action:

```
Research → Decision → Implementation → Verification
  ↑                                    |
  └─────── If verification fails ──────┘
```

- After research, write the code or config change immediately
- If the fix doesn't work, re-enter the research loop with the new error as the query
- Save durable findings to memory DB (e.g., "NCCL_P2P_DISABLE=1 required for L40S PCIe nodes")
- Save architectural decisions to DECISIONS.md with research citations

### Quick-reference: search tool selection

| Need | Tool | Why |
|------|------|-----|
| Find a page about X | `search_web` | Don't know the URL |
| Read a specific URL | `read_url_content` | Have the URL, need content |
| Search codebase | `code_search` / `grep_search` | Answer is in the repo |
| Search GitHub repo docs | `mcp0_ask_question` | DeepWiki knows the repo |
| Check package version | `search_web` + official docs | Need current version info |
| Debug an error | `search_web` with error string | Someone likely hit it before |
