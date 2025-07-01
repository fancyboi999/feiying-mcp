# proxy - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-server-proxy
**Generated:** 2025-06-30

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.server

proxy

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-server-proxy\#fastmcp-server-proxy)  `fastmcp.server.proxy`

## [​](https://gofastmcp.com/python-sdk/fastmcp-server-proxy\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-proxy\#proxytoolmanager)  `ProxyToolManager`

A ToolManager that sources its tools from a remote client in addition to local and mounted tools.

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-proxy\#proxyresourcemanager)  `ProxyResourceManager`

A ResourceManager that sources its resources from a remote client in addition to local and mounted resources.

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-proxy\#proxypromptmanager)  `ProxyPromptManager`

A PromptManager that sources its prompts from a remote client in addition to local and mounted prompts.

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-proxy\#proxytool)  `ProxyTool`

A Tool that represents and executes a tool on a remote server.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-proxy\#from-mcp-tool)  `from_mcp_tool`

Copy

Ask AI

```
from_mcp_tool(cls, client: Client, mcp_tool: mcp.types.Tool) -> ProxyTool

```

Factory method to create a ProxyTool from a raw MCP tool schema.

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-proxy\#proxyresource)  `ProxyResource`

A Resource that represents and reads a resource from a remote server.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-proxy\#from-mcp-resource)  `from_mcp_resource`

Copy

Ask AI

```
from_mcp_resource(cls, client: Client, mcp_resource: mcp.types.Resource) -> ProxyResource

```

Factory method to create a ProxyResource from a raw MCP resource schema.

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-proxy\#proxytemplate)  `ProxyTemplate`

A ResourceTemplate that represents and creates resources from a remote server template.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-proxy\#from-mcp-template)  `from_mcp_template`

Copy

Ask AI

```
from_mcp_template(cls, client: Client, mcp_template: mcp.types.ResourceTemplate) -> ProxyTemplate

```

Factory method to create a ProxyTemplate from a raw MCP template schema.

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-proxy\#proxyprompt)  `ProxyPrompt`

A Prompt that represents and renders a prompt from a remote server.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-proxy\#from-mcp-prompt)  `from_mcp_prompt`

Copy

Ask AI

```
from_mcp_prompt(cls, client: Client, mcp_prompt: mcp.types.Prompt) -> ProxyPrompt

```

Factory method to create a ProxyPrompt from a raw MCP prompt schema.

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-proxy\#fastmcpproxy)  `FastMCPProxy`

A FastMCP server that acts as a proxy to a remote MCP-compliant server.
It uses specialized managers that fulfill requests via an HTTP client.

[openapi](https://gofastmcp.com/python-sdk/fastmcp-server-openapi) [server](https://gofastmcp.com/python-sdk/fastmcp-server-server)

On this page

- [fastmcp.server.proxy](https://gofastmcp.com/python-sdk/fastmcp-server-proxy#fastmcp-server-proxy)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-server-proxy#classes)
- [ProxyToolManager](https://gofastmcp.com/python-sdk/fastmcp-server-proxy#proxytoolmanager)
- [ProxyResourceManager](https://gofastmcp.com/python-sdk/fastmcp-server-proxy#proxyresourcemanager)
- [ProxyPromptManager](https://gofastmcp.com/python-sdk/fastmcp-server-proxy#proxypromptmanager)
- [ProxyTool](https://gofastmcp.com/python-sdk/fastmcp-server-proxy#proxytool)
- [from\_mcp\_tool](https://gofastmcp.com/python-sdk/fastmcp-server-proxy#from-mcp-tool)
- [ProxyResource](https://gofastmcp.com/python-sdk/fastmcp-server-proxy#proxyresource)
- [from\_mcp\_resource](https://gofastmcp.com/python-sdk/fastmcp-server-proxy#from-mcp-resource)
- [ProxyTemplate](https://gofastmcp.com/python-sdk/fastmcp-server-proxy#proxytemplate)
- [from\_mcp\_template](https://gofastmcp.com/python-sdk/fastmcp-server-proxy#from-mcp-template)
- [ProxyPrompt](https://gofastmcp.com/python-sdk/fastmcp-server-proxy#proxyprompt)
- [from\_mcp\_prompt](https://gofastmcp.com/python-sdk/fastmcp-server-proxy#from-mcp-prompt)
- [FastMCPProxy](https://gofastmcp.com/python-sdk/fastmcp-server-proxy#fastmcpproxy)

Assistant

Responses are generated using AI and may contain mistakes.