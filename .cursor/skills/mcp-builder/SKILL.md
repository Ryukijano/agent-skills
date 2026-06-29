---
name: mcp-builder
description: >-
  Create MCP (Model Context Protocol) servers to integrate external APIs and
  services. Use when the user wants to build an MCP server, create custom tools
  for AI agents, or expose APIs via MCP.
---

# MCP Server Development Guide

## Overview
MCP (Model Context Protocol) lets you expose tools, resources, and prompts to AI agents via a standardized protocol.

## High-Level Workflow

### Phase 1: Deep Research and Planning
- Understand what tools/resources the MCP server will expose
- Identify the target API or data source
- Plan the tool schemas (name, description, input/output)

### Phase 2: Implementation
- Use the MCP SDK (Python or TypeScript)
- Implement tools as async functions with type hints
- Register tools with the MCP server
- Handle errors gracefully

### Phase 3: Review and Test
- Test each tool independently
- Verify error handling for edge cases
- Test with actual MCP client

### Phase 4: Create Evaluations
- Write evaluation cases for each tool
- Test with real-world queries

## Quick Start (Python)
```python
from mcp.server import Server
from mcp.types import Tool, TextContent
import mcp.server.stdio

server = Server("my-mcp-server")

@server.list_tools()
async def list_tools():
    return [Tool(name="hello", description="Say hello", inputSchema={"type": "object", "properties": {}})]

@server.call_tool()
async def call_tool(name, arguments):
    if name == "hello":
        return [TextContent(type="text", text="Hello, World!")]

async def main():
    async with mcp.server.stdio.stdio_server() as (read, write):
        await server.run(read, write, server.create_initialization_options())
```

## Reference Files
- Core MCP Documentation: https://modelcontextprotocol.io/
- Python SDK: https://github.com/modelcontextprotocol/python-sdk
- TypeScript SDK: https://github.com/modelcontextprotocol/typescript-sdk
