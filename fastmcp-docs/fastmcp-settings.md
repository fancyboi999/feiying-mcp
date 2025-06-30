# settings - FastMCP

**Source URL:** https://gofastmcp.com/python-sdk/fastmcp-settings
**Generated:** 2025-06-27

---

[FastMCP Cloud](https://fastmcp.link/x0Kyhy2) is coming!

[FastMCP home page\\
FastMCP](https://gofastmcp.com/)

Search the docs...

Ctrl KAsk AI

Search...

Navigation

settings

[Documentation](https://gofastmcp.com/getting-started/welcome) [SDK Reference](https://gofastmcp.com/python-sdk/fastmcp-exceptions)

# [​](https://gofastmcp.com/python-sdk/fastmcp-settings\#fastmcp-settings)  `fastmcp.settings`

## [​](https://gofastmcp.com/python-sdk/fastmcp-settings\#classes)  Classes

### [​](https://gofastmcp.com/python-sdk/fastmcp-settings\#extendedenvsettingssource)  `ExtendedEnvSettingsSource`

A special EnvSettingsSource that allows for multiple env var prefixes to be used.

Raises a deprecation warning if the old `FASTMCP_SERVER_` prefix is used.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-settings\#get-field-value)  `get_field_value`

Copy

Ask AI

```
get_field_value(self, field: FieldInfo, field_name: str) -> tuple[Any, str, bool]

```

### [​](https://gofastmcp.com/python-sdk/fastmcp-settings\#extendedsettingsconfigdict)  `ExtendedSettingsConfigDict`

### [​](https://gofastmcp.com/python-sdk/fastmcp-settings\#settings)  `Settings`

FastMCP settings.

**Methods:**

#### [​](https://gofastmcp.com/python-sdk/fastmcp-settings\#settings-customise-sources)  `settings_customise_sources`

Copy

Ask AI

```
settings_customise_sources(cls, settings_cls: type[BaseSettings], init_settings: PydanticBaseSettingsSource, env_settings: PydanticBaseSettingsSource, dotenv_settings: PydanticBaseSettingsSource, file_secret_settings: PydanticBaseSettingsSource) -> tuple[PydanticBaseSettingsSource, ...]

```

#### [​](https://gofastmcp.com/python-sdk/fastmcp-settings\#settings-2)  `settings`

Copy

Ask AI

```
settings(self) -> Self

```

This property is for backwards compatibility with FastMCP < 2.8.0,
which accessed fastmcp.settings.settings

#### [​](https://gofastmcp.com/python-sdk/fastmcp-settings\#setup-logging)  `setup_logging`

Copy

Ask AI

```
setup_logging(self) -> Self

```

Finalize the settings.

[exceptions](https://gofastmcp.com/python-sdk/fastmcp-exceptions) [\_\_init\_\_](https://gofastmcp.com/python-sdk/fastmcp-cli-__init__)

On this page

- [fastmcp.settings](https://gofastmcp.com/python-sdk/fastmcp-settings#fastmcp-settings)
- [Classes](https://gofastmcp.com/python-sdk/fastmcp-settings#classes)
- [ExtendedEnvSettingsSource](https://gofastmcp.com/python-sdk/fastmcp-settings#extendedenvsettingssource)
- [get\_field\_value](https://gofastmcp.com/python-sdk/fastmcp-settings#get-field-value)
- [ExtendedSettingsConfigDict](https://gofastmcp.com/python-sdk/fastmcp-settings#extendedsettingsconfigdict)
- [Settings](https://gofastmcp.com/python-sdk/fastmcp-settings#settings)
- [settings\_customise\_sources](https://gofastmcp.com/python-sdk/fastmcp-settings#settings-customise-sources)
- [settings](https://gofastmcp.com/python-sdk/fastmcp-settings#settings-2)
- [setup\_logging](https://gofastmcp.com/python-sdk/fastmcp-settings#setup-logging)

Assistant

Responses are generated using AI and may contain mistakes.