"""
查询工具，包括私人虚拟人ID查询功能
"""

import logging
from typing import Dict, Any, List, Optional
from fastmcp.tools import Tool
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import func

from database import get_db
from models import Avatar
from api_client import HiFlyClient

# 配置日志
logger = logging.getLogger(__name__)

async def query_private_avatars_tool(
    user_id: str,
    page: int = 1,
    size: int = 10,
) -> Dict[str, Any]:
    """
    查询用户的私人虚拟人列表。
    
    Args:
        user_id: 用户ID
        page: 页码，默认为1
        size: 每页数量，默认为10
        
    Returns:
        包含私人虚拟人列表和分页信息的结果
    """
    # 参数验证
    if not user_id:
        raise ValueError("用户ID不能为空")
    
    if page < 1:
        raise ValueError("页码必须大于等于1")
    
    if size < 1 or size > 100:
        raise ValueError("每页数量必须在1到100之间")
    
    # 计算偏移量
    offset = (page - 1) * size
    
    # 获取数据库会话
    async for db in get_db():
        try:
            # 查询用户的私人虚拟人总数
            count_query = select(func.count(Avatar.id)).where(
                Avatar.user_id == user_id,
                Avatar.kind == 1  # 1表示私人虚拟人
            )
            result = await db.execute(count_query)
            total = result.scalar()
            
            # 如果没有数据，直接返回空列表
            if total == 0:
                return {
                    "total": 0,
                    "page": page,
                    "size": size,
                    "avatars": []
                }
            
            # 查询用户的私人虚拟人列表，按创建时间倒序排序
            query = select(Avatar).where(
                Avatar.user_id == user_id,
                Avatar.kind == 1  # 1表示私人虚拟人
            ).order_by(Avatar.created_at.desc()).offset(offset).limit(size)
            
            result = await db.execute(query)
            avatars = result.scalars().all()
            
            # 构造返回结果
            avatar_list = []
            for avatar in avatars:
                avatar_list.append({
                    "id": avatar.id,
                    "avatar_id": avatar.avatar_id,
                    "title": avatar.title,
                    "created_at": avatar.created_at.isoformat() if avatar.created_at else None,
                    "task_id": avatar.task_id
                })
            
            # 计算总页数
            total_pages = (total + size - 1) // size
            
            return {
                "total": total,
                "page": page,
                "size": size,
                "total_pages": total_pages,
                "avatars": avatar_list
            }
            
        except Exception as e:
            logger.error(f"查询私人虚拟人失败: {str(e)}")
            raise ValueError(f"查询私人虚拟人失败: {str(e)}")

# 创建FastMCP工具
query_private_avatars = Tool.from_function(
    query_private_avatars_tool,
    name="query_private_avatars",
    description="查询用户的私人虚拟人列表，支持分页",
    tags={"avatar", "query", "private"}
)


# 导出工具列表，用于注册到FastMCP服务器
query_tools = [
    query_private_avatars,
] 