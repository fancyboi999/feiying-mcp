# server - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-server-server
**Generated:** 2025-06-27

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.server

server

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#fastmcp-server-server)  `fastmcp.server.server`

FastMCP - A more ergonomic interface for MCP servers.

## [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#add-resource-prefix)  `add_resource_prefix`

Copy

Ask AI

```
add_resource_prefix(uri: str, prefix: str, prefix_format: Literal['protocol', 'path'] | None = None) -> str

```

Add a prefix to a resource URI.

**Args:**

- `uri`: The original resource URI
- `prefix`: The prefix to add

**Returns:**

- The resource URI with the prefix added

**Examples:**

With new style:

Copy

Ask AI

```
add_resource_prefix("resource://path/to/resource", "prefix")
"resource://prefix/path/to/resource"

```

With legacy style:

Copy

Ask AI

```
add_resource_prefix("resource://path/to/resource", "prefix")
"prefix+resource://path/to/resource"

```

With absolute path:

Copy

Ask AI

```
add_resource_prefix("resource:///absolute/path", "prefix")
"resource://prefix//absolute/path"

```

**Raises:**

- `ValueError`: If the URI doesn’t match the expected protocol://path format

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#remove-resource-prefix)  `remove_resource_prefix`

Copy

Ask AI

```
remove_resource_prefix(uri: str, prefix: str, prefix_format: Literal['protocol', 'path'] | None = None) -> str

```

Remove a prefix from a resource URI.

**Args:**

- `uri`: The resource URI with a prefix
- `prefix`: The prefix to remove
- `prefix_format`: The format of the prefix to remove

Returns:
The resource URI with the prefix removed

**Examples:**

With new style:

Copy

Ask AI

```
remove_resource_prefix("resource://prefix/path/to/resource", "prefix")
"resource://path/to/resource"

```

With legacy style:

Copy

Ask AI

```
remove_resource_prefix("prefix+resource://path/to/resource", "prefix")
"resource://path/to/resource"

```

With absolute path:

Copy

Ask AI

```
remove_resource_prefix("resource://prefix//absolute/path", "prefix")
"resource:///absolute/path"

```

**Raises:**

- `ValueError`: If the URI doesn’t match the expected protocol://path format

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#has-resource-prefix)  `has_resource_prefix`

Copy

Ask AI

```
has_resource_prefix(uri: str, prefix: str, prefix_format: Literal['protocol', 'path'] | None = None) -> bool

```

Check if a resource URI has a specific prefix.

**Args:**

- `uri`: The resource URI to check
- `prefix`: The prefix to look for

**Returns:**

- True if the URI has the specified prefix, False otherwise

**Examples:**

With new style:

Copy

Ask AI

```
has_resource_prefix("resource://prefix/path/to/resource", "prefix")
True

```

With legacy style:

Copy

Ask AI

```
has_resource_prefix("prefix+resource://path/to/resource", "prefix")
True

```

With other path:

Copy

Ask AI

```
has_resource_prefix("resource://other/path/to/resource", "prefix")
False

```

**Raises:**

- `ValueError`: If the URI doesn’t match the expected protocol://path format

## [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#fastmcp)  `FastMCP`

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#settings)  `settings`

Copy

Ask AI

```
settings(self) -> Settings

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#name)  `name`

Copy

Ask AI

```
name(self) -> str

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#instructions)  `instructions`

Copy

Ask AI

```
instructions(self) -> str | None

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#run)  `run`

Copy

Ask AI

```
run(self, transport: Transport | None = None, **transport_kwargs: Any) -> None

```

Run the FastMCP server. Note this is a synchronous function.

**Args:**

- `transport`: Transport protocol to use (“stdio”, “sse”, or “streamable-http”)

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#add-middleware)  `add_middleware`

Copy

Ask AI

```
add_middleware(self, middleware: Middleware) -> None

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#custom-route)  `custom_route`

Copy

Ask AI

```
custom_route(self, path: str, methods: list[str], name: str | None = None, include_in_schema: bool = True)

```

Decorator to register a custom HTTP route on the FastMCP server.

Allows adding arbitrary HTTP endpoints outside the standard MCP protocol,
which can be useful for OAuth callbacks, health checks, or admin APIs.
The handler function must be an async function that accepts a Starlette
Request and returns a Response.

**Args:**

