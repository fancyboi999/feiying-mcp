# Server Composition - FastMCP

**Source URL:** https://gofastmcp.com/servers/composition
**Generated:** 2025-06-30

**Description:** Combine multiple FastMCP servers into a single, larger application using mounting and importing.

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Servers

Server Composition

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

`New in version: 2.2.0`

As your MCP applications grow, you might want to organize your tools, resources, and prompts into logical modules or reuse existing server components. FastMCP supports composition through two methods:

- **`import_server`**: For a one-time copy of components with prefixing (static composition).
- **`mount`**: For creating a live link where the main server delegates requests to the subserver (dynamic composition).

## [​](https://gofastmcp.com/servers/composition\#why-compose-servers%3F)  Why Compose Servers?

- **Modularity**: Break down large applications into smaller, focused servers (e.g., a `WeatherServer`, a `DatabaseServer`, a `CalendarServer`).
- **Reusability**: Create common utility servers (e.g., a `TextProcessingServer`) and mount them wherever needed.
- **Teamwork**: Different teams can work on separate FastMCP servers that are later combined.
- **Organization**: Keep related functionality grouped together logically.

### [​](https://gofastmcp.com/servers/composition\#importing-vs-mounting)  Importing vs Mounting

The choice of importing or mounting depends on your use case and requirements.

| Feature | Importing | Mounting |
| --- | --- | --- |
| **Method** | `FastMCP.import_server(server, prefix=None)` | `FastMCP.mount(server, prefix=None)` |
| **Composition Type** | One-time copy (static) | Live link (dynamic) |
| **Updates** | Changes to subserver NOT reflected | Changes to subserver immediately reflected |
| **Prefix** | Optional - omit for original names | Optional - omit for original names |
| **Best For** | Bundling finalized components | Modular runtime composition |

### [​](https://gofastmcp.com/servers/composition\#proxy-servers)  Proxy Servers

