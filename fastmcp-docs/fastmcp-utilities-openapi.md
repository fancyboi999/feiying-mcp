# openapi - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi
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

openapi

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi\#fastmcp-utilities-openapi)  `fastmcp.utilities.openapi`

## [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi\#parse-openapi-to-http-routes)  `parse_openapi_to_http_routes`

Copy

Ask AI

```
parse_openapi_to_http_routes(openapi_dict: dict[str, Any]) -> list[HTTPRoute]

```

Parses an OpenAPI schema dictionary into a list of HTTPRoute objects
using the openapi-pydantic library.

Supports both OpenAPI 3.0.x and 3.1.x versions.

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi\#clean-schema-for-display)  `clean_schema_for_display`

Copy

Ask AI

```
clean_schema_for_display(schema: JsonSchema | None) -> JsonSchema | None

```

Clean up a schema dictionary for display by removing internal/complex fields.

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi\#generate-example-from-schema)  `generate_example_from_schema`

Copy

Ask AI

```
generate_example_from_schema(schema: JsonSchema | None) -> Any

```

Generate a simple example value from a JSON schema dictionary.
Very basic implementation focusing on types.

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi\#format-json-for-description)  `format_json_for_description`

Copy

Ask AI

```
format_json_for_description(data: Any, indent: int = 2) -> str

```

Formats Python data as a JSON string block for markdown.

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi\#format-description-with-responses)  `format_description_with_responses`

Copy

Ask AI

```
format_description_with_responses(base_description: str, responses: dict[str, Any], parameters: list[ParameterInfo] | None = None, request_body: RequestBodyInfo | None = None) -> str

```

Formats the base description string with response, parameter, and request body information.

**Args:**

- `base_description`: The initial description to be formatted.
- `responses`: A dictionary of response information, keyed by status code.
- `parameters`: A list of parameter information,
including path and query parameters. Each parameter includes details such as name,
location, whether it is required, and a description.
- `request_body`: Information about the request body,
including its description, whether it is required, and its content schema.

**Returns:**

- The formatted description string with additional details about responses, parameters,
- and the request body.

## [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi\#parameterinfo)  `ParameterInfo`

Represents a single parameter for an HTTP operation in our IR.

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi\#requestbodyinfo)  `RequestBodyInfo`

Represents the request body for an HTTP operation in our IR.

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi\#responseinfo)  `ResponseInfo`

Represents response information in our IR.

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi\#httproute)  `HTTPRoute`

Intermediate Representation for a single OpenAPI operation.

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi\#openapiparser)  `OpenAPIParser`

Unified parser for OpenAPI schemas with generic type parameters to handle both 3.0 and 3.1.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi\#parse)  `parse`

Copy

Ask AI

```
parse(self) -> list[HTTPRoute]

```

Parse the OpenAPI schema into HTTP routes.

[mcp\_config](https://gofastmcp.com/python-sdk/fastmcp-utilities-mcp_config) [tests](https://gofastmcp.com/python-sdk/fastmcp-utilities-tests)

On this page

- [fastmcp.utilities.openapi](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi#fastmcp-utilities-openapi)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi#functions)
- [parse\_openapi\_to\_http\_routes](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi#parse-openapi-to-http-routes)
- [clean\_schema\_for\_display](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi#clean-schema-for-display)
- [generate\_example\_from\_schema](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi#generate-example-from-schema)
- [format\_json\_for\_description](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi#format-json-for-description)
- [format\_description\_with\_responses](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi#format-description-with-responses)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi#classes)
- [ParameterInfo](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi#parameterinfo)
- [RequestBodyInfo](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi#requestbodyinfo)
- [ResponseInfo](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi#responseinfo)
- [HTTPRoute](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi#httproute)
- [OpenAPIParser](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi#openapiparser)
- [parse](https://gofastmcp.com/python-sdk/fastmcp-utilities-openapi#parse)

Assistant

Responses are generated using AI and may contain mistakes.