- `path`: URL path for the route (e.g., “/oauth/callback”)
- `methods`: List of HTTP methods to support (e.g., \[“GET”, “POST”\])
- `name`: Optional name for the route (to reference this route with
Starlette’s reverse URL lookup feature)
- `include_in_schema`: Whether to include in OpenAPI schema, defaults to True

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#add-tool)  `add_tool`

Copy

Ask AI

```
add_tool(self, tool: Tool) -> None

```

Add a tool to the server.

The tool function can optionally request a Context object by adding a parameter
with the Context type annotation. See the @tool decorator for examples.

**Args:**

- `tool`: The Tool instance to register

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#remove-tool)  `remove_tool`

Copy

Ask AI

```
remove_tool(self, name: str) -> None

```

Remove a tool from the server.

**Args:**

- `name`: The name of the tool to remove

**Raises:**

- `NotFoundError`: If the tool is not found

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#tool)  `tool`

Copy

Ask AI

```
tool(self, name_or_fn: AnyFunction) -> FunctionTool

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#tool-2)  `tool`

Copy

Ask AI

```
tool(self, name_or_fn: str | None = None) -> Callable[[AnyFunction], FunctionTool]

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#tool-3)  `tool`

Copy

Ask AI

```
tool(self, name_or_fn: str | AnyFunction | None = None) -> Callable[[AnyFunction], FunctionTool] | FunctionTool

```

Decorator to register a tool.

Tools can optionally request a Context object by adding a parameter with the
Context type annotation. The context provides access to MCP capabilities like
logging, progress reporting, and resource access.

This decorator supports multiple calling patterns:

- @server.tool (without parentheses)
- @server.tool (with empty parentheses)
- @server.tool(“custom\_name”) (with name as first argument)
- @server.tool(name=“custom\_name”) (with name as keyword argument)
- server.tool(function, name=“custom\_name”) (direct function call)

**Args:**

- `name_or_fn`: Either a function (when used as @tool), a string name, or None
- `name`: Optional name for the tool (keyword-only, alternative to name\_or\_fn)
- `description`: Optional description of what the tool does
- `tags`: Optional set of tags for categorizing the tool
- `annotations`: Optional annotations about the tool’s behavior
- `exclude_args`: Optional list of argument names to exclude from the tool schema
- `enabled`: Optional boolean to enable or disable the tool

**Examples:**

Register a tool with a custom name:

Copy

Ask AI

```
@server.tool
def my_tool(x: int) -> str:
    return str(x)

# Register a tool with a custom name
@server.tool
def my_tool(x: int) -> str:
    return str(x)

@server.tool("custom_name")
def my_tool(x: int) -> str:
    return str(x)

@server.tool(name="custom_name")
def my_tool(x: int) -> str:
    return str(x)

# Direct function call
server.tool(my_function, name="custom_name")

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#add-resource)  `add_resource`

Copy

Ask AI

```
add_resource(self, resource: Resource) -> None

```

Add a resource to the server.

**Args:**

- `resource`: A Resource instance to add

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#add-template)  `add_template`

Copy

Ask AI

```
add_template(self, template: ResourceTemplate) -> None

```

Add a resource template to the server.

**Args:**

- `template`: A ResourceTemplate instance to add

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#add-resource-fn)  `add_resource_fn`

Copy

Ask AI

```
add_resource_fn(self, fn: AnyFunction, uri: str, name: str | None = None, description: str | None = None, mime_type: str | None = None, tags: set[str] | None = None) -> None

```

Add a resource or template to the server from a function.

If the URI contains parameters (e.g. “resource://”) or the function
has parameters, it will be registered as a template resource.

**Args:**

- `fn`: The function to register as a resource
- `uri`: The URI for the resource
- `name`: Optional name for the resource
- `description`: Optional description of the resource
- `mime_type`: Optional MIME type for the resource
- `tags`: Optional set of tags for categorizing the resource

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#resource)  `resource`

Copy

Ask AI

```
resource(self, uri: str) -> Callable[[AnyFunction], Resource | ResourceTemplate]

