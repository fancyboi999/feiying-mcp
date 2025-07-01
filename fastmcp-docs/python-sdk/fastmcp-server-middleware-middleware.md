# middleware - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware
**Generated:** 2025-06-30

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

middleware

middleware

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware\#fastmcp-server-middleware-middleware)  `fastmcp.server.middleware.middleware`

## [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware\#make-middleware-wrapper)  `make_middleware_wrapper`

Copy

Ask AI

```
make_middleware_wrapper(middleware: Middleware, call_next: CallNext[T, R]) -> CallNext[T, R]

```

Create a wrapper that applies a single middleware to a context. The
closure bakes in the middleware and call\_next function, so it can be
passed to other functions that expect a call\_next function.

## [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware\#callnext)  `CallNext`

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware\#calltoolresult)  `CallToolResult`

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware\#listtoolsresult)  `ListToolsResult`

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware\#listresourcesresult)  `ListResourcesResult`

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware\#listresourcetemplatesresult)  `ListResourceTemplatesResult`

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware\#listpromptsresult)  `ListPromptsResult`

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware\#serverresultprotocol)  `ServerResultProtocol`

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware\#middlewarecontext)  `MiddlewareContext`

Unified context for all middleware operations.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware\#copy)  `copy`

Copy

Ask AI

```
copy(self, **kwargs: Any) -> MiddlewareContext[T]

```

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware\#middleware)  `Middleware`

Base class for FastMCP middleware with dispatching hooks.

[logging](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-logging) [rate\_limiting](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-rate_limiting)

On this page

- [fastmcp.server.middleware.middleware](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware#fastmcp-server-middleware-middleware)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware#functions)
- [make\_middleware\_wrapper](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware#make-middleware-wrapper)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware#classes)
- [CallNext](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware#callnext)
- [CallToolResult](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware#calltoolresult)
- [ListToolsResult](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware#listtoolsresult)
- [ListResourcesResult](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware#listresourcesresult)
- [ListResourceTemplatesResult](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware#listresourcetemplatesresult)
- [ListPromptsResult](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware#listpromptsresult)
- [ServerResultProtocol](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware#serverresultprotocol)
- [MiddlewareContext](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware#middlewarecontext)
- [copy](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware#copy)
- [Middleware](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-middleware#middleware)

Assistant

Responses are generated using AI and may contain mistakes.