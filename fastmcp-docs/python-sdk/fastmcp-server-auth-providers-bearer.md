# bearer - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer
**Generated:** 2025-06-30

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

providers

bearer

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer\#fastmcp-server-auth-providers-bearer)  `fastmcp.server.auth.providers.bearer`

## [​](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer\#jwkdata)  `JWKData`

JSON Web Key data structure.

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer\#jwksdata)  `JWKSData`

JSON Web Key Set data structure.

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer\#rsakeypair)  `RSAKeyPair`

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer\#generate)  `generate`

Copy

Ask AI

```
generate(cls) -> 'RSAKeyPair'

```

Generate an RSA key pair for testing.

**Returns:**

- (private\_key\_pem, public\_key\_pem)

#### [​](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer\#create-token)  `create_token`

Copy

Ask AI

```
create_token(self, subject: str = 'fastmcp-user', issuer: str = 'https://fastmcp.example.com', audience: str | list[str] | None = None, scopes: list[str] | None = None, expires_in_seconds: int = 3600, additional_claims: dict[str, Any] | None = None, kid: str | None = None) -> str

```

Generate a test JWT token for testing purposes.

**Args:**

- `private_key_pem`: RSA private key in PEM format
- `subject`: Subject claim (usually user ID)
- `issuer`: Issuer claim
- `audience`: Audience claim - can be a string or list of strings (optional)
- `scopes`: List of scopes to include
- `expires_in_seconds`: Token expiration time in seconds
- `additional_claims`: Any additional claims to include
- `kid`: Key ID for JWKS lookup (optional)

**Returns:**

- Signed JWT token string

### [​](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer\#bearerauthprovider)  `BearerAuthProvider`

Simple JWT Bearer Token validator for hosted MCP servers.
Uses RS256 asymmetric encryption. Supports either static public key
or JWKS URI for key rotation.

Note that this provider DOES NOT permit client registration or revocation, or any OAuth flows.
It is intended to be used with a control plane that manages clients and tokens.

[\_\_init\_\_](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-__init__) [bearer\_env](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer_env)

On this page

- [fastmcp.server.auth.providers.bearer](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer#fastmcp-server-auth-providers-bearer)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer#classes)
- [JWKData](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer#jwkdata)
- [JWKSData](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer#jwksdata)
- [RSAKeyPair](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer#rsakeypair)
- [generate](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer#generate)
- [create\_token](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer#create-token)
- [BearerAuthProvider](https://gofastmcp.com/python-sdk/fastmcp-server-auth-providers-bearer#bearerauthprovider)

Assistant

Responses are generated using AI and may contain mistakes.