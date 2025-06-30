# tool_transform - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform
**Generated:** 2025-06-27

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.tools

tool\_transform

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform\#fastmcp-tools-tool-transform)  `fastmcp.tools.tool_transform`

## [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform\#argtransform)  `ArgTransform`

Configuration for transforming a parent tool’s argument.

This class allows fine-grained control over how individual arguments are transformed
when creating a new tool from an existing one. You can rename arguments, change their
descriptions, add default values, or hide them from clients while passing constants.

**Examples:**

Rename argument ‘old\_name’ to ‘new\_name’

Copy

Ask AI

```
ArgTransform(name="new_name")

```

Change description only

Copy

Ask AI

```
ArgTransform(description="Updated description")

```

Add a default value (makes argument optional)

Copy

Ask AI

```
ArgTransform(default=42)

```

Add a default factory (makes argument optional)

Copy

Ask AI

```
ArgTransform(default_factory=lambda: time.time())

```

Change the type

Copy

Ask AI

```
ArgTransform(type=str)

```

Hide the argument entirely from clients

Copy

Ask AI

```
ArgTransform(hide=True)

```

Hide argument but pass a constant value to parent

Copy

Ask AI

```
ArgTransform(hide=True, default="constant_value")

```

Hide argument but pass a factory-generated value to parent

Copy

Ask AI

```
ArgTransform(hide=True, default_factory=lambda: uuid.uuid4().hex)

```

Make an optional parameter required (removes any default)

Copy

Ask AI

```
ArgTransform(required=True)

```

Combine multiple transformations

Copy

Ask AI

```
ArgTransform(name="new_name", description="New desc", default=None, type=int)

```

### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform\#transformedtool)  `TransformedTool`

A tool that is transformed from another tool.

This class represents a tool that has been created by transforming another tool.
It supports argument renaming, schema modification, custom function injection,
and provides context for the forward() and forward\_raw() functions.

The transformation can be purely schema-based (argument renaming, dropping, etc.)
or can include a custom function that uses forward() to call the parent tool
with transformed arguments.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform\#from-tool)  `from_tool`

Copy

Ask AI

```
from_tool(cls, tool: Tool, name: str | None = None, description: str | None = None, tags: set[str] | None = None, transform_fn: Callable[..., Any] | None = None, transform_args: dict[str, ArgTransform] | None = None, annotations: ToolAnnotations | None = None, serializer: Callable[[Any], str] | None = None, enabled: bool | None = None) -> TransformedTool

```

Create a transformed tool from a parent tool.

**Args:**

- `tool`: The parent tool to transform.
- `transform_fn`: Optional custom function. Can use forward() and forward\_raw()
to call the parent tool. Functions with \*\*kwargs receive transformed
argument names.
- `name`: New name for the tool. Defaults to parent tool’s name.
- `transform_args`: Optional transformations for parent tool arguments.
Only specified arguments are transformed, others pass through unchanged:
- Simple rename (str)
- Complex transformation (rename/description/default/drop) (ArgTransform)
- Drop the argument (None)
- `description`: New description. Defaults to parent’s description.
- `tags`: New tags. Defaults to parent’s tags.
- `annotations`: New annotations. Defaults to parent’s annotations.
- `serializer`: New serializer. Defaults to parent’s serializer.

**Returns:**

- TransformedTool with the specified transformations.

**Examples:**

# [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform\#transform-specific-arguments-only)  Transform specific arguments only

Copy

Ask AI

```
Tool.from_tool(parent, transform_args={"old": "new"})  # Others unchanged

```

# [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform\#custom-function-with-partial-transforms)  Custom function with partial transforms

Copy

Ask AI

```
async def custom(x: int, y: int) -> str:
    result = await forward(x=x, y=y)
    return f"Custom: {result}"

Tool.from_tool(parent, transform_fn=custom, transform_args={"a": "x", "b": "y"})

```

# [​](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform\#using-kwargs-gets-all-args%2C-transformed-and-untransformed)  Using \*\*kwargs (gets all args, transformed and untransformed)

Copy

Ask AI

```
async def flexible(**kwargs) -> str:
    result = await forward(**kwargs)
    return f"Got: {kwargs}"

Tool.from_tool(parent, transform_fn=flexible, transform_args={"a": "x"})

```

[tool\_manager](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_manager) [\_\_init\_\_](https://gofastmcp.com/python-sdk/fastmcp-utilities-__init__)

On this page

- [fastmcp.tools.tool\_transform](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform#fastmcp-tools-tool-transform)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform#classes)
- [ArgTransform](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform#argtransform)
- [TransformedTool](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform#transformedtool)
- [from\_tool](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform#from-tool)
- [Transform specific arguments only](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform#transform-specific-arguments-only)
- [Custom function with partial transforms](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform#custom-function-with-partial-transforms)
- [Using \*\*kwargs (gets all args, transformed and untransformed)](https://gofastmcp.com/python-sdk/fastmcp-tools-tool_transform#using-kwargs-gets-all-args%2C-transformed-and-untransformed)

Assistant

Responses are generated using AI and may contain mistakes.