# prompt_manager - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt_manager
**Generated:** 2025-06-27

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

fastmcp.prompts

prompt\_manager

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt_manager\#fastmcp-prompts-prompt-manager)  `fastmcp.prompts.prompt_manager`

## [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt_manager\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt_manager\#promptmanager)  `PromptManager`

Manages FastMCP prompts.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt_manager\#mount)  `mount`

Copy

Ask AI

```
mount(self, server: MountedServer) -> None

```

Adds a mounted server as a source for prompts.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt_manager\#add-prompt-from-fn)  `add_prompt_from_fn`

Copy

Ask AI

```
add_prompt_from_fn(self, fn: Callable[..., PromptResult | Awaitable[PromptResult]], name: str | None = None, description: str | None = None, tags: set[str] | None = None) -> FunctionPrompt

```

Create a prompt from a function.

#### [​](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt_manager\#add-prompt)  `add_prompt`

Copy

Ask AI

```
add_prompt(self, prompt: Prompt) -> Prompt

```

Add a prompt to the manager.

[prompt](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt) [\_\_init\_\_](https://gofastmcp.com/python-sdk/fastmcp-resources-__init__)

On this page

- [fastmcp.prompts.prompt\_manager](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt_manager#fastmcp-prompts-prompt-manager)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt_manager#classes)
- [PromptManager](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt_manager#promptmanager)
- [mount](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt_manager#mount)
- [add\_prompt\_from\_fn](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt_manager#add-prompt-from-fn)
- [add\_prompt](https://gofastmcp.com/python-sdk/fastmcp-prompts-prompt_manager#add-prompt)

Assistant

Responses are generated using AI and may contain mistakes.