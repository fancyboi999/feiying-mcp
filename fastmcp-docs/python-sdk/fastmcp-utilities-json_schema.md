# json_schema - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-utilities-json_schema
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

json\_schema

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-json_schema\#fastmcp-utilities-json-schema)  `fastmcp.utilities.json_schema`

## [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-json_schema\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-utilities-json_schema\#compress-schema)  `compress_schema`

Copy

Ask AI

```
compress_schema(schema: dict, prune_params: list[str] | None = None, prune_defs: bool = True, prune_additional_properties: bool = True, prune_titles: bool = False) -> dict

```

Remove the given parameters from the schema.

**Args:**

- `schema`: The schema to compress
- `prune_params`: List of parameter names to remove from properties
- `prune_defs`: Whether to remove unused definitions
- `prune_additional_properties`: Whether to remove additionalProperties: false
- `prune_titles`: Whether to remove title fields from the schema

[inspect](https://gofastmcp.com/python-sdk/fastmcp-utilities-inspect) [logging](https://gofastmcp.com/python-sdk/fastmcp-utilities-logging)

On this page

- [fastmcp.utilities.json\_schema](https://gofastmcp.com/python-sdk/fastmcp-utilities-json_schema#fastmcp-utilities-json-schema)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-utilities-json_schema#functions)
- [compress\_schema](https://gofastmcp.com/python-sdk/fastmcp-utilities-json_schema#compress-schema)

Assistant

Responses are generated using AI and may contain mistakes.