# 使用示例

本文档提供了飞影数字人 MCP 服务器的使用示例，包括如何通过 FastMCP 客户端和 HTTP API 调用服务器提供的工具。

## 目录

- [准备工作](#准备工作)
- [FastMCP 客户端调用示例](#fastmcp-客户端调用示例)
- [HTTP API 调用示例](#http-api-调用示例)
- [与 LLM 集成示例](#与-llm-集成示例)
- [完整工作流示例](#完整工作流示例)

## 准备工作

在开始使用飞影数字人 MCP 服务器之前，请确保：

1. 服务器已正确安装并运行
2. 已配置有效的 API Token
3. 数据库已初始化

## FastMCP 客户端调用示例

### 安装 FastMCP 客户端

```bash
pip install fastmcp
```

### 创建客户端连接

```python
import asyncio
from fastmcp import Client

async def main():
    # 连接到本地 HTTP 服务器
    client = Client("http://127.0.0.1:8000/mcp/")
    
    # 或者连接到本地 STDIO 服务器
    # client = Client("python main.py --transport stdio")
    
    async with client:
        # 在这里调用工具
        pass

if __name__ == "__main__":
    asyncio.run(main())
```

### 创建数字人示例

```python
import asyncio
from fastmcp import Client

async def create_avatar():
    client = Client("http://127.0.0.1:8000/mcp/")
    
    async with client:
        # 通过视频创建数字人
        result = await client.call_tool(
            "create_avatar_by_video",
            {
                "title": "我的数字人",
                "file_path": "/path/to/video.mp4",
                "user_id": "user123"
            }
        )
        
        print(f"任务ID: {result['task_id']}")
        print(f"状态: {result['status']}")
        print(f"消息: {result['message']}")
        
        # 查询任务状态
        task_id = result['task_id']
        while True:
            task_result = await client.call_tool(
                "query_avatar_task",
                {"task_id": task_id}
            )
            
            print(f"任务状态: {task_result['status']}")
            
            if task_result['status'] in ["success", "failed"]:
                break
                
            # 等待10秒后再次查询
            await asyncio.sleep(10)
        
        if task_result['status'] == "success":
            print(f"数字人ID: {task_result['avatar_id']}")

if __name__ == "__main__":
    asyncio.run(create_avatar())
```

### 创建视频示例

```python
import asyncio
from fastmcp import Client

async def create_video():
    client = Client("http://127.0.0.1:8000/mcp/")
    
    async with client:
        # 通过文本创建视频
        result = await client.call_tool(
            "create_video_by_tts",
            {
                "avatar": "avatar123",  # 数字人ID
                "voice": "voice456",    # 声音ID
                "text": "这是一段测试文本，将被转换为视频中的语音。",
                "title": "测试视频",
                "subtitle_enabled": True,
                "user_id": "user123"
            }
        )
        
        print(f"任务ID: {result['task_id']}")
        
        # 查询任务状态
        task_id = result['task_id']
        while True:
            task_result = await client.call_tool(
                "query_video_task",
                {"task_id": task_id}
            )
            
            print(f"任务状态: {task_result['status']}")
            
            if task_result['status'] in ["success", "failed"]:
                break
                
            # 等待10秒后再次查询
            await asyncio.sleep(10)
        
        if task_result['status'] == "success":
            print(f"视频URL: {task_result['video_url']}")
            print(f"视频时长: {task_result['duration']}秒")

if __name__ == "__main__":
    asyncio.run(create_video())
```

## HTTP API 调用示例

服务器默认在 `http://127.0.0.1:8000/mcp/` 提供 HTTP API。

### 使用 curl 调用

```bash
# 查询公共数字人列表
curl -X POST http://127.0.0.1:8000/mcp/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "list_public_avatars",
    "arguments": {
      "page": 1,
      "size": 10
    }
  }'
```

### 使用 Python requests 库调用

```python
import requests
import json
import time

# 服务器地址
SERVER_URL = "http://127.0.0.1:8000/mcp/"

# 创建声音
def create_voice():
    payload = {
        "name": "create_voice",
        "arguments": {
            "title": "我的声音",
            "file_path": "/path/to/audio.mp3",
            "user_id": "user123"
        }
    }
    
    response = requests.post(SERVER_URL, json=payload)
    result = response.json()
    
    print(f"任务ID: {result['result']['task_id']}")
    
    # 查询任务状态
    task_id = result['result']['task_id']
    while True:
        query_payload = {
            "name": "query_voice_task",
            "arguments": {
                "task_id": task_id
            }
        }
        
        query_response = requests.post(SERVER_URL, json=query_payload)
        task_result = query_response.json()['result']
        
        print(f"任务状态: {task_result['status']}")
        
        if task_result['status'] in ["success", "failed"]:
            break
            
        # 等待10秒后再次查询
        time.sleep(10)
    
    if task_result['status'] == "success":
        print(f"声音ID: {task_result['voice_id']}")

if __name__ == "__main__":
    create_voice()
```

## 与 LLM 集成示例

### 在 Claude 中使用

如果您使用 Claude Desktop，可以将服务器以 STDIO 模式运行，然后在 Claude 中配置工具：

```python
# 启动服务器（STDIO模式）
python main.py --transport stdio

# 在 Claude Desktop 中配置工具
{
  "tools": [
    {
      "name": "feiying_mcp",
      "description": "飞影数字人 MCP 服务器，提供数字人克隆、声音克隆、视频创作等功能",
      "command": "python main.py --transport stdio"
    }
  ]
}
```

### 在 OpenAI 中使用

如果您使用 OpenAI API，可以将服务器以 HTTP 模式运行，然后在 OpenAI 中配置工具：

```python
import openai

# 配置 OpenAI API
client = openai.OpenAI(api_key="your_openai_api_key")

# 定义工具
tools = [
    {
        "type": "function",
        "function": {
            "name": "create_video_by_tts",
            "description": "通过文本创建数字人视频",
            "parameters": {
                "type": "object",
                "properties": {
                    "avatar": {
                        "type": "string",
                        "description": "数字人ID"
                    },
                    "voice": {
                        "type": "string",
                        "description": "声音ID"
                    },
                    "text": {
                        "type": "string",
                        "description": "文本内容"
                    },
                    "title": {
                        "type": "string",
                        "description": "视频标题"
                    }
                },
                "required": ["avatar", "voice", "text"]
            }
        }
    }
]

# 调用 OpenAI API
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "你是一个助手，可以帮助用户创建数字人视频。"},
        {"role": "user", "content": "帮我用数字人创建一个介绍人工智能的视频。"}
    ],
    tools=tools
)

# 处理工具调用
tool_calls = response.choices[0].message.tool_calls
if tool_calls:
    for tool_call in tool_calls:
        function_name = tool_call.function.name
        function_args = json.loads(tool_call.function.arguments)
        
        # 这里调用飞影 MCP 服务器的 HTTP API
        if function_name == "create_video_by_tts":
            payload = {
                "name": "create_video_by_tts",
                "arguments": function_args
            }
            
            api_response = requests.post("http://127.0.0.1:8000/mcp/", json=payload)
            result = api_response.json()
            
            # 将结果返回给 OpenAI
            client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "你是一个助手，可以帮助用户创建数字人视频。"},
                    {"role": "user", "content": "帮我用数字人创建一个介绍人工智能的视频。"},
                    {"role": "assistant", "content": None, "tool_calls": tool_calls},
                    {"role": "tool", "tool_call_id": tool_call.id, "content": json.dumps(result)}
                ]
            )
```

## 完整工作流示例

以下是一个完整的工作流示例，从创建数字人和声音，到生成视频的全过程：

```python
import asyncio
from fastmcp import Client

async def complete_workflow():
    client = Client("http://127.0.0.1:8000/mcp/")
    
    async with client:
        # 步骤1：上传视频文件
        upload_result = await client.call_tool(
            "upload_file",
            {"file_path": "/path/to/person.mp4"}
        )
        video_file_id = upload_result["file_id"]
        print(f"视频文件上传成功，文件ID: {video_file_id}")
        
        # 步骤2：创建数字人
        avatar_result = await client.call_tool(
            "create_avatar_by_video",
            {
                "title": "我的数字人",
                "file_id": video_file_id,
                "user_id": "user123"
            }
        )
        avatar_task_id = avatar_result["task_id"]
        print(f"数字人创建任务提交成功，任务ID: {avatar_task_id}")
        
        # 等待数字人创建完成
        avatar_id = await wait_for_task_completion(client, "query_avatar_task", avatar_task_id, "avatar_id")
        print(f"数字人创建成功，数字人ID: {avatar_id}")
        
        # 步骤3：上传音频文件
        upload_audio_result = await client.call_tool(
            "upload_file",
            {"file_path": "/path/to/voice.mp3"}
        )
        audio_file_id = upload_audio_result["file_id"]
        print(f"音频文件上传成功，文件ID: {audio_file_id}")
        
        # 步骤4：创建声音
        voice_result = await client.call_tool(
            "create_voice",
            {
                "title": "我的声音",
                "file_id": audio_file_id,
                "user_id": "user123"
            }
        )
        voice_task_id = voice_result["task_id"]
        print(f"声音创建任务提交成功，任务ID: {voice_task_id}")
        
        # 等待声音创建完成
        voice_id = await wait_for_task_completion(client, "query_voice_task", voice_task_id, "voice_id")
        print(f"声音创建成功，声音ID: {voice_id}")
        
        # 步骤5：创建视频
        video_result = await client.call_tool(
            "create_video_by_tts",
            {
                "avatar": avatar_id,
                "voice": voice_id,
                "text": "你好，我是一个数字人。这是一个测试视频，展示了飞影数字人MCP服务器的功能。",
                "title": "测试视频",
                "subtitle_enabled": True,
                "user_id": "user123"
            }
        )
        video_task_id = video_result["task_id"]
        print(f"视频创建任务提交成功，任务ID: {video_task_id}")
        
        # 等待视频创建完成
        video_url = await wait_for_task_completion(client, "query_video_task", video_task_id, "video_url")
        print(f"视频创建成功，视频URL: {video_url}")

async def wait_for_task_completion(client, query_tool, task_id, result_key):
    """等待任务完成并返回指定的结果值"""
    while True:
        task_result = await client.call_tool(
            query_tool,
            {"task_id": task_id}
        )
        
        print(f"任务状态: {task_result['status']}")
        
        if task_result['status'] == "success":
            return task_result[result_key]
        elif task_result['status'] == "failed":
            raise Exception(f"任务失败: {task_result.get('message', '未知错误')}")
            
        # 等待10秒后再次查询
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(complete_workflow()) 