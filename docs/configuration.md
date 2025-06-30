# 配置指南

飞影数字人 MCP 服务器支持多种配置方式，包括环境变量、配置文件和命令行参数。本文档将详细说明各种配置选项及其用法。

## 配置优先级

配置的优先级从高到低为：

1. 命令行参数
2. 环境变量
3. 配置文件
4. 默认值

这意味着命令行参数会覆盖环境变量，环境变量会覆盖配置文件中的设置，而配置文件会覆盖默认值。

## 配置文件

服务器支持使用 JSON 格式的配置文件。可以通过 `--config` 命令行参数指定配置文件路径：

```bash
python main.py --config config.json
```

配置文件示例（`mcp_server_config_demo.json`）：

```json
{
  "api_token": "your_api_token_here",
  "api_base_url": "https://hfw-api.hifly.cc/api/v2/hifly",
  "database_url": "sqlite+aiosqlite:///./hifly.db",
  "db_echo": false,
  "db_pool_size": 5,
  "db_max_overflow": 10,
  "db_pool_timeout": 30,
  "db_pool_recycle": 1800,
  "server_host": "127.0.0.1",
  "server_port": 8000,
  "server_path": "/mcp/",
  "server_log_level": "info",
  "task_check_interval": 60,
  "task_max_retry": 3
}
```

## 环境变量

服务器会自动加载 `.env` 文件中的环境变量。您也可以直接在系统中设置这些环境变量。

环境变量示例（`env.example`）：

```
# API配置
FLYWORKS_API_TOKEN=your_api_token_here
FLYWORKS_API_BASE_URL=https://hfw-api.hifly.cc/api/v2/hifly

# 数据库配置
DATABASE_URL=sqlite+aiosqlite:///./hifly.db
DB_ECHO=false
DB_POOL_SIZE=5
DB_MAX_OVERFLOW=10
DB_POOL_TIMEOUT=30
DB_POOL_RECYCLE=1800

# 服务器配置
SERVER_HOST=127.0.0.1
SERVER_PORT=8000
SERVER_PATH=/mcp/
SERVER_LOG_LEVEL=info

# 任务配置
TASK_CHECK_INTERVAL=60
TASK_MAX_RETRY=3
```

## 命令行参数

服务器支持以下命令行参数：

- `--config`: 配置文件路径
- `--host`: 服务器主机地址
- `--port`: 服务器端口
- `--path`: 服务器路径
- `--log-level`: 日志级别（debug, info, warning, error, critical）
- `--transport`: 传输协议（stdio, http, sse）

示例：

```bash
python main.py --host 0.0.0.0 --port 8080 --log-level debug --transport http
```

## 配置选项详解

### API 配置

| 配置项 | 环境变量 | 默认值 | 说明 |
|-------|---------|-------|------|
| `api_token` | `FLYWORKS_API_TOKEN` | 空 | 飞影数字人 API Token，必须设置 |
| `api_base_url` | `FLYWORKS_API_BASE_URL` | `https://hfw-api.hifly.cc/api/v2/hifly` | API 基础 URL |

### 数据库配置

| 配置项 | 环境变量 | 默认值 | 说明 |
|-------|---------|-------|------|
| `database_url` | `DATABASE_URL` | `sqlite+aiosqlite:///./hifly.db` | 数据库连接 URL |
| `db_echo` | `DB_ECHO` | `false` | 是否输出 SQL 语句（调试用） |
| `db_pool_size` | `DB_POOL_SIZE` | `5` | 连接池大小 |
| `db_max_overflow` | `DB_MAX_OVERFLOW` | `10` | 连接池最大溢出连接数 |
| `db_pool_timeout` | `DB_POOL_TIMEOUT` | `30` | 连接池超时时间（秒） |
| `db_pool_recycle` | `DB_POOL_RECYCLE` | `1800` | 连接池回收时间（秒） |

#### 数据库 URL 格式

服务器支持多种数据库后端，以下是一些常见的数据库 URL 格式：

- **SQLite**（默认）：`sqlite+aiosqlite:///./hifly.db`
- **PostgreSQL**：`postgresql+asyncpg://user:password@localhost:5432/hifly`
- **MySQL**：`mysql+aiomysql://user:password@localhost:3306/hifly`

### 服务器配置

| 配置项 | 环境变量 | 命令行参数 | 默认值 | 说明 |
|-------|---------|-----------|-------|------|
| `server_host` | `SERVER_HOST` | `--host` | `127.0.0.1` | 服务器监听地址 |
| `server_port` | `SERVER_PORT` | `--port` | `8000` | 服务器监听端口 |
| `server_path` | `SERVER_PATH` | `--path` | `/mcp/` | HTTP API 路径前缀 |
| `server_log_level` | `SERVER_LOG_LEVEL` | `--log-level` | `info` | 日志级别 |

### 任务配置

| 配置项 | 环境变量 | 默认值 | 说明 |
|-------|---------|-------|------|
| `task_check_interval` | `TASK_CHECK_INTERVAL` | `60` | 任务状态检查间隔（秒） |
| `task_max_retry` | `TASK_MAX_RETRY` | `3` | 任务状态检查最大重试次数 |

## 最佳实践

1. **开发环境**：使用 `.env` 文件和默认配置
2. **测试环境**：使用配置文件，便于版本控制和共享
3. **生产环境**：使用环境变量或命令行参数，增强安全性

## 安全注意事项

- **不要在代码中硬编码 API Token**
- **不要将包含真实 API Token 的 `.env` 文件或配置文件提交到版本控制系统**
- **生产环境应使用环境变量注入 API Token，而不是使用配置文件** 