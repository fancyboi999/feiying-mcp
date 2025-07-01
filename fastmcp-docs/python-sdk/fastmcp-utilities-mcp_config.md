# mcp_config - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config
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

mcp\_config

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config\#fastmcp-utilities-mcp-config)  `fastmcp.utilities.mcp_config`

## [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config\#infer-transport-type-from-url)  `infer_transport_type_from_url`

Copy

Ask AI

```
infer_transport_type_from_url(url: str | AnyUrl) -> Literal['http', 'sse']

```

Infer the appropriate transport type from the given URL.

## [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config\#stdiomcpserver)  `StdioMCPServer`

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config\#to-transport)  `to_transport`

Copy

Ask AI

```
to_transport(self) -> StdioTransport

```

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config\#remotemcpserver)  `RemoteMCPServer`

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config\#to-transport-2)  `to_transport`

Copy

Ask AI

```
to_transport(self) -> StreamableHttpTransport | SSETransport

```

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config\#mcpconfig)  `MCPConfig`

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config\#from-dict)  `from_dict`

Copy

Ask AI

```
from_dict(cls, config: dict[str, Any]) -> MCPConfig

```

[logging](https://gofastmcp.com/python-sdk/fastmcp-utilities-logging) [openapi](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi)

On this page

- [fastmcp.utilities.mcp\_config](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config#fastmcp-utilities-mcp-config)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config#functions)
- [infer\_transport\_type\_from\_url](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config#infer-transport-type-from-url)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config#classes)
- [StdioMCPServer](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config#stdiomcpserver)
- [to\_transport](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config#to-transport)
- [RemoteMCPServer](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config#remotemcpserver)
- [to\_transport](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config#to-transport-2)
- [MCPConfig](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config#mcpconfig)
- [from\_dict](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config#from-dict)

Assistant

Responses are generated using AI and may contain mistakes.