# Eunomia Authorization + FastMCP - FastMCP

**Source URL:** https://gofastmcp.com/integrations/eunomia-authorization
**Generated:** 2025-06-30

**Description:** Add policy-based authorization to your FastMCP servers

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Integrations

Eunomia Authorization + FastMCP

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

Add **policy-based authorization** to your FastMCP servers with minimal code changes using Eunomia authorization middleware.

Control which actions MCP clients can perform on your server by restricting how the agent can access resources, tools and prompts by using JSON-based policies, while obtaining a comprehensive audit log of all access attempts and violations.

## [​](https://gofastmcp.com/integrations/eunomia-authorization\#eunomia-authorization-middleware)  Eunomia Authorization Middleware

The middleware intercepts all MCP requests to your server and automatically maps MCP methods to authorization checks.

Eunomia ServerFastMCP ServerEunomia MiddlewareMCP ClientEunomia ServerFastMCP ServerEunomia MiddlewareMCP ClientMiddleware intercepts request to serverMCP RequestAuthorization CheckAuthorization Decision (allow/deny)MCP Unauthorized Error (if denied)MCP Request (if allowed)MCP Response (if allowed)

Eunomia is an AI-specific standalone authorization server that handles policy decisions. You must have an Eunomia server running alongside your FastMCP server for the middleware to function.

Run it in the background with Docker:

Copy

Ask AI

```
docker run -d -p 8000:8000 ttommitt/eunomia-server:latest

```

### [​](https://gofastmcp.com/integrations/eunomia-authorization\#create-a-server-with-authorization)  Create a Server with Authorization

First, install the `eunomia-mcp` package:

Copy

Ask AI

```
pip install eunomia-mcp

```

Then create a FastMCP server and add the Eunomia middleware with a few lines of code:

server.py

Copy

Ask AI

```
from fastmcp import FastMCP
from eunomia_mcp import create_eunomia_middleware

mcp = FastMCP("Secure FastMCP Server 🔒")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

middleware = [create_eunomia_middleware()]
app = mcp.http_app(middleware=middleware)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8080)

```

### [​](https://gofastmcp.com/integrations/eunomia-authorization\#configure-access-policies)  Configure Access Policies

Use the `eunomia-mcp` CLI in your terminal to manage your authorization policies:

Copy

Ask AI

```
# Create a default policy configuration file
eunomia-mcp init

```

This creates a policy file you can customize to control access to your MCP tools and resources.

Copy

Ask AI

```
# Once ready, validate your policy
eunomia-mcp validate mcp_policies.json

# And push it to the Eunomia server
eunomia-mcp push mcp_policies.json

```

### [​](https://gofastmcp.com/integrations/eunomia-authorization\#run-the-server)  Run the Server

Start your FastMCP server normally:

Copy

Ask AI

```
python server.py

```

The middleware will now intercept all MCP requests and check them against your policies. Requests include agent identification through headers like `X-Agent-ID`, `X-User-ID`, or `Authorization` and an automatic mapping of MCP methods to authorization resources and actions.

For detailed policy configuration, custom authentication, and advanced
deployment patterns, visit the [Eunomia MCP Middleware\\
repository](https://github.com/whataboutyou-ai/eunomia/tree/main/pkgs/extensions/mcp).

[OpenAI API](https://gofastmcp.com/integrations/openai) [Contrib Modules](https://gofastmcp.com/integrations/contrib)

On this page

- [Eunomia Authorization Middleware](https://gofastmcp.com/integrations/eunomia-authorization#eunomia-authorization-middleware)
- [Create a Server with Authorization](https://gofastmcp.com/integrations/eunomia-authorization#create-a-server-with-authorization)
- [Configure Access Policies](https://gofastmcp.com/integrations/eunomia-authorization#configure-access-policies)
- [Run the Server](https://gofastmcp.com/integrations/eunomia-authorization#run-the-server)

Assistant

Responses are generated using AI and may contain mistakes.