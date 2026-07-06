---
name: model-quantization
description: >-
  Quantize LLMs to 8-bit or 4-bit with bitsandbytes, GPTQ, AWQ, GGUF. Reduce
  memory 50-75% with minimal accuracy loss. Use when deploying models with
  limited GPU memory.
---

# Model Quantization

## Methods Comparison
| Method | Bits | Calibration | Speed | Accuracy |
|--------|------|-------------|-------|----------|
| bitsandbytes | 8/4 | None | Fast | Good |
| GPTQ | 4 | Required | Medium | Very Good |
| AWQ | 4 | Required | Fast | Very Good |
| GGUF | 2-8 | None | CPU/Metal | Good |
| HQQ | 4-8 | None | Fast | Good |

## bitsandbytes (easiest)
```python
from transformers import BitsAndBytesConfig
config = BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type="nf4")
model = AutoModelForCausalLM.from_pretrained("model_name", quantization_config=config)
```

## AWQ (best for serving)
```python
from awq import AutoAWQForCausalLM
model = AutoAWQForCausalLM.from_pretrained("model_name")
model.quantize("model_name", quant_config={"w_bit": 4, "q_group_size": 128})
```

## GGUF (for llama.cpp/CPU)
```bash
python convert.py model_dir --outtype f16 --quantize q4_k_m
```

## Memory Savings
- FP16: 2 bytes/param (70B = 140GB)
- 8-bit: 1 byte/param (70B = 70GB)
- 4-bit: 0.5 bytes/param (70B = 35GB)

## Tips
- Use NF4 quant type for 4-bit (better than FP4)
- Calibrate on representative data for GPTQ/AWQ
- Merge LoRA adapters before quantizing
- Benchmark latency, not just memory
