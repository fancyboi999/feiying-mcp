# tool_manager - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager
**Generated:** 2025-06-30

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.tools

tool\_manager

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager\#fastmcp-tools-tool-manager)  `fastmcp.tools.tool_manager`

## [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager\#toolmanager)  `ToolManager`

Manages FastMCP tools.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager\#mount)  `mount`

Copy

Ask AI

```
mount(self, server: MountedServer) -> None

```

Adds a mounted server as a source for tools.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager\#add-tool-from-fn)  `add_tool_from_fn`

Copy

Ask AI

```
add_tool_from_fn(self, fn: Callable[..., Any], name: str | None = None, description: str | None = None, tags: set[str] | None = None, annotations: ToolAnnotations | None = None, serializer: Callable[[Any], str] | None = None, exclude_args: list[str] | None = None) -> Tool

```

Add a tool to the server.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager\#add-tool)  `add_tool`

Copy

Ask AI

```
add_tool(self, tool: Tool) -> Tool

```

Register a tool with the server.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager\#remove-tool)  `remove_tool`

Copy

Ask AI

```
remove_tool(self, key: str) -> None

```

Remove a tool from the server.

**Args:**

- `key`: The key of the tool to remove

**Raises:**

- `NotFoundError`: If the tool is not found

[tool](https://gofastmcp.com/python-sdk/fastmcp-tools-tool) [tool\_transform](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform)

On this page

- [fastmcp.tools.tool\_manager](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager#fastmcp-tools-tool-manager)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager#classes)
- [ToolManager](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager#toolmanager)
- [mount](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager#mount)
- [add\_tool\_from\_fn](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager#add-tool-from-fn)
- [add\_tool](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager#add-tool)
- [remove\_tool](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager#remove-tool)

Assistant

Responses are generated using AI and may contain mistakes.