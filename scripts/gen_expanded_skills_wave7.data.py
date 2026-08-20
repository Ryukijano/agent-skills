SKILLS = [
    {
        "name": "llm-reasoning",
        "title": "LLM Reasoning and Chain-of-Thought",
        "description": "Chain-of-thought, self-consistency, tree-of-thoughts, and reasoning-optimized prompting for large language models.",
        "devin_body": r'''
## When to use

You want to improve a language model's performance on multi-step math, logic, code, or planning problems.

## Key concepts

- **Chain-of-thought (CoT)**: prompt the model to emit intermediate reasoning steps.
- **Self-consistency**: sample multiple CoT answers and vote on the final result.
- **Tree-of-thoughts (ToT)**: search over partial reasoning chains and backtrack.
- **Zero-shot CoT**: append "Let's think step by step" or similar to elicit reasoning.
- **Reasoning models**: scaling test-time compute and process-supervised reward models.

## Code pattern

```python
import openai

response = openai.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "user", "content": "Solve: if 3x+2=14, what is x? Let's think step by step."}
    ]
)
print(response.choices[0].message.content)
```

## Tuning notes

- CoT helps most when the task requires explicit intermediate steps.
- Self-consistency increases accuracy at the cost of extra sampling.
- ToT is powerful but requires a way to evaluate partial solutions and a search budget.

## Verification

1. Solve a small arithmetic dataset with and without CoT.
2. Run self-consistency with 5 samples and compare majority vote to greedy decode.
3. Implement a two-step ToT search and verify it finds a better answer on a planning puzzle.
''',
        "references": [
            "https://arxiv.org/abs/2201.11903",
            "https://arxiv.org/abs/2203.11171",
            "https://arxiv.org/abs/2305.10601",
            "https://openai.com/index/learning-to-reason-with-llms/"
        ],
    },
    {
        "name": "tool-use-agents",
        "title": "Tool-Use Agents",
        "description": "Design LLM agents that call functions, APIs, and utilities to gather facts and take actions.",
        "devin_body": r'''
## When to use

You are building an agent that needs to interact with external APIs, calculators, databases, or code execution.

## Key concepts

- **Function calling**: the LLM emits structured JSON arguments for registered tools.
- **Tool definitions**: JSON schema describing name, description, and parameters.
- **Observation loop**: execute the tool, return the result, and let the LLM continue.
- **Tool selection**: retrieval over tool descriptions when many tools are available.

## Code pattern

```python
def get_weather(city: str) -> str:
    return f"Sunny, 22 C in {city}"

tools = [{
    "type": "function",
    "function": {
        "name": "get_weather",
        "description": "Get current weather",
        "parameters": {
            "type": "object",
            "properties": {"city": {"type": "string"}},
            "required": ["city"]
        }
    }
}]
```

## Tuning notes

- Keep tool descriptions as clear as user-facing documentation.
- Validate and sanitize arguments before execution.
- Limit context by only returning compact observations.

## Verification

1. Register a calculator and a search stub; test the agent on a multi-step question.
2. Check that invalid tool calls are rejected safely.
3. Measure success rate on a small tool-use benchmark.
''',
        "references": [
            "https://arxiv.org/abs/2402.12430",
            "https://platform.openai.com/docs/guides/function-calling",
            "https://github.com/anthropics/skills",
            "https://agentskills.io/"
        ],
    },
    {
        "name": "mcp-integration",
        "title": "MCP Server Integration",
        "description": "Connect agents to external tools, databases, and services using the Model Context Protocol (MCP).",
        "devin_body": r'''
## When to use

You want to expose live tools to an agent without hard-coding every integration in the agent prompt.

## Key concepts

- **MCP**: Model Context Protocol standard for tool/resource servers.
- **Server**: a process implementing MCP that exposes tools and resources.
- **Client**: an agent or host that discovers and calls MCP servers.
- **stdio vs SSE transport**: local process pipes or HTTP server-sent events.

## Code pattern

```python
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

params = StdioServerParameters(
    command="python", args=["mcp_server.py"], env=None
)

async with stdio_client(params) as (read, write):
    async with ClientSession(read, write) as session:
        await session.initialize()
        tools = await session.list_tools()
```

## Tuning notes

- Prefer stdio for local trusted servers; use SSE for remote services.
- Use capability descriptions so the agent knows when to call a tool.
- Cache tool metadata at startup to avoid latency.

## Verification

1. Implement an MCP server with one read tool and one action tool.
2. Connect a client, list tools, and invoke one.
3. Verify the server handles errors and returns typed results.
''',
        "references": [
            "https://modelcontextprotocol.io/",
            "https://github.com/modelcontextprotocol",
            "https://www.anthropic.com/news/model-context-protocol",
            "https://github.com/agentskills/agentskills"
        ],
    },
    {
        "name": "long-context-llm",
        "title": "Long-Context LLM Methods",
        "description": "Architectures, position interpolation, and evaluation for language models with very long contexts.",
        "devin_body": r'''
## When to use

You need to process documents, videos, or conversations that exceed the model's native context window.

## Key concepts

- **Position interpolation**: scale RoPE bases or adjust frequencies to extend context.
- **Ring attention / sparse attention**: sub-quadratic attention for long sequences.
- **Needle-in-haystack**: benchmark for retrieving a fact buried in a long prompt.
- **RAG vs long context**: trade-off between retrieval augmentation and full-context feeding.

## Code pattern

```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b-chat-hf")
tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-2-7b-chat-hf")

# Use position-interpolated config if available
context = tokenizer(long_document, return_tensors="pt", truncation=False)
```

## Tuning notes

- RoPE rescaling to 2-8x often requires continued pre-training on long sequences.
- Sparse attention can speed inference but may alter the loss landscape.
- Evaluate with needle-in-haystack before deploying a long-context model.

## Verification

1. Run a needle-in-haystack benchmark at several context lengths.
2. Compare performance with and without position interpolation.
3. Measure perplexity on a long-document validation set.
''',
        "references": [
            "https://arxiv.org/abs/2306.15595",
            "https://arxiv.org/abs/2402.17463",
            "https://github.com/lhao499/RingAttention",
            "https://arxiv.org/abs/2307.03172"
        ],
    },
    {
        "name": "llm-judge-evaluation",
        "title": "LLM-as-a-Judge Evaluation",
        "description": "Use strong language models to evaluate, score, and compare outputs from other models or pipelines.",
        "devin_body": r'''
## When to use

You need an automated, flexible evaluation metric for open-ended generation, chat, or instruction following.

## Key concepts

- **LLM-as-a-judge**: a capable model scores outputs against a rubric.
- **Pairwise vs pointwise**: compare two outputs or score one output.
- **Position bias**: the judge may prefer the first or last candidate.
- **Reference-free vs reference-based**: with or without a gold answer.

## Code pattern

```python
import openai

def judge(prediction, reference=None):
    prompt = f"Rate the following answer 1-5 for correctness and clarity.\n\nAnswer: {prediction}"
    if reference:
        prompt += f"\n\nReference: {reference}"
    response = openai.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
```

## Tuning notes

- Provide detailed rubrics and few-shot examples to reduce variance.
- Swap candidate order to detect and average out position bias.
- Calibrate judge scores with human annotations.

## Verification

1. Build a judge prompt for a summarization task.
2. Evaluate 20 model outputs and correlate with human ratings.
3. Measure inter-rater agreement between judge and human scores.
''',
        "references": [
            "https://arxiv.org/abs/2306.05685",
            "https://arxiv.org/abs/2407.00449",
            "https://github.com/lm-sys/FastChat/tree/main/fastchat/llm_judge",
            "https://huggingface.co/spaces/lm-sys/mt-bench"
        ],
    },
    {
        "name": "prompt-engineering-advanced",
        "title": "Advanced Prompt Engineering",
        "description": "Structured prompting, few-shot, chain-of-thought, role prompts, and prompt optimization for LLMs.",
        "devin_body": r'''
## When to use

You want to get more reliable, structured, or correct output from an LLM without fine-tuning.

## Key concepts

- **Few-shot prompting**: provide input-output examples in the context.
- **Role and style prompts**: frame the model as an expert in a domain.
- **Structured output**: request JSON, XML, or YAML with schemas.
- **Prompt templates**: separate instruction, examples, and user input.
- **Automatic prompt optimization**: e.g., DSPy, APE, OPRO.

## Code pattern

```python
prompt = f"""You are an expert Python reviewer. Given the code, output JSON with fields 'issues' and 'score'.

Code:
{code}

Output JSON only.
"""
```

## Tuning notes

- Use clear delimiters to separate instructions, examples, and input.
- Iterate with a small held-out set rather than one-off tuning.
- Optimize for the specific model and API; prompts may not transfer perfectly.

## Verification

1. Design a few-shot prompt for a classification task and measure F1.
2. Compare role prompts vs neutral prompts on a reasoning task.
3. Generate JSON outputs and validate schema compliance.
''',
        "references": [
            "https://arxiv.org/abs/2307.11760",
            "https://arxiv.org/abs/2312.16171",
            "https://dspy-docs.vercel.app/",
            "https://github.com/keirp/automatic_prompt_engineer"
        ],
    },
    {
        "name": "rag-retrieval-evaluation",
        "title": "RAG Retrieval Evaluation",
        "description": "Evaluate retrieval quality, answer relevance, and end-to-end RAG pipeline performance.",
        "devin_body": r'''
## When to use

You are building or improving a retrieval-augmented generation pipeline and need to measure its components.

## Key concepts

- **Retrieval metrics**: MRR, Recall@k, NDCG, hit rate.
- **Generation metrics**: faithfulness, answer relevance, context precision.
- **RAGAS**: framework with context relevance, answer correctness, etc.
- **LLM-as-judge**: evaluate generated answers against retrieved context.

## Code pattern

```python
from ragas import evaluate
from ragas.metrics import context_recall, faithfulness, answer_relevancy

result = evaluate(
    dataset=eval_dataset,
    metrics=[context_recall, faithfulness, answer_relevancy],
)
print(result)
```

## Tuning notes

- Evaluate retrieval and generation separately before end-to-end.
- Bad retrieval is a common root cause of RAG failures.
- Use domain-specific test questions for realistic benchmarks.

## Verification

1. Build a small Q&A benchmark with gold documents and answers.
2. Compute retrieval Recall@5 and generation faithfulness.
3. A/B test two retrievers and measure end-to-end answer accuracy.
''',
        "references": [
            "https://arxiv.org/abs/2404.01037",
            "https://docs.ragas.io/",
            "https://arxiv.org/abs/2403.18131",
            "https://python.langchain.com/docs/guides/evaluation/"
        ],
    },
    {
        "name": "agent-memory",
        "title": "Agent Memory Systems",
        "description": "Short-term and long-term memory for agents: vector stores, summaries, entity tracking, and memory hierarchies.",
        "devin_body": r'''
## When to use

Your agent must remember facts, user preferences, or prior interactions across a long session or multiple sessions.

## Key concepts

- **Working memory**: current conversation context.
- **Long-term memory**: stored facts, summaries, and embeddings.
- **Entity and event memory**: track objects, people, and occurrences.
- **Memory retrieval**: recency, relevance, and importance scoring.
- **MemGPT / MemoryBank**: example architectures for managing memory.

## Code pattern

```python
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()
memory.save_context({"input": "My name is Alice"}, {"output": "Nice to meet you, Alice"})
print(memory.load_memory_variables({}))
```

## Tuning notes

- Combine embedding retrieval with recent-message injection.
- Summarize old conversation to compress context.
- Protect privacy: do not persist sensitive data without consent.

## Verification

1. Build a simple agent that remembers a user's name and preferences.
2. Test memory recall after many conversational turns.
3. Measure latency of vector-store retrieval vs in-memory summary.
''',
        "references": [
            "https://arxiv.org/abs/2403.12039",
            "https://github.com/cpacker/MemGPT",
            "https://arxiv.org/abs/2312.03689",
            "https://python.langchain.com/docs/modules/memory/"
        ],
    },
    {
        "name": "multi-agent-orchestration",
        "title": "Multi-Agent Orchestration",
        "description": "Coordinate multiple specialist agents to decompose tasks, debate, and synthesize solutions.",
        "devin_body": r'''
## When to use

A single agent is not enough; you need several agents with different roles collaborating on a complex task.

## Key concepts

- **Role-based agents**: planner, coder, reviewer, verifier.
- **Conversation patterns**: sequential, round-robin, hierarchical, group chat.
- **Task decomposition**: break a problem into subtasks assigned to agents.
- **Consensus and aggregation**: voting, merging, or meta-agent summarization.

## Code pattern

```python
# Pseudo-code for a two-agent round-robin
coder = Agent(name="Coder", instructions="Write Python functions.")
reviewer = Agent(name="Reviewer", instructions="Review for bugs.")

debate = GroupChat(agents=[coder, reviewer], messages=[])
result = debate.run("Implement a function that returns prime numbers up to N.")
```

## Tuning notes

- Define clear roles and stopping conditions.
- Limit the number of turns to avoid runaway costs.
- Use a shared scratchpad for intermediate results.

## Verification

1. Set up a coder-reviewer pair and run on a small coding task.
2. Compare multi-agent output to a single agent on the same task.
3. Measure how often the conversation reaches a useful consensus.
''',
        "references": [
            "https://arxiv.org/abs/2402.16820",
            "https://github.com/microsoft/autogen",
            "https://arxiv.org/abs/2401.08507",
            "https://arxiv.org/abs/2402.16672"
        ],
    },
    {
        "name": "llm-redteaming",
        "title": "LLM Red Teaming and Safety",
        "description": "Systematically probe LLMs for harmful outputs, jailbreaks, privacy leaks, and misalignment.",
        "devin_body": r'''
## When to use

You are deploying or fine-tuning an LLM and need to find and mitigate failure modes before release.

## Key concepts

- **Red teaming**: adversarial probing to elicit undesirable behavior.
- **Jailbreaks and prompt injection**: user-level attacks that bypass safety filters.
- **Privacy extraction**: training data or secrets leakage.
- **Safety evals**: toxicity, bias, harmful instructions, misinformation.

## Code pattern

```python
# Probe with a set of adversarial prompts
for prompt in adversarial_prompts:
    response = model.generate(prompt)
    flagged = safety_classifier(response)
    print(prompt, flagged, response[:200])
```

## Tuning notes

- Combine automated probes with human review.
- Use a broad taxonomy of harms, not just a single safety metric.
- Retest after mitigation to ensure over-refusal does not spike.

## Verification

1. Run a small jailbreak probe set and record success rate.
2. Test a classifier on a balanced harmful/harmless test set.
3. Document a failure mode and a mitigating guardrail.
''',
        "references": [
            "https://arxiv.org/abs/2402.09300",
            "https://www.anthropic.com/news/red-teaming-language-models-to-reduce-harms-methods-scaling-behaviors-and-lessons-learned",
            "https://arxiv.org/abs/2312.07401",
            "https://github.com/llm-attacks/llm-attacks"
        ],
    },
    {
        "name": "test-time-compute",
        "title": "Test-Time Compute Scaling",
        "description": "Improve LLM output quality by increasing inference-time computation: search, verification, and reward models.",
        "devin_body": r'''
## When to use

You want better answers from a fixed model by allowing it to think longer or verify candidates at inference.

## Key concepts

- **Compute-optimal inference**: allocate inference compute to maximize pass@k.
- **Process reward models (PRM)**: score each reasoning step.
- **Outcome reward models (ORM)**: score the final answer.
- **Monte Carlo tree search / beam search** over reasoning paths.
- **Verifier ensembles**: multiple verifiers judge a candidate answer.

## Code pattern

```python
def best_of_n(prompt, n=8):
    candidates = [model.generate(prompt) for _ in range(n)]
    scores = [verifier(c) for c in candidates]
    return candidates[argmax(scores)]
```

## Tuning notes

- More samples helps most on hard reasoning tasks with reliable verifiers.
- A weak verifier can hurt performance; calibrate on a dev set.
- Balance sampling budget against latency and cost.

## Verification

1. Implement best-of-N sampling on a math word-problem set.
2. Train or use a small verifier and compare RM selection to majority vote.
3. Plot pass@k and compute-optimal pass rate versus N.
''',
        "references": [
            "https://arxiv.org/abs/2408.03314",
            "https://arxiv.org/abs/2409.01903",
            "https://openai.com/index/learning-to-reason-with-llms/",
            "https://arxiv.org/abs/2402.06178"
        ],
    },
    {
        "name": "agent-evaluation-benchmarks",
        "title": "Agent Evaluation Benchmarks",
        "description": "Measure agent capability on coding, web, tool use, and open-ended reasoning benchmarks.",
        "devin_body": r'''
## When to use

You need to compare agents or track progress across real-world capabilities.

## Key concepts

- **SWE-bench / SWE-bench Verified**: resolve real GitHub issues.
- **WebArena / Mind2Web**: web browsing and form-filling.
- **ToolBench**: API calling and tool selection.
- **HumanEval / MBPP+**: coding proficiency.
- **GAIA**: general assistant tasks requiring reasoning and tools.

## Code pattern

```python
from datasets import load_dataset
from evaluate import load

swebench = load_dataset("princeton-nlp/SWE-bench", " Lite")
# Run your agent on each instance and compare to gold patch.
```

## Tuning notes

- Start with a small subset before running a full benchmark.
- Check that the environment and dependencies are exactly as expected.
- Separate pass@1 from pass with retries and compute budget.

## Verification

1. Run HumanEval on the agent's code generator.
2. Evaluate on a handful of SWE-bench Lite instances.
3. Track success rate per benchmark and per task category.
''',
        "references": [
            "https://arxiv.org/abs/2310.06770",
            "https://www.swebench.com/",
            "https://arxiv.org/abs/2307.13854",
            "https://arxiv.org/abs/2311.08377"
        ],
    },
]
