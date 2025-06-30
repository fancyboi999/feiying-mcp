import asyncio
from tools.avatar_tools import list_public_avatars_tool

async def test_list_public_avatars():
    try:
        result = await list_public_avatars_tool(kind=2, page=1, size=20)
        print(result)
    except Exception as e:
        print(f"测试失败: {str(e)}")

if __name__ == "__main__":
    asyncio.run(test_list_public_avatars())