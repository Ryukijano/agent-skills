---
name: scientific-research-writer
description: >-
  Structure, draft, and refactor scientific papers, arXiv preprints, ablation
  studies, and Google Research-style companion posts using the Contribution Triad
  (Bottleneck-Mechanism-Ablation), Visual Inverted Pyramid, strict one-to-one
  mathematical notation, and Dialectical Paradigm Framing.
---

# Scientific Research & Paper-to-Blog Writer

## Description

Structure, write, and revise peer-reviewed machine learning / scientific manuscripts (NeurIPS, ICML, ICLR, CVPR, MICCAI, Nature-family venues), arXiv preprints, and Google Research-style companion blog announcements. Enforces the Contribution Triad (*Bottleneck–Mechanism–Ablation*), two-part Hero Teaser figure design, bijective mathematical notation, hypothesis-driven ablation tables, and dialectical positioning against prevailing paradigms.

## When to use

- Drafting or revising an Abstract, Introduction, Related Work, Methodology, or Experiments/Ablations section for a research paper or technical report.
- Translating a dense LaTeX manuscript into a visual, accessible Google Research-style companion blog post or project page (`index.html` / Markdown).
- Auditing a draft manuscript for vague claims, inconsistent mathematical symbols, weak "strawman" related work, or unmotivated ablation tables.

## Usage

- **Lock the Contribution Triad before drafting prose:** Every paper and research post must explicitly bind (1) the *Precise Failure Mode / Bottleneck*, (2) the *Core Algorithmic/Physical Mechanism*, and (3) the *Decisive Ablation Proof*.
- **Design the Visual Inverted Pyramid first:** Specify the two-part Hero Teaser Figure (Left: prior paradigm failure mode; Right: proposed mechanism + Pareto win) before writing the Introduction.
- **Maintain a strict 1-to-1 Symbol-to-Concept Ledger:** Never overload a mathematical symbol across sections or introduce an equation without grounding its tensor dimensions and physical intuition in the immediately adjacent sentence.
- **Write falsifiable, question-driven Ablation sub-headers:** Frame every experimental subsection around a specific scientific question rather than a generic setup label.

---

## Core Architecture & Steps

### Step 1: Lock the Contribution Triad & Abstract (5-Sentence Blueprint)
Before writing section prose, define the **Contribution Triad** and compress it into a 5-sentence Abstract (150–220 words):
1. **Domain & High-Stakes Context (1 sentence):** State the concrete scientific or engineering task and why it matters now.
2. **The Fundamental Bottleneck (1 sentence):** State *why* existing approaches fail mathematically or physically (e.g., *"Autoregressive pixel-level world models waste model capacity predicting stochastic high-frequency texture, causing compounding rollout drift over long horizons"*—never *"Existing methods are suboptimal"*).
3. **The Proposed Mechanism (1–2 sentences):** Name the method and state the exact architectural, objective, or hardware-co-design mechanism that resolves the bottleneck.
4. **The Decisive Empirical Proof (1 sentence):** Report the primary benchmark delta, hardware efficiency gain (latency/VRAM/FLOPs), and the key ablation finding that proves the mechanism—not incidental tuning—drove the gain.
5. **Broader Implication / Artifact Release (1 sentence):** State what new capability this unlocks and what open artifacts (code, weights, dataset) are released.

### Step 2: The Visual Inverted Pyramid & Hero Teaser Figure (Google Research Style)
Whether writing a formal paper or a Google Research companion post, readers scan figures before reading paragraphs:
- **Two-Part Hero Teaser (Figure 1):**
  - **Panel A (The Conflict / Failure Mode):** Visually contrast the prevailing baseline's failure mode (e.g., blurry pixel-space rollouts, recompilation spikes, or deep transpiled quantum circuit depth) against your method on a single representative example.
  - **Panel B (The Pareto Win / Mechanism):** Plot performance vs. compute/memory/latency (or show the architectural data-flow delta) so a reader understands the core contribution in 10 seconds without reading the main text.
