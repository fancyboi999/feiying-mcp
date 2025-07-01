"""
音频创作相关的FastMCP工具，包括文本转语音功能
"""

import logging
import datetime
from typing import Dict, Any, Optional, List
from fastmcp.tools import Tool
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update
from sqlalchemy.orm import selectinload

from api_client import HiFlyClient
from database import get_db
from models import Task, Audio, Voice

# 配置日志
logger = logging.getLogger(__name__)

async def create_audio_by_tts_tool(
    text: str,
    voice: str,
    title: Optional[str] = None,
    rate: Optional[str] = "1.0",
    volume: Optional[str] = "1.0",
    pitch: Optional[str] = "1.0",
    user_id: Optional[str] = None,
) -> Dict[str, Any]:
    """
    通过文本创建音频（文本转语音）。
    
    Args:
        text: 文本内容，不超过1000个字
        voice: 声音ID，可以是公共声音ID或自己克隆的声音ID
        title: 音频标题，如不提供则使用文本前10个字符作为标题
        rate: 语速，值为0.5和2.0之间，默认1.0
        volume: 音量，值为0.1和2.0之间，默认1.0
        pitch: 语调，值为0.1和2.0之间，默认1.0
        user_id: 用户ID，用于关联音频所有者，如不提供则使用默认用户
        
    Returns:
        包含任务ID和状态的信息
    """
    # 参数验证
    if not text:
        raise ValueError("文本内容不能为空")
    
    if len(text) > 1000:
        raise ValueError("文本内容不能超过1000个字")
    
    if not voice:
        raise ValueError("声音ID不能为空")
    
    # 验证语速、音量和语调
    try:
        rate_float = float(rate)
        if not (0.5 <= rate_float <= 2.0):
            raise ValueError("语速必须在0.5和2.0之间")
    except ValueError:
        raise ValueError("语速必须是有效的数字")
        
    try:
        volume_float = float(volume)
        if not (0.1 <= volume_float <= 2.0):
            raise ValueError("音量必须在0.1和2.0之间")
    except ValueError:
        raise ValueError("音量必须是有效的数字")
        
    try:
        pitch_float = float(pitch)
        if not (0.1 <= pitch_float <= 2.0):
            raise ValueError("语调必须在0.1和2.0之间")
    except ValueError:
        raise ValueError("语调必须是有效的数字")
    
    # 如果未提供标题，使用文本前10个字符作为标题
    if not title:
        title = text[:10] + ("..." if len(text) > 10 else "")
    
    # 获取数据库会话
    async for db in get_db():
        client = None
        try:
            # 初始化API客户端
            client = HiFlyClient()
            
            # 调用API创建音频
            response = await client.create_audio_by_tts(
                text=text,
                voice=voice,
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
                task_type=4,  # 4表示音频创作
                status=1,  # 1表示等待中
                title=title,
                request_id=request_id,
                user_id=user_id or "default",
            )
            
            # 保存到数据库
            db.add(task)
            await db.commit()
            
            return {
                "task_id": task_id,
                "status": "waiting",
                "message": "音频创作任务已提交，请稍后查询任务状态"
            }
            
        except Exception as e:
            await db.rollback()
            logger.error(f"创建音频失败: {str(e)}")
            raise ValueError(f"创建音频失败: {str(e)}")
        finally:
            # 确保API客户端被关闭
            if client:
                await client.close()

async def query_audio_task_tool(
    task_id: str,
) -> Dict[str, Any]:
    """
    查询音频创作任务状态。
    
    Args:
        task_id: 任务ID
        
    Returns:
        包含任务状态和音频信息的结果
    """
    # 获取数据库会话
    async for db in get_db():
        client = None
        try:
            # 从数据库查询任务，预加载audios关系
            result = await db.execute(
                select(Task).where(Task.task_id == task_id).options(selectinload(Task.audios))
            )
            task = result.scalars().first()
            
            if not task:
                raise ValueError(f"任务不存在: {task_id}")
            
            # 如果任务已经完成或失败，直接返回数据库中的状态
            if task.status in [3, 4]:  # 3:完成 4:失败
                if task.status == 3 and task.audios:
                    audio = task.audios[0]
                    return {
                        "task_id": task_id,
                        "status": "completed",
                        "audio_id": audio.audio_id,
                        "title": audio.title,
                        "url": audio.audio_url,
                        "duration": audio.duration,
                        "text": audio.text
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
            audio_id = response.get("audio_id")
            audio_url = response.get("video_Url")
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
            
            # 如果任务完成，创建音频记录
            if status == 3 and audio_id:  # 3表示完成
                # 检查音频是否已存在
                result = await db.execute(select(Audio).where(Audio.audio_id == audio_id))
                existing_audio = result.scalars().first()
                
                if not existing_audio:
                    # 创建音频记录
                    audio = Audio(
                        audio_id=audio_id,
                        title=task.title,
                        task_id=task_id,
                        audio_url=audio_url,
                        duration=duration,
                        text=response.get("text", ""),
                        user_id=task.user_id
                    )
                    db.add(audio)
                    
                    # 如果任务中有声音ID，关联声音记录
                    voice_id = response.get("voice")
                    if voice_id:
                        result = await db.execute(select(Voice).where(Voice.voice_id == voice_id))
                        voice = result.scalars().first()
                        if voice:
                            audio.voice_id = voice_id
            
            # 提交更改
            await db.commit()
            
            # 返回结果
            status_map = {1: "waiting", 2: "processing", 3: "completed", 4: "failed"}
            result = {
                "task_id": task_id,
                "status": status_map.get(status, "unknown")
            }
            
            if status == 3 and audio_id:
                result["audio_id"] = audio_id
                result["title"] = task.title
                result["url"] = audio_url
                result["duration"] = duration
                result["text"] = response.get("text", "")
            elif status == 4:
                result["message"] = response.get("message", "")
                result["code"] = response.get("code", 0)
            
            return result
            
        except Exception as e:
            await db.rollback()
            logger.error(f"查询任务状态失败: {str(e)}")
            raise ValueError(f"查询任务状态失败: {str(e)}")
        finally:
            # 确保API客户端被关闭
            if client:
                await client.close()

# 创建FastMCP工具
create_audio_by_tts = Tool.from_function(
    create_audio_by_tts_tool,
    name="create_audio_by_tts",
    description="通过文本创建音频（文本转语音），支持指定声音ID、语速、音量和语调",
    tags={"audio", "tts", "creation"}
)

query_audio_task = Tool.from_function(
    query_audio_task_tool,
    name="query_audio_task",
    description="查询音频创作任务状态，获取任务进度和结果",
    tags={"audio", "task", "query"}
)

# 导出工具列表，用于注册到FastMCP服务器
audio_tools = [
    create_audio_by_tts,
    query_audio_task
] 