```

Decorator to register a function as a resource.

The function will be called when the resource is read to generate its content.
The function can return:

- str for text content
- bytes for binary content
- other types will be converted to JSON

Resources can optionally request a Context object by adding a parameter with the
Context type annotation. The context provides access to MCP capabilities like
logging, progress reporting, and session information.

If the URI contains parameters (e.g. “resource://”) or the function
has parameters, it will be registered as a template resource.

**Args:**

- `uri`: URI for the resource (e.g. “resource://my-resource” or “resource://”)
- `name`: Optional name for the resource
- `description`: Optional description of the resource
- `mime_type`: Optional MIME type for the resource
- `tags`: Optional set of tags for categorizing the resource
- `enabled`: Optional boolean to enable or disable the resource

**Examples:**

Register a resource with a custom name:

Copy

Ask AI

```
@server.resource("resource://my-resource")
def get_data() -> str:
    return "Hello, world!"

@server.resource("resource://my-resource")
async get_data() -> str:
    data = await fetch_data()
    return f"Hello, world! {data}"

@server.resource("resource://{city}/weather")
def get_weather(city: str) -> str:
    return f"Weather for {city}"

@server.resource("resource://{city}/weather")
def get_weather_with_context(city: str, ctx: Context) -> str:
    ctx.info(f"Fetching weather for {city}")
    return f"Weather for {city}"

@server.resource("resource://{city}/weather")
async def get_weather(city: str) -> str:
    data = await fetch_weather(city)
    return f"Weather for {city}: {data}"

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#add-prompt)  `add_prompt`

Copy

Ask AI

```
add_prompt(self, prompt: Prompt) -> None

```

Add a prompt to the server.

**Args:**

- `prompt`: A Prompt instance to add

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#prompt)  `prompt`

Copy

Ask AI

```
prompt(self, name_or_fn: AnyFunction) -> FunctionPrompt

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#prompt-2)  `prompt`

Copy

Ask AI

```
prompt(self, name_or_fn: str | None = None) -> Callable[[AnyFunction], FunctionPrompt]

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#prompt-3)  `prompt`

Copy

Ask AI

```
prompt(self, name_or_fn: str | AnyFunction | None = None) -> Callable[[AnyFunction], FunctionPrompt] | FunctionPrompt

```

Decorator to register a prompt.

Prompts can optionally request a Context object by adding a parameter with the
Context type annotation. The context provides access to MCP capabilities like
logging, progress reporting, and session information.

This decorator supports multiple calling patterns:

- @server.prompt (without parentheses)
- @server.prompt() (with empty parentheses)
- @server.prompt(“custom\_name”) (with name as first argument)
- @server.prompt(name=“custom\_name”) (with name as keyword argument)
- server.prompt(function, name=“custom\_name”) (direct function call)

Args:
name\_or\_fn: Either a function (when used as @prompt), a string name, or None
name: Optional name for the prompt (keyword-only, alternative to name\_or\_fn)
description: Optional description of what the prompt does
tags: Optional set of tags for categorizing the prompt
enabled: Optional boolean to enable or disable the prompt

Examples:

Copy

Ask AI

```
@server.prompt
def analyze_table(table_name: str) -> list[Message]:
    schema = read_table_schema(table_name)
    return [\
        {\
            "role": "user",\
            "content": f"Analyze this schema:\
{schema}"\
        }\
    ]

@server.prompt()
def analyze_with_context(table_name: str, ctx: Context) -> list[Message]:
    ctx.info(f"Analyzing table {table_name}")
    schema = read_table_schema(table_name)
    return [\
        {\
            "role": "user",\
            "content": f"Analyze this schema:\
{schema}"\
        }\
    ]

@server.prompt("custom_name")
def analyze_file(path: str) -> list[Message]:
    content = await read_file(path)
    return [\
        {\
            "role": "user",\
            "content": {\
                "type": "resource",\
                "resource": {\
                    "uri": f"file://{path}",\
                    "text": content\
                }\
            }\
        }\
    ]

@server.prompt(name="custom_name")
def another_prompt(data: str) -> list[Message]:
    return [{"role": "user", "content": data}]

# Direct function call
server.prompt(my_function, name="custom_name")

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#sse-app)  `sse_app`

Copy

Ask AI

```
sse_app(self, path: str | None = None, message_path: str | None = None, middleware: list[ASGIMiddleware] | None = None) -> StarletteWithLifespan

```

Create a Starlette app for the SSE server.

**Args:**

- `path`: The path to the SSE endpoint
- `message_path`: The path to the message endpoint
- `middleware`: A list of middleware to apply to the app

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#streamable-http-app)  `streamable_http_app`

Copy

Ask AI

```
streamable_http_app(self, path: str | None = None, middleware: list[ASGIMiddleware] | None = None) -> StarletteWithLifespan

