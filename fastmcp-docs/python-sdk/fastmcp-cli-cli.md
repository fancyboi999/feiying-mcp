# cli - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-cli-cli
**Generated:** 2025-06-30

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.cli

cli

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-cli-cli\#fastmcp-cli-cli)  `fastmcp.cli.cli`

FastMCP CLI tools.

## [​](https://gofastmcp.com/python-sdk/fastmcp-cli-cli\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-cli-cli\#version)  `version`

Copy

Ask AI

```
version(ctx: Context)

```

### [​](https://gofastmcp.com/python-sdk/fastmcp-cli-cli\#dev)  `dev`

Copy

Ask AI

```
dev(server_spec: str = typer.Argument(..., help='Python file to run, optionally with :object suffix'), with_editable: Annotated[Path | None, typer.Option('--with-editable', '-e', help='Directory containing pyproject.toml to install in editable mode', exists=True, file_okay=False, resolve_path=True)] = None, with_packages: Annotated[list[str], typer.Option('--with', help='Additional packages to install')] = [], inspector_version: Annotated[str | None, typer.Option('--inspector-version', help='Version of the MCP Inspector to use')] = None, ui_port: Annotated[int | None, typer.Option('--ui-port', help='Port for the MCP Inspector UI')] = None, server_port: Annotated[int | None, typer.Option('--server-port', help='Port for the MCP Inspector Proxy server')] = None) -> None

```

Run a MCP server with the MCP Inspector.

### [​](https://gofastmcp.com/python-sdk/fastmcp-cli-cli\#run)  `run`

Copy

Ask AI

```
run(ctx: typer.Context, server_spec: str = typer.Argument(..., help='Python file, object specification (file:obj), or URL'), transport: Annotated[str | None, typer.Option('--transport', '-t', help='Transport protocol to use (stdio, http, or sse)')] = None, host: Annotated[str | None, typer.Option('--host', help='Host to bind to when using http transport (default: 127.0.0.1)')] = None, port: Annotated[int | None, typer.Option('--port', '-p', help='Port to bind to when using http transport (default: 8000)')] = None, log_level: Annotated[str | None, typer.Option('--log-level', '-l', help='Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)')] = None) -> None

```

Run a MCP server or connect to a remote one.

The server can be specified in three ways:

1. Module approach: server.py - runs the module directly, looking for an object named mcp/server/app.

2. Import approach: server.py:app - imports and runs the specified server object.

3. URL approach: [http://server-url](http://server-url/) \- connects to a remote server and creates a proxy.


Note: This command runs the server directly. You are responsible for ensuring
all dependencies are available.

Server arguments can be passed after — :
fastmcp run server.py — —config config.json —debug

### [​](https://gofastmcp.com/python-sdk/fastmcp-cli-cli\#install)  `install`

Copy

Ask AI

```
install(server_spec: str = typer.Argument(..., help='Python file to run, optionally with :object suffix'), server_name: Annotated[str | None, typer.Option('--name', '-n', help="Custom name for the server (defaults to server's name attribute or file name)")] = None, with_editable: Annotated[Path | None, typer.Option('--with-editable', '-e', help='Directory containing pyproject.toml to install in editable mode', exists=True, file_okay=False, resolve_path=True)] = None, with_packages: Annotated[list[str], typer.Option('--with', help='Additional packages to install')] = [], env_vars: Annotated[list[str], typer.Option('--env-var', '-v', help='Environment variables in KEY=VALUE format')] = [], env_file: Annotated[Path | None, typer.Option('--env-file', '-f', help='Load environment variables from a .env file', exists=True, file_okay=True, dir_okay=False, resolve_path=True)] = None) -> None

```

Install a MCP server in the Claude desktop app.

Environment variables are preserved once added and only updated if new values
are explicitly provided.

### [​](https://gofastmcp.com/python-sdk/fastmcp-cli-cli\#inspect)  `inspect`

Copy

Ask AI

```
inspect(server_spec: str = typer.Argument(..., help='Python file to inspect, optionally with :object suffix'), output: Annotated[Path, typer.Option('--output', '-o', help='Output file path for the JSON report (default: server-info.json)')] = Path('server-info.json')) -> None

```

Inspect a FastMCP server and generate a JSON report.

This command analyzes a FastMCP server (v1.x or v2.x) and generates
a comprehensive JSON report containing information about the server’s
name, instructions, version, tools, prompts, resources, templates,
and capabilities.

**Examples:**

fastmcp inspect server.py
fastmcp inspect server.py -o report.json
fastmcp inspect server.py:mcp -o analysis.json
fastmcp inspect path/to/server.py:app -o /tmp/server-info.json

[claude](https://gofastmcp.com/python-sdk/fastmcp-cli-claude) [run](https://gofastmcp.com/python-sdk/fastmcp-cli-run)

On this page

- [fastmcp.cli.cli](https://gofastmcp.com/python-sdk/fastmcp-cli-cli#fastmcp-cli-cli)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-cli-cli#functions)
- [version](https://gofastmcp.com/python-sdk/fastmcp-cli-cli#version)
- [dev](https://gofastmcp.com/python-sdk/fastmcp-cli-cli#dev)
- [run](https://gofastmcp.com/python-sdk/fastmcp-cli-cli#run)
- [install](https://gofastmcp.com/python-sdk/fastmcp-cli-cli#install)
- [inspect](https://gofastmcp.com/python-sdk/fastmcp-cli-cli#inspect)

Assistant

Responses are generated using AI and may contain mistakes.