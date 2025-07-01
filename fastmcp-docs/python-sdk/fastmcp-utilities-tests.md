# tests - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-utilities-tests
**Generated:** 2025-06-30

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.utilities

tests

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-tests\#fastmcp-utilities-tests)  `fastmcp.utilities.tests`

## [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-tests\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-tests\#temporary-settings)  `temporary_settings`

Copy

Ask AI

```
temporary_settings(**kwargs: Any)

```

Temporarily override FastMCP setting values.

**Args:**

- `**kwargs`: The settings to override, including nested settings.

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-tests\#run-server-in-process)  `run_server_in_process`

Copy

Ask AI

```
run_server_in_process(server_fn: Callable[..., None], *args, **kwargs) -> Generator[str, None, None]

```

Context manager that runs a FastMCP server in a separate process and
returns the server URL. When the context manager is exited, the server process is killed.

**Args:**

- `server_fn`: The function that runs a FastMCP server. FastMCP servers are
not pickleable, so we need a function that creates and runs one.
- `*args`: Arguments to pass to the server function.
- `provide_host_and_port`: Whether to provide the host and port to the server function as kwargs.
- `**kwargs`: Keyword arguments to pass to the server function.

**Returns:**

- The server URL.

[openapi](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi) [types](https://gofastmcp.com/python-sdk/fastmcp-utilities-types)

On this page

- [fastmcp.utilities.tests](https://gofastmcp.com/python-sdk/fastmcp-utilities-tests#fastmcp-utilities-tests)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-utilities-tests#functions)
- [temporary\_settings](https://gofastmcp.com/python-sdk/fastmcp-utilities-tests#temporary-settings)
- [run\_server\_in\_process](https://gofastmcp.com/python-sdk/fastmcp-utilities-tests#run-server-in-process)

Assistant

Responses are generated using AI and may contain mistakes.