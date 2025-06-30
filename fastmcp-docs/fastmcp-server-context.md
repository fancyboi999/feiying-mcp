# context - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-server-context
**Generated:** 2025-06-27

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.server

context

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-server-context\#fastmcp-server-context)  `fastmcp.server.context`

## [​](https://gofastmcp.com/python-sdk/fastmcp-server-context\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-context\#set-context)  `set_context`

Copy

Ask AI

```
set_context(context: Context) -> Generator[Context, None, None]

```

## [​](https://gofastmcp.com/python-sdk/fastmcp-server-context\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-context\#context)  `Context`

Context object providing access to MCP capabilities.

This provides a cleaner interface to MCP’s RequestContext functionality.
It gets injected into tool and resource functions that request it via type hints.

To use context in a tool function, add a parameter with the Context type annotation:

Copy

Ask AI

```
@server.tool
def my_tool(x: int, ctx: Context) -> str:
    # Log messages to the client
    ctx.info(f"Processing {x}")
    ctx.debug("Debug info")
    ctx.warning("Warning message")
    ctx.error("Error message")

    # Report progress
    ctx.report_progress(50, 100, "Processing")

    # Access resources
    data = ctx.read_resource("resource://data")

    # Get request info
    request_id = ctx.request_id
    client_id = ctx.client_id

    return str(x)

```

The context parameter name can be anything as long as it’s annotated with Context.
The context is optional - tools that don’t need it can omit the parameter.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-context\#request-context)  `request_context`

Copy

Ask AI

```
request_context(self) -> RequestContext

```

Access to the underlying request context.

If called outside of a request context, this will raise a ValueError.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-context\#client-id)  `client_id`

Copy

Ask AI

```
client_id(self) -> str | None

```

Get the client ID if available.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-context\#request-id)  `request_id`

Copy

Ask AI

```
request_id(self) -> str

```

Get the unique ID for this request.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-context\#session-id)  `session_id`

Copy

Ask AI

```
session_id(self) -> str | None

```

Get the MCP session ID for HTTP transports.

Returns the session ID that can be used as a key for session-based
data storage (e.g., Redis) to share data between tool calls within
the same client session.

**Returns:**

- The session ID for HTTP transports (SSE, StreamableHTTP), or None
- for stdio and in-memory transports which don’t use session IDs.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-context\#session)  `session`

Copy

Ask AI

```
session(self)

```

Access to the underlying session for advanced usage.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-context\#get-http-request)  `get_http_request`

Copy

Ask AI

```
get_http_request(self) -> Request

```

Get the active starlette request.

[in\_memory](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-in_memory) [dependencies](https://gofastmcp.com/python-sdk/fastmcp-server-dependencies)

On this page

- [fastmcp.server.context](https://gofastmcp.com/python-sdk/fastmcp-server-context#fastmcp-server-context)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-server-context#functions)
- [set\_context](https://gofastmcp.com/python-sdk/fastmcp-server-context#set-context)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-server-context#classes)
- [Context](https://gofastmcp.com/python-sdk/fastmcp-server-context#context)
- [request\_context](https://gofastmcp.com/python-sdk/fastmcp-server-context#request-context)
- [client\_id](https://gofastmcp.com/python-sdk/fastmcp-server-context#client-id)
- [request\_id](https://gofastmcp.com/python-sdk/fastmcp-server-context#request-id)
- [session\_id](https://gofastmcp.com/python-sdk/fastmcp-server-context#session-id)
- [session](https://gofastmcp.com/python-sdk/fastmcp-server-context#session)
- [get\_http\_request](https://gofastmcp.com/python-sdk/fastmcp-server-context#get-http-request)

Assistant

Responses are generated using AI and may contain mistakes.