- **Self-Contained Captions:** Every figure and table caption must follow a 3-part rule: **(1) What is shown** (axes, units, model variants), **(2) How to read it** (visual cue, e.g., *"Lower and further left is better"*), and **(3) The takeaway message** (the exact empirical conclusion).

### Step 3: Dialectical Introduction & Non-Strawman Related Work (LeCun & Formal Venue Style)
- **Introduction Funnel (4 Paragraphs + Contribution Bullets):**
  1. *Paragraph 1 (The Promise & The Wall):* Contrast what the ideal physical/cognitive system achieves with the wall current methods hit.
  2. *Paragraph 2 (Root-Cause Diagnosis):* Diagnose the mathematical or systems root cause of that wall (e.g., compounding autoregressive error, quadratic token complexity, or NISQ state-preparation overhead).
  3. *Paragraph 3 (Our Insight & Mechanism):* Introduce the core insight and walk through how the proposed architecture/objective directly eliminates the root cause, forward-referencing `Figure 1` and `Section 3`.
  4. *Paragraph 4 (Verifiable Contributions List):* Provide 3–4 bulleted contributions where each bullet starts with an active verb (**Propose**, **Derive**, **Demonstrate**, **Release**) and links to a specific section, theorem, or table.
- **Dialectical Related Work (No Laundry Lists):**
  - Ban chronological sentences of the form *"Author (Year) did X. Author (Year) did Y."*
  - Group prior work into **2–3 competing paradigms**, state each paradigm's best strength charitably, identify the exact structural trade-off it cannot resolve, and position your work as resolving that tension.

### Step 4: Bijective Mathematical Notation & Data-Flow Methodology
- **The Symbol Ledger Rule:** Every scalar ($x$), vector ($\mathbf{x}$), matrix ($\mathbf{X}$), tensor ($\mathcal{X} \in \mathbb{R}^{B \times T \times D}$), and operator must have a 1-to-1 definition upon first use. Never reuse $T$ for both sequence length and diffusion timesteps, or $k$ for both top-$k$ routing and kernel size.
- **Intuition -> Formulation -> Tensor Reality:** For every major equation:
  1. State in plain English *what* the term computes and *why* its functional form is chosen.
  2. Present the numbered equation with clean punctuation.
  3. Immediately specify the input/output tensor shapes, computational complexity $O(\cdot)$, and boundary behavior.

### Step 5: Hypothesis-Driven Ablation Suite & Honest Limitations
- **Question-Driven Experimental Subsections:** Title each analysis subsection with the hypothesis being tested (e.g., *"§4.3 Does Representation-Space Prediction Prevent Rollout Drift?"* or *"§4.4 Ablation: Regional Compilation vs. Quantization Overhead"*).
- **The Cumulative Ablation Ladder:** Show a table starting from the stripped-down baseline and adding one component per row (`Baseline -> + Objective A -> + Architectural Module B -> + Full Method`), plus a "leave-one-out" check if components interact.
- **Calibrated Limitations & Fine Print:** Dedicate an explicit subsection to failure cases, out-of-distribution breakdown regimes, hardware memory ceilings, or physical assumptions. Reviewers reward preemptive, quantified honesty.

### Step 6: Paper-to-Companion-Blog Translation (Google Research Blog Mode)
When asked to turn a paper into a research blog post:
- Replace the formal Abstract with a conversational **3-bullet Summary + Hero GIF/Teaser**.
- Replace the Related Work section with a 1-paragraph visual comparison of **Prior Paradigm vs. Our Approach**.
- Replace proof appendices with **interactive/visual intuition panels** (feature visualizations, failure-vs-success side-by-sides, and a clean Pareto chart).
- Conclude with a **Quick Links & BibTeX** footer linking to the paper, GitHub repo, Hugging Face weights/demo, and citation block.

---

## Code pattern

