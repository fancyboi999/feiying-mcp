# FastMCP CLI - FastMCP

**Source URL:** https://gofastmcp.com/patterns/cli
**Generated:** 2025-06-27

**Description:** Learn how to use the FastMCP command-line interface

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Patterns

FastMCP CLI

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

FastMCP provides a command-line interface (CLI) that makes it easy to run, develop, and install your MCP servers. The CLI is automatically installed when you install FastMCP.

Copy

Ask AI

```
fastmcp --help

```

## [​](https://gofastmcp.com/patterns/cli\#commands-overview)  Commands Overview

| Command | Purpose | Dependency Management |
| --- | --- | --- |
| `run` | Run a FastMCP server directly | Uses your current environment; you are responsible for ensuring all dependencies are available |
| `dev` | Run a server with the MCP Inspector for testing | Creates an isolated environment; dependencies must be explicitly specified with `--with` and/or `--with-editable` |
| `install` | Install a server in the Claude desktop app | Creates an isolated environment; dependencies must be explicitly specified with `--with` and/or `--with-editable` |
| `inspect` | Generate a JSON report about a FastMCP server | Uses your current environment; you are responsible for ensuring all dependencies are available |
| `version` | Display version information | N/A |

## [​](https://gofastmcp.com/patterns/cli\#command-details)  Command Details

### [​](https://gofastmcp.com/patterns/cli\#run)  `run`

Run a FastMCP server directly or proxy a remote server.

Copy

Ask AI

```
fastmcp run server.py

```

This command runs the server directly in your current Python environment. You are responsible for ensuring all dependencies are available.

#### [​](https://gofastmcp.com/patterns/cli\#options)  Options

| Option | Flag | Description |
| --- | --- | --- |
| Transport | `--transport`, `-t` | Transport protocol to use ( `stdio`, `http`, or `sse`) |
| Host | `--host` | Host to bind to when using http transport (default: 127.0.0.1) |
| Port | `--port`, `-p` | Port to bind to when using http transport (default: 8000) |
| Log Level | `--log-level`, `-l` | Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL) |

#### [​](https://gofastmcp.com/patterns/cli\#server-specification)  Server Specification

`New in version: 2.3.5`

The server can be specified in three ways:

1. `server.py` \- imports the module and looks for a FastMCP object named `mcp`, `server`, or `app`. Errors if no such object is found.
2. `server.py:custom_name` \- imports and uses the specified server object
3. `http://server-url/path` or `https://server-url/path` \- connects to a remote server and creates a proxy

When using `fastmcp run` with a local file, it **ignores** the `if __name__ == "__main__"` block entirely. Instead, it finds your server object and calls its `run()` method directly with the transport options you specify. This means you can use `fastmcp run` to override the transport specified in your code.

For example, if your code contains:

Copy

Ask AI

```
# server.py
from fastmcp import FastMCP

mcp = FastMCP("MyServer")

@mcp.tool
def hello(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    # This is ignored when using `fastmcp run`!
    mcp.run(transport="stdio")

```

You can run it with Streamable HTTP transport regardless of what’s in the `__main__` block:

Copy

Ask AI

```
fastmcp run server.py --transport http --port 8000

```

**Examples**

Copy

Ask AI

```
# Run a local server with Streamable HTTP transport on a custom port
fastmcp run server.py --transport http --port 8000

# Connect to a remote server and proxy as a stdio server
fastmcp run https://example.com/mcp-server

# Connect to a remote server with specified log level
fastmcp run https://example.com/mcp-server --log-level DEBUG

```

### [​](https://gofastmcp.com/patterns/cli\#dev)  `dev`

