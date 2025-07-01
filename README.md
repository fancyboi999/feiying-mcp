# 飞影数字人 MCP 服务器

**飞影数字人 MCP 服务器** 是一个基于 [FastMCP](https://github.com/mcp-suite/fastmcp) 框架构建的强大后端服务。它无缝集成了**飞影数字人**的先进 API，为大语言模型（LLM）提供了一套功能丰富的工具集，涵盖了从数字人克隆、声音复制到视频创作的全方位功能。

该项目利用 SQLAlchemy 2.0 进行异步数据库操作，并通过一个后台任务管理器自动更新任务状态，确保了系统的高效和稳定。

## ✨ 功能特性

- **数字人克隆**：支持通过照片或视频创建个性化的数字人形象。
- **声音克隆**：支持通过音频文件或文本创建和管理自定义声音。
- **视频创作**：支持通过文本驱动（Text-to-Video）或音频驱动（Audio-to-Video）两种方式创作数字人视频。
- **音频创作**：支持通过文本生成高质量的语音内容（Text-to-Speech）。
- **文件管理**：提供文件上传接口，方便管理媒体资源。
- **状态查询**：提供任务状态、数字人列表、声音列表等多种查询功能。
- **异步任务处理**：所有耗时操作（如视频生成）均为异步处理，并自动更新任务状态。

## 🛠️ 可用工具

服务器提供以下工具，可供 LLM 或其他客户端直接调用：

### 数字人工具 (`avatar_tools`)
- `create_personal_avatar_by_photo`: 通过单张照片创建个人数字人。
- `create_personal_avatar_by_video`: 通过视频文件创建个人数字人。

### 声音工具 (`voice_tools`)
- `create_voice_by_file`: 通过音频文件克隆声音。
- `create_voice_by_text`: 通过文本创建声音（用于声音定制）。

### 视频创作工具 (`video_tools`)
- `create_video_by_audio`: 使用指定的数字人和音频文件创作视频。
- `create_video_by_script`: 使用指定的数字人和文本脚本创作视频。

### 音频创作工具 (`audio_tools`)
- `create_audio_by_text`: 将文本转换为语音。

### 文件上传工具 (`upload_tools`)
- `upload_file`: 上传媒体文件（音频、视频）到服务器。

### 查询工具 (`query_tools`)
- `query_task_status`: 查询指定任务的当前状态和结果。
- `query_personal_avatars`: 查询已创建的个人数字人列表。
- `query_personal_voices`: 查询已创建的个人声音列表。
- `query_public_avatars`: 查询公共数字人列表。
- `query_public_voices`: 查询公共声音列表。
- `query_video_templates`: 查询可用的视频模板。

## 🚀 快速开始

### 1. 环境要求
- Python 3.8+
- 飞影数字人 API Token

### 2. 安装步骤

1.  **克隆仓库**:
    ```bash
    git clone https://github.com/your-username/feiying-mcp.git
    cd feiying-mcp
    ```

2.  **创建虚拟环境并安装依赖**:
    ```bash
    # 推荐使用 uv, an extremely fast Python package installer
    uv venv
    source .venv/bin/activate
    uv pip install -r requirements.txt
    ```
    如果未使用 `uv`，也可以使用 `venv`:
    ```bash
    python -m venv .venv
    source .venv/bin/activate
    pip install -r requirements.txt
    ```

3.  **配置环境变量**:
    复制示例配置文件并填入您的 API Token。
    ```bash
    cp env.example .env
    ```
    编辑 `.env` 文件，至少需要设置 `FLYWORKS_API_TOKEN`。

### 3. 数据库迁移
在首次运行前，请执行数据库迁移以创建所需的表结构：
```bash
alembic upgrade head
```

### 4. 运行服务器

您可以通过多种方式运行服务器：

- **直接运行 (开发模式)**:
  ```bash
  python main.py --host 0.0.0.0 --port 8000
  ```

- **使用 FastMCP CLI (推荐)**:
  ```bash
  # 运行服务
  fastmcp run main.py

  # 以开发模式运行，开启 MCP Inspector
  fastmcp dev main.py
  ```

- **使用 STDIO 传输协议** (适用于 Claude Desktop 等客户端):
  ```bash
  python main.py --transport stdio
  ```

## ⚙️ 项目结构

```
feiying-mcp/
├── main.py           # 主程序入口，负责启动服务和注册工具
├── config.py         # 配置管理模块，从 .env 或文件中加载配置
├── database.py       # 数据库会话管理
├── models.py         # SQLAlchemy 数据库模型定义
├── api_client.py     # 飞影 API 客户端封装
├── task_manager.py   # 后台任务状态更新管理器
├── tools/            # MCP 工具目录
│   ├── avatar_tools.py  # 数字人相关工具
│   ├── voice_tools.py   # 声音相关工具
│   ├── video_tools.py   # 视频相关工具
│   ├── audio_tools.py   # 音频相关工具
│   ├── upload_tools.py  # 上传相关工具
│   └── query_tools.py   # 查询相关工具
├── migrations/       # Alembic 数据库迁移脚本
├── requirements.txt  # 项目依赖
└── README.md         # 项目文档
```

## 📄 许可证

本项目采用 [MIT License](LICENSE) 授权。

---

如有任何问题，欢迎提交 Issue 或联系项目维护者。