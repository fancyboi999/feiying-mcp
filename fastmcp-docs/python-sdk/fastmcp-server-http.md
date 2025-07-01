# http - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-server-http
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

http

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-server-http\#fastmcp-server-http)  `fastmcp.server.http`

## [​](https://gofastmcp.com/python-sdk/fastmcp-server-http\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-http\#set-http-request)  `set_http_request`

Copy

Ask AI

```
set_http_request(request: Request) -> Generator[Request, None, None]

```

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-http\#setup-auth-middleware-and-routes)  `setup_auth_middleware_and_routes`

Copy

Ask AI

```
setup_auth_middleware_and_routes(auth: OAuthProvider) -> tuple[list[Middleware], list[BaseRoute], list[str]]

```

Set up authentication middleware and routes if auth is enabled.

**Args:**

- `auth`: The OAuthProvider authorization server provider

**Returns:**

- Tuple of (middleware, auth\_routes, required\_scopes)

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-http\#create-base-app)  `create_base_app`

Copy

Ask AI

```
create_base_app(routes: list[BaseRoute], middleware: list[Middleware], debug: bool = False, lifespan: Callable | None = None) -> StarletteWithLifespan

```

Create a base Starlette app with common middleware and routes.

**Args:**

- `routes`: List of routes to include in the app
- `middleware`: List of middleware to include in the app
- `debug`: Whether to enable debug mode
- `lifespan`: Optional lifespan manager for the app

**Returns:**

- A Starlette application

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-http\#create-sse-app)  `create_sse_app`

Copy

Ask AI

```
create_sse_app(server: FastMCP[LifespanResultT], message_path: str, sse_path: str, auth: OAuthProvider | None = None, debug: bool = False, routes: list[BaseRoute] | None = None, middleware: list[Middleware] | None = None) -> StarletteWithLifespan

```

Return an instance of the SSE server app.

**Args:**

- `server`: The FastMCP server instance
- `message_path`: Path for SSE messages
- `sse_path`: Path for SSE connections
- `auth`: Optional auth provider
- `debug`: Whether to enable debug mode
- `routes`: Optional list of custom routes
- `middleware`: Optional list of middleware

Returns:
A Starlette application with RequestContextMiddleware

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-http\#create-streamable-http-app)  `create_streamable_http_app`

Copy

Ask AI

```
create_streamable_http_app(server: FastMCP[LifespanResultT], streamable_http_path: str, event_store: EventStore | None = None, auth: OAuthProvider | None = None, json_response: bool = False, stateless_http: bool = False, debug: bool = False, routes: list[BaseRoute] | None = None, middleware: list[Middleware] | None = None) -> StarletteWithLifespan

```

Return an instance of the StreamableHTTP server app.

**Args:**

- `server`: The FastMCP server instance
- `streamable_http_path`: Path for StreamableHTTP connections
- `event_store`: Optional event store for session management
- `auth`: Optional auth provider
- `json_response`: Whether to use JSON response format
- `stateless_http`: Whether to use stateless mode (new transport per request)
- `debug`: Whether to enable debug mode
- `routes`: Optional list of custom routes
- `middleware`: Optional list of middleware

**Returns:**

- A Starlette application with StreamableHTTP support

## [​](https://gofastmcp.com/python-sdk/fastmcp-server-http\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-http\#starlettewithlifespan)  `StarletteWithLifespan`

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-http\#lifespan)  `lifespan`

Copy

Ask AI

```
lifespan(self) -> Lifespan

```

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-http\#requestcontextmiddleware)  `RequestContextMiddleware`

Middleware that stores each request in a ContextVar

[dependencies](https://gofastmcp.com/python-sdk/fastmcp-server-dependencies) [\_\_init\_\_](https://gofastmcp.com/python-sdk/fastmcp-server-middleware-__init__)

On this page

- [fastmcp.server.http](https://gofastmcp.com/python-sdk/fastmcp-server-http#fastmcp-server-http)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-server-http#functions)
- [set\_http\_request](https://gofastmcp.com/python-sdk/fastmcp-server-http#set-http-request)
- [setup\_auth\_middleware\_and\_routes](https://gofastmcp.com/python-sdk/fastmcp-server-http#setup-auth-middleware-and-routes)
- [create\_base\_app](https://gofastmcp.com/python-sdk/fastmcp-server-http#create-base-app)
- [create\_sse\_app](https://gofastmcp.com/python-sdk/fastmcp-server-http#create-sse-app)
- [create\_streamable\_http\_app](https://gofastmcp.com/python-sdk/fastmcp-server-http#create-streamable-http-app)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-server-http#classes)
- [StarletteWithLifespan](https://gofastmcp.com/python-sdk/fastmcp-server-http#starlettewithlifespan)
- [lifespan](https://gofastmcp.com/python-sdk/fastmcp-server-http#lifespan)
- [RequestContextMiddleware](https://gofastmcp.com/python-sdk/fastmcp-server-http#requestcontextmiddleware)

Assistant

Responses are generated using AI and may contain mistakes.