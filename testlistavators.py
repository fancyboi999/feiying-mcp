import asyncio
import logging
from api_client import HiFlyClient
from tools.audio_tools import query_audio_task_tool

# 测试音频生成任务状态

client = HiFlyClient()
async def test_audio_task():
    response = await query_audio_task_tool("JvEFA4UAv8Kqet4c39V-Mw")
    print(f"音频生成任务状态: {response}")

if __name__ == "__main__":
    asyncio.run(test_audio_task())