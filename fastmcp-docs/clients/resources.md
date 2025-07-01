# Resource Operations - FastMCP

**Source URL:** https://gofastmcp.com/clients/resources
**Generated:** 2025-06-30

**Description:** Access static and templated resources from MCP servers.

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Core Operations

Resource Operations

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

`New in version: 2.0.0`

Resources are data sources exposed by MCP servers. They can be static files or dynamic templates that generate content based on parameters.

## [​](https://gofastmcp.com/clients/resources\#types-of-resources)  Types of Resources

MCP servers expose two types of resources:

- **Static Resources**: Fixed content accessible via URI (e.g., configuration files, documentation)
- **Resource Templates**: Dynamic resources that accept parameters to generate content (e.g., API endpoints, database queries)

## [​](https://gofastmcp.com/clients/resources\#listing-resources)  Listing Resources

### [​](https://gofastmcp.com/clients/resources\#static-resources)  Static Resources

Use `list_resources()` to retrieve all static resources available on the server:

Copy

Ask AI

```
async with client:
    resources = await client.list_resources()
    # resources -> list[mcp.types.Resource]

    for resource in resources:
        print(f"Resource URI: {resource.uri}")
        print(f"Name: {resource.name}")
        print(f"Description: {resource.description}")
        print(f"MIME Type: {resource.mimeType}")

```

### [​](https://gofastmcp.com/clients/resources\#resource-templates)  Resource Templates

Use `list_resource_templates()` to retrieve available resource templates:

Copy

Ask AI

```
async with client:
    templates = await client.list_resource_templates()
    # templates -> list[mcp.types.ResourceTemplate]

    for template in templates:
        print(f"Template URI: {template.uriTemplate}")
        print(f"Name: {template.name}")
        print(f"Description: {template.description}")

```

## [​](https://gofastmcp.com/clients/resources\#reading-resources)  Reading Resources

### [​](https://gofastmcp.com/clients/resources\#static-resources-2)  Static Resources

Read a static resource using its URI:

Copy

Ask AI

```
async with client:
    # Read a static resource
    content = await client.read_resource("file:///path/to/README.md")
    # content -> list[mcp.types.TextResourceContents | mcp.types.BlobResourceContents]

    # Access text content
    if hasattr(content[0], 'text'):
        print(content[0].text)

    # Access binary content
    if hasattr(content[0], 'blob'):
        print(f"Binary data: {len(content[0].blob)} bytes")

```

### [​](https://gofastmcp.com/clients/resources\#resource-templates-2)  Resource Templates

Read from a resource template by providing the URI with parameters:

Copy

Ask AI

```
async with client:
    # Read a resource generated from a template
    # For example, a template like "weather://{{city}}/current"
    weather_content = await client.read_resource("weather://london/current")

    # Access the generated content
    print(weather_content[0].text)  # Assuming text JSON response

```

## [​](https://gofastmcp.com/clients/resources\#content-types)  Content Types

Resources can return different content types:

### [​](https://gofastmcp.com/clients/resources\#text-resources)  Text Resources

Copy

Ask AI

```
async with client:
    content = await client.read_resource("resource://config/settings.json")

    for item in content:
        if hasattr(item, 'text'):
            print(f"Text content: {item.text}")
            print(f"MIME type: {item.mimeType}")

```

### [​](https://gofastmcp.com/clients/resources\#binary-resources)  Binary Resources

Copy

Ask AI

```
async with client:
    content = await client.read_resource("resource://images/logo.png")

    for item in content:
        if hasattr(item, 'blob'):
            print(f"Binary content: {len(item.blob)} bytes")
            print(f"MIME type: {item.mimeType}")

            # Save to file
            with open("downloaded_logo.png", "wb") as f:
                f.write(item.blob)

```

## [​](https://gofastmcp.com/clients/resources\#working-with-multi-server-clients)  Working with Multi-Server Clients

When using multi-server clients, resource URIs are automatically prefixed with the server name:

Copy

Ask AI

```
async with client:  # Multi-server client
    # Access resources from different servers
    weather_icons = await client.read_resource("weather://weather/icons/sunny")
    templates = await client.read_resource("resource://assistant/templates/list")

    print(f"Weather icon: {weather_icons[0].blob}")
    print(f"Templates: {templates[0].text}")

```

## [​](https://gofastmcp.com/clients/resources\#raw-mcp-protocol-access)  Raw MCP Protocol Access

For access to the complete MCP protocol objects, use the `*_mcp` methods:

Copy

Ask AI

```
async with client:
    # Raw MCP methods return full protocol objects
    resources_result = await client.list_resources_mcp()
    # resources_result -> mcp.types.ListResourcesResult

    templates_result = await client.list_resource_templates_mcp()
    # templates_result -> mcp.types.ListResourceTemplatesResult

    content_result = await client.read_resource_mcp("resource://example")
    # content_result -> mcp.types.ReadResourceResult

```

## [​](https://gofastmcp.com/clients/resources\#common-resource-uri-patterns)  Common Resource URI Patterns

Different MCP servers may use various URI schemes:

Copy

Ask AI

```
# File system resources
"file:///path/to/file.txt"

# Custom protocol resources
"weather://london/current"
"database://users/123"

# Generic resource protocol
"resource://config/settings"
"resource://templates/email"

```

Resource URIs and their formats depend on the specific MCP server implementation. Check the server’s documentation for available resources and their URI patterns.

[Tools](https://gofastmcp.com/clients/tools) [Prompts](https://gofastmcp.com/clients/prompts)

On this page

- [Types of Resources](https://gofastmcp.com/clients/resources#types-of-resources)
- [Listing Resources](https://gofastmcp.com/clients/resources#listing-resources)
- [Static Resources](https://gofastmcp.com/clients/resources#static-resources)
- [Resource Templates](https://gofastmcp.com/clients/resources#resource-templates)
- [Reading Resources](https://gofastmcp.com/clients/resources#reading-resources)
- [Static Resources](https://gofastmcp.com/clients/resources#static-resources-2)
- [Resource Templates](https://gofastmcp.com/clients/resources#resource-templates-2)
- [Content Types](https://gofastmcp.com/clients/resources#content-types)
- [Text Resources](https://gofastmcp.com/clients/resources#text-resources)
- [Binary Resources](https://gofastmcp.com/clients/resources#binary-resources)
- [Working with Multi-Server Clients](https://gofastmcp.com/clients/resources#working-with-multi-server-clients)
- [Raw MCP Protocol Access](https://gofastmcp.com/clients/resources#raw-mcp-protocol-access)
- [Common Resource URI Patterns](https://gofastmcp.com/clients/resources#common-resource-uri-patterns)

Assistant

Responses are generated using AI and may contain mistakes.