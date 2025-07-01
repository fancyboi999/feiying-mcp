# Tool Transformation - FastMCP

**Source URL:** https://gofastmcp.com/patterns/tool-transformation
**Generated:** 2025-06-30

**Description:** Create enhanced tool variants with modified schemas, argument mappings, and custom behavior.

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Patterns

Tool Transformation

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

`New in version: 2.8.0`

Tool transformation allows you to create new, enhanced tools from existing ones. This powerful feature enables you to adapt tools for different contexts, simplify complex interfaces, or add custom logic without duplicating code.

## [​](https://gofastmcp.com/patterns/tool-transformation\#why-transform-tools%3F)  Why Transform Tools?

Often, an existing tool is _almost_ perfect for your use case, but it might have:

- A confusing description (or no description at all).
- Argument names or descriptions that are not intuitive for an LLM (e.g., `q` instead of `query`).
- Unnecessary parameters that you want to hide from the LLM.
- A need for input validation before the original tool is called.
- A need to modify or format the tool’s output.

Instead of rewriting the tool from scratch, you can **transform** it to fit your needs.

## [​](https://gofastmcp.com/patterns/tool-transformation\#basic-transformation)  Basic Transformation

The primary way to create a transformed tool is with the `Tool.from_tool()` class method. At its simplest, you can use it to change a tool’s top-level metadata like its `name`, `description`, or `tags`.

In the following simple example, we take a generic `search` tool and adjust its name and description to help an LLM client better understand its purpose.

Copy

Ask AI

```
from fastmcp import FastMCP
from fastmcp.tools import Tool

mcp = FastMCP()

# The original, generic tool
@mcp.tool
def search(query: str, category: str = "all") -> list[dict]:
    """Searches for items in the database."""
    return database.search(query, category)

# Create a more domain-specific version by changing its metadata
product_search_tool = Tool.from_tool(
    search,
    name="find_products",
    description="""
        Search for products in the e-commerce catalog.
        Use this when customers ask about finding specific items,
        checking availability, or browsing product categories.
        """,
)

mcp.add_tool(product_search_tool)

```

When you transform a tool, the original tool remains registered on the server. To avoid confusing an LLM with two similar tools, you can disable the original one:

Copy

Ask AI

```
from fastmcp import FastMCP
from fastmcp.tools import Tool

mcp = FastMCP()

# The original, generic tool
@mcp.tool
def search(query: str, category: str = "all") -> list[dict]:
    ...

# Create a more domain-specific version
product_search_tool = Tool.from_tool(search, ...)
mcp.add_tool(product_search_tool)

# Disable the original tool
search.disable()

```

Now, clients see a tool named `find_products` with a clear, domain-specific purpose and relevant tags, even though it still uses the original generic `search` function’s logic.

### [​](https://gofastmcp.com/patterns/tool-transformation\#parameters)  Parameters

The `Tool.from_tool()` class method is the primary way to create a transformed tool. It takes the following parameters:

