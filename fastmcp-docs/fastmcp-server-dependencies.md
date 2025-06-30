# dependencies - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-server-dependencies
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

dependencies

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-server-dependencies\#fastmcp-server-dependencies)  `fastmcp.server.dependencies`

## [​](https://gofastmcp.com/python-sdk/fastmcp-server-dependencies\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-dependencies\#get-context)  `get_context`

Copy

Ask AI

```
get_context() -> Context

```

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-dependencies\#get-http-request)  `get_http_request`

Copy

Ask AI

```
get_http_request() -> Request

```

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-dependencies\#get-http-headers)  `get_http_headers`

Copy

Ask AI

```
get_http_headers(include_all: bool = False) -> dict[str, str]

```

Extract headers from the current HTTP request if available.

Never raises an exception, even if there is no active HTTP request (in which case
an empty dict is returned).

By default, strips problematic headers like `content-length` that cause issues if forwarded to downstream clients.
If `include_all` is True, all headers are returned.

[context](https://gofastmcp.com/python-sdk/fastmcp-server-context) [http](https://gofastmcp.com/python-sdk/fastmcp-server-http)

On this page

- [fastmcp.server.dependencies](https://gofastmcp.com/python-sdk/fastmcp-server-dependencies#fastmcp-server-dependencies)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-server-dependencies#functions)
- [get\_context](https://gofastmcp.com/python-sdk/fastmcp-server-dependencies#get-context)
- [get\_http\_request](https://gofastmcp.com/python-sdk/fastmcp-server-dependencies#get-http-request)
- [get\_http\_headers](https://gofastmcp.com/python-sdk/fastmcp-server-dependencies#get-http-headers)

Assistant

Responses are generated using AI and may contain mistakes.