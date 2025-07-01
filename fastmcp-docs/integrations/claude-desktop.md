# Claude Desktop + FastMCP - FastMCP

**Source URL:** https://gofastmcp.com/integrations/claude-desktop
**Generated:** 2025-06-30

**Description:** Call FastMCP servers from Claude Desktop

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Integrations

Claude Desktop + FastMCP

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

Claude Desktop supports MCP servers through local STDIO connections and remote servers (beta), allowing you to extend Claude’s capabilities with custom tools, resources, and prompts from your FastMCP servers.

Remote MCP server support is currently in beta and available for users on Claude Pro, Max, Team, and Enterprise plans (as of June 2025). Most users will still need to use local STDIO connections.

This guide focuses specifically on using FastMCP servers with Claude Desktop. For general Claude Desktop MCP setup and official examples, see the [official Claude Desktop quickstart guide](https://modelcontextprotocol.io/quickstart/user).

## [​](https://gofastmcp.com/integrations/claude-desktop\#requirements)  Requirements

Claude Desktop traditionally requires MCP servers to run locally using STDIO transport, where your server communicates with Claude through standard input/output rather than HTTP. However, users on certain plans now have access to remote server support as well.

If you don’t have access to remote server support or need to connect to remote servers, you can create a **proxy server** that runs locally via STDIO and forwards requests to remote HTTP servers. See the [Proxy Servers](https://gofastmcp.com/integrations/claude-desktop#proxy-servers) section below.

## [​](https://gofastmcp.com/integrations/claude-desktop\#create-a-server)  Create a Server

The examples in this guide will use the following simple dice-rolling server, saved as `server.py`.

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
    mcp.run()

```

## [​](https://gofastmcp.com/integrations/claude-desktop\#install-the-server)  Install the Server

### [​](https://gofastmcp.com/integrations/claude-desktop\#fastmcp-cli)  FastMCP CLI

The easiest way to install a FastMCP server in Claude Desktop is using the `fastmcp install` command. This automatically handles the configuration and dependency management.

Copy

Ask AI

```
fastmcp install server.py

```

The install command supports the same `file.py:object` notation as the `run` command. If no object is specified, it will automatically look for a FastMCP server object named `mcp`, `server`, or `app` in your file:

Copy

Ask AI

```
# These are equivalent if your server object is named 'mcp'
fastmcp install server.py
fastmcp install server.py:mcp

# Use explicit object name if your server has a different name
fastmcp install server.py:my_custom_server

```

After installation, restart Claude Desktop completely. You should see a hammer icon (🔨) in the bottom left of the input box, indicating that MCP tools are available.

#### [​](https://gofastmcp.com/integrations/claude-desktop\#dependencies)  Dependencies

If your server has dependencies, include them with the `--with` flag:

Copy

Ask AI

```
fastmcp install server.py --with pandas --with requests

```

Alternatively, you can specify dependencies directly in your server code:

server.py

Copy

Ask AI

```
from fastmcp import FastMCP

mcp = FastMCP(
    name="Dice Roller",
    dependencies=["pandas", "requests"]
)

```

#### [​](https://gofastmcp.com/integrations/claude-desktop\#environment-variables)  Environment Variables

Claude Desktop runs servers in a completely isolated environment with no access to your shell environment or locally installed applications. You must explicitly pass any environment variables your server needs.

If your server needs environment variables (like API keys), you must include them:

Copy

Ask AI

```
fastmcp install server.py --name "Weather Server" \
  --env-var API_KEY=your-api-key \
  --env-var DEBUG=true

```

Or load them from a `.env` file:

Copy

Ask AI

```
fastmcp install server.py --name "Weather Server" --env-file .env

```

- **`uv` must be installed and available in your system PATH**. Claude Desktop runs in its own isolated environment and needs `uv` to manage dependencies.
- **On macOS, it is recommended to install `uv` globally with Homebrew** so that Claude Desktop will detect it: `brew install uv`. Installing `uv` with other methods may not make it accessible to Claude Desktop.

### [​](https://gofastmcp.com/integrations/claude-desktop\#manual-configuration)  Manual Configuration

For more control over the configuration, you can manually edit Claude Desktop’s configuration file. You can open the configuration file from Claude’s developer settings, or find it in the following locations:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

The configuration file is a JSON object with a `mcpServers` key, which contains the configuration for each MCP server.

Copy

Ask AI

```
{
  "mcpServers": {
    "dice-roller": {
      "command": "python",
      "args": ["path/to/your/server.py"]
    }
  }
}

```

After updating the configuration file, restart Claude Desktop completely. Look for the hammer icon (🔨) to confirm your server is loaded.

#### [​](https://gofastmcp.com/integrations/claude-desktop\#dependencies-2)  Dependencies

If your server has dependencies, you can use `uv` or another package manager to set up the environment.

Copy

Ask AI

```
{
  "mcpServers": {
    "dice-roller": {
      "command": "uv",
      "args": [\
        "run",\
        "--with", "pandas",\
        "--with", "requests",\
        "python",\
        "path/to/your/server.py"\
      ]
    }
  }
}

```

- **`uv` must be installed and available in your system PATH**. Claude Desktop runs in its own isolated environment and needs `uv` to manage dependencies.
- **On macOS, it is recommended to install `uv` globally with Homebrew** so that Claude Desktop will detect it: `brew install uv`. Installing `uv` with other methods may not make it accessible to Claude Desktop.

#### [​](https://gofastmcp.com/integrations/claude-desktop\#environment-variables-2)  Environment Variables

You can also specify environment variables in the configuration:

Copy

Ask AI

```
{
  "mcpServers": {
    "weather-server": {
      "command": "python",
      "args": ["path/to/weather_server.py"],
      "env": {
        "API_KEY": "your-api-key",
        "DEBUG": "true"
      }
    }
  }
}

```

Claude Desktop runs servers in a completely isolated environment with no access to your shell environment or locally installed applications. You must explicitly pass any environment variables your server needs.

## [​](https://gofastmcp.com/integrations/claude-desktop\#remote-servers)  Remote Servers

Users on Claude Pro, Max, Team, and Enterprise plans have first-class remote server support via integrations. For other users, or as an alternative approach, FastMCP can create a proxy server that forwards requests to a remote HTTP server. You can install the proxy server in Claude Desktop.

Create a proxy server that connects to a remote HTTP server:

proxy\_server.py

Copy

Ask AI

```
from fastmcp import FastMCP

# Create a proxy to a remote server
proxy = FastMCP.as_proxy(
    "https://example.com/mcp/sse",
    name="Remote Server Proxy"
)

if __name__ == "__main__":
    proxy.run()  # Runs via STDIO for Claude Desktop

```

### [​](https://gofastmcp.com/integrations/claude-desktop\#authentication)  Authentication

For authenticated remote servers, create an authenticated client following the guidance in the [client auth documentation](https://gofastmcp.com/clients/auth/bearer) and pass it to the proxy:

auth\_proxy\_server.py

Copy

Ask AI

```
from fastmcp import FastMCP, Client
from fastmcp.client.auth import BearerAuth

# Create authenticated client
client = Client(
    "https://api.example.com/mcp/sse",
    auth=BearerAuth(token="your-access-token")
)

# Create proxy using the authenticated client
proxy = FastMCP.as_proxy(client, name="Authenticated Proxy")

if __name__ == "__main__":
    proxy.run()

```

[Claude Code](https://gofastmcp.com/integrations/claude-code) [Gemini SDK](https://gofastmcp.com/integrations/gemini)

On this page

- [Requirements](https://gofastmcp.com/integrations/claude-desktop#requirements)
- [Create a Server](https://gofastmcp.com/integrations/claude-desktop#create-a-server)
- [Install the Server](https://gofastmcp.com/integrations/claude-desktop#install-the-server)
- [FastMCP CLI](https://gofastmcp.com/integrations/claude-desktop#fastmcp-cli)
- [Dependencies](https://gofastmcp.com/integrations/claude-desktop#dependencies)
- [Environment Variables](https://gofastmcp.com/integrations/claude-desktop#environment-variables)
- [Manual Configuration](https://gofastmcp.com/integrations/claude-desktop#manual-configuration)
- [Dependencies](https://gofastmcp.com/integrations/claude-desktop#dependencies-2)
- [Environment Variables](https://gofastmcp.com/integrations/claude-desktop#environment-variables-2)
- [Remote Servers](https://gofastmcp.com/integrations/claude-desktop#remote-servers)
- [Authentication](https://gofastmcp.com/integrations/claude-desktop#authentication)

Assistant

Responses are generated using AI and may contain mistakes.