Run a MCP server with the [MCP Inspector](https://github.com/modelcontextprotocol/inspector) for testing.

Copy

Ask AI

```
fastmcp dev server.py

```

This command runs your server in an isolated environment. All dependencies must be explicitly specified using the `--with` and/or `--with-editable` options.

The `dev` command is a shortcut for testing a server over STDIO only. When the Inspector launches, you may need to:

1. Select “STDIO” from the transport dropdown
2. Connect manually

This command does not support HTTP testing. To test a server over Streamable HTTP or SSE:

1. Start your server manually with the appropriate transport using either the command line:







Copy







Ask AI











```
fastmcp run server.py --transport http

```







or by setting the transport in your code:







Copy







Ask AI











```
python server.py  # Assuming your __main__ block sets Streamable HTTP transport

```

2. Open the MCP Inspector separately and connect to your running server

#### [​](https://gofastmcp.com/patterns/cli\#options-2)  Options

| Option | Flag | Description |
| --- | --- | --- |
| Editable Package | `--with-editable`, `-e` | Directory containing pyproject.toml to install in editable mode |
| Additional Packages | `--with` | Additional packages to install (can be used multiple times) |
| Inspector Version | `--inspector-version` | Version of the MCP Inspector to use |
| UI Port | `--ui-port` | Port for the MCP Inspector UI |
| Server Port | `--server-port` | Port for the MCP Inspector Proxy server |

**Example**

Copy

Ask AI

```
# Run dev server with editable mode and additional packages
fastmcp dev server.py -e . --with pandas --with matplotlib

```

### [​](https://gofastmcp.com/patterns/cli\#install)  `install`

Install a MCP server in the Claude desktop app.

Copy

Ask AI

```
fastmcp install server.py

```

Note that for security reasons, Claude runs every MCP server in a completely isolated environment. Therefore, all dependencies must be explicitly specified using the `--with` and/or `--with-editable` options (following `uv` conventions) or by attaching them to your server in code via the `dependencies` parameter.

- **`uv` must be installed and available in your system PATH**. Claude Desktop runs in its own isolated environment and needs `uv` to manage dependencies.
- **On macOS, it is recommended to install `uv` globally with Homebrew** so that Claude Desktop will detect it: `brew install uv`. Installing `uv` with other methods may not make it accessible to Claude Desktop.

The `install` command currently only sets up servers for STDIO transport. When installed in the Claude desktop app, your server will be run using STDIO regardless of any transport configuration in your code.

#### [​](https://gofastmcp.com/patterns/cli\#server-specification-2)  Server Specification

The `install` command supports the same `file.py:object` notation as the `run` command:

1. `server.py` \- imports the module and looks for a FastMCP object named `mcp`, `server`, or `app`. Errors if no such object is found.
2. `server.py:custom_name` \- imports and uses the specified server object

**Examples**

Copy

Ask AI

```
# Auto-detects server object (looks for 'mcp', 'server', or 'app')
fastmcp install server.py

# Uses specific server object
fastmcp install server.py:my_server

# With custom name and dependencies
fastmcp install server.py:my_server -n "My Analysis Server" --with pandas

```

### [​](https://gofastmcp.com/patterns/cli\#inspect)  `inspect`

`New in version: 2.9.0`

Generate a detailed JSON report about a FastMCP server, including information about its tools, prompts, resources, and capabilities.

Copy

Ask AI

```
fastmcp inspect server.py

```

The command supports the same server specification format as `run` and `install`:

Copy

Ask AI

```
# Auto-detect server object
fastmcp inspect server.py

# Specify server object
fastmcp inspect server.py:my_server

# Custom output location
fastmcp inspect server.py --output analysis.json

```

### [​](https://gofastmcp.com/patterns/cli\#version)  `version`

Display version information about FastMCP and related components.

Copy

Ask AI

```
fastmcp version

```

[Testing](https://gofastmcp.com/patterns/testing) [What is MCP?](https://gofastmcp.com/tutorials/mcp)

On this page

- [Commands Overview](https://gofastmcp.com/patterns/cli#commands-overview)
- [Command Details](https://gofastmcp.com/patterns/cli#command-details)
- [run](https://gofastmcp.com/patterns/cli#run)
- [Options](https://gofastmcp.com/patterns/cli#options)
- [Server Specification](https://gofastmcp.com/patterns/cli#server-specification)
- [dev](https://gofastmcp.com/patterns/cli#dev)
- [Options](https://gofastmcp.com/patterns/cli#options-2)
- [install](https://gofastmcp.com/patterns/cli#install)
- [Server Specification](https://gofastmcp.com/patterns/cli#server-specification-2)
- [inspect](https://gofastmcp.com/patterns/cli#inspect)
- [version](https://gofastmcp.com/patterns/cli#version)

Assistant

Responses are generated using AI and may contain mistakes.