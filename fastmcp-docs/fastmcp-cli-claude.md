# claude - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-cli-claude
**Generated:** 2025-06-27

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.cli

claude

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-cli-claude\#fastmcp-cli-claude)  `fastmcp.cli.claude`

Claude app integration utilities.

## [​](https://gofastmcp.com/python-sdk/fastmcp-cli-claude\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-cli-claude\#get-claude-config-path)  `get_claude_config_path`

Copy

Ask AI

```
get_claude_config_path() -> Path | None

```

Get the Claude config directory based on platform.

### [​](https://gofastmcp.com/python-sdk/fastmcp-cli-claude\#update-claude-config)  `update_claude_config`

Copy

Ask AI

```
update_claude_config(file_spec: str, server_name: str) -> bool

```

Add or update a FastMCP server in Claude’s configuration.

**Args:**

- `file_spec`: Path to the server file, optionally with :object suffix
- `server_name`: Name for the server in Claude’s config
- `with_editable`: Optional directory to install in editable mode
- `with_packages`: Optional list of additional packages to install
- `env_vars`: Optional dictionary of environment variables. These are merged with
any existing variables, with new values taking precedence.

**Raises:**

- `RuntimeError`: If Claude Desktop’s config directory is not found, indicating
Claude Desktop may not be installed or properly set up.

[\_\_init\_\_](https://gofastmcp.com/python-sdk/fastmcp-cli-__init__) [cli](https://gofastmcp.com/python-sdk/fastmcp-cli-cli)

On this page

- [fastmcp.cli.claude](https://gofastmcp.com/python-sdk/fastmcp-cli-claude#fastmcp-cli-claude)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-cli-claude#functions)
- [get\_claude\_config\_path](https://gofastmcp.com/python-sdk/fastmcp-cli-claude#get-claude-config-path)
- [update\_claude\_config](https://gofastmcp.com/python-sdk/fastmcp-cli-claude#update-claude-config)

Assistant

Responses are generated using AI and may contain mistakes.