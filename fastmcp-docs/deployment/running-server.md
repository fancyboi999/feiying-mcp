# Running Your FastMCP Server - FastMCP

**Source URL:** https://gofastmcp.com/deployment/running-server
**Generated:** 2025-06-30

**Description:** Learn how to run and deploy your FastMCP server using various transport protocols like STDIO, Streamable HTTP, and SSE.

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Deployment

Running Your FastMCP Server

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

FastMCP servers can be run in different ways depending on your application’s needs, from local command-line tools to persistent web services. This guide covers the primary methods for running your server, focusing on the available transport protocols: STDIO, Streamable HTTP, and SSE.

## [​](https://gofastmcp.com/deployment/running-server\#the-run-method)  The `run()` Method

FastMCP servers can be run directly from Python by calling the `run()` method on a `FastMCP` instance.

For maximum compatibility, it’s best practice to place the `run()` call within an `if __name__ == "__main__":` block. This ensures the server starts only when the script is executed directly, not when imported as a module.

my\_server.py

Copy

Ask AI

```
from fastmcp import FastMCP

mcp = FastMCP(name="MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    mcp.run()

```

You can now run this MCP server by executing `python my_server.py`.

MCP servers can be run with a variety of different transport options, depending on your application’s requirements. The `run()` method can take a `transport` argument and other transport-specific keyword arguments to configure how the server operates.

## [​](https://gofastmcp.com/deployment/running-server\#the-fastmcp-cli)  The FastMCP CLI

FastMCP also provides a command-line interface for running servers without modifying the source code. After installing FastMCP, you can run your server directly from the command line:

Copy

Ask AI

```
fastmcp run server.py

```

**Important**: When using `fastmcp run`, it **ignores** the `if __name__ == "__main__"` block entirely. Instead, it looks for a FastMCP object named `mcp`, `server`, or `app` and calls its `run()` method directly with the transport options you specify.

This means you can use `fastmcp run` to override the transport specified in your code, which is particularly useful for testing or changing deployment methods without modifying the code.

You can specify transport options and other configuration:

Copy

Ask AI

```
fastmcp run server.py --transport sse --port 9000

```

For development and testing, you can use the `dev` command to run your server with the MCP Inspector:

Copy

Ask AI

```
fastmcp dev server.py

```

