# types - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-utilities-types
**Generated:** 2025-06-27

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.utilities

types

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-types\#fastmcp-utilities-types)  `fastmcp.utilities.types`

Common types used across FastMCP.

## [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-types\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-types\#get-cached-typeadapter)  `get_cached_typeadapter`

Copy

Ask AI

```
get_cached_typeadapter(cls: T) -> TypeAdapter[T]

```

TypeAdapters are heavy objects, and in an application context we’d typically
create them once in a global scope and reuse them as often as possible.
However, this isn’t feasible for user-generated functions. Instead, we use a
cache to minimize the cost of creating them as much as possible.

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-types\#issubclass-safe)  `issubclass_safe`

Copy

Ask AI

```
issubclass_safe(cls: type, base: type) -> bool

```

Check if cls is a subclass of base, even if cls is a type variable.

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-types\#is-class-member-of-type)  `is_class_member_of_type`

Copy

Ask AI

```
is_class_member_of_type(cls: type, base: type) -> bool

```

Check if cls is a member of base, even if cls is a type variable.

Base can be a type, a UnionType, or an Annotated type. Generic types are not
considered members (e.g. T is not a member of list\[T\]).

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-types\#find-kwarg-by-type)  `find_kwarg_by_type`

Copy

Ask AI

```
find_kwarg_by_type(fn: Callable, kwarg_type: type) -> str | None

```

Find the name of the kwarg that is of type kwarg\_type.

Includes union types that contain the kwarg\_type, as well as Annotated types.

## [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-types\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-types\#fastmcpbasemodel)  `FastMCPBaseModel`

Base model for FastMCP models.

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-types\#image)  `Image`

Helper class for returning images from tools.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-types\#to-image-content)  `to_image_content`

Copy

Ask AI

```
to_image_content(self, mime_type: str | None = None, annotations: Annotations | None = None) -> ImageContent

```

Convert to MCP ImageContent.

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-types\#audio)  `Audio`

Helper class for returning audio from tools.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-types\#to-audio-content)  `to_audio_content`

Copy

Ask AI

```
to_audio_content(self, mime_type: str | None = None, annotations: Annotations | None = None) -> AudioContent

```

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-types\#file)  `File`

Helper class for returning audio from tools.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-types\#to-resource-content)  `to_resource_content`

Copy

Ask AI

```
to_resource_content(self, mime_type: str | None = None, annotations: Annotations | None = None) -> EmbeddedResource

```

[tests](https://gofastmcp.com/python-sdk/fastmcp-utilities-tests)

On this page

- [fastmcp.utilities.types](https://gofastmcp.com/python-sdk/fastmcp-utilities-types#fastmcp-utilities-types)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-utilities-types#functions)
- [get\_cached\_typeadapter](https://gofastmcp.com/python-sdk/fastmcp-utilities-types#get-cached-typeadapter)
- [issubclass\_safe](https://gofastmcp.com/python-sdk/fastmcp-utilities-types#issubclass-safe)
- [is\_class\_member\_of\_type](https://gofastmcp.com/python-sdk/fastmcp-utilities-types#is-class-member-of-type)
- [find\_kwarg\_by\_type](https://gofastmcp.com/python-sdk/fastmcp-utilities-types#find-kwarg-by-type)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-utilities-types#classes)
- [FastMCPBaseModel](https://gofastmcp.com/python-sdk/fastmcp-utilities-types#fastmcpbasemodel)
- [Image](https://gofastmcp.com/python-sdk/fastmcp-utilities-types#image)
- [to\_image\_content](https://gofastmcp.com/python-sdk/fastmcp-utilities-types#to-image-content)
- [Audio](https://gofastmcp.com/python-sdk/fastmcp-utilities-types#audio)
- [to\_audio\_content](https://gofastmcp.com/python-sdk/fastmcp-utilities-types#to-audio-content)
- [File](https://gofastmcp.com/python-sdk/fastmcp-utilities-types#file)
- [to\_resource\_content](https://gofastmcp.com/python-sdk/fastmcp-utilities-types#to-resource-content)

Assistant

Responses are generated using AI and may contain mistakes.