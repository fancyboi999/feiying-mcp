# 飞影数字人 MCP 服务器

基于 FastMCP 框架的飞影数字人 API 集成服务，提供数字人克隆、声音克隆、视频创作等功能的工具接口，方便大语言模型（LLM）调用。

## 项目概述

飞影数字人 MCP 服务器是一个集成了飞影数字人 API 的 FastMCP 服务，它提供了以下功能：

- **数字人克隆**：创建和管理自定义数字人形象
- **声音克隆**：创建和管理自定义声音
- **视频创作**：通过文本或音频创建数字人视频
- **音频创作**：通过文本创建语音内容
- **文件上传**：上传音频、视频等媒体文件
- **查询功能**：查询任务状态、私人虚拟人列表等

该项目使用 SQLAlchemy 进行数据库管理，支持异步操作，并实现了任务状态自动更新机制。

## 安装步骤

### 前置要求

- Python 3.8 或更高版本
- 飞影数字人 API Token（需要向飞影申请）

### 安装过程

1. **克隆仓库**

   ```bash
   git clone https://github.com/your-username/feiying-mcp.git
   cd feiying-mcp
   ```

2. **创建虚拟环境并安装依赖**

   ```bash
   # 使用 venv 创建虚拟环境
   python -m venv venv
   source venv/bin/activate  # Windows 使用: venv\Scripts\activate
   
   # 使用 uv 安装依赖
   uv pip install -r requirements.txt
   ```

3. **配置环境变量**

   从示例文件创建 `.env` 文件，并设置必要的配置：

   ```bash
   cp env.example .env
   ```

   编辑 `.env` 文件，至少需要设置：
   - `FLYWORKS_API_TOKEN`：飞影数字人 API Token

   更多配置选项请参考 [配置指南](docs/configuration.md)。

## 运行服务器

飞影数字人 MCP 服务器支持多种运行方式：

### 使用 Python 直接运行

```bash
# 默认 HTTP 模式，监听 127.0.0.1:8000
python main.py

# 指定主机和端口
python main.py --host 0.0.0.0 --port 8080

# 使用 STDIO 传输协议（适用于 Claude Desktop 等客户端）
python main.py --transport stdio

# 使用配置文件
python main.py --config config.json
```

### 使用 FastMCP CLI 运行

如果已安装 FastMCP CLI，可以使用以下命令：

```bash
# 默认模式
fastmcp run main.py

# 开发模式（带 MCP Inspector）
fastmcp dev main.py

# 指定传输协议和端口
fastmcp run main.py --transport http --port 9000
```

## 使用方法

服务器启动后，可以通过以下方式使用：

1. **HTTP API 调用**：服务器默认在 `http://127.0.0.1:8000/mcp/` 提供 HTTP API
2. **FastMCP 客户端调用**：使用 FastMCP 客户端库调用服务器提供的工具
3. **与 LLM 集成**：将服务器与支持工具调用的 LLM（如 Claude、GPT-4 等）集成

详细的 API 文档和使用示例请参考：
- [API 文档](docs/api.md)
- [使用示例](docs/examples.md)

## 项目结构

```
feiying-mcp/
├── main.py           # 主程序入口
├── config.py         # 配置管理模块
├── database.py       # 数据库连接管理
├── models.py         # 数据库模型定义
├── api_client.py     # 飞影 API 客户端
├── task_manager.py   # 任务状态更新管理器
├── tools/            # 工具实现目录
│   ├── __init__.py   # 工具注册
│   ├── avatar_tools.py  # 数字人相关工具
│   ├── voice_tools.py   # 声音相关工具
│   ├── video_tools.py   # 视频相关工具
│   ├── audio_tools.py   # 音频相关工具
│   ├── upload_tools.py  # 上传相关工具
│   └── query_tools.py   # 查询相关工具
├── migrations/       # 数据库迁移脚本
└── docs/            # 文档目录
    ├── api.md       # API 文档
    ├── configuration.md  # 配置指南
    └── examples.md  # 使用示例
```

## 许可证

[MIT License](LICENSE)

## 贡献指南

欢迎提交 Issue 和 Pull Request！

## 联系方式

如有问题，请联系项目维护者。
