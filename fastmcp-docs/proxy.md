# Proxy Servers - FastMCP

**Source URL:** https://gofastmcp.com/servers/proxy
**Generated:** 2025-06-27

**Description:** Use FastMCP to act as an intermediary or change transport for other MCP servers.

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Servers

Proxy Servers

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

`New in version: 2.0.0`

FastMCP provides a powerful proxying capability that allows one FastMCP server instance to act as a frontend for another MCP server (which could be remote, running on a different transport, or even another FastMCP instance). This is achieved using the `FastMCP.as_proxy()` class method.

`as_proxy()` accepts either an existing `Client` or any argument that can be passed to a `Client` as its `transport` parameter—such as another `FastMCP` instance, a URL to a remote server, or an MCP configuration dictionary.

## [​](https://gofastmcp.com/servers/proxy\#what-is-proxying%3F)  What is Proxying?

Proxying means setting up a FastMCP server that doesn’t implement its own tools or resources directly. Instead, when it receives a request (like `tools/call` or `resources/read`), it forwards that request to a _backend_ MCP server, receives the response, and then relays that response back to the original client.

Backend MCP Server (e.g., remote SSE)FastMCP Proxy ServerYour Client (e.g., Claude Desktop)Backend MCP Server (e.g., remote SSE)FastMCP Proxy ServerYour Client (e.g., Claude Desktop)Proxy forwards the requestProxy relays the responseMCP Request (e.g. stdio)MCP Request (e.g. sse)MCP Response (e.g. sse)MCP Response (e.g. stdio)

### [​](https://gofastmcp.com/servers/proxy\#use-cases)  Use Cases

- **Transport Bridging**: Expose a server running on one transport (e.g., a remote SSE server) via a different transport (e.g., local Stdio for Claude Desktop).
- **Adding Functionality**: Insert a layer in front of an existing server to add caching, logging, authentication, or modify requests/responses (though direct modification requires subclassing `FastMCPProxy`).
- **Security Boundary**: Use the proxy as a controlled gateway to an internal server.
- **Simplifying Client Configuration**: Provide a single, stable endpoint (the proxy) even if the backend server’s location or transport changes.

## [​](https://gofastmcp.com/servers/proxy\#creating-a-proxy)  Creating a Proxy

The easiest way to create a proxy is using the `FastMCP.as_proxy()` class method. This creates a standard FastMCP server that forwards requests to another MCP server.

Copy

Ask AI

```
from fastmcp import FastMCP

# Provide the backend in any form accepted by Client
proxy_server = FastMCP.as_proxy(
    "backend_server.py",  # Could also be a FastMCP instance, config dict, or a remote URL
    name="MyProxyServer"  # Optional settings for the proxy
)

# Or create the Client yourself for custom configuration
backend_client = Client("backend_server.py")
proxy_from_client = FastMCP.as_proxy(backend_client)

```

**How `as_proxy` Works:**

1. It connects to the backend server using the provided client.
2. It discovers all the tools, resources, resource templates, and prompts available on the backend server.
3. It creates corresponding “proxy” components that forward requests to the backend.
4. It returns a standard `FastMCP` server instance that can be used like any other.

Currently, proxying focuses primarily on exposing the major MCP objects (tools, resources, templates, and prompts). Some advanced MCP features like notifications and sampling are not fully supported in proxies in the current version. Support for these additional features may be added in future releases.

### [​](https://gofastmcp.com/servers/proxy\#bridging-transports)  Bridging Transports

A common use case is to bridge transports. For example, making a remote SSE server available locally via Stdio:

Copy

Ask AI

```
from fastmcp import FastMCP

# Target a remote SSE server directly by URL
proxy = FastMCP.as_proxy("http://example.com/mcp/sse", name="SSE to Stdio Proxy")

# The proxy can now be used with any transport
# No special handling needed - it works like any FastMCP server

```

### [​](https://gofastmcp.com/servers/proxy\#in-memory-proxies)  In-Memory Proxies

You can also proxy an in-memory `FastMCP` instance, which is useful for adjusting the configuration or behavior of a server you don’t completely control.

Copy

Ask AI

```
from fastmcp import FastMCP

# Original server
original_server = FastMCP(name="Original")

@original_server.tool
def tool_a() -> str:
    return "A"

# Create a proxy of the original server directly
proxy = FastMCP.as_proxy(
    original_server,
    name="Proxy Server"
)

# proxy is now a regular FastMCP server that forwards
# requests to original_server

```

### [​](https://gofastmcp.com/servers/proxy\#configuration-based-proxies)  Configuration-Based Proxies

`New in version: 2.4.0`

You can create a proxy directly from a configuration dictionary that follows the MCPConfig schema. This is useful for quickly setting up proxies to remote servers without manually configuring each connection detail.

Copy

Ask AI

```
from fastmcp import FastMCP

# Create a proxy directly from a config dictionary
config = {
    "mcpServers": {
        "default": {  # For single server configs, 'default' is commonly used
            "url": "https://example.com/mcp",
            "transport": "http"
        }
    }
}

# Create a proxy to the configured server
proxy = FastMCP.as_proxy(config, name="Config-Based Proxy")

# Run the proxy with stdio transport for local access
if __name__ == "__main__":
    proxy.run()

```

The MCPConfig format follows an emerging standard for MCP server configuration and may evolve as the specification matures. While FastMCP aims to maintain compatibility with future versions, be aware that field names or structure might change.

You can also use MCPConfig to create a proxy to multiple servers. When multiple servers are specified, they are automatically mounted with their config names as prefixes, providing a unified interface to all servers:

Copy

Ask AI

```
from fastmcp import FastMCP

# Multi-server configuration
config = {
    "mcpServers": {
        "weather": {
            "url": "https://weather-api.example.com/mcp",
            "transport": "http"
        },
        "calendar": {
            "url": "https://calendar-api.example.com/mcp",
            "transport": "http"
        }
    }
}

# Create a proxy to multiple servers
composite_proxy = FastMCP.as_proxy(config, name="Composite Proxy")

# Tools and resources are accessible with prefixes:
# - weather_get_forecast, calendar_add_event
# - weather://weather/icons/sunny, calendar://calendar/events/today

```

## [​](https://gofastmcp.com/servers/proxy\#fastmcpproxy-class)  `FastMCPProxy` Class

Internally, `FastMCP.as_proxy()` uses the `FastMCPProxy` class. You generally don’t need to interact with this class directly, but it’s available if needed.

Using the class directly might be necessary for advanced scenarios, like subclassing `FastMCPProxy` to add custom logic before or after forwarding requests.

[OpenAPI Integration](https://gofastmcp.com/servers/openapi) [Composition](https://gofastmcp.com/servers/composition)

On this page

- [What is Proxying?](https://gofastmcp.com/servers/proxy#what-is-proxying%3F)
- [Use Cases](https://gofastmcp.com/servers/proxy#use-cases)
- [Creating a Proxy](https://gofastmcp.com/servers/proxy#creating-a-proxy)
- [Bridging Transports](https://gofastmcp.com/servers/proxy#bridging-transports)
- [In-Memory Proxies](https://gofastmcp.com/servers/proxy#in-memory-proxies)
- [Configuration-Based Proxies](https://gofastmcp.com/servers/proxy#configuration-based-proxies)
- [FastMCPProxy Class](https://gofastmcp.com/servers/proxy#fastmcpproxy-class)

Assistant

Responses are generated using AI and may contain mistakes.