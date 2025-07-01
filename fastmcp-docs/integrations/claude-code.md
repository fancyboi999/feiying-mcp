# Claude Code + FastMCP - FastMCP

**Source URL:** https://gofastmcp.com/integrations/claude-code
**Generated:** 2025-06-30

**Description:** Connect FastMCP servers to Claude Code

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Integrations

Claude Code + FastMCP

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

Claude Code supports MCP servers through multiple transport methods, allowing you to extend Claude’s capabilities with custom tools, resources, and prompts from your FastMCP servers.

Claude Code supports both local and remote MCP servers with flexible configuration options. See the [Claude Code MCP documentation](https://docs.anthropic.com/en/docs/claude-code/mcp) for other transport methods.

Claude Code provides built-in MCP management commands to easily add, configure, and authenticate your FastMCP servers.

## [​](https://gofastmcp.com/integrations/claude-code\#create-a-server)  Create a Server

You can create FastMCP servers using STDIO transport, remote HTTP servers, or local HTTP servers. This example shows one common approach: running an HTTP server locally for development.

server.py

Copy

Ask AI

```
import random
from fastmcp import FastMCP

mcp = FastMCP(name="Dice Roller")

@mcp.tool
def roll_dice(n_dice: int) -> list[int]:
    """Roll `n_dice` 6-sided dice and return the results."""
    return [random.randint(1, 6) for _ in range(n_dice)]

if __name__ == "__main__":
    mcp.run(transport="http", port=8000)

```

## [​](https://gofastmcp.com/integrations/claude-code\#connect-to-claude-code)  Connect to Claude Code

Start your server and add it to Claude Code:

Copy

Ask AI

```
# Start your server first
python server.py

```

Then add it to Claude Code:

Copy

Ask AI

```
claude mcp add dice --transport http http://localhost:8000/mcp/

```

## [​](https://gofastmcp.com/integrations/claude-code\#using-your-server)  Using Your Server

Once connected, Claude Code will automatically discover and use your server’s tools when relevant:

Copy

Ask AI

```
Roll some dice for me

```

Claude will call your `roll_dice` tool and provide the results. If your server provides resources, you can reference them with `@` mentions like `@dice:file://path/to/resource`.

[ChatGPT](https://gofastmcp.com/integrations/chatgpt) [Claude Desktop](https://gofastmcp.com/integrations/claude-desktop)

On this page

- [Create a Server](https://gofastmcp.com/integrations/claude-code#create-a-server)
- [Connect to Claude Code](https://gofastmcp.com/integrations/claude-code#connect-to-claude-code)
- [Using Your Server](https://gofastmcp.com/integrations/claude-code#using-your-server)

Assistant

Responses are generated using AI and may contain mistakes.