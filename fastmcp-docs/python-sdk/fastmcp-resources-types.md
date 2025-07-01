# types - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-resources-types
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

types

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-resources-types\#fastmcp-resources-types)  `fastmcp.resources.types`

Concrete resource implementations.

## [​](https://gofastmcp.com/python-sdk/fastmcp-resources-types\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-types\#textresource)  `TextResource`

A resource that reads from a string.

### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-types\#binaryresource)  `BinaryResource`

A resource that reads from bytes.

### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-types\#fileresource)  `FileResource`

A resource that reads from a file.

Set is\_binary=True to read file as binary data instead of text.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-types\#validate-absolute-path)  `validate_absolute_path`

Copy

Ask AI

```
validate_absolute_path(cls, path: Path) -> Path

```

Ensure path is absolute.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-types\#set-binary-from-mime-type)  `set_binary_from_mime_type`

Copy

Ask AI

```
set_binary_from_mime_type(cls, is_binary: bool, info: ValidationInfo) -> bool

```

Set is\_binary based on mime\_type if not explicitly set.

### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-types\#httpresource)  `HttpResource`

A resource that reads from an HTTP endpoint.

### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-types\#directoryresource)  `DirectoryResource`

A resource that lists files in a directory.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-types\#validate-absolute-path-2)  `validate_absolute_path`

Copy

Ask AI

```
validate_absolute_path(cls, path: Path) -> Path

```

Ensure path is absolute.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-types\#list-files)  `list_files`

Copy

Ask AI

```
list_files(self) -> list[Path]

```

List files in the directory.

[template](https://gofastmcp.com/python-sdk/fastmcp-resources-template) [\_\_init\_\_](https://gofastmcp.com/python-sdk/fastmcp-server-__init__)

On this page

- [fastmcp.resources.types](https://gofastmcp.com/python-sdk/fastmcp-resources-types#fastmcp-resources-types)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-resources-types#classes)
- [TextResource](https://gofastmcp.com/python-sdk/fastmcp-resources-types#textresource)
- [BinaryResource](https://gofastmcp.com/python-sdk/fastmcp-resources-types#binaryresource)
- [FileResource](https://gofastmcp.com/python-sdk/fastmcp-resources-types#fileresource)
- [validate\_absolute\_path](https://gofastmcp.com/python-sdk/fastmcp-resources-types#validate-absolute-path)
- [set\_binary\_from\_mime\_type](https://gofastmcp.com/python-sdk/fastmcp-resources-types#set-binary-from-mime-type)
- [HttpResource](https://gofastmcp.com/python-sdk/fastmcp-resources-types#httpresource)
- [DirectoryResource](https://gofastmcp.com/python-sdk/fastmcp-resources-types#directoryresource)
- [validate\_absolute\_path](https://gofastmcp.com/python-sdk/fastmcp-resources-types#validate-absolute-path-2)
- [list\_files](https://gofastmcp.com/python-sdk/fastmcp-resources-types#list-files)

Assistant

Responses are generated using AI and may contain mistakes.