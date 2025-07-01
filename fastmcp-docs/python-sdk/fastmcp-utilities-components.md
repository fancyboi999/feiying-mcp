# components - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-utilities-components
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

components

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-components\#fastmcp-utilities-components)  `fastmcp.utilities.components`

## [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-components\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-components\#fastmcpcomponent)  `FastMCPComponent`

Base class for FastMCP tools, prompts, resources, and resource templates.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-components\#key)  `key`

Copy

Ask AI

```
key(self) -> str

```

The key of the component. This is used for internal bookkeeping
and may reflect e.g. prefixes or other identifiers. You should not depend on
keys having a certain value, as the same tool loaded from different
hierarchies of servers may have different keys.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-components\#with-key)  `with_key`

Copy

Ask AI

```
with_key(self, key: str) -> Self

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-components\#enable)  `enable`

Copy

Ask AI

```
enable(self) -> None

```

Enable the component.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-components\#disable)  `disable`

Copy

Ask AI

```
disable(self) -> None

```

Disable the component.

[cache](https://gofastmcp.com/python-sdk/fastmcp-utilities-cache) [exceptions](https://gofastmcp.com/python-sdk/fastmcp-utilities-exceptions)

On this page

- [fastmcp.utilities.components](https://gofastmcp.com/python-sdk/fastmcp-utilities-components#fastmcp-utilities-components)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-utilities-components#classes)
- [FastMCPComponent](https://gofastmcp.com/python-sdk/fastmcp-utilities-components#fastmcpcomponent)
- [key](https://gofastmcp.com/python-sdk/fastmcp-utilities-components#key)
- [with\_key](https://gofastmcp.com/python-sdk/fastmcp-utilities-components#with-key)
- [enable](https://gofastmcp.com/python-sdk/fastmcp-utilities-components#enable)
- [disable](https://gofastmcp.com/python-sdk/fastmcp-utilities-components#disable)

Assistant

Responses are generated using AI and may contain mistakes.