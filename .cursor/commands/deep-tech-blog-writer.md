# Deep-Tech Blog & X Article Writer Run

1. Select the primary writing archetype (or explicit blend):
   - **Archetype 1 (Sayak Paul & PyTorch Blog):** Optimization Ladder — 3-bullet TL;DR + latency/VRAM delta, bottleneck profiling (`torch.compile`, regional compile, quantization, offloading), diff-highlighted code blocks, and a closing Pareto table.
   - **Archetype 2 (Andrej Karpathy & Aritra Roy Gosthipaty):** Paper-to-Tensor Pedagogy — inspect data/objective first, write an atomic tensor-transformation list before code, and provide deterministic, shape-annotated (`# (B, N, D)`) minimal PyTorch with intermediate visual/numerical sanity checks.
   - **Archetype 3 (Merve Noyan & Hugging Face Blog):** Ecosystem Taxonomy & Onboarding — group model releases into a functional taxonomy table, provide a zero-friction runnable snippet, and state when to fine-tune (`pt`) vs. use out-of-the-box (`mix`/`instruct`).
   - **Archetype 4 (Yann LeCun, Anastasia Marchenkova & High-Signal X Articles):** Dialectical Paradigm Critique + "Read the Fine Print" — contrast mathematical failure modes of prevailing paradigms (e.g., compounding autoregressive error vs. JEPA representation prediction) and audit hardware reality (QRAM/data loading, logical-to-physical qubit overhead, gate depth, transpilation).
2. Draft the headline and `> **TL;DR**` block in the first 5 lines with concrete metrics or a falsifiable thesis (zero generic AI throat-clearing).
3. Construct the tabular/visual anchors first (Taxonomy matrix, Atomic Tensor list, or Pareto Benchmark Ladder).
4. Execute **Step 2.5 ("Read the Fine Print" Gate)**: document recompilation triggers, memory ceilings, PCIe transfer penalties, or physical hardware routing limits.
5. Verify every code block compiles/runs and uses either `+` diff highlights or inline tensor shape comments.

Apply `deep-tech-blog-writer`, `scientific-research-writer`.