FastMCP supports [MCP proxying](https://gofastmcp.com/servers/proxy), which allows you to mirror a local or remote server in a local FastMCP instance. Proxies are fully compatible with both importing and mounting.

`New in version: 2.4.0`

You can also create proxies from configuration dictionaries that follow the MCPConfig schema, which is useful for quickly connecting to one or more remote servers. See the [Proxy Servers documentation](https://gofastmcp.com/servers/proxy#configuration-based-proxies) for details on configuration-based proxying. Note that MCPConfig follows an emerging standard and its format may evolve over time.

## [​](https://gofastmcp.com/servers/composition\#importing-static-composition)  Importing (Static Composition)

The `import_server()` method copies all components (tools, resources, templates, prompts) from one `FastMCP` instance (the _subserver_) into another (the _main server_). An optional `prefix` can be provided to avoid naming conflicts. If no prefix is provided, components are imported without modification. When multiple servers are imported with the same prefix (or no prefix), the most recently imported server’s components take precedence.

Copy

Ask AI

```
from fastmcp import FastMCP
import asyncio

# Define subservers
weather_mcp = FastMCP(name="WeatherService")

@weather_mcp.tool
def get_forecast(city: str) -> dict:
    """Get weather forecast."""
    return {"city": city, "forecast": "Sunny"}

@weather_mcp.resource("data://cities/supported")
def list_supported_cities() -> list[str]:
    """List cities with weather support."""
    return ["London", "Paris", "Tokyo"]

# Define main server
main_mcp = FastMCP(name="MainApp")

# Import subserver
async def setup():
    await main_mcp.import_server(weather_mcp, prefix="weather")

# Result: main_mcp now contains prefixed components:
# - Tool: "weather_get_forecast"
# - Resource: "data://weather/cities/supported"

if __name__ == "__main__":
    asyncio.run(setup())
    main_mcp.run()

```

### [​](https://gofastmcp.com/servers/composition\#how-importing-works)  How Importing Works

When you call `await main_mcp.import_server(subserver, prefix={whatever})`:

1. **Tools**: All tools from `subserver` are added to `main_mcp` with names prefixed using `{prefix}_`.

   - `subserver.tool(name="my_tool")` becomes `main_mcp.tool(name="{prefix}_my_tool")`.
2. **Resources**: All resources are added with URIs prefixed in the format `protocol://{prefix}/path`.

   - `subserver.resource(uri="data://info")` becomes `main_mcp.resource(uri="data://{prefix}/info")`.
3. **Resource Templates**: Templates are prefixed similarly to resources.

   - `subserver.resource(uri="data://{id}")` becomes `main_mcp.resource(uri="data://{prefix}/{id}")`.
4. **Prompts**: All prompts are added with names prefixed using `{prefix}_`.

   - `subserver.prompt(name="my_prompt")` becomes `main_mcp.prompt(name="{prefix}_my_prompt")`.

Note that `import_server` performs a **one-time copy** of components. Changes made to the `subserver` _after_ importing **will not** be reflected in `main_mcp`. The `subserver`’s `lifespan` context is also **not** executed by the main server.

The `prefix` parameter is optional. If omitted, components are imported without modification.

#### [​](https://gofastmcp.com/servers/composition\#importing-without-prefixes)  Importing Without Prefixes

`New in version: 2.9.0`

You can also import servers without specifying a prefix, which copies components using their original names:

Copy

Ask AI

```

from fastmcp import FastMCP
import asyncio

# Define subservers
weather_mcp = FastMCP(name="WeatherService")

@weather_mcp.tool
def get_forecast(city: str) -> dict:
    """Get weather forecast."""
    return {"city": city, "forecast": "Sunny"}

@weather_mcp.resource("data://cities/supported")
def list_supported_cities() -> list[str]:
    """List cities with weather support."""
    return ["London", "Paris", "Tokyo"]

# Define main server
main_mcp = FastMCP(name="MainApp")

# Import subserver
async def setup():
    # Import without prefix - components keep original names
    await main_mcp.import_server(weather_mcp)

# Result: main_mcp now contains:
# - Tool: "get_forecast" (original name preserved)
# - Resource: "data://cities/supported" (original URI preserved)

if __name__ == "__main__":
    asyncio.run(setup())
    main_mcp.run()

```

#### [​](https://gofastmcp.com/servers/composition\#conflict-resolution)  Conflict Resolution

`New in version: 2.9.0`

When importing multiple servers with the same prefix, or no prefix, components from the **most recently imported** server take precedence.

## [​](https://gofastmcp.com/servers/composition\#mounting-live-linking)  Mounting (Live Linking)

The `mount()` method creates a **live link** between the `main_mcp` server and the `subserver`. Instead of copying components, requests for components matching the optional `prefix` are **delegated** to the `subserver` at runtime. If no prefix is provided, the subserver’s components are accessible without prefixing. When multiple servers are mounted with the same prefix (or no prefix), the most recently mounted server takes precedence for conflicting component names.

Copy

Ask AI

```
import asyncio
from fastmcp import FastMCP, Client

# Define subserver
dynamic_mcp = FastMCP(name="DynamicService")

@dynamic_mcp.tool
def initial_tool():
    """Initial tool demonstration."""
    return "Initial Tool Exists"

# Mount subserver (synchronous operation)
main_mcp = FastMCP(name="MainAppLive")
main_mcp.mount(dynamic_mcp, prefix="dynamic")

# Add a tool AFTER mounting - it will be accessible through main_mcp
@dynamic_mcp.tool
def added_later():
    """Tool added after mounting."""
    return "Tool Added Dynamically!"

# Testing access to mounted tools
async def test_dynamic_mount():
    tools = await main_mcp.get_tools()
    print("Available tools:", list(tools.keys()))
    # Shows: ['dynamic_initial_tool', 'dynamic_added_later']

    async with Client(main_mcp) as client:
        result = await client.call_tool("dynamic_added_later")
        print("Result:", result[0].text)
        # Shows: "Tool Added Dynamically!"

if __name__ == "__main__":
    asyncio.run(test_dynamic_mount())

```

### [​](https://gofastmcp.com/servers/composition\#how-mounting-works)  How Mounting Works

When mounting is configured:

1. **Live Link**: The parent server establishes a connection to the mounted server.
2. **Dynamic Updates**: Changes to the mounted server are immediately reflected when accessed through the parent.
3. **Prefixed Access**: The parent server uses prefixes to route requests to the mounted server.
4. **Delegation**: Requests for components matching the prefix are delegated to the mounted server at runtime.

The same prefixing rules apply as with `import_server` for naming tools, resources, templates, and prompts.

The `prefix` parameter is optional. If omitted, components are mounted without modification.

#### [​](https://gofastmcp.com/servers/composition\#mounting-without-prefixes)  Mounting Without Prefixes

`New in version: 2.9.0`

You can also mount servers without specifying a prefix, which makes components accessible without prefixing. This works identically to [importing without prefixes](https://gofastmcp.com/servers/composition#importing-without-prefixes), including [conflict resolution](https://gofastmcp.com/servers/composition#conflict-resolution).

### [​](https://gofastmcp.com/servers/composition\#direct-vs-proxy-mounting)  Direct vs. Proxy Mounting

`New in version: 2.2.7`

FastMCP supports two mounting modes:

1. **Direct Mounting** (default): The parent server directly accesses the mounted server’s objects in memory.

   - No client lifecycle events occur on the mounted server
   - The mounted server’s lifespan context is not executed
   - Communication is handled through direct method calls
2. **Proxy Mounting**: The parent server treats the mounted server as a separate entity and communicates with it through a client interface.

   - Full client lifecycle events occur on the mounted server
   - The mounted server’s lifespan is executed when a client connects
   - Communication happens via an in-memory Client transport

Copy

Ask AI

```
# Direct mounting (default when no custom lifespan)
main_mcp.mount(api_server, prefix="api")

# Proxy mounting (preserves full client lifecycle)
main_mcp.mount(api_server, prefix="api", as_proxy=True)

# Mounting without a prefix (components accessible without prefixing)
main_mcp.mount(api_server)

```

FastMCP automatically uses proxy mounting when the mounted server has a custom lifespan, but you can override this behavior with the `as_proxy` parameter.

#### [​](https://gofastmcp.com/servers/composition\#interaction-with-proxy-servers)  Interaction with Proxy Servers

When using `FastMCP.as_proxy()` to create a proxy server, mounting that server will always use proxy mounting:

Copy

Ask AI

```
# Create a proxy for a remote server
remote_proxy = FastMCP.as_proxy(Client("http://example.com/mcp"))

# Mount the proxy (always uses proxy mounting)
main_server.mount(remote_proxy, prefix="remote")

```

## [​](https://gofastmcp.com/servers/composition\#resource-prefix-formats)  Resource Prefix Formats

`New in version: 2.4.0`

When mounting or importing servers, resource URIs are usually prefixed to avoid naming conflicts. FastMCP supports two different formats for resource prefixes:

### [​](https://gofastmcp.com/servers/composition\#path-format-default)  Path Format (Default)

In path format, prefixes are added to the path component of the URI:

Copy

Ask AI

```
resource://prefix/path/to/resource

```

This is the default format since FastMCP 2.4. This format is recommended because it avoids issues with URI protocol restrictions (like underscores not being allowed in protocol names).

### [​](https://gofastmcp.com/servers/composition\#protocol-format-legacy)  Protocol Format (Legacy)

In protocol format, prefixes are added as part of the protocol:

Copy

Ask AI

```
prefix+resource://path/to/resource

```

This was the default format in FastMCP before 2.4. While still supported, it’s not recommended for new code as it can cause problems with prefix names that aren’t valid in URI protocols.

### [​](https://gofastmcp.com/servers/composition\#configuring-the-prefix-format)  Configuring the Prefix Format

You can configure the prefix format globally in code:

Copy

Ask AI

```
import fastmcp
fastmcp.settings.resource_prefix_format = "protocol"

```

Or via environment variable:

Copy

Ask AI

```
FASTMCP_RESOURCE_PREFIX_FORMAT=protocol

```

Or per-server:

Copy

Ask AI

```
from fastmcp import FastMCP

# Create a server that uses legacy protocol format
server = FastMCP("LegacyServer", resource_prefix_format="protocol")

# Create a server that uses new path format
server = FastMCP("NewServer", resource_prefix_format="path")

```

When mounting or importing servers, the prefix format of the parent server is used.

[Proxy Servers](https://gofastmcp.com/servers/proxy) [Running the Server](https://gofastmcp.com/deployment/running-server)

On this page

- [Why Compose Servers?](https://gofastmcp.com/servers/composition#why-compose-servers%3F)
- [Importing vs Mounting](https://gofastmcp.com/servers/composition#importing-vs-mounting)
- [Proxy Servers](https://gofastmcp.com/servers/composition#proxy-servers)
- [Importing (Static Composition)](https://gofastmcp.com/servers/composition#importing-static-composition)
- [How Importing Works](https://gofastmcp.com/servers/composition#how-importing-works)
- [Importing Without Prefixes](https://gofastmcp.com/servers/composition#importing-without-prefixes)
- [Conflict Resolution](https://gofastmcp.com/servers/composition#conflict-resolution)
- [Mounting (Live Linking)](https://gofastmcp.com/servers/composition#mounting-live-linking)
- [How Mounting Works](https://gofastmcp.com/servers/composition#how-mounting-works)
- [Mounting Without Prefixes](https://gofastmcp.com/servers/composition#mounting-without-prefixes)
- [Direct vs. Proxy Mounting](https://gofastmcp.com/servers/composition#direct-vs-proxy-mounting)
- [Interaction with Proxy Servers](https://gofastmcp.com/servers/composition#interaction-with-proxy-servers)
- [Resource Prefix Formats](https://gofastmcp.com/servers/composition#resource-prefix-formats)
- [Path Format (Default)](https://gofastmcp.com/servers/composition#path-format-default)
- [Protocol Format (Legacy)](https://gofastmcp.com/servers/composition#protocol-format-legacy)
- [Configuring the Prefix Format](https://gofastmcp.com/servers/composition#configuring-the-prefix-format)

Assistant

Responses are generated using AI and may contain mistakes.