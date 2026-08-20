| name | biotech-materials-ai-papers |
|------|------|
| description | Index of AI-for-science papers spanning protein/antibody design, genomics, neuroscience imaging, and AI-driven materials discovery. Use when the user asks about protein sequence alignment, antibody generation, RNA interactomes, neuroimaging AI, crystal generation via RL, molecular deep learning, or optical/metasurface computer vision hardware. |

# Biotech, Materials Science & AI-for-Science Paper Index

## Prerequisites

This is a reference-only skill summarizing papers stored in the Drive `Research_and_papers` folder and organized into the `Biotech & Quantum Computing Research` NotebookLM notebook (categorized folders: Genomics, Material Science, Neuroscience, Organic Synthesis, Computational Chemistry).

## Core Rules

- **Cite by DOI suffix** (e.g. `s41587-026-03095-3`) when referencing a specific paper's finding.
- **Never reproduce full abstracts or figures** verbatim — summarize in your own words per copyright policy.
- **Route deep Q&A** to the `Biotech & Quantum Computing Research` NotebookLM notebook, which already has these sources loaded and categorized.

## Reference Papers Indexed

### Genomics / Protein / Structural Biology
| Paper | Key Contribution |
|---|---|
| s41587-026-03095-3 (Nat. Biotech) | FAMSA2 — fast, accurate multiple protein-sequence alignment at scale |
| s41587-026-03187-0 (Nat. Biotech) | Germinal — efficient generation of epitope-targeted antibodies |
| s41592-026-03105-x (Nat. Methods) | Encyclopedic regulatory/functional atlas of RNA interactomes |
| s41594-026-01814-7 (Nat. Struct. Mol. Biol) | Structures of protein folding intermediates on the ribosome |
| s41467-023-42451-8 (Nat. Comms) | Intelligent surgical workflow recognition for endoscopic submucosal dissection — directly relevant to AI-Endo / surgical CV work |

### Neuroscience / Medical Imaging
| Paper | Key Contribution |
|---|---|
| s41591-026-04567-4 (Nat. Medicine) | Learning from routine health-system data builds better neuroimaging AI models |
| s41592-024-02581-3 (Nat. Methods) | Geometric deep learning for interpreting/comparing neural activity across systems |
| s41592-026-03110-0 (Nat. Methods) | Cloud-based microscope enabling 24h+ live neuroimaging with worldwide access |
| s41598-025-88177-z (Sci. Reports) | Predicting temperature-dependent optoelectronic properties of semiconductor defects with equivariant neural networks |

### Materials Science / Computational Chemistry
| Paper | Key Contribution |
|---|---|
| nomura-et-al (npj Comput. Materials) | Allegro-FM — equivariant foundation model for exascale molecular dynamics |
| s41928-025-01416-z (Nat. Electronics) | Materials/device paper (see Drive for full abstract) |
| s42256-026-01216-w (Nat. Machine Intelligence) | Molecular deep learning at the edge of chemical space |
| s42256-026-01262-4 (Nat. Machine Intelligence) | Guiding generative models to uncover diverse/novel crystals via reinforcement learning |
| s41565-026-02197-y (Nat. Nanotechnology) | Optical multistability in a compact microcavity |
| s41586-026-10635-z (Nature) | Optical metasurfaces for general vision processing — relevant to CV hardware acceleration |
| s42484-024-00224-6 | Materials paper (see Drive for full abstract) |
| s41557-026-02166-x (Nat. Chemistry) | Redox-neutral ketone-olefin coupling via mild ketyl-type radical conversion |
| s41557-026-02168-9 (Nat. Chemistry) | Molecular rotation and large polarization in charge-transfer ferroelectric cocrystals |
| s41524-026-02111-z (npj Comput. Materials) | Companion/duplicate publication on semiconductor defect prediction with equivariant NNs, see s41598-025-88177-z |

## Usage Pattern

1. Match the user's question to the relevant paper category (genomics, neuro, materials, chemistry).
2. Summarize findings concisely with citation to the DOI suffix.
3. For deep multi-paper synthesis, direct the user to ask the `Biotech & Quantum Computing Research` NotebookLM notebook directly, since it already has these sources ingested and categorized into folders.
4. If the user's question relates to their AI-Endo colonoscopy/surgical CV project specifically, prioritize `s41467-023-42451-8` and mention the DINO-Endo related source materials already in that Drive folder.

## Related Skills

- `quantum-error-correction-theory` (companion skill for the physics/quantum papers from the same Drive folder)
