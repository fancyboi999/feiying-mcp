# Client Roots - FastMCP

**Source URL:** https://gofastmcp.com/clients/roots
**Generated:** 2025-06-30

**Description:** Provide local context and resource boundaries to MCP servers.

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Advanced Features

Client Roots

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

`New in version: 2.0.0`

Roots are a way for clients to inform servers about the resources they have access to. Servers can use this information to adjust behavior or provide more relevant responses.

## [​](https://gofastmcp.com/clients/roots\#setting-static-roots)  Setting Static Roots

Provide a list of roots when creating the client:

Static Roots

Dynamic Roots Callback

Copy

Ask AI

```
from fastmcp import Client

client = Client(
    "my_mcp_server.py",
    roots=["/path/to/root1", "/path/to/root2"]
)

```

[Messages](https://gofastmcp.com/clients/messages) [Transports](https://gofastmcp.com/clients/transports)

On this page

- [Setting Static Roots](https://gofastmcp.com/clients/roots#setting-static-roots)

Assistant

Responses are generated using AI and may contain mistakes.