# resource_manager - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager
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

resource\_manager

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager\#fastmcp-resources-resource-manager)  `fastmcp.resources.resource_manager`

Resource manager functionality.

## [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager\#resourcemanager)  `ResourceManager`

Manages FastMCP resources.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager\#mount)  `mount`

Copy

Ask AI

```
mount(self, server: MountedServer) -> None

```

Adds a mounted server as a source for resources and templates.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager\#add-resource-or-template-from-fn)  `add_resource_or_template_from_fn`

Copy

Ask AI

```
add_resource_or_template_from_fn(self, fn: Callable[..., Any], uri: str, name: str | None = None, description: str | None = None, mime_type: str | None = None, tags: set[str] | None = None) -> Resource | ResourceTemplate

```

Add a resource or template to the manager from a function.

**Args:**

- `fn`: The function to register as a resource or template
- `uri`: The URI for the resource or template
- `name`: Optional name for the resource or template
- `description`: Optional description of the resource or template
- `mime_type`: Optional MIME type for the resource or template
- `tags`: Optional set of tags for categorizing the resource or template

**Returns:**

- The added resource or template. If a resource or template with the same URI already exists,
- returns the existing resource or template.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager\#add-resource-from-fn)  `add_resource_from_fn`

Copy

Ask AI

```
add_resource_from_fn(self, fn: Callable[..., Any], uri: str, name: str | None = None, description: str | None = None, mime_type: str | None = None, tags: set[str] | None = None) -> Resource

```

Add a resource to the manager from a function.

**Args:**

- `fn`: The function to register as a resource
- `uri`: The URI for the resource
- `name`: Optional name for the resource
- `description`: Optional description of the resource
- `mime_type`: Optional MIME type for the resource
- `tags`: Optional set of tags for categorizing the resource

**Returns:**

- The added resource. If a resource with the same URI already exists,
- returns the existing resource.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager\#add-resource)  `add_resource`

Copy

Ask AI

```
add_resource(self, resource: Resource) -> Resource

```

Add a resource to the manager.

**Args:**

- `resource`: A Resource instance to add. The resource’s .key attribute
will be used as the storage key. To overwrite it, call
Resource.with\_key() before calling this method.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager\#add-template-from-fn)  `add_template_from_fn`

Copy

Ask AI

```
add_template_from_fn(self, fn: Callable[..., Any], uri_template: str, name: str | None = None, description: str | None = None, mime_type: str | None = None, tags: set[str] | None = None) -> ResourceTemplate

```

Create a template from a function.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager\#add-template)  `add_template`

Copy

Ask AI

```
add_template(self, template: ResourceTemplate) -> ResourceTemplate

```

Add a template to the manager.

**Args:**

- `template`: A ResourceTemplate instance to add. The template’s .key attribute
will be used as the storage key. To overwrite it, call
ResourceTemplate.with\_key() before calling this method.

**Returns:**

- The added template. If a template with the same URI already exists,
- returns the existing template.

[resource](https://gofastmcp.com/python-sdk/fastmcp-resources-resource) [template](https://gofastmcp.com/python-sdk/fastmcp-resources-template)

On this page

- [fastmcp.resources.resource\_manager](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager#fastmcp-resources-resource-manager)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager#classes)
- [ResourceManager](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager#resourcemanager)
- [mount](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager#mount)
- [add\_resource\_or\_template\_from\_fn](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager#add-resource-or-template-from-fn)
- [add\_resource\_from\_fn](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager#add-resource-from-fn)
- [add\_resource](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager#add-resource)
- [add\_template\_from\_fn](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager#add-template-from-fn)
- [add\_template](https://gofastmcp.com/python-sdk/fastmcp-resources-resource_manager#add-template)

Assistant

Responses are generated using AI and may contain mistakes.