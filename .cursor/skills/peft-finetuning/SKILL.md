# PEFT Fine-Tuning

## Overview
Parameter-Efficient Fine-Tuning (PEFT) adapts large models by training only small adapter modules.

## LoRA
```python
from peft import LoraConfig, get_peft_model
config = LoraConfig(
    r=16, lora_alpha=32, lora_dropout=0.05,
    target_modules=["q_proj", "v_proj"],
    task_type="CAUSAL_LM",
)
model = get_peft_model(base_model, config)
```

## QLoRA (4-bit quantization + LoRA)
```python
from transformers import BitsAndBytesConfig
bnb_config = BitsAndBytesConfig(
    load_in_4bit=True,
    bnb_4bit_quant_type="nf4",
    bnb_4bit_compute_dtype=torch.bfloat16,
)
model = AutoModelForCausalLM.from_pretrained(
    "meta-llama/Llama-3.1-70B",
    quantization_config=bnb_config,
)
```

## Methods
- **LoRA**: Low-rank adapters, r=8-64, 0.1-1% trainable params
- **QLoRA**: 4-bit base + LoRA adapters, 70B on single GPU
- **DoRA**: Decomposed weight updates, better than LoRA
- **IA3**: Scaled activations, fewest params
- **Prefix Tuning**: Soft prompts, good for generation

## Best Practices
- Target modules: q_proj, k_proj, v_proj, o_proj for attention
- For MLP: gate_proj, up_proj, down_proj
- r=16 is a good default, r=64 for complex tasks
- Learning rate: 1e-4 to 3e-4 (10x higher than full FT)
- Merge adapters before deployment: model.merge_and_unload()
