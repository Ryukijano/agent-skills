# Gyanateet Automation Starter Kit

This kit contains a practical first version of the workflow automations discussed:

1. Daily Research Radar
2. GitHub Issue Triage
3. Experiment Report Generator
4. Paper Reading Queue
5. Meeting/Event Briefing
6. Inbox-to-Tasks
7. Weekly Personal Review

It is designed around GitHub Actions + n8n + Microsoft 365/Power Automate + Copilot Studio.

## Quick start

### A. GitHub Actions
Copy files from `github-actions/workflows/` into your repository under `.github/workflows/`.

Recommended repository secrets:

- `OPENAI_API_KEY` or your preferred LLM provider key
- `SLACK_WEBHOOK_URL` or Teams webhook if used
- `NOTION_API_KEY` if using Notion
- `ZOTERO_API_KEY` if using Zotero

### B. n8n
Import JSON files from `n8n-workflows/` into n8n.

Before enabling them:

- Replace placeholder credentials.
- Replace destination URLs.
- Add API keys in n8n Credentials, not hard-coded nodes.
- Keep destructive actions disabled until tested.

### C. Power Automate
Use the specifications in `power-automate/` to recreate flows in Power Automate.
These are intentionally written as build specs because Power Automate import packages require environment-specific connection references.

### D. Copilot Studio
Use the instruction files in `copilot-studio/` to create your personal research/engineering assistant.

## Safety defaults

- Generated emails/messages are drafted, not sent.
- AI PRs are opened for review, not merged.
- File deletion is disabled.
- Weekly review is read-only.
- Inbox/task extraction should require approval for ambiguous commitments.

## Research reading lists

Curated paper lists for Gyanateet's research areas:

- **[RL Reading List](docs/rl-reading-list.md)** — 21 papers covering PPO → GRPO → 
  DAPO → REPO, RL from scratch (AlphaZero, RPT), diversity/mode collapse prevention 
  (DARLING, GAPO, SetPO), exploration & curiosity (ICM, World Models), and quantum 
  circuit RL (RLVQC, FlowQ-Net, TensorRL-QAS). Organized into 6 tiers from foundations 
  to quantum-specific methods, with connections to DINOv2/V-JEPA2/SSL background.

- **[Physics-Based ML Reading List](docs/physics-ml-reading-list.md)** — 15 papers 
  covering the progression from U-Net surrogates → Fourier Neural Operators → PINNs → 
  AI weather/climate models (GraphCast, FourCastNet, GenCast, NeuralGCM) → graph-based 
  physics simulation (GNS, MPNN). Includes connections to Conditional-GQE, diffusion 
  models, and the UvA DL / Physics-Based Deep Learning course materials.

## Suggested first deployment order

1. GitHub CI and experiment report workflow.
2. Daily research radar in n8n.
3. Inbox-to-tasks in Power Automate.
4. Weekly review.
5. Copilot Studio research assistant.
