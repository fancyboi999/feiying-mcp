# prompt - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt
**Generated:** 2025-06-30

---

FastMCP Cloud is here! [Join the beta](https://fastmcp.link/x0Kyhy2).

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.prompts

prompt

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt\#fastmcp-prompts-prompt)  `fastmcp.prompts.prompt`

Base classes for FastMCP prompts.

## [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt\#functions)  Functions

### [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt\#message)  `Message`

Copy

Ask AI

```
Message(content: str | MCPContent, role: Role | None = None, **kwargs: Any) -> PromptMessage

```

A user-friendly constructor for PromptMessage.

## [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt\#promptargument)  `PromptArgument`

An argument that can be passed to a prompt.

### [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt\#prompt)  `Prompt`

A prompt template that can be rendered with parameters.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt\#to-mcp-prompt)  `to_mcp_prompt`

Copy

Ask AI

```
to_mcp_prompt(self, **overrides: Any) -> MCPPrompt

```

Convert the prompt to an MCP prompt.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt\#from-function)  `from_function`

Copy

Ask AI

```
from_function(fn: Callable[..., PromptResult | Awaitable[PromptResult]], name: str | None = None, description: str | None = None, tags: set[str] | None = None, enabled: bool | None = None) -> FunctionPrompt

```

Create a Prompt from a function.

The function can return:

- A string (converted to a message)
- A Message object
- A dict (converted to a message)
- A sequence of any of the above

### [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt\#functionprompt)  `FunctionPrompt`

A prompt that is a function.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt\#from-function-2)  `from_function`

Copy

Ask AI

```
from_function(cls, fn: Callable[..., PromptResult | Awaitable[PromptResult]], name: str | None = None, description: str | None = None, tags: set[str] | None = None, enabled: bool | None = None) -> FunctionPrompt

```

Create a Prompt from a function.

The function can return:

- A string (converted to a message)
- A Message object
- A dict (converted to a message)
- A sequence of any of the above

[\_\_init\_\_](https://gofastmcp.com/python-sdk/fastmcp-prompts-__init__) [prompt\_manager](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt_manager)

On this page

- [fastmcp.prompts.prompt](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt#fastmcp-prompts-prompt)
- [Functions](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt#functions)
- [Message](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt#message)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt#classes)
- [PromptArgument](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt#promptargument)
- [Prompt](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt#prompt)
- [to\_mcp\_prompt](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt#to-mcp-prompt)
- [from\_function](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt#from-function)
- [FunctionPrompt](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt#functionprompt)
- [from\_function](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt#from-function-2)

Assistant

Responses are generated using AI and may contain mistakes.