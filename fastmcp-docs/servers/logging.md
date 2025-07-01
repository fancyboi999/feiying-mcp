# Server Logging - FastMCP

**Source URL:** https://gofastmcp.com/servers/logging
**Generated:** 2025-06-30

**Description:** Send log messages back to MCP clients through the context.

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Advanced Features

Server Logging

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

This documentation covers **MCP client logging** \- sending messages from your server to MCP clients. For standard server-side logging (e.g., writing to files, console), use `fastmcp.utilities.logging.get_logger()` or Python’s built-in `logging` module.

Server logging allows MCP tools to send debug, info, warning, and error messages back to the client. This provides visibility into function execution and helps with debugging during development and operation.

## [​](https://gofastmcp.com/servers/logging\#why-use-server-logging%3F)  Why Use Server Logging?

Server logging is essential for:

- **Debugging**: Send detailed execution information to help diagnose issues
- **Progress visibility**: Keep users informed about what the tool is doing
- **Error reporting**: Communicate problems and their context to clients
- **Audit trails**: Create records of tool execution for compliance or analysis

Unlike standard Python logging, MCP server logging sends messages directly to the client, making them visible in the client’s interface or logs.

### [​](https://gofastmcp.com/servers/logging\#basic-usage)  Basic Usage

Use the context logging methods within any tool function:

Copy

Ask AI

```
from fastmcp import FastMCP, Context

mcp = FastMCP("LoggingDemo")

@mcp.tool
async def analyze_data(data: list[float], ctx: Context) -> dict:
    """Analyze numerical data with comprehensive logging."""
    await ctx.debug("Starting analysis of numerical data")
    await ctx.info(f"Analyzing {len(data)} data points")

    try:
        if not data:
            await ctx.warning("Empty data list provided")
            return {"error": "Empty data list"}

        result = sum(data) / len(data)
        await ctx.info(f"Analysis complete, average: {result}")
        return {"average": result, "count": len(data)}

    except Exception as e:
        await ctx.error(f"Analysis failed: {str(e)}")
        raise

```

## [​](https://gofastmcp.com/servers/logging\#logging-methods)  Logging Methods

## Context Logging Methods

[​](https://gofastmcp.com/servers/logging#param-ctx-debug)

ctx.debug

async method

Send debug-level messages for detailed execution information

Show parameters

[​](https://gofastmcp.com/servers/logging#param-message)

message

str

The debug message to send to the client

[​](https://gofastmcp.com/servers/logging#param-ctx-info)

ctx.info

async method

Send informational messages about normal execution

Show parameters

[​](https://gofastmcp.com/servers/logging#param-message-1)

message

str

The information message to send to the client

[​](https://gofastmcp.com/servers/logging#param-ctx-warning)

ctx.warning

async method

Send warning messages for potential issues that didn’t prevent execution

Show parameters

[​](https://gofastmcp.com/servers/logging#param-message-2)

message

str

The warning message to send to the client

[​](https://gofastmcp.com/servers/logging#param-ctx-error)

ctx.error

async method

Send error messages for problems that occurred during execution

Show parameters

[​](https://gofastmcp.com/servers/logging#param-message-3)

message

str

The error message to send to the client

[​](https://gofastmcp.com/servers/logging#param-ctx-log)

ctx.log

async method

Generic logging method with custom level and logger name

Show parameters

[​](https://gofastmcp.com/servers/logging#param-level)

level

Literal\['debug', 'info', 'warning', 'error'\]

The log level for the message

[​](https://gofastmcp.com/servers/logging#param-message-4)

message

str

The message to send to the client

[​](https://gofastmcp.com/servers/logging#param-logger-name)

logger\_name

str \| None

default:"None"

Optional custom logger name for categorizing messages

## [​](https://gofastmcp.com/servers/logging\#log-levels)  Log Levels

### [​](https://gofastmcp.com/servers/logging\#debug)  Debug

Use for detailed information that’s typically only useful when diagnosing problems:

Copy

Ask AI

```
@mcp.tool
async def process_file(file_path: str, ctx: Context) -> str:
    """Process a file with detailed debug logging."""
    await ctx.debug(f"Starting to process file: {file_path}")
    await ctx.debug("Checking file permissions")

    # File processing logic
    await ctx.debug("File processing completed successfully")
    return "File processed"

```

### [​](https://gofastmcp.com/servers/logging\#info)  Info

Use for general information about normal program execution:

Copy

Ask AI

```
@mcp.tool
async def backup_database(ctx: Context) -> str:
    """Backup database with progress information."""
    await ctx.info("Starting database backup")
    await ctx.info("Connecting to database")
    await ctx.info("Backup completed successfully")
    return "Database backed up"

```

### [​](https://gofastmcp.com/servers/logging\#warning)  Warning

Use for potentially harmful situations that don’t prevent execution:

Copy

Ask AI

```
@mcp.tool
async def validate_config(config: dict, ctx: Context) -> dict:
    """Validate configuration with warnings for deprecated options."""
    if "old_api_key" in config:
        await ctx.warning("Using deprecated 'old_api_key' field. Please use 'api_key' instead")

    if config.get("timeout", 30) > 300:
        await ctx.warning("Timeout value is very high (>5 minutes), this may cause issues")

    return {"status": "valid", "warnings": "see logs"}

```

### [​](https://gofastmcp.com/servers/logging\#error)  Error

Use for error events that might still allow the application to continue:

Copy

Ask AI

```
@mcp.tool
async def batch_process(items: list[str], ctx: Context) -> dict:
    """Process multiple items, logging errors for failed items."""
    successful = 0
    failed = 0

    for item in items:
        try:
            # Process item
            successful += 1
        except Exception as e:
            await ctx.error(f"Failed to process item '{item}': {str(e)}")
            failed += 1

    return {"successful": successful, "failed": failed}

```

## [​](https://gofastmcp.com/servers/logging\#client-handling)  Client Handling

Log messages are sent to the client through the MCP protocol. How clients handle these messages depends on their implementation:

- **Development clients**: May display logs in real-time for debugging
- **Production clients**: May store logs for later analysis or display to users
- **Integration clients**: May forward logs to external logging systems

See [Client Logging](https://gofastmcp.com/clients/logging) for details on how clients can handle server log messages.

[Elicitation](https://gofastmcp.com/servers/elicitation) [Progress](https://gofastmcp.com/servers/progress)

On this page

- [Why Use Server Logging?](https://gofastmcp.com/servers/logging#why-use-server-logging%3F)
- [Basic Usage](https://gofastmcp.com/servers/logging#basic-usage)
- [Logging Methods](https://gofastmcp.com/servers/logging#logging-methods)
- [Log Levels](https://gofastmcp.com/servers/logging#log-levels)
- [Debug](https://gofastmcp.com/servers/logging#debug)
- [Info](https://gofastmcp.com/servers/logging#info)
- [Warning](https://gofastmcp.com/servers/logging#warning)
- [Error](https://gofastmcp.com/servers/logging#error)
- [Client Handling](https://gofastmcp.com/servers/logging#client-handling)

Assistant

Responses are generated using AI and may contain mistakes.