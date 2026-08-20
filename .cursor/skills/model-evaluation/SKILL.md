# Model Evaluation & Benchmarking

## Overview
Systematic approach to evaluating ML models: selecting metrics, designing benchmarks, running fair comparisons, and reporting results.

## Evaluation Framework

### 1. Define Evaluation Protocol
- **Metrics**: Choose primary + secondary metrics (e.g., mAP + FPS for detection)
- **Splits**: Train/val/test with no leakage (see `data-management` skill)
- **Statistical significance**: Run 3-5 seeds, report mean ± std
- **Fair comparison**: Same hardware, same data, same training budget

### 2. Metric Selection by Task
| Task | Primary Metrics | Secondary |
|------|----------------|-----------|
| Object Detection | mAP@0.5, mAP@0.5:0.95 | FPS, params, FLOPs |
| MOT | HOTA, MOTA, MOTAP | DetA, AssA, IDSW |
| Segmentation | Dice, IoU | HD95, ASSD |
| 3D Recon | Chamfer distance, F1 | completeness, accuracy |
| LLM | perplexity, MMLU | MT-Bench, human eval |

### 3. Benchmark Design
- **Baselines**: Include at least 2-3 established methods
- **Ablations**: Remove components one at a time (see `ablation-study` skill)
- **Compute-matched**: Compare at same FLOPs/params, not just same method
- **Edge cases**: Test on hard examples, not just averages

### 4. Reporting
- Report confidence intervals, not just point estimates
- Include failure case analysis
- Show statistical significance tests (paired t-test, Wilcoxon)
- Use tables for numbers, plots for trends

## Tools
- **W&B**: `wandb-experiment` skill for tracking runs
- **HF Evals**: `huggingface-community-evals` skill for Hub model evaluation
- **Custom**: `benchmark_kernel` MCP tool for latency benchmarks

## Paper Evaluation Section Template
```
## Experiments
### Datasets
[Describe train/val/test splits, statistics]

### Metrics
[Define all metrics with formulas]

### Baselines
[List comparison methods with citations]

### Main Results
[Table with your method vs baselines]

### Ablation Study
[Component-by-component analysis]

### Qualitative Results
[Failure cases and success cases]
```

## Reference Files
- Skills: `ablation-study`, `experiment-tracking`, `wandb-experiment`
- HF Skill: `huggingface-community-evals`
- MCP: `mcp_servers/dgx_monitor/server.py` (for hardware monitoring during eval)

