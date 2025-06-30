"""
视频创作相关的FastMCP工具，包括音频驱动视频创作、文本驱动视频创作和查询功能
"""

import logging
import datetime
from typing import Dict, Any, Optional, List
from fastmcp.tools import Tool
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update

from api_client import HiFlyClient
from database import get_db
from models import Task, Video, Avatar, Voice

# 配置日志
logger = logging.getLogger(__name__)

async def create_video_by_audio_tool(
    avatar: str,
    file_id: Optional[str] = None,
    audio_url: Optional[str] = None,
    title: Optional[str] = None,
    user_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    通过音频创建视频（音频驱动视频创作）。
    
    Args:
        avatar: 数字人ID，可以是公共数字人ID或自己克隆的数字人ID
        file_id: 上传的音频文件ID，与audio_url二选一必填
        audio_url: 音频URL，与file_id二选一必填
        title: 视频标题，如不提供则使用"未命名"
        user_id: 用户ID，用于关联视频所有者，如不提供则使用默认用户
        
    Returns:
        包含任务ID和状态的信息
    """
    # 参数验证
    if not avatar:
        raise ValueError("数字人ID不能为空")
    
    if not file_id and not audio_url:
        raise ValueError("文件ID和音频URL必须提供一个")
    
    # 如果未提供标题，使用默认标题
    if not title:
        title = "未命名"
    
    # 获取数据库会话
    async for db in get_db():
        try:
            # 初始化API客户端
            client = HiFlyClient()
            
            # 调用API创建视频
            response = await client.create_video_by_audio(
                avatar=avatar,
                file_id=file_id,
                audio_url=audio_url,
                title=title
            )
            
            # 获取任务ID
            task_id = response.get("task_id")
            request_id = response.get("request_id")
            
            if not task_id:
                raise ValueError("API返回的任务ID为空")
            
            # 创建任务记录
            task = Task(
                task_id=task_id,
                task_type=1,  # 1表示视频作品
                status=1,  # 1表示等待中
                title=title,
                request_id=request_id,
                user_id=user_id or "default",
            )
            
            # 保存到数据库
            db.add(task)
            
            # 创建视频记录
            video = Video(
                title=title,
                avatar_id=avatar,
                task_id=task_id,
                file_id=file_id,
                audio_url=audio_url,
                user_id=user_id or "default",
            )
            
            db.add(video)
            await db.commit()
            
            # 关闭API客户端
            await client.close()
            
            return {
                "task_id": task_id,
                "status": "waiting",
                "message": "视频创作任务已提交，请稍后查询任务状态"
            }
            
        except Exception as e:
            await db.rollback()
            logger.error(f"创建视频失败: {str(e)}")
            # 关闭API客户端
            if 'client' in locals():
                await client.close()
            raise ValueError(f"创建视频失败: {str(e)}")

async def create_video_by_tts_tool(
    avatar: str,
    voice: str,
    text: str,
    title: Optional[str] = None,
    st_show: int = 0,
    st_font_name: Optional[str] = None,
    st_font_size: Optional[int] = None,
    st_primary_color: Optional[str] = None,
    st_outline_color: Optional[str] = None,
    st_width: Optional[int] = None,
    st_height: Optional[int] = None,
    st_pos_x: Optional[int] = None,
    st_pos_y: Optional[int] = None,
    user_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    通过文本创建视频（文本驱动视频创作）。
    
    Args:
        avatar: 数字人ID，可以是公共数字人ID或自己克隆的数字人ID
        voice: 声音ID，可以是公共声音ID或自己克隆的声音ID
        text: 文本内容
        title: 视频标题，如不提供则使用"未命名"
        st_show: 是否显示字幕，1:显示，0:不显示，默认不显示
        st_font_name: 字幕字体名称
        st_font_size: 字幕字体大小
        st_primary_color: 字幕主要颜色，如"#FFFFFF"
        st_outline_color: 字幕轮廓颜色，如"#000000"
        st_width: 字幕宽度
        st_height: 字幕高度
        st_pos_x: 字幕X坐标
        st_pos_y: 字幕Y坐标
        user_id: 用户ID，用于关联视频所有者，如不提供则使用默认用户
        
    Returns:
        包含任务ID和状态的信息
    """
    # 参数验证
    if not avatar:
        raise ValueError("数字人ID不能为空")
    
    if not voice:
        raise ValueError("声音ID不能为空")
    
    if not text:
        raise ValueError("文本内容不能为空")
    
    # 如果未提供标题，使用默认标题
    if not title:
        title = "未命名"
    
    # 获取数据库会话
    async for db in get_db():
        try:
            # 初始化API客户端
            client = HiFlyClient()
            
            # 准备字幕参数
            subtitle_params = {}
            if st_font_name:
                subtitle_params["st_font_name"] = st_font_name
            if st_font_size:
                subtitle_params["st_font_size"] = st_font_size
            if st_primary_color:
                subtitle_params["st_primary_color"] = st_primary_color
            if st_outline_color:
                subtitle_params["st_outline_color"] = st_outline_color
            if st_width:
                subtitle_params["st_width"] = st_width
            if st_height:
                subtitle_params["st_height"] = st_height
            if st_pos_x:
                subtitle_params["st_pos_x"] = st_pos_x
            if st_pos_y:
                subtitle_params["st_pos_y"] = st_pos_y
            
            # 调用API创建视频
            response = await client.create_video_by_tts(
                avatar=avatar,
                voice=voice,
                text=text,
                title=title,
                st_show=st_show,
                **subtitle_params
            )
            
            # 获取任务ID
            task_id = response.get("task_id")
            request_id = response.get("request_id")
            
            if not task_id:
                raise ValueError("API返回的任务ID为空")
            
            # 创建任务记录
            task = Task(
                task_id=task_id,
                task_type=1,  # 1表示视频作品
                status=1,  # 1表示等待中
                title=title,
                request_id=request_id,
                user_id=user_id or "default",
            )
            
            # 保存到数据库
            db.add(task)
            
            # 创建视频记录
            video = Video(
                title=title,
                avatar_id=avatar,
                voice_id=voice,
                task_id=task_id,
                text=text,
                user_id=user_id or "default",
            )
            
            db.add(video)
            await db.commit()
            
            # 关闭API客户端
            await client.close()
            
            return {
                "task_id": task_id,
                "status": "waiting",
                "message": "视频创作任务已提交，请稍后查询任务状态"
            }
            
        except Exception as e:
            await db.rollback()
            logger.error(f"创建视频失败: {str(e)}")
            # 关闭API客户端
            if 'client' in locals():
                await client.close()
            raise ValueError(f"创建视频失败: {str(e)}")

async def query_video_task_tool(
    task_id: str,
) -> Dict[str, Any]:
    """
    查询视频创作任务状态。
    
    Args:
        task_id: 任务ID
        
    Returns:
        包含任务状态和视频信息的结果
    """
    # 获取数据库会话
    async for db in get_db():
        try:
            # 从数据库查询任务
            result = await db.execute(select(Task).where(Task.task_id == task_id))
            task = result.scalars().first()
            
            if not task:
                raise ValueError(f"任务不存在: {task_id}")
            
            # 如果任务已经完成或失败，直接返回数据库中的状态
            if task.status in [3, 4]:  # 3:完成 4:失败
                if task.status == 3 and task.videos:
                    video = task.videos[0]
                    return {
                        "task_id": task_id,
                        "status": "completed",
                        "title": video.title,
                        "video_url": video.video_url,
                        "duration": video.duration,
                        "avatar_id": video.avatar_id,
                        "voice_id": video.voice_id
                    }
                elif task.status == 4:
                    return {
                        "task_id": task_id,
                        "status": "failed",
                        "message": task.message,
                        "code": task.code
                    }
            
            # 如果任务还在进行中，调用API查询最新状态
            client = HiFlyClient()
            response = await client.get_video_task(task_id)
            
            # 获取状态
            status = response.get("status")
            video_url = response.get("url")
            duration = response.get("duration", 0)
            
            # 更新数据库中的任务状态
            await db.execute(
                update(Task)
                .where(Task.task_id == task_id)
                .values(
                    status=status,
                    message=response.get("message", ""),
                    code=response.get("code", 0),
                    updated_at=datetime.datetime.utcnow()
                )
            )
            
            # 如果任务完成，更新视频记录
            if status == 3 and video_url:  # 3表示完成
                # 查询视频记录
                result = await db.execute(select(Video).where(Video.task_id == task_id))
                video = result.scalars().first()
                
                if video:
                    # 更新视频记录
                    video.video_url = video_url
                    video.duration = duration
                    
            # 提交更改
            await db.commit()
            
            # 关闭API客户端
            await client.close()
            
            # 返回结果
            status_map = {1: "waiting", 2: "processing", 3: "completed", 4: "failed"}
            result = {
                "task_id": task_id,
                "status": status_map.get(status, "unknown")
            }
            
            if status == 3 and video_url:
                # 查询视频记录
                result = await db.execute(select(Video).where(Video.task_id == task_id))
                video = result.scalars().first()
                
                if video:
                    result["title"] = video.title
                    result["video_url"] = video_url
                    result["duration"] = duration
                    result["avatar_id"] = video.avatar_id
                    result["voice_id"] = video.voice_id
            elif status == 4:
                result["message"] = response.get("message", "")
                result["code"] = response.get("code", 0)
            
            return result
            
        except Exception as e:
            await db.rollback()
            logger.error(f"查询任务状态失败: {str(e)}")
            # 关闭API客户端
            if 'client' in locals():
                await client.close()
            raise ValueError(f"查询任务状态失败: {str(e)}")

# 创建FastMCP工具
create_video_by_audio = Tool.from_function(
    create_video_by_audio_tool,
    name="create_video_by_audio",
    description="通过音频创建视频（音频驱动视频创作），支持指定数字人ID和音频文件",
    tags={"video", "audio", "creation"}
)

create_video_by_tts = Tool.from_function(
    create_video_by_tts_tool,
    name="create_video_by_tts",
    description="通过文本创建视频（文本驱动视频创作），支持指定数字人ID、声音ID和文本内容",
    tags={"video", "tts", "creation"}
)

query_video_task = Tool.from_function(
    query_video_task_tool,
    name="query_video_task",
    description="查询视频创作任务状态，获取任务进度和结果",
    tags={"video", "task", "query"}
)

# 导出工具列表，用于注册到FastMCP服务器
video_tools = [
    create_video_by_audio,
    create_video_by_tts,
    query_video_task
] 