```

Create a Starlette app for the StreamableHTTP server.

**Args:**

- `path`: The path to the StreamableHTTP endpoint
- `middleware`: A list of middleware to apply to the app

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#http-app)  `http_app`

Copy

Ask AI

```
http_app(self, path: str | None = None, middleware: list[ASGIMiddleware] | None = None, json_response: bool | None = None, stateless_http: bool | None = None, transport: Literal['http', 'streamable-http', 'sse'] = 'http') -> StarletteWithLifespan

```

Create a Starlette app using the specified HTTP transport.

**Args:**

- `path`: The path for the HTTP endpoint
- `middleware`: A list of middleware to apply to the app
- `transport`: Transport protocol to use - either “streamable-http” (default) or “sse”

**Returns:**

- A Starlette application configured with the specified transport

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#mount)  `mount`

Copy

Ask AI

```
mount(self, server: FastMCP[LifespanResultT], prefix: str | None = None, as_proxy: bool | None = None) -> None

```

Mount another FastMCP server on this server with an optional prefix.

Unlike importing (with import\_server), mounting establishes a dynamic connection
between servers. When a client interacts with a mounted server’s objects through
the parent server, requests are forwarded to the mounted server in real-time.
This means changes to the mounted server are immediately reflected when accessed
through the parent.

When a server is mounted with a prefix:

- Tools from the mounted server are accessible with prefixed names.
Example: If server has a tool named “get\_weather”, it will be available as “prefix\_get\_weather”.
- Resources are accessible with prefixed URIs.
Example: If server has a resource with URI “weather://forecast”, it will be available as
“weather://prefix/forecast”.
- Templates are accessible with prefixed URI templates.
Example: If server has a template with URI “weather://location/”, it will be available
as “weather://prefix/location/”.
- Prompts are accessible with prefixed names.
Example: If server has a prompt named “weather\_prompt”, it will be available as
“prefix\_weather\_prompt”.

When a server is mounted without a prefix (prefix=None), its tools, resources, templates,
and prompts are accessible with their original names. Multiple servers can be mounted
without prefixes, and they will be tried in order until a match is found.

There are two modes for mounting servers:

1. Direct mounting (default when server has no custom lifespan): The parent server
directly accesses the mounted server’s objects in-memory for better performance.
In this mode, no client lifecycle events occur on the mounted server, including
lifespan execution.

2. Proxy mounting (default when server has a custom lifespan): The parent server
treats the mounted server as a separate entity and communicates with it via a
Client transport. This preserves all client-facing behaviors, including lifespan
execution, but with slightly higher overhead.


**Args:**

- `server`: The FastMCP server to mount.
- `prefix`: Optional prefix to use for the mounted server’s objects. If None,
the server’s objects are accessible with their original names.
- `as_proxy`: Whether to treat the mounted server as a proxy. If None (default),
automatically determined based on whether the server has a custom lifespan
(True if it has a custom lifespan, False otherwise).
- `tool_separator`: Deprecated. Separator character for tool names.
- `resource_separator`: Deprecated. Separator character for resource URIs.
- `prompt_separator`: Deprecated. Separator character for prompt names.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#from-openapi)  `from_openapi`

Copy

Ask AI

```
from_openapi(cls, openapi_spec: dict[str, Any], client: httpx.AsyncClient, route_maps: list[RouteMap] | None = None, route_map_fn: OpenAPIRouteMapFn | None = None, mcp_component_fn: OpenAPIComponentFn | None = None, mcp_names: dict[str, str] | None = None, tags: set[str] | None = None, **settings: Any) -> FastMCPOpenAPI

```

Create a FastMCP server from an OpenAPI specification.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#from-fastapi)  `from_fastapi`

Copy

Ask AI

```
from_fastapi(cls, app: Any, name: str | None = None, route_maps: list[RouteMap] | None = None, route_map_fn: OpenAPIRouteMapFn | None = None, mcp_component_fn: OpenAPIComponentFn | None = None, mcp_names: dict[str, str] | None = None, httpx_client_kwargs: dict[str, Any] | None = None, tags: set[str] | None = None, **settings: Any) -> FastMCPOpenAPI

```

Create a FastMCP server from a FastAPI application.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#as-proxy)  `as_proxy`

Copy

Ask AI

```
as_proxy(cls, backend: Client[ClientTransportT] | ClientTransport | FastMCP[Any] | AnyUrl | Path | MCPConfig | dict[str, Any] | str, **settings: Any) -> FastMCPProxy

