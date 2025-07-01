# Bearer Token Authentication - FastMCP

**Source URL:** https://gofastmcp.com/clients/auth/bearer
**Generated:** 2025-06-30

**Description:** Authenticate your FastMCP client with a Bearer token.

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Authentication

Bearer Token Authentication

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

`New in version: 2.6.0`

Bearer Token authentication is only relevant for HTTP-based transports.

You can configure your FastMCP client to use **bearer authentication** by supplying a valid access token. This is most appropriate for service accounts, long-lived API keys, CI/CD, applications where authentication is managed separately, or other non-interactive authentication methods.

A Bearer token is a JSON Web Token (JWT) that is used to authenticate a request. It is most commonly used in the `Authorization` header of an HTTP request, using the `Bearer` scheme:

Copy

Ask AI

```
Authorization: Bearer <token>

```

## [​](https://gofastmcp.com/clients/auth/bearer\#client-usage)  Client Usage

The most straightforward way to use a pre-existing Bearer token is to provide it as a string to the `auth` parameter of the `fastmcp.Client` or transport instance. FastMCP will automatically format it correctly for the `Authorization` header and bearer scheme.

If you’re using a string token, do not include the `Bearer` prefix. FastMCP will add it for you.

Copy

Ask AI

```
from fastmcp import Client

async with Client(
    "https://fastmcp.cloud/mcp",
    auth="<your-token>",
) as client:
    await client.ping()

```

You can also supply a Bearer token to a transport instance, such as `StreamableHttpTransport` or `SSETransport`:

Copy

Ask AI

```
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

transport = StreamableHttpTransport(
    "http://fastmcp.cloud/mcp",
    auth="<your-token>",
)

async with Client(transport) as client:
    await client.ping()

```

## [​](https://gofastmcp.com/clients/auth/bearer\#bearerauth-helper)  `BearerAuth` Helper

If you prefer to be more explicit and not rely on FastMCP to transform your string token, you can use the `BearerAuth` class yourself, which implements the `httpx.Auth` interface.

Copy

Ask AI

```
from fastmcp import Client
from fastmcp.client.auth import BearerAuth

async with Client(
    "https://fastmcp.cloud/mcp",
    auth=BearerAuth(token="<your-token>"),
) as client:
    await client.ping()

```

## [​](https://gofastmcp.com/clients/auth/bearer\#custom-headers)  Custom Headers

If the MCP server expects a custom header or token scheme, you can manually set the client’s `headers` instead of using the `auth` parameter by setting them on your transport:

Copy

Ask AI

```
from fastmcp import Client
from fastmcp.client.transports import StreamableHttpTransport

async with Client(
    transport=StreamableHttpTransport(
        "https://fastmcp.cloud/mcp",
        headers={"X-API-Key": "<your-token>"},
    ),
) as client:
    await client.ping()

```

[OAuth](https://gofastmcp.com/clients/auth/oauth) [Anthropic API](https://gofastmcp.com/integrations/anthropic)

On this page

- [Client Usage](https://gofastmcp.com/clients/auth/bearer#client-usage)
- [BearerAuth Helper](https://gofastmcp.com/clients/auth/bearer#bearerauth-helper)
- [Custom Headers](https://gofastmcp.com/clients/auth/bearer#custom-headers)

Assistant

Responses are generated using AI and may contain mistakes.