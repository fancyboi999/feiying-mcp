# Server Logging - FastMCP

**Source URL:** https://gofastmcp.com/clients/logging
**Generated:** 2025-06-27

**Description:** Receive and handle log messages from MCP servers.

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Advanced Features

Server Logging

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

`New in version: 2.0.0`

MCP servers can emit log messages to clients. The client can handle these logs through a log handler callback.

## [​](https://gofastmcp.com/clients/logging\#log-handler)  Log Handler

Provide a `log_handler` function when creating the client:

Copy

Ask AI

```
from fastmcp import Client
from fastmcp.client.logging import LogMessage

async def log_handler(message: LogMessage):
    level = message.level.upper()
    logger = message.logger or 'server'
    data = message.data
    print(f"[{level}] {logger}: {data}")

client = Client(
    "my_mcp_server.py",
    log_handler=log_handler,
)

```

### [​](https://gofastmcp.com/clients/logging\#handler-parameters)  Handler Parameters

The `log_handler` is called every time a log message is received. It receives a `LogMessage` object:

## Log Handler Parameters

[​](https://gofastmcp.com/clients/logging#param-log-message)

LogMessage

Log Message Object

Show attributes

[​](https://gofastmcp.com/clients/logging#param-level)

level

Literal\["debug", "info", "notice", "warning", "error", "critical", "alert", "emergency"\]

The log level

[​](https://gofastmcp.com/clients/logging#param-logger)

logger

str \| None

The logger name (optional, may be None)

[​](https://gofastmcp.com/clients/logging#param-data)

data

Any

The actual log message content

Copy

Ask AI

```
async def detailed_log_handler(message: LogMessage):
    if message.level == "error":
        print(f"ERROR: {message.data}")
    elif message.level == "warning":
        print(f"WARNING: {message.data}")
    else:
        print(f"{message.level.upper()}: {message.data}")

```

## [​](https://gofastmcp.com/clients/logging\#default-log-handling)  Default Log Handling

If you don’t provide a custom `log_handler`, FastMCP uses a default handler that emits a DEBUG-level FastMCP log for every log message received from the server, which is useful for visibility without polluting your own logs.

Copy

Ask AI

```
client = Client("my_mcp_server.py")

async with client:
    # Server logs will be emitted at DEBUG level automatically
    await client.call_tool("some_tool")

```

[Prompts](https://gofastmcp.com/clients/prompts) [Progress](https://gofastmcp.com/clients/progress)

On this page

- [Log Handler](https://gofastmcp.com/clients/logging#log-handler)
- [Handler Parameters](https://gofastmcp.com/clients/logging#handler-parameters)
- [Default Log Handling](https://gofastmcp.com/clients/logging#default-log-handling)

Assistant

Responses are generated using AI and may contain mistakes.