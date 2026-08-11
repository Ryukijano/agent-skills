---
name: huggingface-hub
description: >-
  Upload models, datasets, and Spaces to Hugging Face Hub. Use when publishing models, creating datasets, deploying Gradio demos, or managing HF repositories.
---

# Hugging Face Hub Operations

## Overview
Guide for publishing and managing models, datasets, and demos on the Hugging Face Hub.

## Setup
```bash
# Install HF CLI
pip install huggingface_hub

# Login (get token from huggingface.co/settings/tokens)
hf auth login
# or: export HF_TOKEN=hf_your_token
```

## Upload a Model
```bash
# Create repo
hf repo create my-model --type model --public

# Upload folder
hf upload my-model ./model_weights/ --commit-message "Initial upload"

# Upload single file
hf upload my-model ./model.pt model.pt
```

## Upload a Dataset
```bash
# Create dataset repo
hf repo create my-dataset --type dataset --public

# Upload data
hf upload my-dataset ./data/ --commit-message "Add dataset files"
```

## Create a Gradio Space
```bash
# Create Space
hf repo create my-demo --type space --space-sdk gradio --public

# Upload app
hf upload my-demo ./app/ --commit-message "Initial app"
```

## MCP Integration
The Hugging Face MCP Server is configured in all agent configs:
- Search models: "Find Qwen 3 quantizations on Hugging Face"
- Explore datasets: "Show datasets about surgical video"
- Find Spaces: "Find a Space that can transcribe audio"
- Search papers: "Find recent papers on vision-language models"

## HF Skills Available
- `hf-cli`: Full Hub CLI operations
- `huggingface-datasets`: Dataset Viewer API
- `huggingface-llm-trainer`: TRL training on HF Jobs
- `huggingface-vision-trainer`: Vision model training
- `huggingface-community-evals`: Model evaluation
- `huggingface-trackio`: Experiment tracking
- `huggingface-papers`: Paper lookup
- `huggingface-paper-publisher`: Publish papers
- `huggingface-gradio`: Build Gradio demos
- `transformers-js`: Run ML in JavaScript
- `huggingface-best`: Find best models for tasks
- `huggingface-tool-builder`: Build HF API scripts

## Reference Files
- HF Skills: `.cursor/skills/hf-cli/`, `.cursor/skills/huggingface-*/`
- HF MCP: configured in `~/.cursor/mcp.json`, `~/.config/devin/mcp_config.json`, etc.

