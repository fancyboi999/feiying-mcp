# Contrib Modules - FastMCP

**Source URL:** https://gofastmcp.com/integrations/contrib
**Generated:** 2025-06-30

**Description:** Community-contributed modules extending FastMCP

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Integrations

Contrib Modules

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

`New in version: 2.2.1`

FastMCP includes a `contrib` package that holds community-contributed modules. These modules extend FastMCP’s functionality but aren’t officially maintained by the core team.

Contrib modules provide additional features, integrations, or patterns that complement the core FastMCP library. They offer a way for the community to share useful extensions while keeping the core library focused and maintainable.

The available modules can be viewed in the [contrib directory](https://github.com/jlowin/fastmcp/tree/main/src/fastmcp/contrib).

## [​](https://gofastmcp.com/integrations/contrib\#usage)  Usage

To use a contrib module, import it from the `fastmcp.contrib` package:

Copy

Ask AI

```
from fastmcp.contrib import my_module

```

## [​](https://gofastmcp.com/integrations/contrib\#important-considerations)  Important Considerations

- **Stability**: Modules in `contrib` may have different testing requirements or stability guarantees compared to the core library.
- **Compatibility**: Changes to core FastMCP might break modules in `contrib` without explicit warnings in the main changelog.
- **Dependencies**: Contrib modules may have additional dependencies not required by the core library. These dependencies are typically documented in the module’s README or separate requirements files.

## [​](https://gofastmcp.com/integrations/contrib\#contributing)  Contributing

We welcome contributions to the `contrib` package! If you have a module that extends FastMCP in a useful way, consider contributing it:

1. Create a new directory in `src/fastmcp/contrib/` for your module
2. Add proper tests for your module in `tests/contrib/`
3. Include comprehensive documentation in a README.md file, including usage and examples, as well as any additional dependencies or installation instructions
4. Submit a pull request

The ideal contrib module:

- Solves a specific use case or integration need
- Follows FastMCP coding standards
- Includes thorough documentation and examples
- Has comprehensive tests
- Specifies any additional dependencies

[Eunomia Authorization](https://gofastmcp.com/integrations/eunomia-authorization) [Tool Transformation](https://gofastmcp.com/patterns/tool-transformation)

On this page

- [Usage](https://gofastmcp.com/integrations/contrib#usage)
- [Important Considerations](https://gofastmcp.com/integrations/contrib#important-considerations)
- [Contributing](https://gofastmcp.com/integrations/contrib#contributing)

Assistant

Responses are generated using AI and may contain mistakes.