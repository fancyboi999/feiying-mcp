# oauth_callback - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback
**Generated:** 2025-06-30

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.client

oauth\_callback

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback\#fastmcp-client-oauth-callback)  `fastmcp.client.oauth_callback`

OAuth callback server for handling authorization code flows.

This module provides a reusable callback server that can handle OAuth redirects
and display styled responses to users.

## [​](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback\#create-callback-html)  `create_callback_html`

Copy

Ask AI

```
create_callback_html(message: str, is_success: bool = True, title: str = 'FastMCP OAuth', server_url: str | None = None) -> str

```

Create a styled HTML response for OAuth callbacks.

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback\#create-oauth-callback-server)  `create_oauth_callback_server`

Copy

Ask AI

```
create_oauth_callback_server(port: int, callback_path: str = '/callback', server_url: str | None = None, response_future: asyncio.Future | None = None) -> Server

```

Create an OAuth callback server.

**Args:**

- `port`: The port to run the server on
- `callback_path`: The path to listen for OAuth redirects on
- `server_url`: Optional server URL to display in success messages
- `response_future`: Optional future to resolve when OAuth callback is received

**Returns:**

- Configured uvicorn Server instance (not yet running)

## [​](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback\#callbackresponse)  `CallbackResponse`

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback\#from-dict)  `from_dict`

Copy

Ask AI

```
from_dict(cls, data: dict[str, str]) -> CallbackResponse

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback\#to-dict)  `to_dict`

Copy

Ask AI

```
to_dict(self) -> dict[str, str]

```

[logging](https://gofastmcp.com/python-sdk/fastmcp-client-logging) [progress](https://gofastmcp.com/python-sdk/fastmcp-client-progress)

On this page

- [fastmcp.client.oauth\_callback](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback#fastmcp-client-oauth-callback)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback#functions)
- [create\_callback\_html](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback#create-callback-html)
- [create\_oauth\_callback\_server](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback#create-oauth-callback-server)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback#classes)
- [CallbackResponse](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback#callbackresponse)
- [from\_dict](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback#from-dict)
- [to\_dict](https://gofastmcp.com/python-sdk/fastmcp-client-oauth_callback#to-dict)

Assistant

Responses are generated using AI and may contain mistakes.