- `tool`: The tool to transform. This is the only required argument.
- `name`: An optional name for the new tool.
- `description`: An optional description for the new tool.
- `transform_args`: A dictionary of `ArgTransform` objects, one for each argument you want to modify.
- `transform_fn`: An optional function that will be called instead of the parent tool’s logic.
- `output_schema`: Control output schema and structured outputs (see [Output Schema Control](https://gofastmcp.com/patterns/tool-transformation#output-schema-control)).
- `tags`: An optional set of tags for the new tool.
- `annotations`: An optional set of `ToolAnnotations` for the new tool.
- `serializer`: An optional function that will be called to serialize the result of the new tool.

The result is a new `TransformedTool` object that wraps the parent tool and applies the transformations you specify. You can add this tool to your MCP server using its `add_tool()` method.

## [​](https://gofastmcp.com/patterns/tool-transformation\#modifying-arguments)  Modifying Arguments

To modify a tool’s parameters, provide a dictionary of `ArgTransform` objects to the `transform_args` parameter of `Tool.from_tool()`. Each key is the name of the _original_ argument you want to modify.

You only need to provide a `transform_args` entry for arguments you want to modify. All other arguments will be passed through unchanged.

### [​](https://gofastmcp.com/patterns/tool-transformation\#the-argtransform-class)  The ArgTransform Class

To modify an argument, you need to create an `ArgTransform` object. This object has the following parameters:

- `name`: The new name for the argument.
- `description`: The new description for the argument.
- `default`: The new default value for the argument.
- `default_factory`: A function that will be called to generate a default value for the argument. This is useful for arguments that need to be generated for each tool call, such as timestamps or unique IDs.
- `hide`: Whether to hide the argument from the LLM.
- `required`: Whether the argument is required, usually used to make an optional argument be required instead.
- `type`: The new type for the argument.

Certain combinations of parameters are not allowed. For example, you can only use `default_factory` with `hide=True`, because dynamic defaults cannot be represented in a JSON schema for the client. You can only set required=True for arguments that do not declare a default value.

### [​](https://gofastmcp.com/patterns/tool-transformation\#descriptions)  Descriptions

By far the most common reason to transform a tool, after its own description, is to improve its argument descriptions. A good description is crucial for helping an LLM understand how to use a parameter correctly. This is especially important when wrapping tools from external APIs, whose argument descriptions may be missing or written for developers, not LLMs.

In this example, we add a helpful description to the `user_id` argument:

Copy

Ask AI

```
from fastmcp import FastMCP
from fastmcp.tools import Tool
from fastmcp.tools.tool_transform import ArgTransform

mcp = FastMCP()

@mcp.tool
def find_user(user_id: str):
    """Finds a user by their ID."""
    ...

new_tool = Tool.from_tool(
    find_user,
    transform_args={
        "user_id": ArgTransform(
            description=(
                "The unique identifier for the user, "
                "usually in the format 'usr-xxxxxxxx'."
            )
        )
    }
)

```

### [​](https://gofastmcp.com/patterns/tool-transformation\#names)  Names

At times, you may want to rename an argument to make it more intuitive for an LLM.

For example, in the following example, we take a generic `q` argument and expand it to `search_query`:

Copy

Ask AI

```
from fastmcp import FastMCP
from fastmcp.tools import Tool
from fastmcp.tools.tool_transform import ArgTransform

mcp = FastMCP()

@mcp.tool
def search(q: str):
    """Searches for items in the database."""
    return database.search(q)

new_tool = Tool.from_tool(
    search,
    transform_args={
        "q": ArgTransform(name="search_query")
    }
)

```

### [​](https://gofastmcp.com/patterns/tool-transformation\#default-values)  Default Values

You can update the default value for any argument using the `default` parameter. Here, we change the default value of the `y` argument to 10:

Copy

Ask AI

```
from fastmcp import FastMCP
from fastmcp.tools import Tool
from fastmcp.tools.tool_transform import ArgTransform

mcp = FastMCP()

@mcp.tool
def add(x: int, y: int) -> int:
    """Adds two numbers."""
    return x + y

new_tool = Tool.from_tool(
    add,
    transform_args={
        "y": ArgTransform(default=10)
    }
)

```

Default values are especially useful in combination with hidden arguments.

### [​](https://gofastmcp.com/patterns/tool-transformation\#hiding-arguments)  Hiding Arguments

Sometimes a tool requires arguments that shouldn’t be exposed to the LLM, such as API keys, configuration flags, or internal IDs. You can hide these parameters using `hide=True`. Note that you can only hide arguments that have a default value (or for which you provide a new default), because the LLM can’t provide a value at call time.

To pass a constant value to the parent tool, combine `hide=True` with `default=<value>`.

Copy

Ask AI

```
import os
from fastmcp import FastMCP
from fastmcp.tools import Tool
from fastmcp.tools.tool_transform import ArgTransform

mcp = FastMCP()

@mcp.tool
def send_email(to: str, subject: str, body: str, api_key: str):
    """Sends an email."""
    ...

# Create a simplified version that hides the API key
new_tool = Tool.from_tool(
    send_email,
    name="send_notification",
    transform_args={
        "api_key": ArgTransform(
            hide=True,
            default=os.environ.get("EMAIL_API_KEY"),
        )
    }
)

```

The LLM now only sees the `to`, `subject`, and `body` parameters. The `api_key` is supplied automatically from an environment variable.

For values that must be generated for each tool call (like timestamps or unique IDs), use `default_factory`, which is called with no arguments every time the tool is called. For example,

Copy

Ask AI

```
transform_args = {
    'timestamp': ArgTransform(
        hide=True,
        default_factory=lambda: datetime.now(),
    )
}

```

`default_factory` can only be used with `hide=True`. This is because visible parameters need static defaults that can be represented in a JSON schema for the client.

### [​](https://gofastmcp.com/patterns/tool-transformation\#required-values)  Required Values

In rare cases where you want to make an optional argument required, you can set `required=True`. This has no effect if the argument was already required.

Copy

Ask AI

```
transform_args = {
    'user_id': ArgTransform(
        required=True,
    )
}

```

## [​](https://gofastmcp.com/patterns/tool-transformation\#modifying-tool-behavior)  Modifying Tool Behavior

With great power comes great responsibility. Modifying tool behavior is a very advanced feature.

In addition to changing a tool’s schema, advanced users can also modify its behavior. This is useful for adding validation logic, or for post-processing the tool’s output.

The `from_tool()` method takes a `transform_fn` parameter, which is an async function that replaces the parent tool’s logic and gives you complete control over the tool’s execution.

### [​](https://gofastmcp.com/patterns/tool-transformation\#the-transform-function)  The Transform Function

The `transform_fn` is an async function that **completely replaces** the parent tool’s logic.

Critically, the transform function’s arguments are used to determine the new tool’s final schema. Any arguments that are not already present in the parent tool schema OR the `transform_args` will be added to the new tool’s schema. Note that when `transform_args` and your function have the same argument name, the `transform_args` metadata will take precedence, if provided.

Copy

Ask AI

```
async def my_custom_logic(user_input: str, max_length: int = 100) -> str:
    # Your custom logic here - this completely replaces the parent tool
    return f"Custom result for: {user_input[:max_length]}"

Tool.from_tool(transform_fn=my_custom_logic)

```

The name / docstring of the `transform_fn` are ignored. Only its arguments are used to determine the final schema.

### [​](https://gofastmcp.com/patterns/tool-transformation\#calling-the-parent-tool)  Calling the Parent Tool

Most of the time, you don’t want to completely replace the parent tool’s behavior. Instead, you want to add validation, modify inputs, or post-process outputs while still leveraging the parent tool’s core functionality. For this, FastMCP provides the special `forward()` and `forward_raw()` functions.

Both `forward()` and `forward_raw()` are async functions that let you call the parent tool from within your `transform_fn`:

- **`forward()`** (recommended): Automatically handles argument mapping based on your `ArgTransform` configurations. Call it with the transformed argument names.
- **`forward_raw()`**: Bypasses all transformation and calls the parent tool directly with its original argument names. This is rarely needed unless you’re doing complex argument manipulation, perhaps without `arg_transforms`.

The most common transformation pattern is to validate (potentially renamed) arguments before calling the parent tool. Here’s an example that validates that `x` and `y` are positive before calling the parent tool:

- Using forward()
- Using forward() with renamed args
- Using forward\_raw()

In the simplest case, your parent tool and your transform function have the same arguments. You can call `forward()` with the same argument names as the parent tool:

Copy

Ask AI

```
from fastmcp import FastMCP
from fastmcp.tools import Tool
from fastmcp.tools.tool_transform import forward

mcp = FastMCP()

@mcp.tool
def add(x: int, y: int) -> int:
    """Adds two numbers."""
    return x + y

async def ensure_positive(x: int, y: int) -> int:
    if x <= 0 or y <= 0:
        raise ValueError("x and y must be positive")
    return await forward(x=x, y=y)

new_tool = Tool.from_tool(
    add,
    transform_fn=ensure_positive,
)

mcp.add_tool(new_tool)

```

In the simplest case, your parent tool and your transform function have the same arguments. You can call `forward()` with the same argument names as the parent tool:

Copy

Ask AI

```
from fastmcp import FastMCP
from fastmcp.tools import Tool
from fastmcp.tools.tool_transform import forward

mcp = FastMCP()

@mcp.tool
def add(x: int, y: int) -> int:
    """Adds two numbers."""
    return x + y

async def ensure_positive(x: int, y: int) -> int:
    if x <= 0 or y <= 0:
        raise ValueError("x and y must be positive")
    return await forward(x=x, y=y)

new_tool = Tool.from_tool(
    add,
    transform_fn=ensure_positive,
)

mcp.add_tool(new_tool)

```

When your transformed tool has different argument names than the parent tool, you can call `forward()` with the renamed arguments and it will automatically map the arguments to the parent tool’s arguments:

Copy

Ask AI

```
from fastmcp import FastMCP
from fastmcp.tools import Tool
from fastmcp.tools.tool_transform import forward

mcp = FastMCP()

@mcp.tool
def add(x: int, y: int) -> int:
    """Adds two numbers."""
    return x + y

async def ensure_positive(a: int, b: int) -> int:
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive")
    return await forward(a=a, b=b)

new_tool = Tool.from_tool(
    add,
    transform_fn=ensure_positive,
    transform_args={
        "x": ArgTransform(name="a"),
        "y": ArgTransform(name="b"),
    }
)

mcp.add_tool(new_tool)

```

Finally, you can use `forward_raw()` to bypass all argument mapping and call the parent tool directly with its original argument names.

Copy

Ask AI

```
from fastmcp import FastMCP
from fastmcp.tools import Tool
from fastmcp.tools.tool_transform import forward

mcp = FastMCP()

@mcp.tool
def add(x: int, y: int) -> int:
    """Adds two numbers."""
    return x + y

async def ensure_positive(a: int, b: int) -> int:
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive")
    return await forward_raw(x=a, y=b)

new_tool = Tool.from_tool(
    add,
    transform_fn=ensure_positive,
    transform_args={
        "x": ArgTransform(name="a"),
        "y": ArgTransform(name="b"),
    }
)

mcp.add_tool(new_tool)

```

### [​](https://gofastmcp.com/patterns/tool-transformation\#passing-arguments-with-kwargs)  Passing Arguments with \*\*kwargs

If your `transform_fn` includes `**kwargs` in its signature, it will receive **all arguments from the parent tool after `ArgTransform` configurations have been applied**. This is powerful for creating flexible validation functions that don’t require you to add every argument to the function signature.

In the following example, we wrap a parent tool that accepts two arguments `x` and `y`. These are renamed to `a` and `b` in the transformed tool, and the transform only validates `a`, passing the other argument through as `**kwargs`.

Copy

Ask AI

```
from fastmcp import FastMCP
from fastmcp.tools import Tool
from fastmcp.tools.tool_transform import forward

mcp = FastMCP()

@mcp.tool
def add(x: int, y: int) -> int:
    """Adds two numbers."""
    return x + y

async def ensure_a_positive(a: int, **kwargs) -> int:
    if a <= 0:
        raise ValueError("a must be positive")
    return await forward(a=a, **kwargs)

new_tool = Tool.from_tool(
    add,
    transform_fn=ensure_a_positive,
    transform_args={
        "x": ArgTransform(name="a"),
        "y": ArgTransform(name="b"),
    }
)

mcp.add_tool(new_tool)

```

In the above example, `**kwargs` receives the renamed argument `b`, not the original argument `y`. It is therefore recommended to use with `forward()`, not `forward_raw()`.

## [​](https://gofastmcp.com/patterns/tool-transformation\#output-schema-control)  Output Schema Control

`New in version: 2.10.0`

Transformed tools inherit output schemas from their parent by default, but you can control this behavior:

**Inherit from Parent (Default)**

Copy

Ask AI

```
Tool.from_tool(parent_tool, name="renamed_tool")

```

The transformed tool automatically uses the parent tool’s output schema and structured output behavior.

**Custom Output Schema**

Copy

Ask AI

```
Tool.from_tool(parent_tool, output_schema={
    "type": "object",
    "properties": {"status": {"type": "string"}}
})

```

Provide your own schema that differs from the parent. The tool must return data matching this schema.

**Remove Output Schema**

Copy

Ask AI

```
Tool.from_tool(parent_tool, output_schema=False)

```

Removes the output schema declaration. Automatic structured content still works for object-like returns (dict, dataclass, Pydantic models) but primitive types won’t be structured.

**Full Control with Transform Functions**

Copy

Ask AI

```
async def custom_output(**kwargs) -> ToolResult:
    result = await forward(**kwargs)
    return ToolResult(content=[...], structured_content={...})

Tool.from_tool(parent_tool, transform_fn=custom_output)

```

Use a transform function returning `ToolResult` for complete control over both content blocks and structured outputs.

## [​](https://gofastmcp.com/patterns/tool-transformation\#common-patterns)  Common Patterns

Tool transformation is a flexible feature that supports many powerful patterns. Here are a few common use cases to give you ideas.

### [​](https://gofastmcp.com/patterns/tool-transformation\#adapting-remote-or-generated-tools)  Adapting Remote or Generated Tools

This is one of the most common reasons to use tool transformation. Tools from remote servers (via a [proxy](https://gofastmcp.com/servers/proxy)) or generated from an [OpenAPI spec](https://gofastmcp.com/servers/openapi) are often too generic for direct use by an LLM. You can use transformation to create a simpler, more intuitive version for your specific needs.

### [​](https://gofastmcp.com/patterns/tool-transformation\#chaining-transformations)  Chaining Transformations

You can chain transformations by using an already transformed tool as the parent for a new transformation. This lets you build up complex behaviors in layers, for example, first renaming arguments, and then adding validation logic to the renamed tool.

### [​](https://gofastmcp.com/patterns/tool-transformation\#context-aware-tool-factories)  Context-Aware Tool Factories

You can write functions that act as “factories,” generating specialized versions of a tool for different contexts. For example, you could create a `get_my_data` tool that is specific to the currently logged-in user by hiding the `user_id` parameter and providing it automatically.

[Contrib Modules](https://gofastmcp.com/integrations/contrib) [Decorating Methods](https://gofastmcp.com/patterns/decorating-methods)

On this page

- [Why Transform Tools?](https://gofastmcp.com/patterns/tool-transformation#why-transform-tools%3F)
- [Basic Transformation](https://gofastmcp.com/patterns/tool-transformation#basic-transformation)
- [Parameters](https://gofastmcp.com/patterns/tool-transformation#parameters)
- [Modifying Arguments](https://gofastmcp.com/patterns/tool-transformation#modifying-arguments)
- [The ArgTransform Class](https://gofastmcp.com/patterns/tool-transformation#the-argtransform-class)
- [Descriptions](https://gofastmcp.com/patterns/tool-transformation#descriptions)
- [Names](https://gofastmcp.com/patterns/tool-transformation#names)
- [Default Values](https://gofastmcp.com/patterns/tool-transformation#default-values)
- [Hiding Arguments](https://gofastmcp.com/patterns/tool-transformation#hiding-arguments)
- [Required Values](https://gofastmcp.com/patterns/tool-transformation#required-values)
- [Modifying Tool Behavior](https://gofastmcp.com/patterns/tool-transformation#modifying-tool-behavior)
- [The Transform Function](https://gofastmcp.com/patterns/tool-transformation#the-transform-function)
- [Calling the Parent Tool](https://gofastmcp.com/patterns/tool-transformation#calling-the-parent-tool)
- [Passing Arguments with \*\*kwargs](https://gofastmcp.com/patterns/tool-transformation#passing-arguments-with-kwargs)
- [Output Schema Control](https://gofastmcp.com/patterns/tool-transformation#output-schema-control)
- [Common Patterns](https://gofastmcp.com/patterns/tool-transformation#common-patterns)
- [Adapting Remote or Generated Tools](https://gofastmcp.com/patterns/tool-transformation#adapting-remote-or-generated-tools)
- [Chaining Transformations](https://gofastmcp.com/patterns/tool-transformation#chaining-transformations)
- [Context-Aware Tool Factories](https://gofastmcp.com/patterns/tool-transformation#context-aware-tool-factories)

Assistant

Responses are generated using AI and may contain mistakes.