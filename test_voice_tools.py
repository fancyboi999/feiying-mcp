import asyncio
import logging
from tools.voice_tools import list_voices_tool

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def test_list_voices():
    """测试list_voices_tool函数"""
    
    logger.info("=== 测试list_voices_tool函数 ===")
    
    # 第一次调用
    logger.info("第一次调用list_voices_tool:")
    result1 = await list_voices_tool(page=1, size=20, kind=1)
    logger.info(f"第一次调用结果: {result1}")
    
    # 第二次调用
    logger.info("\n第二次调用list_voices_tool:")
    result2 = await list_voices_tool(page=1, size=20, kind=1)
    logger.info(f"第二次调用结果: {result2}")
    
    logger.info("\n=== 测试完成 ===")

if __name__ == "__main__":
    asyncio.run(test_list_voices()) 