```

Create a FastMCP proxy server for the given backend.

The `backend` argument can be either an existing `fastmcp.client.Client`
instance or any value accepted as the `transport` argument of
`fastmcp.client.Client`. This mirrors the convenience of the
`fastmcp.client.Client` constructor.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#from-client)  `from_client`

Copy

Ask AI

```
from_client(cls, client: Client[ClientTransportT], **settings: Any) -> FastMCPProxy

```

Create a FastMCP proxy server from a FastMCP client.

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-server\#mountedserver)  `MountedServer`

[proxy](https://gofastmcp.com/python-sdk/fastmcp-server-proxy) [\_\_init\_\_](https://gofastmcp.com/python-sdk/fastmcp-tools-__init__)

On this page

- [fastmcp.server.server](https://gofastmcp.com/python-sdk/fastmcp-server-server#fastmcp-server-server)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-server-server#functions)
- [add\_resource\_prefix](https://gofastmcp.com/python-sdk/fastmcp-server-server#add-resource-prefix)
- [remove\_resource\_prefix](https://gofastmcp.com/python-sdk/fastmcp-server-server#remove-resource-prefix)
- [has\_resource\_prefix](https://gofastmcp.com/python-sdk/fastmcp-server-server#has-resource-prefix)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-server-server#classes)
- [FastMCP](https://gofastmcp.com/python-sdk/fastmcp-server-server#fastmcp)
- [settings](https://gofastmcp.com/python-sdk/fastmcp-server-server#settings)
- [name](https://gofastmcp.com/python-sdk/fastmcp-server-server#name)
- [instructions](https://gofastmcp.com/python-sdk/fastmcp-server-server#instructions)
- [run](https://gofastmcp.com/python-sdk/fastmcp-server-server#run)
- [add\_middleware](https://gofastmcp.com/python-sdk/fastmcp-server-server#add-middleware)
- [custom\_route](https://gofastmcp.com/python-sdk/fastmcp-server-server#custom-route)
- [add\_tool](https://gofastmcp.com/python-sdk/fastmcp-server-server#add-tool)
- [remove\_tool](https://gofastmcp.com/python-sdk/fastmcp-server-server#remove-tool)
- [tool](https://gofastmcp.com/python-sdk/fastmcp-server-server#tool)
- [tool](https://gofastmcp.com/python-sdk/fastmcp-server-server#tool-2)
- [tool](https://gofastmcp.com/python-sdk/fastmcp-server-server#tool-3)
- [add\_resource](https://gofastmcp.com/python-sdk/fastmcp-server-server#add-resource)
- [add\_template](https://gofastmcp.com/python-sdk/fastmcp-server-server#add-template)
- [add\_resource\_fn](https://gofastmcp.com/python-sdk/fastmcp-server-server#add-resource-fn)
- [resource](https://gofastmcp.com/python-sdk/fastmcp-server-server#resource)
- [add\_prompt](https://gofastmcp.com/python-sdk/fastmcp-server-server#add-prompt)
- [prompt](https://gofastmcp.com/python-sdk/fastmcp-server-server#prompt)
- [prompt](https://gofastmcp.com/python-sdk/fastmcp-server-server#prompt-2)
- [prompt](https://gofastmcp.com/python-sdk/fastmcp-server-server#prompt-3)
- [sse\_app](https://gofastmcp.com/python-sdk/fastmcp-server-server#sse-app)
- [streamable\_http\_app](https://gofastmcp.com/python-sdk/fastmcp-server-server#streamable-http-app)
- [http\_app](https://gofastmcp.com/python-sdk/fastmcp-server-server#http-app)
- [mount](https://gofastmcp.com/python-sdk/fastmcp-server-server#mount)
- [from\_openapi](https://gofastmcp.com/python-sdk/fastmcp-server-server#from-openapi)
- [from\_fastapi](https://gofastmcp.com/python-sdk/fastmcp-server-server#from-fastapi)
- [as\_proxy](https://gofastmcp.com/python-sdk/fastmcp-server-server#as-proxy)
- [from\_client](https://gofastmcp.com/python-sdk/fastmcp-server-server#from-client)
- [MountedServer](https://gofastmcp.com/python-sdk/fastmcp-server-server#mountedserver)

Assistant

Responses are generated using AI and may contain mistakes.