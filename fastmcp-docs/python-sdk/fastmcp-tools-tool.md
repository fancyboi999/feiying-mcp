# tool - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-tools-tool
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

tool

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool\#fastmcp-tools-tool)  `fastmcp.tools.tool`

## [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool\#default-serializer)  `default_serializer`

Copy

Ask AI

```
default_serializer(data: Any) -> str

```

## [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool\#tool)  `Tool`

Internal tool registration info.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool\#to-mcp-tool)  `to_mcp_tool`

Copy

Ask AI

```
to_mcp_tool(self, **overrides: Any) -> MCPTool

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool\#from-function)  `from_function`

Copy

Ask AI

```
from_function(fn: Callable[..., Any], name: str | None = None, description: str | None = None, tags: set[str] | None = None, annotations: ToolAnnotations | None = None, exclude_args: list[str] | None = None, serializer: Callable[[Any], str] | None = None, enabled: bool | None = None) -> FunctionTool

```

Create a Tool from a function.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool\#from-tool)  `from_tool`

Copy

Ask AI

```
from_tool(cls, tool: Tool, transform_fn: Callable[..., Any] | None = None, name: str | None = None, transform_args: dict[str, ArgTransform] | None = None, description: str | None = None, tags: set[str] | None = None, annotations: ToolAnnotations | None = None, serializer: Callable[[Any], str] | None = None, enabled: bool | None = None) -> TransformedTool

```

### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool\#functiontool)  `FunctionTool`

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool\#from-function-2)  `from_function`

Copy

Ask AI

```
from_function(cls, fn: Callable[..., Any], name: str | None = None, description: str | None = None, tags: set[str] | None = None, annotations: ToolAnnotations | None = None, exclude_args: list[str] | None = None, serializer: Callable[[Any], str] | None = None, enabled: bool | None = None) -> FunctionTool

```

Create a Tool from a function.

### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool\#parsedfunction)  `ParsedFunction`

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool\#from-function-3)  `from_function`

Copy

Ask AI

```
from_function(cls, fn: Callable[..., Any], exclude_args: list[str] | None = None, validate: bool = True) -> ParsedFunction

```

[\_\_init\_\_](https://gofastmcp.com/python-sdk/fastmcp-tools-__init__) [tool\_manager](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager)

On this page

- [fastmcp.tools.tool](https://gofastmcp.com/python-sdk/fastmcp-tools-tool#fastmcp-tools-tool)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-tools-tool#functions)
- [default\_serializer](https://gofastmcp.com/python-sdk/fastmcp-tools-tool#default-serializer)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-tools-tool#classes)
- [Tool](https://gofastmcp.com/python-sdk/fastmcp-tools-tool#tool)
- [to\_mcp\_tool](https://gofastmcp.com/python-sdk/fastmcp-tools-tool#to-mcp-tool)
- [from\_function](https://gofastmcp.com/python-sdk/fastmcp-tools-tool#from-function)
- [from\_tool](https://gofastmcp.com/python-sdk/fastmcp-tools-tool#from-tool)
- [FunctionTool](https://gofastmcp.com/python-sdk/fastmcp-tools-tool#functiontool)
- [from\_function](https://gofastmcp.com/python-sdk/fastmcp-tools-tool#from-function-2)
- [ParsedFunction](https://gofastmcp.com/python-sdk/fastmcp-tools-tool#parsedfunction)
- [from\_function](https://gofastmcp.com/python-sdk/fastmcp-tools-tool#from-function-3)

Assistant

Responses are generated using AI and may contain mistakes.