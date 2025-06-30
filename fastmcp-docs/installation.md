# Installation - FastMCP

**Source URL:** https://gofastmcp.com/getting-started/installation
**Generated:** 2025-06-27

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Get Started

Installation

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

## [​](https://gofastmcp.com/getting-started/installation\#install-fastmcp)  Install FastMCP

We recommend using [uv](https://docs.astral.sh/uv/getting-started/installation/) to install and manage FastMCP.

If you plan to use FastMCP in your project, you can add it as a dependency with:

Copy

Ask AI

```
uv add fastmcp

```

Alternatively, you can install it directly with `pip` or `uv pip`:

uv

pip

Copy

Ask AI

```
uv pip install fastmcp

```

### [​](https://gofastmcp.com/getting-started/installation\#verify-installation)  Verify Installation

To verify that FastMCP is installed correctly, you can run the following command:

Copy

Ask AI

```
fastmcp version

```

You should see output like the following:

Copy

Ask AI

```
$ fastmcp version

FastMCP version:   0.4.2.dev41+ga077727.d20250410
MCP version:                                1.6.0
Python version:                            3.12.2
Platform:            macOS-15.3.1-arm64-arm-64bit
FastMCP root path:            ~/Developer/fastmcp

```

## [​](https://gofastmcp.com/getting-started/installation\#upgrading-from-the-official-mcp-sdk)  Upgrading from the Official MCP SDK

Upgrading from the official MCP SDK’s FastMCP 1.0 to FastMCP 2.0 is generally straightforward. The core server API is highly compatible, and in many cases, changing your import statement from `from mcp.server.fastmcp import FastMCP` to `from fastmcp import FastMCP` will be sufficient.

Copy

Ask AI

```
# Before
# from mcp.server.fastmcp import FastMCP

# After
from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")

```

Prior to `fastmcp==2.3.0` and `mcp==1.8.0`, the 2.x API always mirrored the official 1.0 API. However, as the projects diverge, this can not be guaranteed. You may see deprecation warnings if you attempt to use 1.0 APIs in FastMCP 2.x. Please refer to this documentation for details on new capabilities.

## [​](https://gofastmcp.com/getting-started/installation\#versioning-and-breaking-changes)  Versioning and Breaking Changes

While we make every effort not to introduce backwards-incompatible changes to our public APIs and behavior, FastMCP exists in a rapidly evolving MCP landscape. We’re committed to bringing the most cutting-edge features to our users, which occasionally necessitates changes to existing functionality.

As a practice, breaking changes will only occur on minor version changes (e.g., 2.3.x to 2.4.0). A minor version change indicates either:

- A significant new feature set that warrants a new minor version
- Introducing breaking changes that may affect behavior on upgrade

For users concerned about stability in production environments, we recommend pinning FastMCP to a specific version in your dependencies.

Whenever possible, FastMCP will issue deprecation warnings when users attempt to use APIs that are either deprecated or destined for future removal. These warnings will be maintained for at least 1 minor version release, and may be maintained longer.

Note that the “public API” includes the public functionality of the `FastMCP` server, core FastMCP components like `Tool`, `Prompt`, `Resource`, and `ResourceTemplate`, and their respective public methods. It does not include private methods, utilities, or objects that are stored as private attributes, as we do not expect users to rely on those implementation details.

## [​](https://gofastmcp.com/getting-started/installation\#installing-for-development)  Installing for Development

If you plan to contribute to FastMCP, you should begin by cloning the repository and using uv to install all dependencies (development dependencies are installed automatically):

Copy

Ask AI

```
git clone https://github.com/jlowin/fastmcp.git
cd fastmcp
uv sync

```

This will install all dependencies, including ones for development, and create a virtual environment, which you can activate and use as normal.

### [​](https://gofastmcp.com/getting-started/installation\#unit-tests)  Unit Tests

FastMCP has a comprehensive unit test suite, and all PR’s must introduce and pass appropriate tests. To run the tests, use pytest:

Copy

Ask AI

```
pytest

```

### [​](https://gofastmcp.com/getting-started/installation\#pre-commit-hooks)  Pre-Commit Hooks

FastMCP uses pre-commit to manage code quality, including formatting, linting, and type-safety. All PRs must pass the pre-commit hooks, which are run as a part of the CI process. To install the pre-commit hooks, run:

Copy

Ask AI

```
uv run pre-commit install

```

Alternatively, to run pre-commit manually at any time, use:

Copy

Ask AI

```
pre-commit run --all-files

```

[Welcome!](https://gofastmcp.com/getting-started/welcome) [Quickstart](https://gofastmcp.com/getting-started/quickstart)

On this page

- [Install FastMCP](https://gofastmcp.com/getting-started/installation#install-fastmcp)
- [Verify Installation](https://gofastmcp.com/getting-started/installation#verify-installation)
- [Upgrading from the Official MCP SDK](https://gofastmcp.com/getting-started/installation#upgrading-from-the-official-mcp-sdk)
- [Versioning and Breaking Changes](https://gofastmcp.com/getting-started/installation#versioning-and-breaking-changes)
- [Installing for Development](https://gofastmcp.com/getting-started/installation#installing-for-development)
- [Unit Tests](https://gofastmcp.com/getting-started/installation#unit-tests)
- [Pre-Commit Hooks](https://gofastmcp.com/getting-started/installation#pre-commit-hooks)

Assistant

Responses are generated using AI and may contain mistakes.