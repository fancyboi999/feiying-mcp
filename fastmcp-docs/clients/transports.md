# Client Transports - FastMCP

**Source URL:** https://gofastmcp.com/clients/transports
**Generated:** 2025-06-30

**Description:** Understand the different ways FastMCP Clients can connect to servers.

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Clients

Client Transports

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

`New in version: 2.0.0`

The FastMCP `Client` relies on a `ClientTransport` object to handle the specifics of connecting to and communicating with an MCP server. FastMCP provides several built-in transport implementations for common connection methods.

While the `Client` often infers the correct transport automatically (see [Client Overview](https://gofastmcp.com/clients/client#transport-inference)), you can also instantiate transports explicitly for more control.

Clients are lightweight objects, so don’t hesitate to create new ones as needed. However, be mindful of the context management - each time you open a client context ( `async with client:`), a new connection or process starts. For best performance, keep client contexts open while performing multiple operations rather than repeatedly opening and closing them.

## [​](https://gofastmcp.com/clients/transports\#choosing-a-transport)  Choosing a Transport

Choose the transport that best fits your use case:

- **Connecting to Remote/Persistent Servers:** Use `StreamableHttpTransport` (recommended, default for HTTP URLs) or `SSETransport` (legacy option) for web-based deployments.

- **Local Development/Testing:** Use `FastMCPTransport` for in-memory, same-process testing of your FastMCP servers.

- **Running Local Servers:** Use `UvxStdioTransport` (Python/uv) or `NpxStdioTransport` (Node/npm) if you need to run MCP servers as packaged tools.


## [​](https://gofastmcp.com/clients/transports\#network-transports)  Network Transports

These transports connect to servers running over a network, typically long-running services accessible via URLs.

### [​](https://gofastmcp.com/clients/transports\#streamable-http)  Streamable HTTP

`New in version: 2.3.0`

Streamable HTTP is the recommended transport for web-based deployments, providing efficient bidirectional communication over HTTP.

#### [​](https://gofastmcp.com/clients/transports\#overview)  Overview

- **Class:** `fastmcp.client.transports.StreamableHttpTransport`
- **Inferred From:** URLs starting with `http://` or `https://` (default for HTTP URLs since v2.3.0) that do not contain `/sse/` in the path
- **Server Compatibility:** Works with FastMCP servers running in `http` mode

#### [​](https://gofastmcp.com/clients/transports\#basic-usage)  Basic Usage

The simplest way to use Streamable HTTP is to let the transport be inferred from a URL:

Copy

Ask AI

```
from fastmcp import Client
import asyncio

# The Client automatically uses StreamableHttpTransport for HTTP URLs
client = Client("https://example.com/mcp")

async def main():
    async with client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")

asyncio.run(main())

```

You can also explicitly instantiate the transport:

Copy

Ask AI

```
from fastmcp.client.transports import StreamableHttpTransport

transport = StreamableHttpTransport(url="https://example.com/mcp")
client = Client(transport)

```

#### [​](https://gofastmcp.com/clients/transports\#authentication-with-headers)  Authentication with Headers

For servers requiring authentication:

Copy

Ask AI

```
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

# Create transport with authentication headers
transport = StreamableHttpTransport(
    url="https://example.com/mcp",
    headers={"Authorization": "Bearer your-token-here"}
)

client = Client(transport)

```

### [​](https://gofastmcp.com/clients/transports\#sse-server-sent-events)  SSE (Server-Sent Events)

`New in version: 2.0.0`

Server-Sent Events (SSE) is a transport that allows servers to push data to clients over HTTP connections. While still supported, Streamable HTTP is now the recommended transport for new web-based deployments.

#### [​](https://gofastmcp.com/clients/transports\#overview-2)  Overview

- **Class:** `fastmcp.client.transports.SSETransport`
- **Inferred From:** HTTP URLs containing `/sse/` in the path
- **Server Compatibility:** Works with FastMCP servers running in `sse` mode

#### [​](https://gofastmcp.com/clients/transports\#basic-usage-2)  Basic Usage

The simplest way to use SSE is to let the transport be inferred from a URL with `/sse/` in the path:

Copy

Ask AI

```
from fastmcp import Client
import asyncio

# The Client automatically uses SSETransport for URLs containing /sse/ in the path
client = Client("https://example.com/sse")

async def main():
    async with client:
        tools = await client.list_tools()
        print(f"Available tools: {tools}")

asyncio.run(main())

```

You can also explicitly instantiate the transport for URLs that do not contain `/sse/` in the path or for more control:

Copy

Ask AI

```
from fastmcp.client.transports import SSETransport

transport = SSETransport(url="https://example.com/sse")
client = Client(transport)

```

#### [​](https://gofastmcp.com/clients/transports\#authentication-with-headers-2)  Authentication with Headers

SSE transport also supports custom headers for authentication:

Copy

Ask AI

```
from fastmcp import Client
from fastmcp.client.transports import SSETransport

# Create SSE transport with authentication headers
transport = SSETransport(
    url="https://example.com/sse",
    headers={"Authorization": "Bearer your-token-here"}
)

client = Client(transport)

```

#### [​](https://gofastmcp.com/clients/transports\#when-to-use-sse-vs-streamable-http)  When to Use SSE vs. Streamable HTTP

- **Use Streamable HTTP when:**
  - Setting up new deployments (recommended default)
  - You need bidirectional streaming
  - You’re connecting to FastMCP servers running in `http` mode
- **Use SSE when:**
  - Connecting to legacy FastMCP servers running in `sse` mode
  - Working with infrastructure optimized for Server-Sent Events

## [​](https://gofastmcp.com/clients/transports\#local-transports)  Local Transports

These transports manage an MCP server running as a subprocess, communicating with it via standard input (stdin) and standard output (stdout). This is the standard mechanism used by clients like Claude Desktop.

### [​](https://gofastmcp.com/clients/transports\#session-management)  Session Management

All stdio transports support a `keep_alive` parameter (default: `True`) that controls session persistence across multiple client context managers:

- **`keep_alive=True` (default)**: The subprocess and session are maintained between client context exits and re-entries. This improves performance when making multiple separate connections to the same server.
- **`keep_alive=False`**: A new subprocess is started for each client context, ensuring complete isolation between sessions.

When `keep_alive=True`, you can manually close the session using `await client.close()` if needed. This will terminate the subprocess and require a new one to be started on the next connection.

keep\_alive=True

keep\_alive=False

Copy

Ask AI

```
from fastmcp import Client

# Client with keep_alive=True (default)
client = Client("my_mcp_server.py")

async def example():
    # First session
    async with client:
        await client.ping()

    # Second session - uses the same subprocess
    async with client:
        await client.ping()

    # Manually close the session
    await client.close()

    # Third session - will start a new subprocess
    async with client:
        await client.ping()

asyncio.run(example())

```

### [​](https://gofastmcp.com/clients/transports\#python-stdio)  Python Stdio

- **Class:** `fastmcp.client.transports.PythonStdioTransport`
- **Inferred From:** Paths to `.py` files
- **Use Case:** Running a Python-based MCP server script in a subprocess

This is the most common way to interact with local FastMCP servers during development or when integrating with tools that expect to launch a server script.

Copy

Ask AI

```
from fastmcp import Client
from fastmcp.client.transports import PythonStdioTransport

server_script = "my_mcp_server.py" # Path to your server script

# Option 1: Inferred transport
client = Client(server_script)

# Option 2: Explicit transport with custom configuration
transport = PythonStdioTransport(
    script_path=server_script,
    python_cmd="/usr/bin/python3.11", # Optional: specify Python interpreter
    # args=["--some-server-arg"],      # Optional: pass arguments to the script
    # env={"MY_VAR": "value"},         # Optional: set environment variables
)
client = Client(transport)

async def main():
    async with client:
        tools = await client.list_tools()
        print(f"Connected via Python Stdio, found tools: {tools}")

asyncio.run(main())

```

The server script must include logic to start the MCP server and listen on stdio, typically via `mcp.run()` or `fastmcp.server.run()`. The Client only launches the script; it doesn’t inject the server logic.

### [​](https://gofastmcp.com/clients/transports\#node-js-stdio)  Node.js Stdio

- **Class:** `fastmcp.client.transports.NodeStdioTransport`
- **Inferred From:** Paths to `.js` files
- **Use Case:** Running a Node.js-based MCP server script in a subprocess

Similar to the Python transport, but for JavaScript servers.

Copy

Ask AI

```
from fastmcp import Client
from fastmcp.client.transports import NodeStdioTransport

node_server_script = "my_mcp_server.js" # Path to your Node.js server script

# Option 1: Inferred transport
client = Client(node_server_script)

# Option 2: Explicit transport
transport = NodeStdioTransport(
    script_path=node_server_script,
    node_cmd="node", # Optional: specify path to Node executable
)
client = Client(transport)

async def main():
    async with client:
        tools = await client.list_tools()
        print(f"Connected via Node.js Stdio, found tools: {tools}")

asyncio.run(main())

```

### [​](https://gofastmcp.com/clients/transports\#uvx-stdio-experimental)  UVX Stdio (Experimental)

- **Class:** `fastmcp.client.transports.UvxStdioTransport`
- **Inferred From:** Not automatically inferred
- **Use Case:** Running an MCP server packaged as a Python tool using [`uvx`](https://docs.astral.sh/uv/reference/cli/#uvx)

This is useful for executing MCP servers distributed as command-line tools or packages without installing them into your environment.

Copy

Ask AI

```
from fastmcp import Client
from fastmcp.client.transports import UvxStdioTransport

# Run a hypothetical 'cloud-analyzer-mcp' tool via uvx
transport = UvxStdioTransport(
    tool_name="cloud-analyzer-mcp",
    # from_package="cloud-analyzer-cli", # Optional: specify package if tool name differs
    # with_packages=["boto3", "requests"] # Optional: add dependencies
)
client = Client(transport)

async def main():
    async with client:
        result = await client.call_tool("analyze_bucket", {"name": "my-data"})
        print(f"Analysis result: {result}")

asyncio.run(main())

```

### [​](https://gofastmcp.com/clients/transports\#npx-stdio-experimental)  NPX Stdio (Experimental)

- **Class:** `fastmcp.client.transports.NpxStdioTransport`
- **Inferred From:** Not automatically inferred
- **Use Case:** Running an MCP server packaged as an NPM package using `npx`

Similar to `UvxStdioTransport`, but for the Node.js ecosystem.

Copy

Ask AI

```
from fastmcp import Client
from fastmcp.client.transports import NpxStdioTransport

# Run an MCP server from an NPM package
transport = NpxStdioTransport(
    package="mcp-server-package",
    # args=["--port", "stdio"] # Optional: pass arguments to the package
)
client = Client(transport)

async def main():
    async with client:
        result = await client.call_tool("get_npm_data", {})
        print(f"Result: {result}")

asyncio.run(main())

```

## [​](https://gofastmcp.com/clients/transports\#in-memory-transports)  In-Memory Transports

### [​](https://gofastmcp.com/clients/transports\#fastmcp-transport)  FastMCP Transport

- **Class:** `fastmcp.client.transports.FastMCPTransport`
- **Inferred From:** An instance of `fastmcp.server.FastMCP` or a **FastMCP 1.0 server** ( `mcp.server.fastmcp.FastMCP`)
- **Use Case:** Connecting directly to a FastMCP server instance in the same Python process

This is extremely useful for testing your FastMCP servers.

Copy

Ask AI

```
from fastmcp import FastMCP, Client
import asyncio

# 1. Create your FastMCP server instance
server = FastMCP(name="InMemoryServer")

@server.tool
def ping():
    return "pong"

# 2. Create a client pointing directly to the server instance
client = Client(server)  # Transport is automatically inferred

async def main():
    async with client:
        result = await client.call_tool("ping")
        print(f"In-memory call result: {result}")

asyncio.run(main())

```

Communication happens through efficient in-memory queues, making it very fast and ideal for unit testing.

## [​](https://gofastmcp.com/clients/transports\#configuration-based-transports)  Configuration-Based Transports

### [​](https://gofastmcp.com/clients/transports\#mcpconfig-transport)  MCPConfig Transport

`New in version: 2.4.0`

- **Class:** `fastmcp.client.transports.MCPConfigTransport`
- **Inferred From:** An instance of `MCPConfig` or a dictionary matching the MCPConfig schema
- **Use Case:** Connecting to one or more MCP servers defined in a configuration object

MCPConfig follows an emerging standard for MCP server configuration but is subject to change as the specification evolves. The standard supports both local servers (running via stdio) and remote servers (accessed via HTTP).

Copy

Ask AI

```
from fastmcp import Client

# Configuration for multiple MCP servers (both local and remote)
config = {
    "mcpServers": {
        # Remote HTTP server
        "weather": {
            "url": "https://weather-api.example.com/mcp",
            "transport": "http"
        },
        # Local stdio server
        "assistant": {
            "command": "python",
            "args": ["./assistant_server.py"],
            "env": {"DEBUG": "true"}
        },
        # Another remote server
        "calendar": {
            "url": "https://calendar-api.example.com/mcp",
            "transport": "http"
        }
    }
}

# Create a transport from the config (happens automatically with Client)
client = Client(config)

async def main():
    async with client:
        # Tools are accessible with server name prefixes
        weather = await client.call_tool("weather_get_forecast", {"city": "London"})
        answer = await client.call_tool("assistant_answer_question", {"query": "What is MCP?"})
        events = await client.call_tool("calendar_list_events", {"date": "2023-06-01"})

        # Resources use prefixed URI paths
        icons = await client.read_resource("weather://weather/icons/sunny")
        docs = await client.read_resource("resource://assistant/docs/mcp")

asyncio.run(main())

```

If your configuration has only a single server, the client will connect directly to that server without any prefixing. This makes it convenient to switch between single and multi-server configurations without changing your client code.

The MCPConfig format is an emerging standard for MCP server configuration and may change as the MCP ecosystem evolves. While FastMCP aims to maintain compatibility with future versions, be aware that field names or structure might change.

[Roots](https://gofastmcp.com/clients/roots) [OAuth](https://gofastmcp.com/clients/auth/oauth)

On this page

- [Choosing a Transport](https://gofastmcp.com/clients/transports#choosing-a-transport)
- [Network Transports](https://gofastmcp.com/clients/transports#network-transports)
- [Streamable HTTP](https://gofastmcp.com/clients/transports#streamable-http)
- [Overview](https://gofastmcp.com/clients/transports#overview)
- [Basic Usage](https://gofastmcp.com/clients/transports#basic-usage)
- [Authentication with Headers](https://gofastmcp.com/clients/transports#authentication-with-headers)
- [SSE (Server-Sent Events)](https://gofastmcp.com/clients/transports#sse-server-sent-events)
- [Overview](https://gofastmcp.com/clients/transports#overview-2)
- [Basic Usage](https://gofastmcp.com/clients/transports#basic-usage-2)
- [Authentication with Headers](https://gofastmcp.com/clients/transports#authentication-with-headers-2)
- [When to Use SSE vs. Streamable HTTP](https://gofastmcp.com/clients/transports#when-to-use-sse-vs-streamable-http)
- [Local Transports](https://gofastmcp.com/clients/transports#local-transports)
- [Session Management](https://gofastmcp.com/clients/transports#session-management)
- [Python Stdio](https://gofastmcp.com/clients/transports#python-stdio)
- [Node.js Stdio](https://gofastmcp.com/clients/transports#node-js-stdio)
- [UVX Stdio (Experimental)](https://gofastmcp.com/clients/transports#uvx-stdio-experimental)
- [NPX Stdio (Experimental)](https://gofastmcp.com/clients/transports#npx-stdio-experimental)
- [In-Memory Transports](https://gofastmcp.com/clients/transports#in-memory-transports)
- [FastMCP Transport](https://gofastmcp.com/clients/transports#fastmcp-transport)
- [Configuration-Based Transports](https://gofastmcp.com/clients/transports#configuration-based-transports)
- [MCPConfig Transport](https://gofastmcp.com/clients/transports#mcpconfig-transport)

Assistant

Responses are generated using AI and may contain mistakes.