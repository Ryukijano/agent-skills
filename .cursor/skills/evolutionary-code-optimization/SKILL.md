# Evolutionary Code Optimization

## Overview
Use LLMs to evolve code through mutation, evaluation, and selection. Works with any LLM (Gemini, GPT, Claude) and any evaluation function.

## The Evolutionary Loop
```
1. Start with a seed program
2. LLM generates N mutations (prompted by best programs so far)
3. Evaluator scores each mutation
4. Keep top-K programs in the population
5. Go to step 2, using best programs as context
6. Repeat for G generations
```

## Without AlphaEvolve (Local Implementation)
```python
import openai
import json

def evolve(seed_code, evaluator, generations=50, population=20, model="gpt-4"):
    population_db = [{"code": seed_code, "score": evaluator(seed_code)}]
    
    for gen in range(generations):
        # Select best programs as context
        best = sorted(population_db, key=lambda x: x["score"], reverse=True)[:5]
        context = "\n\n".join([f"Program (score={p['score']}):\n{p['code']}" for p in best])
        
        # Generate mutations
        for _ in range(population):
            response = openai.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": "Improve the code to maximize the score. Return only code."},
                    {"role": "user", "content": f"Best programs so far:\n{context}\n\nGenerate an improved version."},
                ],
            )
            mutated = response.choices[0].message.content
            score = evaluator(mutated)
            population_db.append({"code": mutated, "score": score})
        
        # Keep top performers
        population_db = sorted(population_db, key=lambda x: x["score"], reverse=True)[:population]
        print(f"Gen {gen}: best={population_db[0]['score']:.4f}")
    
    return population_db[0]
```

## With AlphaEvolve (Google Cloud)
Use the `alphaevolve-orchestrator` skill for the full managed experience with Gemini models, program database, and distributed evaluation.

## Best Practices

### Seed Program
- Start with a working baseline — the better the seed, the faster convergence
- Mark evolvable regions clearly (EVOLVE-BLOCK markers for AlphaEvolve)
- Keep interfaces stable — only evolve implementations, not signatures

### Evaluator Design
- Must be deterministic — same input → same output
- Handle failures gracefully: return -inf or sentinel score for broken code
- Use timeouts to prevent infinite loops
- Multi-objective: return multiple metrics, optimize primary
- Prevent reward hacking: held-out tests, constraint checks

### LLM Configuration
- Use a mix of fast (breadth) and powerful (depth) models
- Temperature 0.7-1.0 for exploration
- Include insights from failures in the prompt to guide improvement
- Show top-K programs with scores as context

### Search Budget
- Start small (50-100 programs) to validate the setup
- Scale up (500-1000+) for production runs
- Monitor for plateaus — if no improvement for 50+ generations, consider stopping
- Progress is non-monotonic — don't stop early on plateaus

## Use Cases
- **Algorithm optimization**: sorting, packing, routing, scheduling
- **Hyperparameter tuning**: LoRA configs, learning rates, batch sizes
- **Kernel optimization**: GPU kernels, matrix multiplication
- **Quantum circuits**: gate sequence optimization (see Conditional-GQE)
- **Training loops**: loss functions, augmentation strategies
- **Data pipelines**: preprocessing, feature engineering
