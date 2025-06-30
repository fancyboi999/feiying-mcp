# template - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-resources-template
**Generated:** 2025-06-27

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.resources

template

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-resources-template\#fastmcp-resources-template)  `fastmcp.resources.template`

Resource template functionality.

## [​](https://gofastmcp.com/python-sdk/fastmcp-resources-template\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-template\#build-regex)  `build_regex`

Copy

Ask AI

```
build_regex(template: str) -> re.Pattern

```

### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-template\#match-uri-template)  `match_uri_template`

Copy

Ask AI

```
match_uri_template(uri: str, uri_template: str) -> dict[str, str] | None

```

## [​](https://gofastmcp.com/python-sdk/fastmcp-resources-template\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-template\#resourcetemplate)  `ResourceTemplate`

A template for dynamically creating resources.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-template\#from-function)  `from_function`

Copy

Ask AI

```
from_function(fn: Callable[..., Any], uri_template: str, name: str | None = None, description: str | None = None, mime_type: str | None = None, tags: set[str] | None = None, enabled: bool | None = None) -> FunctionResourceTemplate

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-template\#set-default-mime-type)  `set_default_mime_type`

Copy

Ask AI

```
set_default_mime_type(cls, mime_type: str | None) -> str

```

Set default MIME type if not provided.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-template\#matches)  `matches`

Copy

Ask AI

```
matches(self, uri: str) -> dict[str, Any] | None

```

Check if URI matches template and extract parameters.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-template\#to-mcp-template)  `to_mcp_template`

Copy

Ask AI

```
to_mcp_template(self, **overrides: Any) -> MCPResourceTemplate

```

Convert the resource template to an MCPResourceTemplate.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-template\#from-mcp-template)  `from_mcp_template`

Copy

Ask AI

```
from_mcp_template(cls, mcp_template: MCPResourceTemplate) -> ResourceTemplate

```

Creates a FastMCP ResourceTemplate from a raw MCP ResourceTemplate object.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-template\#key)  `key`

Copy

Ask AI

```
key(self) -> str

```

The key of the component. This is used for internal bookkeeping
and may reflect e.g. prefixes or other identifiers. You should not depend on
keys having a certain value, as the same tool loaded from different
hierarchies of servers may have different keys.

### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-template\#functionresourcetemplate)  `FunctionResourceTemplate`

A template for dynamically creating resources.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-template\#from-function-2)  `from_function`

Copy

Ask AI

```
from_function(cls, fn: Callable[..., Any], uri_template: str, name: str | None = None, description: str | None = None, mime_type: str | None = None, tags: set[str] | None = None, enabled: bool | None = None) -> FunctionResourceTemplate

```

Create a template from a function.

[resource\_manager](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager) [types](https://gofastmcp.com/python-sdk/fastmcp-resources-types)

On this page

- [fastmcp.resources.template](https://gofastmcp.com/python-sdk/fastmcp-resources-template#fastmcp-resources-template)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-resources-template#functions)
- [build\_regex](https://gofastmcp.com/python-sdk/fastmcp-resources-template#build-regex)
- [match\_uri\_template](https://gofastmcp.com/python-sdk/fastmcp-resources-template#match-uri-template)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-resources-template#classes)
- [ResourceTemplate](https://gofastmcp.com/python-sdk/fastmcp-resources-template#resourcetemplate)
- [from\_function](https://gofastmcp.com/python-sdk/fastmcp-resources-template#from-function)
- [set\_default\_mime\_type](https://gofastmcp.com/python-sdk/fastmcp-resources-template#set-default-mime-type)
- [matches](https://gofastmcp.com/python-sdk/fastmcp-resources-template#matches)
- [to\_mcp\_template](https://gofastmcp.com/python-sdk/fastmcp-resources-template#to-mcp-template)
- [from\_mcp\_template](https://gofastmcp.com/python-sdk/fastmcp-resources-template#from-mcp-template)
- [key](https://gofastmcp.com/python-sdk/fastmcp-resources-template#key)
- [FunctionResourceTemplate](https://gofastmcp.com/python-sdk/fastmcp-resources-template#functionresourcetemplate)
- [from\_function](https://gofastmcp.com/python-sdk/fastmcp-resources-template#from-function-2)

Assistant

Responses are generated using AI and may contain mistakes.