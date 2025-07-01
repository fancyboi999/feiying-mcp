# HTTP Requests - FastMCP

**Source URL:** https://gofastmcp.com/patterns/http-requests
**Generated:** 2025-06-30

**Description:** Accessing and using HTTP requests in FastMCP servers

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Patterns

HTTP Requests

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

`New in version: 2.2.11`

## [​](https://gofastmcp.com/patterns/http-requests\#overview)  Overview

When running FastMCP as a web server, your MCP tools, resources, and prompts might need to access the underlying HTTP request information, such as headers, client IP, or query parameters.

FastMCP provides a clean way to access HTTP request information through a dependency function.

## [​](https://gofastmcp.com/patterns/http-requests\#accessing-http-requests)  Accessing HTTP Requests

The recommended way to access the current HTTP request is through the `get_http_request()` dependency function:

Copy

Ask AI

```
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_request
from starlette.requests import Request

mcp = FastMCP(name="HTTP Request Demo")

@mcp.tool
async def user_agent_info() -> dict:
    """Return information about the user agent."""
    # Get the HTTP request
    request: Request = get_http_request()

    # Access request data
    user_agent = request.headers.get("user-agent", "Unknown")
    client_ip = request.client.host if request.client else "Unknown"

    return {
        "user_agent": user_agent,
        "client_ip": client_ip,
        "path": request.url.path,
    }

```

This approach works anywhere within a request’s execution flow, not just within your MCP function. It’s useful when:

1. You need access to HTTP information in helper functions
2. You’re calling nested functions that need HTTP request data
3. You’re working with middleware or other request processing code

## [​](https://gofastmcp.com/patterns/http-requests\#accessing-http-headers-only)  Accessing HTTP Headers Only

If you only need request headers and want to avoid potential errors, you can use the `get_http_headers()` helper:

Copy

Ask AI

```
from fastmcp import FastMCP
from fastmcp.server.dependencies import get_http_headers

mcp = FastMCP(name="Headers Demo")

@mcp.tool
async def safe_header_info() -> dict:
    """Safely get header information without raising errors."""
    # Get headers (returns empty dict if no request context)
    headers = get_http_headers()

    # Get authorization header
    auth_header = headers.get("authorization", "")
    is_bearer = auth_header.startswith("Bearer ")

    return {
        "user_agent": headers.get("user-agent", "Unknown"),
        "content_type": headers.get("content-type", "Unknown"),
        "has_auth": bool(auth_header),
        "auth_type": "Bearer" if is_bearer else "Other" if auth_header else "None",
        "headers_count": len(headers)
    }

```

By default, `get_http_headers()` excludes problematic headers like `host` and `content-length`. To include all headers, use `get_http_headers(include_all=True)`.

## [​](https://gofastmcp.com/patterns/http-requests\#important-notes)  Important Notes

- HTTP requests are only available when FastMCP is running as part of a web application
- Accessing the HTTP request with `get_http_request()` outside of a web request context will raise a `RuntimeError`
- The `get_http_headers()` function **never raises errors** \- it returns an empty dict when no request context is available
- The `get_http_request()` function returns a standard [Starlette Request](https://www.starlette.io/requests/) object

[Decorating Methods](https://gofastmcp.com/patterns/decorating-methods) [Testing](https://gofastmcp.com/patterns/testing)

On this page

- [Overview](https://gofastmcp.com/patterns/http-requests#overview)
- [Accessing HTTP Requests](https://gofastmcp.com/patterns/http-requests#accessing-http-requests)
- [Accessing HTTP Headers Only](https://gofastmcp.com/patterns/http-requests#accessing-http-headers-only)
- [Important Notes](https://gofastmcp.com/patterns/http-requests#important-notes)

Assistant

Responses are generated using AI and may contain mistakes.