---
name: deep-tech-blog-writer
description: >-
  Write high-signal deep-tech blog posts, engineering tutorials, and X long-form
  articles by distilling the signature writing styles of Sayak Paul & PyTorch Blog
  (Optimization Ladder), Andrej Karpathy & Aritra Roy Gosthipaty (Paper-to-Tensor
  Pedagogy), Merve Noyan & Hugging Face Blog (Ecosystem Taxonomy & Onboarding),
  Yann LeCun (Dialectical Paradigm Critique), and Anastasia Marchenkova ("Read the
  Fine Print" Hardware Reality Checks).
---

# Deep-Tech Blog & X Article Writer

## Description

Plan, structure, and draft high-signal technical blog posts, runnable developer tutorials, and long-form X articles across AI/ML, computer vision, systems optimization, and quantum computing. Replaces generic AI filler with four battle-tested practitioner archetypes distilled from Sayak Paul, PyTorch Developer Blogs, Andrej Karpathy, Aritra Roy Gosthipaty, Merve Noyan, Hugging Face Blogs, Yann LeCun, and Anastasia Marchenkova.

## When to use

- Drafting or refactoring an engineering deep-dive, optimization guide, model release post, paper walkthrough, or long-form X article.
- Turning benchmark logs, profiling traces (`torch.compile`, quantization, CUDA kernels), or research code into a practitioner narrative.
- Explaining an architectural paradigm shift (e.g., World Models/JEPA vs. autoregressive token prediction) or auditing deep-tech/quantum claims against physical hardware constraints.

## Usage

- **Select a primary Archetype (or explicit blend) before writing prose** so the post has a clear structural spine.
- **Lead with concrete numbers or a falsifiable thesis** in the first 5 lines—never open with generic historical throat-clearing ("In recent years, AI has grown rapidly...").
- **Enforce shape-annotated, minimal diffs and runnable snippets** where every code block either shows exact `+` diff lines or inline tensor dimensions `# (B, N, D)`.
- **Audit every theoretical speedup or capability claim against "The Fine Print"** (compile warmup, PCIe transfer overhead, dynamic shape recompiles, or logical-to-physical qubit ratios).

---

## The Four Signature Archetypes

### Archetype 1: The Optimization Ladder (Sayak Paul & PyTorch Blog Style)
Best for: Systems performance, `torch.compile`, quantization (`torchao`, FP8/NVFP4, NF4), memory offloading, and kernel fusion.
- **Opening Hook:** A `> **TL;DR**` callout box stating the exact speedup (`1.5x–2.4x`), peak VRAM drop (`33.0 GB -> 14.2 GB`), target hardware (`H100` / `RTX 4090` / `GB10`), and quality retention.
- **Audience Split:** Explicitly state what *Model Authors* vs. *Practitioners/Users* will take away in 2 bullets.
- **The Rung-by-Rung Climb:**
  1. *Baseline & Bottleneck:* Measure eager BF16 execution and identify whether the workload is compute-bound, memory-bandwidth-bound, or framework-overhead-bound.
  2. *Rung 1 — Memory & Offloading:* Show one-line or minimal-diff memory wins (e.g., CPU/group offloading, `channels_last`) and honestly note any latency trade-off.
  3. *Rung 2 — Quantization Backends:* Introduce weight-only or dynamic activation quantization (`autoquant`, `int4_weight_only`, `fp8_e4m3`), contrasting perceptual quality vs. memory after loading vs. peak runtime VRAM.
  4. *Rung 3 — Compilation & Regional Compile:* Layer `torch.compile(mode="max-autotune", fullgraph=True)` or `compile_repeated_blocks()` to slash cold-start compile latency (e.g., `67s -> 9.6s`) and handle resolution changes via `dynamic=True`.
- **Closing Artifact:** A single **Pareto Summary Table** (`Strategy Combination | Cold Compile (s) | Latency (s) | Peak VRAM (GB)`) plus a link to the reproducible benchmark script.

### Archetype 2: Paper-to-Tensor Pedagogy (Andrej Karpathy & Aritra Roy Gosthipaty Style)
Best for: Architectural deep dives (ViT, SigLIP 2, nanoVLM, attention variants, diffusion schedulers) and "build-it-from-scratch" tutorials.
- **"Become One with the Data/Objective" First:** Before touching `nn.Module`, inspect a single concrete input/output pair and state what representation property is missing (e.g., locality, dense features, aspect-ratio invariance).
- **Atomic Tensor-Transformation List:** Translate the paper's core equation into a numbered sequence of tensor operations *before* showing code:
  1. `Input Image (B, 3, H, W)` -> Unfold into non-overlapping patches `(B, N, 3*P*P)`
  2. Linear projection + learnable positional embedding -> `x: (B, N, D)`
  3. Sigmoid pairwise loss vs. softmax contrastive loss across batch dimension
- **No-Magic Minimal Code:** Write dependency-light PyTorch with deterministic seeds, explicit tensor shape comments on every shape-changing line, and intermediate sanity checks (verifying loss at initialization $= -\ln(1/C)$ or visualizing attention/patch norms).
- **Incremental Complexity Rule:** Never introduce unverified complexity all at once; add one trick per section and verify its isolated effect.

### Archetype 3: Ecosystem Taxonomy & Practitioner Onboarding (Merve Noyan & Hugging Face Blog Style)
Best for: Fast-moving model family guides (VLMs, SmolVLM, PaliGemma, 3D vision, agentic toolkits) and "which model/tool should I use?" explainers.
- **The Landscape Map:** Group a chaotic zoo of releases into a 3–4 bucket functional taxonomy (e.g., *Pretrained Transfer Checkpoints* vs. *Instruction Mix Checkpoints*, or * Sub-2B Edge VLMs* vs. *OCR/Document Specialists*).
- **Architecture-at-a-Glance Table:** Provide a scannable matrix (`Variant | Vision Encoder | LLM Backbone | Native Resolution | Best Downstream Task`).
- **Zero-Friction Quickstart:** Give a 10-line copy-pasteable inference or FastAPI/Gradio snippet using standard Hub primitives (`AutoProcessor`, `from_pretrained(..., torch_dtype=torch.bfloat16, device_map="auto")`) that runs on a free Colab or single GPU.
- **When to Use / When NOT to Use:** Explicitly tell practitioners when a base `pt` checkpoint requires fine-tuning versus when a `mix`/`instruct` checkpoint works out-of-the-box.

### Archetype 4: Dialectical Paradigm Critique & "Read the Fine Print" (Yann LeCun, Anastasia Marchenkova & High-Signal X Article Style)
Best for: Position pieces, X long-form articles, architectural critiques (World Models/JEPA vs. Autoregressive LLMs), and quantum/deep-tech reality checks.
- **The Dialectical Thesis:** Open with a sharp observation contrasting human/physical efficiency against current paradigm scaling limits (e.g., a teenager learns to drive in 20 hours; autoregressive token prediction compounds errors exponentially as $P(\text{correct}) = (1 - \epsilon)^n$).
- **Generative Pixel/Token Prediction vs. Representation Prediction:** Contrast predicting every unpredictable surface detail (leaves rustling, carpet texture) with predicting in abstract representation space (JEPA / World Models) where irrelevant variance is discarded.
- **Step 2.5 — "Read the Fine Print" Hardware & Complexity Audit (Marchenkova Protocol):**
  Whenever evaluating an algorithm claiming exponential or generational speedup (HHL, Shor's, VQE, PQC migration, or custom silicon kernels), enumerate the 4 hidden physical caveats:
  1. **Data Loading / State Preparation Bottleneck:** Does an $O(\log N)$ runtime assume a non-existent QRAM or zero-cost host-to-device transfer?
  2. **Logical vs. Physical Overhead:** Translate logical circuit/tensor assumptions into physical reality (NISQ gate infidelity, surface/cat-code physical-to-logical qubit ratios, connectivity map routing, Multi-Controlled Toffoli depth vs. ancilla trade-offs).
  3. **Conditioning & Readout Limits:** Does extracting the answer require $O(N)$ repeated shots or well-conditioned uniform matrices?
  4. **Co-Design & Integration Reality:** Frame accelerators (quantum QPUs or specialized NPUs) not as standalone replacements, but as co-designed coprocessors integrated with classical HPC for specific subroutines.

---

## Steps

1. **Lock the Archetype & Audience:** Identify which of the 4 Archetypes (or pair, such as *Archetype 2 + Archetype 1* for a paper-to-compiled-kernel post, or *Archetype 4* for an X article) matches the user's goal.
2. **Draft the Headline & TL;DR Box:** Write a specific, metric- or thesis-driven title and a 3-bullet `> **TL;DR**` block containing the core quantitative delta or architectural thesis.
3. **Build the Visual & Tabular Anchors First:** Draft the Architecture/Taxonomy Markdown table, the Atomic Tensor-Transformation flow, and the final Pareto Benchmark table before filling in narrative paragraphs.
4. **Execute Step 2.5 ("Read the Fine Print" Gate):** Add a dedicated subsection auditing the real-world failure modes: recompilation triggers, CPU-GPU synchronization stalls, OOM boundaries, or physical hardware/transpilation constraints.
5. **Write Shape-Annotated / Diff-Highlighted Code:** Use `diff` blocks (`+` lines) for optimization additions so readers immediately see the 3 lines that matter, and annotate tensor shapes `# (B, T, C, H, W)` on architectural code.
6. **Format for Scannability (Blog or X Article):** Keep paragraphs under 4 sentences, use bold lead-ins for bullet points, and ensure every sub-header states a conclusion rather than a generic topic label (e.g., *"Regional Compilation Cuts Cold-Start 7x (67s -> 9.6s)"* instead of *"Compilation Results"*).

## Code pattern

```python
import dataclasses
from typing import List


@dataclasses.dataclass
class OptimizationRung:
    strategy: str
    compile_time_s: float
    latency_s: float
    peak_vram_gb: float
    notes: str


def render_pareto_markdown_table(
    model_name: str,
    gpu_name: str,
    rungs: List[OptimizationRung],
) -> str:
    """Format an Optimization Ladder Pareto table (Sayak Paul / PyTorch Blog style)."""
    baseline = rungs[0]
    lines = [
        f"### Benchmark Pareto Ladder: `{model_name}` on {gpu_name}",
        "",
        "| Optimization Strategy | Cold Compile (s) | Latency (s) | Speedup | Peak VRAM (GB) | Fine Print / Trade-off |",
        "| :--- | :---: | :---: | :---: | :---: | :--- |",
    ]
    for r in rungs:
        speedup = baseline.latency_s / r.latency_s if r.latency_s > 0 else 1.0
        lines.append(
            f"| {r.strategy} | {r.compile_time_s:.1f} | {r.latency_s:.2f} | "
            f"**{speedup:.2f}x** | {r.peak_vram_gb:.2f} | {r.notes} |"
        )
    return "\n".join(lines)


if __name__ == "__main__":
    sample_rungs = [
        OptimizationRung("Eager BF16 (Baseline)", 0.0, 6.43, 33.10, "OOMs on 24GB consumer GPUs"),
        OptimizationRung("+ Model CPU Offload", 0.0, 21.50, 22.70, "Fits 24GB; PCIe transfer penalty"),
        OptimizationRung("+ Regional compile_repeated_blocks", 9.6, 4.28, 33.10, "7x faster compile vs full compile (67s)"),
        OptimizationRung("+ TorchAO autoquant + compile", 11.2, 3.48, 14.94, "dynamic=True avoids resolution recompiles"),
    ]
    print(render_pareto_markdown_table("FLUX.1-dev", "NVIDIA H100 80GB", sample_rungs))
```

## Tuning notes

- **Kill AI throat-clearing:** Delete phrases like *"In the rapidly evolving landscape of..."*, *"Let's dive deep into..."*, *"It is important to note that..."*, and *"Unleashing the power of..."*. Start directly with the bottleneck, the tensor shape, or the benchmark table.
- **Diff blocks over walls of boilerplate:** When showing how to optimize an existing pipeline (Diffusers, Transformers, vLLM), use ` ```diff ` fenced blocks highlighting the exact `+` lines added, matching Sayak Paul's signature style.
- **Always separate Cold Compile vs. Warm Steady-State:** Never report `torch.compile` or Triton kernel speedups without stating the first-iteration compilation cost and how `compile_repeated_blocks` or AoT caching mitigates it.
- **Logical vs. Physical honesty in Quantum/Hardware posts:** Never quote logical qubit counts (e.g., 4,000 qubits for RSA-2048) without immediately stating the physical qubit overhead required for error correction, gate fidelity limits, and circuit depth constraints.

## Verification

1. **First-5-Lines Audit:** Confirm the draft opens with a concrete `> **TL;DR**` containing quantitative metrics or a falsifiable architectural thesis.
2. **Code & Shape Check:** Verify that every architectural snippet includes inline `# (B, ...)` tensor shape comments and every optimization snippet includes a `diff` block or Pareto table row.
3. **Fine-Print Check:** Confirm at least one subsection explicitly documents when the method degrades, recompiles, OOMs, or hits state-preparation / hardware-routing bottlenecks.

## References

- https://pytorch.org/blog/torch-compile-and-diffusers-a-hands-on-guide-to-peak-performance/
- https://huggingface.co/blog/diffusers-quantization
- https://huggingface.co/blog/siglip2
- https://huggingface.co/blog/nanovlm
- https://karpathy.github.io/2019/04/25/recipe/
- https://www.amarchenkova.com/posts/quantum-machine-learning-aaronson
- https://openreview.net/forum?id=BZ5a1r-kVsf
