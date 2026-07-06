---
name: model-merging
description: >-
  Combine multiple models with TIES, DARE, SLERP using mergekit. Create
  ensemble-like models without extra inference cost. Use when combining fine-
  tuned variants.
---

# Model Merging

## Overview
Combine multiple fine-tuned models into one without extra inference cost.

## Methods
- **SLERP**: Spherical interpolation between two models
- **TIES**: Trim, sign-resolve, merge (handles conflicts)
- **DARE**: Drop and rescale, reduces interference
- **Linear**: Simple weighted average

## mergekit
```yaml
# merge_config.yaml
models:
  - model: meta-llama/Llama-3.1-8B
    parameters:
      weight: 0.5
  - model: fine-tuned-variant
    parameters:
      weight: 0.5
merge_method: ties
dtype: bfloat16
```

```bash
mergekit-yaml merge_config.yaml ./merged-model
```

## Best Practices
- Merge models with same base architecture
- Use TIES or DARE for conflicting weights
- Start with 50/50 weights, experiment from there
- Evaluate merged model on all source tasks
- Can merge >2 models (3-5 is common)

## Use Cases
- Combine language + code fine-tunes
- Merge multilingual models
- Create generalist from specialists
- Reduce deployment cost (one model vs ensemble)
