# agentic-context-engineering

## Description
Implement Agentic Context Engineering (ACE) - a Stanford research approach that replaces model fine-tuning with intelligent context construction. Proves you can make LLMs smarter without touching weights by engineering what goes into the context window.

## Background
From X bookmarks (Jul 2026): "RIP fine-tuning... This new Stanford paper just killed it. It's called 'Agentic Context Engineering (ACE)' and it proves you can make models smarter without touching a single weight."

## Core Concepts
- **Context-First Architecture**: Instead of fine-tuning, construct rich context with demonstrations, tools, memory, and instructions
- **Dynamic Context Assembly**: Retrieve relevant examples, tool schemas, and past interactions at inference time
- **Progressive Disclosure**: Load context components lazily - only what the agent needs for the current step
- **Context Budget Management**: Track token usage; prioritize high-value context when approaching limits

## ACE Components
1. **Instructions** - System prompt with role, constraints, output format
2. **Demonstrations** - Few-shot examples retrieved by similarity to current task
3. **Tool Schemas** - Only include tools relevant to current subtask
4. **Memory/State** - Working memory: completed steps, intermediate results, decisions made
5. **External Knowledge** - Retrieved documents, code snippets, API responses
6. **Environment State** - Current file contents, error messages, test results

## Implementation Pattern
```python
class AgenticContextBuilder:
    def build_context(self, task, agent_state, token_budget=8000):
        context_parts = []
        used_tokens = 0
        
        # Priority 1: Core instructions (always include)
        instructions = self.get_instructions(task.type)
        context_parts.append(instructions)
        used_tokens += count_tokens(instructions)
        
        # Priority 2: Relevant demonstrations (retrieved by similarity)
        if used_tokens < token_budget * 0.3:
            demos = self.retrieve_demos(task, k=3, max_tokens=token_budget*0.2)
            context_parts.extend(demos)
            used_tokens += sum(count_tokens(d) for d in demos)
        
        # Priority 3: Tool schemas (only relevant ones)
        tools = self.select_tools(task.subtask_type)
        context_parts.append(format_tools(tools))
        used_tokens += count_tokens(format_tools(tools))
        
        # Priority 4: Working memory / agent state
        memory = self.compress_memory(agent_state, max_tokens=token_budget*0.2)
        context_parts.append(memory)
        
        # Priority 5: Retrieved knowledge
        remaining = token_budget - used_tokens
        docs = self.retrieve_knowledge(task.query, max_tokens=remaining)
        context_parts.extend(docs)
        
        return "\n\n".join(context_parts)
```

## When to Use ACE vs Fine-tuning
| Situation | Recommendation |
|---|---|
| New task domain, few examples | ACE with few-shot demos |
| Need to update behavior quickly | ACE (no retraining) |
| Consistent low-level formatting | Fine-tuning |
| Complex multi-step reasoning | ACE with chain-of-thought demos |
| Resource-constrained inference | ACE (no larger model needed) |
| Style/persona consistency | Fine-tuning or ACE with persistent instructions |

## Related Skills
- `nemotron-agent-loop` - Multi-step agent loops
- `agentic-loop-design` - Agent architecture patterns
- `mcp-builder` - Tool schema design for agents
- `literature-search-arxiv` - RAG for research papers

## Tags
ace, agentic, context-engineering, llm, few-shot, retrieval, stanford, no-finetuning
