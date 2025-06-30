# transports - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-client-transports
**Generated:** 2025-06-27

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.client

transports

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#fastmcp-client-transports)  `fastmcp.client.transports`

## [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#infer-transport)  `infer_transport`

Copy

Ask AI

```
infer_transport(transport: ClientTransport | FastMCP | FastMCP1Server | AnyUrl | Path | MCPConfig | dict[str, Any] | str) -> ClientTransport

```

Infer the appropriate transport type from the given transport argument.

This function attempts to infer the correct transport type from the provided
argument, handling various input types and converting them to the appropriate
ClientTransport subclass.

The function supports these input types:

- ClientTransport: Used directly without modification
- FastMCP or FastMCP1Server: Creates an in-memory FastMCPTransport
- Path or str (file path): Creates PythonStdioTransport (.py) or NodeStdioTransport (.js)
- AnyUrl or str (URL): Creates StreamableHttpTransport (default) or SSETransport (for /sse endpoints)
- MCPConfig or dict: Creates MCPConfigTransport, potentially connecting to multiple servers

For HTTP URLs, they are assumed to be Streamable HTTP URLs unless they end in `/sse`.

For MCPConfig with multiple servers, a composite client is created where each server
is mounted with its name as prefix. This allows accessing tools and resources from multiple
servers through a single unified client interface, using naming patterns like
`servername_toolname` for tools and `protocol://servername/path` for resources.
If the MCPConfig contains only one server, a direct connection is established without prefixing.

**Examples:**

Copy

Ask AI

```
# Connect to a local Python script
transport = infer_transport("my_script.py")

# Connect to a remote server via HTTP
transport = infer_transport("http://example.com/mcp")

# Connect to multiple servers using MCPConfig
config = {
    "mcpServers": {
        "weather": {"url": "http://weather.example.com/mcp"},
        "calendar": {"url": "http://calendar.example.com/mcp"}
    }
}
transport = infer_transport(config)

```

## [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#sessionkwargs)  `SessionKwargs`

Keyword arguments for the MCP ClientSession constructor.

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#clienttransport)  `ClientTransport`

Abstract base class for different MCP client transport mechanisms.

A Transport is responsible for establishing and managing connections
to an MCP server, and providing a ClientSession within an async context.

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#wstransport)  `WSTransport`

Transport implementation that connects to an MCP server via WebSockets.

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#ssetransport)  `SSETransport`

Transport implementation that connects to an MCP server via Server-Sent Events.

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#streamablehttptransport)  `StreamableHttpTransport`

Transport implementation that connects to an MCP server via Streamable HTTP Requests.

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#stdiotransport)  `StdioTransport`

Base transport for connecting to an MCP server via subprocess with stdio.

This is a base class that can be subclassed for specific command-based
transports like Python, Node, Uvx, etc.

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#pythonstdiotransport)  `PythonStdioTransport`

Transport for running Python scripts.

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#fastmcpstdiotransport)  `FastMCPStdioTransport`

Transport for running FastMCP servers using the FastMCP CLI.

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#nodestdiotransport)  `NodeStdioTransport`

Transport for running Node.js scripts.

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#uvxstdiotransport)  `UvxStdioTransport`

Transport for running commands via the uvx tool.

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#npxstdiotransport)  `NpxStdioTransport`

Transport for running commands via the npx tool.

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#fastmcptransport)  `FastMCPTransport`

In-memory transport for FastMCP servers.

This transport connects directly to a FastMCP server instance in the same
Python process. It works with both FastMCP 2.x servers and FastMCP 1.0
servers from the low-level MCP SDK. This is particularly useful for unit
tests or scenarios where client and server run in the same runtime.

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-transports\#mcpconfigtransport)  `MCPConfigTransport`

Transport for connecting to one or more MCP servers defined in an MCPConfig.

This transport provides a unified interface to multiple MCP servers defined in an MCPConfig
object or dictionary matching the MCPConfig schema. It supports two key scenarios:

1. If the MCPConfig contains exactly one server, it creates a direct transport to that server.
2. If the MCPConfig contains multiple servers, it creates a composite client by mounting
all servers on a single FastMCP instance, with each server’s name used as its mounting prefix.

In the multi-server case, tools are accessible with the prefix pattern `{server_name}_{tool_name}`
and resources with the pattern `protocol://{server_name}/path/to/resource`.

This is particularly useful for creating clients that need to interact with multiple specialized
MCP servers through a single interface, simplifying client code.

**Examples:**

Copy

Ask AI

```
from fastmcp import Client
from fastmcp.utilities.mcp_config import MCPConfig

# Create a config with multiple servers
config = {
    "mcpServers": {
        "weather": {
            "url": "https://weather-api.example.com/mcp",
            "transport": "http"
        },
        "calendar": {
            "url": "https://calendar-api.example.com/mcp",
            "transport": "http"
        }
    }
}

# Create a client with the config
client = Client(config)

async with client:
    # Access tools with prefixes
    weather = await client.call_tool("weather_get_forecast", {"city": "London"})
    events = await client.call_tool("calendar_list_events", {"date": "2023-06-01"})

    # Access resources with prefixed URIs
    icons = await client.read_resource("weather://weather/icons/sunny")

```

[sampling](https://gofastmcp.com/python-sdk/fastmcp-client-sampling) [\_\_init\_\_](https://gofastmcp.com/python-sdk/fastmcp-prompts-__init__)

On this page

- [fastmcp.client.transports](https://gofastmcp.com/python-sdk/fastmcp-client-transports#fastmcp-client-transports)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-client-transports#functions)
- [infer\_transport](https://gofastmcp.com/python-sdk/fastmcp-client-transports#infer-transport)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-client-transports#classes)
- [SessionKwargs](https://gofastmcp.com/python-sdk/fastmcp-client-transports#sessionkwargs)
- [ClientTransport](https://gofastmcp.com/python-sdk/fastmcp-client-transports#clienttransport)
- [WSTransport](https://gofastmcp.com/python-sdk/fastmcp-client-transports#wstransport)
- [SSETransport](https://gofastmcp.com/python-sdk/fastmcp-client-transports#ssetransport)
- [StreamableHttpTransport](https://gofastmcp.com/python-sdk/fastmcp-client-transports#streamablehttptransport)
- [StdioTransport](https://gofastmcp.com/python-sdk/fastmcp-client-transports#stdiotransport)
- [PythonStdioTransport](https://gofastmcp.com/python-sdk/fastmcp-client-transports#pythonstdiotransport)
- [FastMCPStdioTransport](https://gofastmcp.com/python-sdk/fastmcp-client-transports#fastmcpstdiotransport)
- [NodeStdioTransport](https://gofastmcp.com/python-sdk/fastmcp-client-transports#nodestdiotransport)
- [UvxStdioTransport](https://gofastmcp.com/python-sdk/fastmcp-client-transports#uvxstdiotransport)
- [NpxStdioTransport](https://gofastmcp.com/python-sdk/fastmcp-client-transports#npxstdiotransport)
- [FastMCPTransport](https://gofastmcp.com/python-sdk/fastmcp-client-transports#fastmcptransport)
- [MCPConfigTransport](https://gofastmcp.com/python-sdk/fastmcp-client-transports#mcpconfigtransport)

Assistant

Responses are generated using AI and may contain mistakes.