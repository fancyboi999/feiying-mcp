FROM python:3.10-slim

# 设置工作目录
WORKDIR /app

# 设置环境变量
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    PYTHONPATH=/app

# 安装依赖
RUN pip install --no-cache-dir uv && \
    apt-get update && \
    apt-get install -y --no-install-recommends gcc build-essential curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# 复制项目文件
COPY . /app/

# 使用uv安装项目依赖
RUN uv pip install --system --no-cache-dir -e .

# 创建必要的目录
RUN mkdir -p /app/excel_files /app/data

# 如果没有.env文件，则复制示例文件（但不覆盖已存在的.env）
RUN if [ ! -f .env ]; then cp -n env.example .env || true; fi

# 暴露端口
# Smithery会设置PORT环境变量，我们需要在启动脚本中使用它
EXPOSE 8000

# 创建启动脚本
RUN echo '#!/bin/sh\n\
# 检查环境变量\n\
if [ -z "$FLYWORKS_API_TOKEN" ]; then\n\
  echo "错误: FLYWORKS_API_TOKEN 环境变量未设置!"\n\
  echo "请确保已通过环境变量或配置提供API令牌"\n\
  exit 1\n\
fi\n\
\n\
# 设置端口，优先使用PORT环境变量（Smithery提供）\n\
if [ -n "$PORT" ]; then\n\
  export SERVER_PORT=$PORT\n\
fi\n\
\n\
echo "Running database migrations..."\n\
alembic upgrade head || echo "Warning: Database migration failed, but continuing..."\n\
echo "Starting Feiying MCP server..."\n\
exec feiying-mcp http --host ${SERVER_HOST:-0.0.0.0} --port ${SERVER_PORT:-8000} --path ${SERVER_PATH:-/mcp} --log-level ${SERVER_LOG_LEVEL:-info}\n\
' > /app/start.sh && chmod +x /app/start.sh

# 启动命令
CMD ["/app/start.sh"]

# 健康检查
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f -H "Accept: text/event-stream" http://localhost:${SERVER_PORT:-8000}${SERVER_PATH:-/mcp}/health || exit 1
