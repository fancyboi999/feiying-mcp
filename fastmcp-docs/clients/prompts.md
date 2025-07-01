# Prompts - FastMCP

**Source URL:** https://gofastmcp.com/clients/prompts
**Generated:** 2025-06-30

**Description:** Use server-side prompt templates with automatic argument serialization.

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

Core Operations

Prompts

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

`New in version: 2.0.0`

Prompts are reusable message templates exposed by MCP servers. They can accept arguments to generate personalized message sequences for LLM interactions.

## [​](https://gofastmcp.com/clients/prompts\#listing-prompts)  Listing Prompts

Use `list_prompts()` to retrieve all available prompt templates:

Copy

Ask AI

```
async with client:
    prompts = await client.list_prompts()
    # prompts -> list[mcp.types.Prompt]

    for prompt in prompts:
        print(f"Prompt: {prompt.name}")
        print(f"Description: {prompt.description}")
        if prompt.arguments:
            print(f"Arguments: {[arg.name for arg in prompt.arguments]}")

```

## [​](https://gofastmcp.com/clients/prompts\#using-prompts)  Using Prompts

### [​](https://gofastmcp.com/clients/prompts\#basic-usage)  Basic Usage

Request a rendered prompt using `get_prompt()` with the prompt name and arguments:

Copy

Ask AI

```
async with client:
    # Simple prompt without arguments
    result = await client.get_prompt("welcome_message")
    # result -> mcp.types.GetPromptResult

    # Access the generated messages
    for message in result.messages:
        print(f"Role: {message.role}")
        print(f"Content: {message.content}")

```

### [​](https://gofastmcp.com/clients/prompts\#prompts-with-arguments)  Prompts with Arguments

Pass arguments as a dictionary to customize the prompt:

Copy

Ask AI

```
async with client:
    # Prompt with simple arguments
    result = await client.get_prompt("user_greeting", {
        "name": "Alice",
        "role": "administrator"
    })

    # Access the personalized messages
    for message in result.messages:
        print(f"Generated message: {message.content}")

```

## [​](https://gofastmcp.com/clients/prompts\#automatic-argument-serialization)  Automatic Argument Serialization

`New in version: 2.9.0`

FastMCP automatically serializes complex arguments to JSON strings as required by the MCP specification. This allows you to pass typed objects directly:

Copy

Ask AI

```
from dataclasses import dataclass

@dataclass
class UserData:
    name: str
    age: int

async with client:
    # Complex arguments are automatically serialized
    result = await client.get_prompt("analyze_user", {
        "user": UserData(name="Alice", age=30),     # Automatically serialized to JSON
        "preferences": {"theme": "dark"},           # Dict serialized to JSON string
        "scores": [85, 92, 78],                     # List serialized to JSON string
        "simple_name": "Bob"                        # Strings passed through unchanged
    })

```

The client handles serialization using `pydantic_core.to_json()` for consistent formatting. FastMCP servers can automatically deserialize these JSON strings back to the expected types.

### [​](https://gofastmcp.com/clients/prompts\#serialization-examples)  Serialization Examples

Copy

Ask AI

```
async with client:
    result = await client.get_prompt("data_analysis", {
        # These will be automatically serialized to JSON strings:
        "config": {
            "format": "csv",
            "include_headers": True,
            "delimiter": ","
        },
        "filters": [\
            {"field": "age", "operator": ">", "value": 18},\
            {"field": "status", "operator": "==", "value": "active"}\
        ],
        # This remains a string:
        "report_title": "Monthly Analytics Report"
    })

```

## [​](https://gofastmcp.com/clients/prompts\#working-with-prompt-results)  Working with Prompt Results

The `get_prompt()` method returns a `GetPromptResult` object containing a list of messages:

Copy

Ask AI

```
async with client:
    result = await client.get_prompt("conversation_starter", {"topic": "climate"})

    # Access individual messages
    for i, message in enumerate(result.messages):
        print(f"Message {i + 1}:")
        print(f"  Role: {message.role}")
        print(f"  Content: {message.content.text if hasattr(message.content, 'text') else message.content}")

```

## [​](https://gofastmcp.com/clients/prompts\#raw-mcp-protocol-access)  Raw MCP Protocol Access

For access to the complete MCP protocol objects, use the `*_mcp` methods:

Copy

Ask AI

```
async with client:
    # Raw MCP method returns full protocol object
    prompts_result = await client.list_prompts_mcp()
    # prompts_result -> mcp.types.ListPromptsResult

    prompt_result = await client.get_prompt_mcp("example_prompt", {"arg": "value"})
    # prompt_result -> mcp.types.GetPromptResult

```

## [​](https://gofastmcp.com/clients/prompts\#multi-server-clients)  Multi-Server Clients

When using multi-server clients, prompts are accessible without prefixing (unlike tools):

Copy

Ask AI

```
async with client:  # Multi-server client
    # Prompts from any server are directly accessible
    result1 = await client.get_prompt("weather_prompt", {"city": "London"})
    result2 = await client.get_prompt("assistant_prompt", {"query": "help"})

```

## [​](https://gofastmcp.com/clients/prompts\#common-prompt-patterns)  Common Prompt Patterns

### [​](https://gofastmcp.com/clients/prompts\#system-messages)  System Messages

Many prompts generate system messages for LLM configuration:

Copy

Ask AI

```
async with client:
    result = await client.get_prompt("system_configuration", {
        "role": "helpful assistant",
        "expertise": "python programming"
    })

    # Typically returns messages with role="system"
    system_message = result.messages[0]
    print(f"System prompt: {system_message.content}")

```

### [​](https://gofastmcp.com/clients/prompts\#conversation-templates)  Conversation Templates

Prompts can generate multi-turn conversation templates:

Copy

Ask AI

```
async with client:
    result = await client.get_prompt("interview_template", {
        "candidate_name": "Alice",
        "position": "Senior Developer"
    })

    # Multiple messages for a conversation flow
    for message in result.messages:
        print(f"{message.role}: {message.content}")

```

Prompt arguments and their expected types depend on the specific prompt implementation. Check the server’s documentation or use `list_prompts()` to see available arguments for each prompt.

[Resources](https://gofastmcp.com/clients/resources) [Elicitation](https://gofastmcp.com/clients/elicitation)

On this page

- [Listing Prompts](https://gofastmcp.com/clients/prompts#listing-prompts)
- [Using Prompts](https://gofastmcp.com/clients/prompts#using-prompts)
- [Basic Usage](https://gofastmcp.com/clients/prompts#basic-usage)
- [Prompts with Arguments](https://gofastmcp.com/clients/prompts#prompts-with-arguments)
- [Automatic Argument Serialization](https://gofastmcp.com/clients/prompts#automatic-argument-serialization)
- [Serialization Examples](https://gofastmcp.com/clients/prompts#serialization-examples)
- [Working with Prompt Results](https://gofastmcp.com/clients/prompts#working-with-prompt-results)
- [Raw MCP Protocol Access](https://gofastmcp.com/clients/prompts#raw-mcp-protocol-access)
- [Multi-Server Clients](https://gofastmcp.com/clients/prompts#multi-server-clients)
- [Common Prompt Patterns](https://gofastmcp.com/clients/prompts#common-prompt-patterns)
- [System Messages](https://gofastmcp.com/clients/prompts#system-messages)
- [Conversation Templates](https://gofastmcp.com/clients/prompts#conversation-templates)

Assistant

Responses are generated using AI and may contain mistakes.