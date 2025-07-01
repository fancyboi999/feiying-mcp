# Bearer Token Authentication - FastMCP

**Source URL:** https://gofastmcp.com/servers/auth/bearer
**Generated:** 2025-06-30

**Description:** Secure your FastMCP server's HTTP endpoints by validating JWT Bearer tokens.

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

Authentication and authorization are only relevant for HTTP-based transports.

The [MCP specification](https://modelcontextprotocol.io/specification/2025-03-26/basic/authorization) requires servers to implement full OAuth 2.1 authorization flows with dynamic client registration, server metadata discovery, and complete token endpoints. FastMCP’s Bearer Token authentication provides a simpler, more practical alternative by directly validating pre-issued JWT tokens—ideal for service-to-service communication and programmatic environments where full OAuth flows may be impractical, and in accordance with how the MCP ecosystem is pragmatically evolving. However, please note that since it doesn’t implement the full OAuth 2.1 flow, this implementation does not strictly comply with the MCP specification.

Bearer Token authentication is a common way to secure HTTP-based APIs. In this model, the client sends a token (usually a JSON Web Token or JWT) in the `Authorization` header with the “Bearer” scheme. The server then validates this token to grant or deny access.

FastMCP supports Bearer Token authentication for its HTTP-based transports ( `http` and `sse`), allowing you to protect your server from unauthorized access.

## [​](https://gofastmcp.com/servers/auth/bearer\#authentication-strategy)  Authentication Strategy

FastMCP uses **asymmetric encryption** for token validation, which provides a clean security separation between token issuers and FastMCP servers. This approach means:

- **No shared secrets**: Your FastMCP server never needs access to private keys or client secrets
- **Public key verification**: The server only needs a public key (or JWKS endpoint) to verify token signatures
- **Secure token issuance**: Tokens are signed by an external service using a private key that never leaves the issuer
- **Scalable architecture**: Multiple FastMCP servers can validate tokens without coordinating secrets

This design allows you to integrate FastMCP servers into existing authentication infrastructures without compromising security boundaries.

## [​](https://gofastmcp.com/servers/auth/bearer\#configuration)  Configuration

To enable Bearer Token validation on your FastMCP server, use the `BearerAuthProvider` class. This provider validates incoming JWTs by verifying signatures, checking expiration, and optionally validating claims.

The `BearerAuthProvider` validates tokens; it does **not** issue them (or implement any part of an OAuth flow). You’ll need to generate tokens separately, either using FastMCP utilities or an external Identity Provider (IdP) or OAuth 2.1 Authorization Server.

### [​](https://gofastmcp.com/servers/auth/bearer\#basic-setup)  Basic Setup

To configure bearer token authentication, instantiate a `BearerAuthProvider` instance and pass it to the `auth` parameter of the `FastMCP` instance.

The `BearerAuthProvider` requires either a static public key or a JWKS URI (but not both!) in order to verify the token’s signature. All other parameters are optional — if they are provided, they will be used as additional validation criteria.

Copy

Ask AI

```
from fastmcp import FastMCP
from fastmcp.server.auth import BearerAuthProvider

auth = BearerAuthProvider(
    jwks_uri="https://my-identity-provider.com/.well-known/jwks.json",
    issuer="https://my-identity-provider.com/",
    audience="my-mcp-server"
)

mcp = FastMCP(name="My MCP Server", auth=auth)

```

### [​](https://gofastmcp.com/servers/auth/bearer\#configuration-parameters)  Configuration Parameters

## BearerAuthProvider Configuration

[​](https://gofastmcp.com/servers/auth/bearer#param-public-key)

public\_key

str

RSA public key in PEM format for static key validation. Required if `jwks_uri` is not provided

[​](https://gofastmcp.com/servers/auth/bearer#param-jwks-uri)

jwks\_uri

str

URL for JSON Web Key Set endpoint. Required if `public_key` is not provided

[​](https://gofastmcp.com/servers/auth/bearer#param-issuer)

issuer

str \| None

Expected JWT `iss` claim value

[​](https://gofastmcp.com/servers/auth/bearer#param-audience)

audience

str \| None

Expected JWT `aud` claim value

[​](https://gofastmcp.com/servers/auth/bearer#param-required-scopes)

required\_scopes

list\[str\] \| None

Global scopes required for all requests

#### [​](https://gofastmcp.com/servers/auth/bearer\#public-key)  Public Key

If you have a public key in PEM format, you can provide it to the `BearerAuthProvider` as a string.

Copy

Ask AI

```
from fastmcp.server.auth import BearerAuthProvider
import inspect

public_key_pem = inspect.cleandoc(
    """
    -----BEGIN PUBLIC KEY-----
    MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAy...
    -----END PUBLIC KEY-----
    """
)

auth = BearerAuthProvider(public_key=public_key_pem)

```

#### [​](https://gofastmcp.com/servers/auth/bearer\#jwks-uri)  JWKS URI

Copy

Ask AI

```
provider = BearerAuthProvider(
    jwks_uri="https://idp.example.com/.well-known/jwks.json"
)

```

JWKS is recommended for production as it supports automatic key rotation and multiple signing keys.

## [​](https://gofastmcp.com/servers/auth/bearer\#generating-tokens)  Generating Tokens

For development and testing, FastMCP provides the `RSAKeyPair` utility class to generate tokens without needing an external OAuth provider.

The `RSAKeyPair` utility is intended for development and testing only. For production, use a proper OAuth 2.1 Authorization Server or Identity Provider.

### [​](https://gofastmcp.com/servers/auth/bearer\#basic-token-generation)  Basic Token Generation

Copy

Ask AI

```
from fastmcp import FastMCP
from fastmcp.server.auth import BearerAuthProvider
from fastmcp.server.auth.providers.bearer import RSAKeyPair

# Generate a new key pair
key_pair = RSAKeyPair.generate()

# Configure the auth provider with the public key
auth = BearerAuthProvider(
    public_key=key_pair.public_key,
    issuer="https://dev.example.com",
    audience="my-dev-server"
)

mcp = FastMCP(name="Development Server", auth=auth)

# Generate a token for testing
token = key_pair.create_token(
    subject="dev-user",
    issuer="https://dev.example.com",
    audience="my-dev-server",
    scopes=["read", "write"]
)

print(f"Test token: {token}")

```

### [​](https://gofastmcp.com/servers/auth/bearer\#token-creation-parameters)  Token Creation Parameters

The `create_token()` method accepts these parameters:

## create\_token() Parameters

[​](https://gofastmcp.com/servers/auth/bearer#param-subject)

subject

str

default:"fastmcp-user"

JWT subject claim (usually user ID)

[​](https://gofastmcp.com/servers/auth/bearer#param-issuer-1)

issuer

str

default:"https://fastmcp.example.com"

JWT issuer claim

[​](https://gofastmcp.com/servers/auth/bearer#param-audience-1)

audience

str \| None

JWT audience claim

[​](https://gofastmcp.com/servers/auth/bearer#param-scopes)

scopes

list\[str\] \| None

OAuth scopes to include

[​](https://gofastmcp.com/servers/auth/bearer#param-expires-in-seconds)

expires\_in\_seconds

int

default:"3600"

Token expiration time in seconds

[​](https://gofastmcp.com/servers/auth/bearer#param-additional-claims)

additional\_claims

dict \| None

Extra claims to include in the token

[​](https://gofastmcp.com/servers/auth/bearer#param-kid)

kid

str \| None

Key ID for JWKS lookup

## [​](https://gofastmcp.com/servers/auth/bearer\#accessing-token-claims)  Accessing Token Claims

Once authenticated, your tools, resources, or prompts can access token information using the `get_access_token()` dependency function:

Copy

Ask AI

```
from fastmcp import FastMCP, Context, ToolError
from fastmcp.server.dependencies import get_access_token, AccessToken

@mcp.tool
async def get_my_data(ctx: Context) -> dict:
    access_token: AccessToken = get_access_token()

    user_id = access_token.client_id  # From JWT 'sub' or 'client_id' claim
    user_scopes = access_token.scopes

    if "data:read_sensitive" not in user_scopes:
        raise ToolError("Insufficient permissions: 'data:read_sensitive' scope required.")

    return {
        "user": user_id,
        "sensitive_data": f"Private data for {user_id}",
        "granted_scopes": user_scopes
    }

```

### [​](https://gofastmcp.com/servers/auth/bearer\#accesstoken-properties)  AccessToken Properties

## AccessToken Properties

[​](https://gofastmcp.com/servers/auth/bearer#param-token)

token

str

The raw JWT string

[​](https://gofastmcp.com/servers/auth/bearer#param-client-id)

client\_id

str

Authenticated principal identifier

[​](https://gofastmcp.com/servers/auth/bearer#param-scopes-1)

scopes

list\[str\]

Granted scopes

[​](https://gofastmcp.com/servers/auth/bearer#param-expires-at)

expires\_at

datetime \| None

Token expiration timestamp

[Sampling](https://gofastmcp.com/servers/sampling) [Middleware](https://gofastmcp.com/servers/middleware)

On this page

- [Authentication Strategy](https://gofastmcp.com/servers/auth/bearer#authentication-strategy)
- [Configuration](https://gofastmcp.com/servers/auth/bearer#configuration)
- [Basic Setup](https://gofastmcp.com/servers/auth/bearer#basic-setup)
- [Configuration Parameters](https://gofastmcp.com/servers/auth/bearer#configuration-parameters)
- [Public Key](https://gofastmcp.com/servers/auth/bearer#public-key)
- [JWKS URI](https://gofastmcp.com/servers/auth/bearer#jwks-uri)
- [Generating Tokens](https://gofastmcp.com/servers/auth/bearer#generating-tokens)
- [Basic Token Generation](https://gofastmcp.com/servers/auth/bearer#basic-token-generation)
- [Token Creation Parameters](https://gofastmcp.com/servers/auth/bearer#token-creation-parameters)
- [Accessing Token Claims](https://gofastmcp.com/servers/auth/bearer#accessing-token-claims)
- [AccessToken Properties](https://gofastmcp.com/servers/auth/bearer#accesstoken-properties)

Assistant

Responses are generated using AI and may contain mistakes.