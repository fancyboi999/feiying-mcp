# logging - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-utilities-logging
**Generated:** 2025-06-27

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.utilities

logging

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-logging\#fastmcp-utilities-logging)  `fastmcp.utilities.logging`

Logging utilities for FastMCP.

## [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-logging\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-logging\#get-logger)  `get_logger`

Copy

Ask AI

```
get_logger(name: str) -> logging.Logger

```

Get a logger nested under FastMCP namespace.

**Args:**

- `name`: the name of the logger, which will be prefixed with ‘FastMCP.’

**Returns:**

- a configured logger instance

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-logging\#configure-logging)  `configure_logging`

Copy

Ask AI

```
configure_logging(level: Literal['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'] | int = 'INFO', logger: logging.Logger | None = None, enable_rich_tracebacks: bool = True) -> None

```

Configure logging for FastMCP.

**Args:**

- `logger`: the logger to configure
- `level`: the log level to use

[json\_schema](https://gofastmcp.com/python-sdk/fastmcp-utilities-json_schema) [mcp\_config](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config)

On this page

- [fastmcp.utilities.logging](https://gofastmcp.com/python-sdk/fastmcp-utilities-logging#fastmcp-utilities-logging)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-utilities-logging#functions)
- [get\_logger](https://gofastmcp.com/python-sdk/fastmcp-utilities-logging#get-logger)
- [configure\_logging](https://gofastmcp.com/python-sdk/fastmcp-utilities-logging#configure-logging)

Assistant

Responses are generated using AI and may contain mistakes.