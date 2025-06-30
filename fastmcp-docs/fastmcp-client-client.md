# client - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-client-client
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

client

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-client-client\#fastmcp-client-client)  `fastmcp.client.client`

## [​](https://gofastmcp.com/python-sdk/fastmcp-client-client\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-client\#client)  `Client`

MCP client that delegates connection management to a Transport instance.

The Client class is responsible for MCP protocol logic, while the Transport
handles connection establishment and management. Client provides methods for
working with resources, prompts, tools and other MCP capabilities.

**Args:**

- `transport`: Connection source specification, which can be:
- ClientTransport: Direct transport instance
- FastMCP: In-process FastMCP server
- AnyUrl \| str: URL to connect to
- Path: File path for local socket
- MCPConfig: MCP server configuration
- dict: Transport configuration
- `roots`: Optional RootsList or RootsHandler for filesystem access
- `sampling_handler`: Optional handler for sampling requests
- `log_handler`: Optional handler for log messages
- `message_handler`: Optional handler for protocol messages
- `progress_handler`: Optional handler for progress notifications
- `timeout`: Optional timeout for requests (seconds or timedelta)
- `init_timeout`: Optional timeout for initial connection (seconds or timedelta).
Set to 0 to disable. If None, uses the value in the FastMCP global settings.

**Examples:**

\# Connect to FastMCP server client =

Copy

Ask AI

```
Client("http://localhost:8080")

async with client:
    # List available resources resources = await client.list_resources()

    # Call a tool result = await client.call_tool("my_tool", {"param":
    "value"})

```

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-client-client\#session)  `session`

Copy

Ask AI

```
session(self) -> ClientSession

```

Get the current active session. Raises RuntimeError if not connected.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-client-client\#initialize-result)  `initialize_result`

Copy

Ask AI

```
initialize_result(self) -> mcp.types.InitializeResult

```

Get the result of the initialization request.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-client-client\#set-roots)  `set_roots`

Copy

Ask AI

```
set_roots(self, roots: RootsList | RootsHandler) -> None

```

Set the roots for the client. This does not automatically call `send_roots_list_changed`.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-client-client\#set-sampling-callback)  `set_sampling_callback`

Copy

Ask AI

```
set_sampling_callback(self, sampling_callback: SamplingHandler) -> None

```

Set the sampling callback for the client.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-client-client\#is-connected)  `is_connected`

Copy

Ask AI

```
is_connected(self) -> bool

```

Check if the client is currently connected.

[oauth](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth) [logging](https://gofastmcp.com/python-sdk/fastmcp-client-logging)

On this page

- [fastmcp.client.client](https://gofastmcp.com/python-sdk/fastmcp-client-client#fastmcp-client-client)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-client-client#classes)
- [Client](https://gofastmcp.com/python-sdk/fastmcp-client-client#client)
- [session](https://gofastmcp.com/python-sdk/fastmcp-client-client#session)
- [initialize\_result](https://gofastmcp.com/python-sdk/fastmcp-client-client#initialize-result)
- [set\_roots](https://gofastmcp.com/python-sdk/fastmcp-client-client#set-roots)
- [set\_sampling\_callback](https://gofastmcp.com/python-sdk/fastmcp-client-client#set-sampling-callback)
- [is\_connected](https://gofastmcp.com/python-sdk/fastmcp-client-client#is-connected)

Assistant

Responses are generated using AI and may contain mistakes.