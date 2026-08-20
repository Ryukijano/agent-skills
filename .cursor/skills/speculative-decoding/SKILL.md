# Speculative Decoding

## Overview
A small draft model proposes tokens, a large verifier model accepts/rejects them in parallel. 1.5-3.6x speedup.

## How It Works
1. Draft model generates k candidate tokens autoregressively (fast)
2. Verifier model processes all k tokens in one forward pass
3. Accept tokens that match, reject and resample at first mismatch
4. Repeat

## vLLM Usage
```bash
python -m vllm.entrypoints.openai.api_server \
  --model meta-llama/Llama-3.1-70B \
  --speculative-model meta-llama/Llama-3.2-1B \
  --num-speculative-tokens 5
```

## HuggingFace
```python
from transformers import AutoModelForCausalLM
main = AutoModelForCausalLM.from_pretrained("big-model")
draft = AutoModelForCausalLM.from_pretrained("small-model")
# Use Medusa heads or EAGLE for implementation
```

## Methods
- **Medusa**: Multiple heads predict next k tokens simultaneously
- **Lookahead**: N-gram based, no draft model needed
- **EAGLE**: Trained draft head, best quality
- **Speculative streaming**: For streaming applications

## Requirements
- Draft model must share tokenizer/vocab with main model
- Draft model should be 10-50x smaller
- Optimal k: 3-7 tokens
- Speedup depends on acceptance rate (aim for >70%)