See the [CLI documentation](https://gofastmcp.com/patterns/cli) for detailed information about all available commands and options.

### [​](https://gofastmcp.com/deployment/running-server\#passing-arguments-to-servers)  Passing Arguments to Servers

When servers accept command line arguments (using argparse, click, or other libraries), you can pass them after `--`:

Copy

Ask AI

```
fastmcp run config_server.py -- --config config.json
fastmcp run database_server.py -- --database-path /tmp/db.sqlite --debug

```

This is useful for servers that need configuration files, database paths, API keys, or other runtime options.

## [​](https://gofastmcp.com/deployment/running-server\#transport-options)  Transport Options

Below is a comparison of available transport options to help you choose the right one for your needs:

| Transport | Use Cases | Recommendation |
| --- | --- | --- |
| **STDIO** | Local tools, command-line scripts, and integrations with clients like Claude Desktop | Best for local tools and when clients manage server processes |
| **Streamable HTTP** | Web-based deployments, microservices, exposing MCP over a network | Recommended choice for web-based deployments |
| **SSE** | Existing web-based deployments that rely on SSE | Deprecated - prefer Streamable HTTP for new projects |

### [​](https://gofastmcp.com/deployment/running-server\#stdio)  STDIO

The STDIO transport is the default and most widely compatible option for local MCP server execution. It is ideal for local tools, command-line integrations, and clients like Claude Desktop. However, it has the disadvantage of having to run the MCP code locally, which can introduce security concerns with third-party servers.

STDIO is the default transport, so you don’t need to specify it when calling `run()`. However, you can specify it explicitly to make your intent clear:

Copy

Ask AI

```
from fastmcp import FastMCP

mcp = FastMCP()

if __name__ == "__main__":
    mcp.run(transport="stdio")

```

When using Stdio transport, you will typically _not_ run the server yourself as a separate process. Rather, your _clients_ will spin up a new server process for each session. As such, no additional configuration is required.

### [​](https://gofastmcp.com/deployment/running-server\#streamable-http)  Streamable HTTP

`New in version: 2.3.0`

Streamable HTTP is a modern, efficient transport for exposing your MCP server via HTTP. It is the recommended transport for web-based deployments.

To run a server using Streamable HTTP, you can use the `run()` method with the `transport` argument set to `"http"`. This will start a Uvicorn server on the default host ( `127.0.0.1`), port ( `8000`), and path ( `/mcp/`).

server.py

client.py

Copy

Ask AI

```
from fastmcp import FastMCP

mcp = FastMCP()

if __name__ == "__main__":
    mcp.run(transport="http")

```

For backward compatibility, wherever `"http"` is accepted as a transport name, you can also pass `"streamable-http"` as a fully supported alias. This is particularly useful when upgrading from FastMCP 1.x in the official Python SDK and FastMCP <= 2.9, where `"streamable-http"` was the standard name.

To customize the host, port, path, or log level, provide appropriate keyword arguments to the `run()` method.

server.py

client.py

Copy

Ask AI

```
from fastmcp import FastMCP

mcp = FastMCP()

if __name__ == "__main__":
    mcp.run(
        transport="http",
        host="127.0.0.1",
        port=4200,
        path="/my-custom-path",
        log_level="debug",
    )

```

### [​](https://gofastmcp.com/deployment/running-server\#sse)  SSE

The SSE transport is deprecated and may be removed in a future version.
New applications should use Streamable HTTP transport instead.

Server-Sent Events (SSE) is an HTTP-based protocol for server-to-client streaming. While FastMCP still supports SSE, it is deprecated and Streamable HTTP is preferred for new projects.

To run a server using SSE, you can use the `run()` method with the `transport` argument set to `"sse"`. This will start a Uvicorn server on the default host ( `127.0.0.1`), port ( `8000`), and with default SSE path ( `/sse/`) and message path ( `/messages/`).

server.py

client.py

Copy

Ask AI

```
from fastmcp import FastMCP

mcp = FastMCP()

if __name__ == "__main__":
    mcp.run(transport="sse")

```

Notice that the client in the above example uses an explicit `SSETransport` to connect to the server. FastMCP will attempt to infer the appropriate transport from the provided configuration, but HTTP URLs are assumed to be Streamable HTTP (as of FastMCP 2.3.0).

To customize the host, port, or log level, provide appropriate keyword arguments to the `run()` method. You can also adjust the SSE path (which clients should connect to) and the message POST endpoint (which clients use to send subsequent messages).

server.py

client.py

Copy

Ask AI

```
from fastmcp import FastMCP

mcp = FastMCP()

if __name__ == "__main__":
    mcp.run(
        transport="sse",
        host="127.0.0.1",
        port=4200,
        log_level="debug",
        path="/my-custom-sse-path",
    )

```

## [​](https://gofastmcp.com/deployment/running-server\#async-usage)  Async Usage

FastMCP provides both synchronous and asynchronous APIs for running your server. The `run()` method seen in previous examples is a synchronous method that internally uses `anyio.run()` to run the asynchronous server. For applications that are already running in an async context, FastMCP provides the `run_async()` method.

Copy

Ask AI

```
from fastmcp import FastMCP
import asyncio

mcp = FastMCP(name="MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

async def main():
    # Use run_async() in async contexts
    await mcp.run_async(transport="http")

if __name__ == "__main__":
    asyncio.run(main())

```

The `run()` method cannot be called from inside an async function because it already creates its own async event loop internally. If you attempt to call `run()` from inside an async function, you’ll get an error about the event loop already running.

Always use `run_async()` inside async functions and `run()` in synchronous contexts.

Both `run()` and `run_async()` accept the same transport arguments, so all the examples above apply to both methods.

## [​](https://gofastmcp.com/deployment/running-server\#custom-routes)  Custom Routes

You can also add custom web routes to your FastMCP server, which will be exposed alongside the MCP endpoint. To do so, use the `@custom_route` decorator. Note that this is less flexible than using a full ASGI framework, but can be useful for adding simple endpoints like health checks to your standalone server.

Copy

Ask AI

```
from fastmcp import FastMCP
from starlette.requests import Request
from starlette.responses import PlainTextResponse

mcp = FastMCP("MyServer")

@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    return PlainTextResponse("OK")

if __name__ == "__main__":
    mcp.run()

```

[Composition](https://gofastmcp.com/servers/composition) [ASGI Integration](https://gofastmcp.com/deployment/asgi)

On this page

- [The run() Method](https://gofastmcp.com/deployment/running-server#the-run-method)
- [The FastMCP CLI](https://gofastmcp.com/deployment/running-server#the-fastmcp-cli)
- [Passing Arguments to Servers](https://gofastmcp.com/deployment/running-server#passing-arguments-to-servers)
- [Transport Options](https://gofastmcp.com/deployment/running-server#transport-options)
- [STDIO](https://gofastmcp.com/deployment/running-server#stdio)
- [Streamable HTTP](https://gofastmcp.com/deployment/running-server#streamable-http)
- [SSE](https://gofastmcp.com/deployment/running-server#sse)
- [Async Usage](https://gofastmcp.com/deployment/running-server#async-usage)
- [Custom Routes](https://gofastmcp.com/deployment/running-server#custom-routes)

Assistant

Responses are generated using AI and may contain mistakes.