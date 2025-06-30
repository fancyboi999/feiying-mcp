# oauth - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth
**Generated:** 2025-06-27

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

auth

oauth

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth\#fastmcp-client-auth-oauth)  `fastmcp.client.auth.oauth`

## [​](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth\#default-cache-dir)  `default_cache_dir`

Copy

Ask AI

```
default_cache_dir() -> Path

```

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth\#oauth)  `OAuth`

Copy

Ask AI

```
OAuth(mcp_url: str, scopes: str | list[str] | None = None, client_name: str = 'FastMCP Client', token_storage_cache_dir: Path | None = None, additional_client_metadata: dict[str, Any] | None = None) -> _MCPOAuthClientProvider

```

Create an OAuthClientProvider for an MCP server.

This is intended to be provided to the `auth` parameter of an
httpx.AsyncClient (or appropriate FastMCP client/transport instance)

**Args:**

- `mcp_url`: Full URL to the MCP endpoint (e.g. “http://host/mcp/sse/”)
- `scopes`: OAuth scopes to request. Can be a
- `client_name`: Name for this client during registration
- `token_storage_cache_dir`: Directory for FileTokenStorage
- `additional_client_metadata`: Extra fields for OAuthClientMetadata

**Returns:**

- OAuthClientProvider

## [​](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth\#serveroauthmetadata)  `ServerOAuthMetadata`

More flexible OAuth metadata model that accepts broader ranges of values
than the restrictive MCP standard model.

This handles real-world OAuth servers like PayPal that may support
additional methods not in the MCP specification.

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth\#oauthclientprovider)  `OAuthClientProvider`

OAuth client provider with more flexible OAuth metadata discovery.

### [​](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth\#filetokenstorage)  `FileTokenStorage`

File-based token storage implementation for OAuth credentials and tokens.
Implements the mcp.client.auth.TokenStorage protocol.

Each instance is tied to a specific server URL for proper token isolation.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth\#get-base-url)  `get_base_url`

Copy

Ask AI

```
get_base_url(url: str) -> str

```

Extract the base URL (scheme + host) from a URL.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth\#get-cache-key)  `get_cache_key`

Copy

Ask AI

```
get_cache_key(self) -> str

```

Generate a safe filesystem key from the server’s base URL.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth\#clear)  `clear`

Copy

Ask AI

```
clear(self) -> None

```

Clear all cached data for this server.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth\#clear-all)  `clear_all`

Copy

Ask AI

```
clear_all(cls, cache_dir: Path | None = None) -> None

```

Clear all cached data for all servers.

[bearer](https://gofastmcp.com/python-sdk/fastmcp-client-auth-bearer) [client](https://gofastmcp.com/python-sdk/fastmcp-client-client)

On this page

- [fastmcp.client.auth.oauth](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth#fastmcp-client-auth-oauth)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth#functions)
- [default\_cache\_dir](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth#default-cache-dir)
- [OAuth](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth#oauth)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth#classes)
- [ServerOAuthMetadata](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth#serveroauthmetadata)
- [OAuthClientProvider](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth#oauthclientprovider)
- [FileTokenStorage](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth#filetokenstorage)
- [get\_base\_url](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth#get-base-url)
- [get\_cache\_key](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth#get-cache-key)
- [clear](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth#clear)
- [clear\_all](https://gofastmcp.com/python-sdk/fastmcp-client-auth-oauth#clear-all)

Assistant

Responses are generated using AI and may contain mistakes.