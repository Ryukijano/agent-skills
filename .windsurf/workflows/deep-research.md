---
description: Systematic web research and deep reasoning workflow for complex technical questions
---

## Deep Research Workflow

Use this workflow when investigating unfamiliar technologies, debugging obscure errors, comparing approaches, or making evidence-backed architectural decisions.

### Phase 1: Frame the Question

1. **Restate the problem** in your own words. What specifically do you need to know?
2. **Identify what you already know** — check memory DB, codebase, existing configs.
3. **Decompose** complex questions into 2-4 independent sub-questions.
4. **Set a budget**: 3-5 search iterations for most tasks, up to 10 for deep research.

### Phase 2: Search Loop

5. **Issue initial queries** (broad-to-narrow):
   ```
   search_web("broad topic keyword")
   ```
   Start broad, then narrow based on what you find.

6. **Evaluate results**:
   - Is the source authoritative? (official docs > GitHub issues > blogs)
   - Is it current? (Check dates — API docs from 2022 may be wrong for 2025)
   - Does it address the specific sub-question?

7. **Fetch full content** for top 1-2 results:
   ```
   read_url_content("https://docs.example.com/relevant-page")
   ```
   Snippets are not content. Always fetch before quoting.

8. **Identify gaps** — what's still unknown? What conflicts with what you have?

9. **Refine queries** targeting specific gaps (not minor rephrasings):
   - Poor: "NCCL crash" → "NCCL crash GPU" → "NCCL crash GPU error"
   - Good: "NCCL crash" → "NCCL_P2P_DISABLE PCIe GPU fix" → "PyTorch NCCL version mismatch LD_PRELOAD"

10. **Repeat steps 5-9** until gaps are closed or budget is hit.

### Phase 3: Deep Thinking

11. **Restate findings** — summarize what the evidence says.
12. **Enumerate options** — list 2-3 possible approaches.
13. **Evaluate each** against evidence:
    - Does it match official docs?
    - Do others report success with this approach?
    - What are the risks/edge cases?
14. **Check for failure modes**:
    - What breaks at scale?
    - What are version-specific issues?
    - What assumptions might not hold?
15. **Decide and justify** — pick the best option, explain why with citations.

### Phase 4: Act and Verify

16. **Implement** the solution immediately based on research findings.
17. **Verify** — run the code, test the fix, check the output.
18. **If verification fails**: Re-enter the search loop with the new error as the query.
19. **Save durable findings** to memory DB:
    ```
    create_memory(
      Title: "NCCL L40S PCIe workaround",
      Content: "NCCL_P2P_DISABLE=1 required on L40S PCIe-only nodes...",
      Tags: ["nccl", "l40s", "ddp", "pytorch"]
    )
    ```
20. **Save architectural decisions** to `DECISIONS.md` with research citations:
    ```markdown
    ## 2026-06-24: Chose progressive unfreezing over full fine-tuning
    - **Decision**: Unfreeze encoder blocks gradually (2 → 4 → 6 → 12)
    - **Why**: Research showed L2-SP + progressive unfreezing prevents
      catastrophic forgetting (source: https://arxiv.org/abs/...)
    - **Alternatives considered**: Full fine-tune (risk of collapse),
      LoRA-only (insufficient adaptation), frozen encoder (no domain adaptation)
    ```

### When to skip this workflow

- The answer is in the codebase → use `code_search` instead
- The answer is in memory → check system-retrieved memories
- Simple factual question → reason from training data
- User explicitly tells you the answer → don't search
- One-page lookup (docs URL known) → just `read_url_content`, skip the loop

### Search budget guidelines

| Task type | Max iterations | Max fetches | Rationale |
|-----------|---------------|-------------|-----------|
| API/library lookup | 2 | 2 | Usually one official docs page |
| Error debugging | 3 | 3 | Error string + context + fix |
| Library comparison | 4 | 5 | Need feature matrices from multiple sources |
| Research method investigation | 5 | 8 | Papers + blogs + discussions |
| Architecture decision | 5 | 6 | Trade-offs need multiple perspectives |
