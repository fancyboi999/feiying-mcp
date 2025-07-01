# resource - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-resources-resource
**Generated:** 2025-06-30

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.resources

resource

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource\#fastmcp-resources-resource)  `fastmcp.resources.resource`

Base classes and interfaces for FastMCP resources.

## [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource\#resource)  `Resource`

Base class for all resources.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource\#from-function)  `from_function`

Copy

Ask AI

```
from_function(fn: Callable[[], Any], uri: str | AnyUrl, name: str | None = None, description: str | None = None, mime_type: str | None = None, tags: set[str] | None = None, enabled: bool | None = None) -> FunctionResource

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource\#set-default-mime-type)  `set_default_mime_type`

Copy

Ask AI

```
set_default_mime_type(cls, mime_type: str | None) -> str

```

Set default MIME type if not provided.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource\#set-default-name)  `set_default_name`

Copy

Ask AI

```
set_default_name(self) -> Self

```

Set default name from URI if not provided.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource\#to-mcp-resource)  `to_mcp_resource`

Copy

Ask AI

```
to_mcp_resource(self, **overrides: Any) -> MCPResource

```

Convert the resource to an MCPResource.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource\#key)  `key`

Copy

Ask AI

```
key(self) -> str

```

The key of the component. This is used for internal bookkeeping
and may reflect e.g. prefixes or other identifiers. You should not depend on
keys having a certain value, as the same tool loaded from different
hierarchies of servers may have different keys.

### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource\#functionresource)  `FunctionResource`

A resource that defers data loading by wrapping a function.

The function is only called when the resource is read, allowing for lazy loading
of potentially expensive data. This is particularly useful when listing resources,
as the function won’t be called until the resource is actually accessed.

The function can return:

- str for text content (default)
- bytes for binary content
- other types will be converted to JSON

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource\#from-function-2)  `from_function`

Copy

Ask AI

```
from_function(cls, fn: Callable[[], Any], uri: str | AnyUrl, name: str | None = None, description: str | None = None, mime_type: str | None = None, tags: set[str] | None = None, enabled: bool | None = None) -> FunctionResource

```

Create a FunctionResource from a function.

[\_\_init\_\_](https://gofastmcp.com/python-sdk/fastmcp-resources-__init__) [resource\_manager](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager)

On this page

- [fastmcp.resources.resource](https://gofastmcp.com/python-sdk/fastmcp-resources-resource#fastmcp-resources-resource)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-resources-resource#classes)
- [Resource](https://gofastmcp.com/python-sdk/fastmcp-resources-resource#resource)
- [from\_function](https://gofastmcp.com/python-sdk/fastmcp-resources-resource#from-function)
- [set\_default\_mime\_type](https://gofastmcp.com/python-sdk/fastmcp-resources-resource#set-default-mime-type)
- [set\_default\_name](https://gofastmcp.com/python-sdk/fastmcp-resources-resource#set-default-name)
- [to\_mcp\_resource](https://gofastmcp.com/python-sdk/fastmcp-resources-resource#to-mcp-resource)
- [key](https://gofastmcp.com/python-sdk/fastmcp-resources-resource#key)
- [FunctionResource](https://gofastmcp.com/python-sdk/fastmcp-resources-resource#functionresource)
- [from\_function](https://gofastmcp.com/python-sdk/fastmcp-resources-resource#from-function-2)

Assistant

Responses are generated using AI and may contain mistakes.