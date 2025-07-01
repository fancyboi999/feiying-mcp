# error_handling - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-server-middleware-error_handling
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

error\_handling

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-error_handling\#fastmcp-server-middleware-error-handling)  `fastmcp.server.middleware.error_handling`

Error handling middleware for consistent error responses and tracking.

## [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-error_handling\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-error_handling\#errorhandlingmiddleware)  `ErrorHandlingMiddleware`

Middleware that provides consistent error handling and logging.

Catches exceptions, logs them appropriately, and converts them to
proper MCP error responses. Also tracks error patterns for monitoring.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-error_handling\#get-error-stats)  `get_error_stats`

Copy

Ask AI

```
get_error_stats(self) -> dict[str, int]

```

Get error statistics for monitoring.

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-error_handling\#retrymiddleware)  `RetryMiddleware`

Middleware that implements automatic retry logic for failed requests.

Retries requests that fail with transient errors, using exponential
backoff to avoid overwhelming the server or external dependencies.

[\_\_init\_\_](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-__init__) [logging](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-logging)

On this page

- [fastmcp.server.middleware.error\_handling](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-error_handling#fastmcp-server-middleware-error-handling)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-error_handling#classes)
- [ErrorHandlingMiddleware](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-error_handling#errorhandlingmiddleware)
- [get\_error\_stats](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-error_handling#get-error-stats)
- [RetryMiddleware](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-error_handling#retrymiddleware)

Assistant

Responses are generated using AI and may contain mistakes.