```python
import re
from collections import defaultdict
from typing import Dict, List


def audit_scientific_draft(tex_or_md: str) -> Dict[str, object]:
    """Audit a manuscript draft for laundry-list citations, passive bloat, and notation hygiene."""
    paragraphs = [p.strip() for p in re.split(r"\n\s*\n", tex_or_md) if p.strip()]

    # 1. Detect "Author (Year) did X" laundry-list sentences in Related Work
    laundry_pattern = re.compile(
        r"\b([A-Z][a-z]+ et al\.|\\citet\{[^}]+\})\s+(propose[ds]?|introduce[ds]?|use[ds]?|show(?:ed|s)?)\b"
    )
    laundry_hits = [p[:120] + "..." for p in paragraphs if len(laundry_pattern.findall(p)) >= 3]

    # 2. Detect vague/unquantified claims
    vague_phrases = [
        "significantly outperforms",
        "vastly superior",
        "achieves state-of-the-art",
        "novel framework",
        "dramatically reduces",
    ]
    unquantified_hits: List[str] = []
    for p in paragraphs:
        for phrase in vague_phrases:
            if phrase in p.lower() and not re.search(r"\d+(\.\d+)?(%|x|\s*dB|\s*ms|\s*GB)", p):
                unquantified_hits.append(f"'{phrase}' without number in: {p[:90]}...")

    # 3. Extract inline math symbols to check for definition hygiene
    math_spans = re.findall(r"\$([^$]+)\$", tex_or_md)
    symbol_counts: Dict[str, int] = defaultdict(int)
    for span in math_spans:
        for sym in re.findall(r"\\[a-zA-Z]+|[a-zA-Z]", span):
            symbol_counts[sym] += 1

    return {
        "paragraph_count": len(paragraphs),
        "laundry_list_paragraphs": laundry_hits,
        "unquantified_claims": unquantified_hits,
        "top_math_symbols": sorted(symbol_counts.items(), key=lambda kv: -kv[1])[:10],
    }


if __name__ == "__main__":
    sample_draft = (
        "Smith et al. proposed a vision encoder. Jones et al. introduced patch merging. "
        "Lee et al. used contrastive loss for alignment.\n\n"
        "Our novel framework significantly outperforms prior baselines on dense prediction."
    )
    print(audit_scientific_draft(sample_draft))
```

## Tuning notes

- **Ban unquantified superlatives:** Never write *"significantly faster"* or *"substantial improvement"* without parenthetically citing the exact delta (`+4.2 mAP`, `2.1x lower latency`, `p < 0.001`).
- **One claim, one pointer:** Every high-level claim in the Introduction must point to a specific Figure, Table, Equation, or Section (`see Table 2`, `Eq. 4`).
- **Table design (`booktabs` / Markdown):** Bold the best result, underline the second-best, include `± std` across $N \ge 3$ seeds when variance is non-trivial, and always include a column for parameter count, FLOPs, or wall-clock latency so accuracy gains aren't hiding compute inflation.
- **Combine with `deep-tech-blog-writer`:** When writing a launch post or X thread for a new paper, use `scientific-research-writer` Step 1–2 to lock the Contribution Triad and Hero Figure, then switch to `deep-tech-blog-writer` Archetype 1 or 2 for the code and systems walkthrough.

## Verification

1. **Contribution Triad Check:** Verify the Abstract and Introduction clearly state the *Bottleneck*, *Mechanism*, and *Decisive Ablation* with concrete metrics.
2. **Notation & Figure Audit:** Run `audit_scientific_draft` (or inspect manually) to confirm zero laundry-list Related Work paragraphs, zero unquantified superlatives, and self-contained 3-part captions on every figure/table.
3. **Ablation Completeness:** Confirm the experimental section answers at least 3 explicit scientific questions and isolates each proposed component in a cumulative ablation table.

## References

- https://research.google/blog/feature-visualization/
- https://distill.pub/2017/feature-visualization/
- https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1005619
- https://www.gatsby.ucl.ac.uk/~pel/misc/gopen_swan.pdf
- https://openreview.net/forum?id=BZ5a1r-kVsf
- https://huggingface.co/blog/siglip2
