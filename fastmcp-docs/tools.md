# Tool Operations - FastMCP

**Source URL:** https://gofastmcp.com/clients/tools
**Generated:** 2025-06-27

**Description:** Discover and execute server-side tools with the FastMCP client.

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Core Operations

Tool Operations

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

`New in version: 2.0.0`

Tools are executable functions exposed by MCP servers. The FastMCP client provides methods to discover available tools and execute them with arguments.

## [​](https://gofastmcp.com/clients/tools\#discovering-tools)  Discovering Tools

Use `list_tools()` to retrieve all tools available on the server:

Copy

Ask AI

```
async with client:
    tools = await client.list_tools()
    # tools -> list[mcp.types.Tool]

    for tool in tools:
        print(f"Tool: {tool.name}")
        print(f"Description: {tool.description}")
        if tool.inputSchema:
            print(f"Parameters: {tool.inputSchema}")

```

## [​](https://gofastmcp.com/clients/tools\#executing-tools)  Executing Tools

### [​](https://gofastmcp.com/clients/tools\#basic-execution)  Basic Execution

Execute a tool using `call_tool()` with the tool name and arguments:

Copy

Ask AI

```
async with client:
    # Simple tool call
    result = await client.call_tool("add", {"a": 5, "b": 3})
    # result -> list[mcp.types.TextContent | mcp.types.ImageContent | ...]

    # Access the result content
    print(result[0].text)  # Assuming TextContent, e.g., '8'

```

### [​](https://gofastmcp.com/clients/tools\#advanced-execution-options)  Advanced Execution Options

The `call_tool()` method supports additional parameters for timeout control and progress monitoring:

Copy

Ask AI

```
async with client:
    # With timeout (aborts if execution takes longer than 2 seconds)
    result = await client.call_tool(
        "long_running_task",
        {"param": "value"},
        timeout=2.0
    )

    # With progress handler (to track execution progress)
    result = await client.call_tool(
        "long_running_task",
        {"param": "value"},
        progress_handler=my_progress_handler
    )

```

**Parameters:**

- `name`: The tool name (string)
- `arguments`: Dictionary of arguments to pass to the tool (optional)
- `timeout`: Maximum execution time in seconds (optional, overrides client-level timeout)
- `progress_handler`: Progress callback function (optional, overrides client-level handler)

## [​](https://gofastmcp.com/clients/tools\#handling-results)  Handling Results

Tool execution returns a list of content objects. The most common types are:

- **`TextContent`**: Text-based results with a `.text` attribute
- **`ImageContent`**: Image data with image-specific attributes
- **`BlobContent`**: Binary data content

Copy

Ask AI

```
async with client:
    result = await client.call_tool("get_weather", {"city": "London"})

    for content in result:
        if hasattr(content, 'text'):
            print(f"Text result: {content.text}")
        elif hasattr(content, 'data'):
            print(f"Binary data: {len(content.data)} bytes")

```

## [​](https://gofastmcp.com/clients/tools\#error-handling)  Error Handling

### [​](https://gofastmcp.com/clients/tools\#exception-based-error-handling)  Exception-Based Error Handling

By default, `call_tool()` raises a `ToolError` if the tool execution fails:

Copy

Ask AI

```
from fastmcp.exceptions import ToolError

async with client:
    try:
        result = await client.call_tool("potentially_failing_tool", {"param": "value"})
        print("Tool succeeded:", result)
    except ToolError as e:
        print(f"Tool failed: {e}")

```

### [​](https://gofastmcp.com/clients/tools\#manual-error-checking)  Manual Error Checking

For more granular control, use `call_tool_mcp()` which returns the raw MCP protocol object with an `isError` flag:

Copy

Ask AI

```
async with client:
    result = await client.call_tool_mcp("potentially_failing_tool", {"param": "value"})
    # result -> mcp.types.CallToolResult

    if result.isError:
        print(f"Tool failed: {result.content}")
    else:
        print(f"Tool succeeded: {result.content}")

```

## [​](https://gofastmcp.com/clients/tools\#argument-handling)  Argument Handling

Arguments are passed as a dictionary to the tool:

Copy

Ask AI

```
async with client:
    # Simple arguments
    result = await client.call_tool("greet", {"name": "World"})

    # Complex arguments
    result = await client.call_tool("process_data", {
        "config": {"format": "json", "validate": True},
        "items": [1, 2, 3, 4, 5],
        "metadata": {"source": "api", "version": "1.0"}
    })

```

For multi-server clients, tool names are automatically prefixed with the server name (e.g., `weather_get_forecast` for a tool named `get_forecast` on the `weather` server).

[Overview](https://gofastmcp.com/clients/client) [Resources](https://gofastmcp.com/clients/resources)

On this page

- [Discovering Tools](https://gofastmcp.com/clients/tools#discovering-tools)
- [Executing Tools](https://gofastmcp.com/clients/tools#executing-tools)
- [Basic Execution](https://gofastmcp.com/clients/tools#basic-execution)
- [Advanced Execution Options](https://gofastmcp.com/clients/tools#advanced-execution-options)
- [Handling Results](https://gofastmcp.com/clients/tools#handling-results)
- [Error Handling](https://gofastmcp.com/clients/tools#error-handling)
- [Exception-Based Error Handling](https://gofastmcp.com/clients/tools#exception-based-error-handling)
- [Manual Error Checking](https://gofastmcp.com/clients/tools#manual-error-checking)
- [Argument Handling](https://gofastmcp.com/clients/tools#argument-handling)

Assistant

Responses are generated using AI and may contain mistakes.