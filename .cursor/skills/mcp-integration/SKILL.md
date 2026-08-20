# MCP Server Integration

## Description

Connect agents to external tools, databases, and services using the Model Context Protocol (MCP).

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

## References

- https://modelcontextprotocol.io/
- https://github.com/modelcontextprotocol
- https://www.anthropic.com/news/model-context-protocol
- https://github.com/agentskills/agentskills
