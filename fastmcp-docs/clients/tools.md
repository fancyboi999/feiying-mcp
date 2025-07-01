# Tool Operations - FastMCP

**Source URL:** https://gofastmcp.com/clients/tools
**Generated:** 2025-06-30

**Description:** Discover and execute server-side tools with the FastMCP client.

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

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
    # result -> CallToolResult with structured and unstructured data

    # Access structured data (automatically deserialized)
    print(result.data)  # 8 (int) or {"result": 8} for primitive types

    # Access traditional content blocks
    print(result.content[0].text)  # "8" (TextContent)

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

`New in version: 2.10.0`

Tool execution returns a `CallToolResult` object with both structured and traditional content. FastMCP’s standout feature is the `.data` property, which doesn’t just provide raw JSON but actually hydrates complete Python objects including complex types like datetimes, UUIDs, and custom classes.

### [​](https://gofastmcp.com/clients/tools\#calltoolresult-properties)  CallToolResult Properties

## CallToolResult Properties

[​](https://gofastmcp.com/clients/tools#param-data)

.data

Any

**FastMCP exclusive**: Fully hydrated Python objects with complex type support (datetimes, UUIDs, custom classes). Goes beyond JSON to provide complete object reconstruction from output schemas.

[​](https://gofastmcp.com/clients/tools#param-content)

.content

list\[mcp.types.ContentBlock\]

Standard MCP content blocks ( `TextContent`, `ImageContent`, `AudioContent`, etc.) available from all MCP servers.

[​](https://gofastmcp.com/clients/tools#param-structured-content)

.structured\_content

dict\[str, Any\] \| None

Standard MCP structured JSON data as sent by the server, available from all MCP servers that support structured outputs.

[​](https://gofastmcp.com/clients/tools#param-is-error)

.is\_error

bool

Boolean indicating if the tool execution failed.

### [​](https://gofastmcp.com/clients/tools\#structured-data-access)  Structured Data Access

FastMCP’s `.data` property provides fully hydrated Python objects, not just JSON dictionaries. This includes complex type reconstruction:

Copy

Ask AI

```
from datetime import datetime
from uuid import UUID

async with client:
    result = await client.call_tool("get_weather", {"city": "London"})

    # FastMCP reconstructs complete Python objects from the server's output schema
    weather = result.data  # Server-defined WeatherReport object
    print(f"Temperature: {weather.temperature}°C at {weather.timestamp}")
    print(f"Station: {weather.station_id}")
    print(f"Humidity: {weather.humidity}%")

    # The timestamp is a real datetime object, not a string!
    assert isinstance(weather.timestamp, datetime)
    assert isinstance(weather.station_id, UUID)

    # Compare with raw structured JSON (standard MCP)
    print(f"Raw JSON: {result.structured_content}")
    # {"temperature": 20, "timestamp": "2024-01-15T14:30:00Z", "station_id": "123e4567-..."}

    # Traditional content blocks (standard MCP)
    print(f"Text content: {result.content[0].text}")

```

### [​](https://gofastmcp.com/clients/tools\#fallback-behavior)  Fallback Behavior

For tools without output schemas or when deserialization fails, `.data` will be `None`:

Copy

Ask AI

```
async with client:
    result = await client.call_tool("legacy_tool", {"param": "value"})

    if result.data is not None:
        # Structured output available and successfully deserialized
        print(f"Structured: {result.data}")
    else:
        # No structured output or deserialization failed - use content blocks
        for content in result.content:
            if hasattr(content, 'text'):
                print(f"Text result: {content.text}")
            elif hasattr(content, 'data'):
                print(f"Binary data: {len(content.data)} bytes")

```

### [​](https://gofastmcp.com/clients/tools\#primitive-type-unwrapping)  Primitive Type Unwrapping

FastMCP servers automatically wrap non-object results (like `int`, `str`, `bool`) in a `{"result": value}` structure to create valid structured outputs. FastMCP clients understand this convention and automatically unwrap the value in `.data` for convenience, so you get the original primitive value instead of a wrapper object.

Copy

Ask AI

```
async with client:
    result = await client.call_tool("calculate_sum", {"a": 5, "b": 3})

    # FastMCP client automatically unwraps for convenience
    print(result.data)  # 8 (int) - the original value

    # Raw structured content shows the server-side wrapping
    print(result.structured_content)  # {"result": 8}

    # Other MCP clients would need to manually access ["result"]
    # value = result.structured_content["result"]  # Not needed with FastMCP!

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
        print("Tool succeeded:", result.data)
    except ToolError as e:
        print(f"Tool failed: {e}")

```

### [​](https://gofastmcp.com/clients/tools\#manual-error-checking)  Manual Error Checking

You can disable automatic error raising and manually check the result:

Copy

Ask AI

```
async with client:
    result = await client.call_tool(
        "potentially_failing_tool",
        {"param": "value"},
        raise_on_error=False
    )

    if result.is_error:
        print(f"Tool failed: {result.content[0].text}")
    else:
        print(f"Tool succeeded: {result.data}")

```

### [​](https://gofastmcp.com/clients/tools\#raw-mcp-protocol-access)  Raw MCP Protocol Access

For complete control, use `call_tool_mcp()` which returns the raw MCP protocol object:

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
        # Note: No automatic deserialization with call_tool_mcp()

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
- [CallToolResult Properties](https://gofastmcp.com/clients/tools#calltoolresult-properties)
- [Structured Data Access](https://gofastmcp.com/clients/tools#structured-data-access)
- [Fallback Behavior](https://gofastmcp.com/clients/tools#fallback-behavior)
- [Primitive Type Unwrapping](https://gofastmcp.com/clients/tools#primitive-type-unwrapping)
- [Error Handling](https://gofastmcp.com/clients/tools#error-handling)
- [Exception-Based Error Handling](https://gofastmcp.com/clients/tools#exception-based-error-handling)
- [Manual Error Checking](https://gofastmcp.com/clients/tools#manual-error-checking)
- [Raw MCP Protocol Access](https://gofastmcp.com/clients/tools#raw-mcp-protocol-access)
- [Argument Handling](https://gofastmcp.com/clients/tools#argument-handling)

Assistant

Responses are generated using AI and may contain mistakes.