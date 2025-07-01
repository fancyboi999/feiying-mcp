# run - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-cli-run
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

run

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-cli-run\#fastmcp-cli-run)  `fastmcp.cli.run`

FastMCP run command implementation.

## [​](https://gofastmcp.com/python-sdk/fastmcp-cli-run\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-cli-run\#is-url)  `is_url`

Copy

Ask AI

```
is_url(path: str) -> bool

```

Check if a string is a URL.

### [​](https://gofastmcp.com/python-sdk/fastmcp-cli-run\#parse-file-path)  `parse_file_path`

Copy

Ask AI

```
parse_file_path(server_spec: str) -> tuple[Path, str | None]

```

Parse a file path that may include a server object specification.

**Args:**

- `server_spec`: Path to file, optionally with :object suffix

**Returns:**

- Tuple of (file\_path, server\_object)

### [​](https://gofastmcp.com/python-sdk/fastmcp-cli-run\#import-server)  `import_server`

Copy

Ask AI

```
import_server(file: Path, server_object: str | None = None) -> Any

```

Import a MCP server from a file.

**Args:**

- `file`: Path to the file
- `server_object`: Optional object name in format “module:object” or just “object”

**Returns:**

- The server object

### [​](https://gofastmcp.com/python-sdk/fastmcp-cli-run\#create-client-server)  `create_client_server`

Copy

Ask AI

```
create_client_server(url: str) -> Any

```

Create a FastMCP server from a client URL.

**Args:**

- `url`: The URL to connect to

**Returns:**

- A FastMCP server instance

### [​](https://gofastmcp.com/python-sdk/fastmcp-cli-run\#import-server-with-args)  `import_server_with_args`

Copy

Ask AI

```
import_server_with_args(file: Path, server_object: str | None = None, server_args: list[str] | None = None) -> Any

```

Import a server with optional command line arguments.

**Args:**

- `file`: Path to the server file
- `server_object`: Optional server object name
- `server_args`: Optional command line arguments to inject

**Returns:**

- The imported server object

### [​](https://gofastmcp.com/python-sdk/fastmcp-cli-run\#run-command)  `run_command`

Copy

Ask AI

```
run_command(server_spec: str, transport: str | None = None, host: str | None = None, port: int | None = None, log_level: str | None = None, server_args: list[str] | None = None) -> None

```

Run a MCP server or connect to a remote one.

**Args:**

- `server_spec`: Python file, object specification (file:obj), or URL
- `transport`: Transport protocol to use
- `host`: Host to bind to when using http transport
- `port`: Port to bind to when using http transport
- `log_level`: Log level
- `server_args`: Additional arguments to pass to the server

[cli](https://gofastmcp.com/python-sdk/fastmcp-cli-cli) [\_\_init\_\_](https://gofastmcp.com/python-sdk/fastmcp-client-__init__)

On this page

- [fastmcp.cli.run](https://gofastmcp.com/python-sdk/fastmcp-cli-run#fastmcp-cli-run)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-cli-run#functions)
- [is\_url](https://gofastmcp.com/python-sdk/fastmcp-cli-run#is-url)
- [parse\_file\_path](https://gofastmcp.com/python-sdk/fastmcp-cli-run#parse-file-path)
- [import\_server](https://gofastmcp.com/python-sdk/fastmcp-cli-run#import-server)
- [create\_client\_server](https://gofastmcp.com/python-sdk/fastmcp-cli-run#create-client-server)
- [import\_server\_with\_args](https://gofastmcp.com/python-sdk/fastmcp-cli-run#import-server-with-args)
- [run\_command](https://gofastmcp.com/python-sdk/fastmcp-cli-run#run-command)

Assistant

Responses are generated using AI and may contain mistakes.