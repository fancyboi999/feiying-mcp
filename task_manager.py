"""
任务状态更新管理器，定期检查任务状态并更新数据库
"""

import asyncio
import logging
import datetime
from typing import Dict, Any, List, Optional, Set
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy import update, and_

from api_client import HiFlyClient
from database import get_db, AsyncSessionLocal
from models import Task, Avatar, Voice, Video, Audio

# 配置日志
logger = logging.getLogger(__name__)

# 任务类型映射
TASK_TYPE_MAP = {
    1: "视频作品",
    2: "数字人克隆",
    3: "声音克隆",
    4: "音频创作"
}

# 任务状态映射
TASK_STATUS_MAP = {
    1: "等待中",
    2: "处理中",
    3: "完成",
    4: "失败"
}

class TaskManager:
    """任务状态更新管理器"""
    
    def __init__(self, check_interval: int = 60, max_retry: int = 3):
        """
        初始化任务管理器
        
        Args:
            check_interval: 检查间隔时间（秒）
            max_retry: 任务处理最大重试次数
        """
        self.check_interval = check_interval
        self.max_retry = max_retry
        self.running = False
        self.task = None
        self.processing_tasks: Set[str] = set()  # 正在处理的任务ID集合，避免重复处理
        self.client = None  # API客户端实例
        
        logger.info(f"TaskManager initialized with check_interval={check_interval}s, max_retry={max_retry}")
    
    async def start(self):
        """启动任务状态更新循环"""
        if self.running:
            logger.warning("TaskManager is already running")
            return
        
        # 创建API客户端
        self.client = HiFlyClient()
        logger.info("Created API client for TaskManager")
        
        self.running = True
        self.task = asyncio.create_task(self._update_loop())
        logger.info("TaskManager started")
    
    async def stop(self):
        """停止任务状态更新循环"""
        if not self.running:
            logger.warning("TaskManager is not running")
            return
        
        self.running = False
        if self.task:
            self.task.cancel()
            try:
                await self.task
            except asyncio.CancelledError:
                pass
            self.task = None
        
        # 关闭API客户端
        if self.client:
            await self.client.close()
            self.client = None
            logger.info("Closed API client for TaskManager")
            
        logger.info("TaskManager stopped")
    
    async def _update_loop(self):
        """任务状态更新循环"""
        while self.running:
            try:
                await self._check_and_update_tasks()
            except Exception as e:
                logger.error(f"Error in task update loop: {str(e)}")
            
            # 等待下一次检查
            await asyncio.sleep(self.check_interval)
    
    async def _check_and_update_tasks(self):
        """检查并更新所有未完成任务的状态"""
        logger.debug("Starting task status check...")
        
        # 获取数据库会话
        async with AsyncSessionLocal() as db:
            try:
                # 查询所有未完成的任务
                result = await db.execute(
                    select(Task).where(
                        and_(
                            Task.status.in_([1, 2]),  # 1:等待中, 2:处理中
                            Task.task_id.notin_(self.processing_tasks)  # 排除正在处理的任务
                        )
                    )
                )
                tasks = result.scalars().all()
                
                if not tasks:
                    logger.debug("No pending tasks found")
                    return
                
                logger.info(f"Found {len(tasks)} pending tasks")
                
                # 确保客户端存在
                if not self.client:
                    self.client = HiFlyClient()
                    logger.info("Re-created API client for TaskManager")
                
                # 处理每个未完成的任务
                for task in tasks:
                    # 标记任务为正在处理
                    self.processing_tasks.add(task.task_id)
                    
                    try:
                        # 根据任务类型调用不同的API查询任务状态
                        await self._update_task_status(db, self.client, task)
                    except Exception as e:
                        logger.error(f"Error updating task {task.task_id}: {str(e)}")
                    finally:
                        # 无论成功失败，都从处理集合中移除
                        self.processing_tasks.remove(task.task_id)
                
            except Exception as e:
                logger.error(f"Error checking tasks: {str(e)}")
    
    async def _update_task_status(self, db: AsyncSession, client: HiFlyClient, task: Task):
        """
        更新单个任务的状态
        
        Args:
            db: 数据库会话
            client: API客户端
            task: 任务对象
        """
        logger.debug(f"Updating task {task.task_id} (type: {TASK_TYPE_MAP.get(task.task_type, 'Unknown')})")
        
        try:
            # 根据任务类型调用不同的API
            if task.task_type == 1:  # 视频作品
                response = await client.get_video_task(task.task_id)
                await self._process_video_task(db, task, response)
            elif task.task_type == 2:  # 数字人克隆
                response = await client.get_avatar_task(task.task_id)
                await self._process_avatar_task(db, task, response)
            elif task.task_type == 3:  # 声音克隆
                response = await client.get_voice_task(task.task_id)
                await self._process_voice_task(db, task, response)
            elif task.task_type == 4:  # 音频创作
                response = await client.get_audio_task(task.task_id)
                await self._process_audio_task(db, task, response)
            else:
                logger.warning(f"Unknown task type: {task.task_type}")
                return
            
            # 提交更改
            await db.commit()
            
        except Exception as e:
            await db.rollback()
            logger.error(f"Error updating task {task.task_id}: {str(e)}")
    
    async def _process_video_task(self, db: AsyncSession, task: Task, response: Dict[str, Any]):
        """处理视频任务状态更新"""
        # 获取状态
        status = response.get("status")
        video_url = response.get("url")
        duration = response.get("duration", 0)
        
        # 更新任务状态
        await self._update_task_record(db, task, status, response)
        
        # 如果任务完成，更新视频记录
        if status == 3 and video_url:  # 3表示完成
            # 查询视频记录
            result = await db.execute(select(Video).where(Video.task_id == task.task_id))
            video = result.scalars().first()
            
            if video:
                # 更新视频记录
                video.video_url = video_url
                video.duration = duration
                logger.info(f"Updated video record for task {task.task_id}")
    
    async def _process_avatar_task(self, db: AsyncSession, task: Task, response: Dict[str, Any]):
        """处理数字人克隆任务状态更新"""
        # 获取状态
        status = response.get("status")
        avatar_id = response.get("avatar")
        
        # 更新任务状态
        await self._update_task_record(db, task, status, response)
        
        # 如果任务完成，更新数字人记录
        if status == 3 and avatar_id:  # 3表示完成
            # 查询数字人记录
            result = await db.execute(select(Avatar).where(Avatar.task_id == task.task_id))
            avatar = result.scalars().first()
            
            if avatar:
                # 更新数字人记录
                avatar.avatar_id = avatar_id
                logger.info(f"Updated avatar record for task {task.task_id}")
            else:
                # 创建数字人记录
                avatar = Avatar(
                    avatar_id=avatar_id,
                    title=task.title,
                    task_id=task.task_id,
                    user_id=task.user_id,
                    kind=1  # 1表示自己克隆的
                )
                db.add(avatar)
                logger.info(f"Created avatar record for task {task.task_id}")
    
    async def _process_voice_task(self, db: AsyncSession, task: Task, response: Dict[str, Any]):
        """处理声音克隆任务状态更新"""
        # 获取状态
        status = response.get("status")
        voice_id = response.get("voice_id")
        
        # 更新任务状态
        await self._update_task_record(db, task, status, response)
        
        # 如果任务完成，创建声音记录
        if status == 3 and voice_id:  # 3表示完成
            # 检查声音是否已存在
            result = await db.execute(select(Voice).where(Voice.voice_id == voice_id))
            existing_voice = result.scalars().first()
            
            if not existing_voice:
                # 创建声音记录
                voice = Voice(
                    voice_id=voice_id,
                    title=task.title,
                    task_id=task.task_id,
                    user_id=task.user_id,
                    voice_type=response.get("voice_type", 8),
                    demo_url=response.get("demo_url")
                )
                db.add(voice)
                logger.info(f"Created voice record for task {task.task_id}")
    
    async def _process_audio_task(self, db: AsyncSession, task: Task, response: Dict[str, Any]):
        """处理音频创作任务状态更新"""
        # 获取状态
        status = response.get("status")
        audio_id = response.get("audio_id")
        audio_url = response.get("url")
        duration = response.get("duration", 0)
        
        # 更新任务状态
        await self._update_task_record(db, task, status, response)
        
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
                    task_id=task.task_id,
                    url=audio_url,
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
                
                logger.info(f"Created audio record for task {task.task_id}")
    
    async def _update_task_record(self, db: AsyncSession, task: Task, status: int, response: Dict[str, Any]):
        """更新任务记录"""
        # 如果状态没有变化，不需要更新
        if task.status == status:
            return
        
        # 更新任务状态
        task.status = status
        task.message = response.get("message", "")
        task.code = response.get("code", 0)
        task.updated_at = datetime.datetime.utcnow()
        
        logger.info(f"Updated task {task.task_id} status to {TASK_STATUS_MAP.get(status, 'Unknown')}")

# 创建全局任务管理器实例
task_manager = TaskManager()

async def start_task_manager():
    """启动任务管理器"""
    await task_manager.start()

async def stop_task_manager():
    """停止任务管理器"""
    await task_manager.stop()

# 手动触发任务状态检查
async def check_tasks_now():
    """手动触发任务状态检查"""
    try:
        await task_manager._check_and_update_tasks()
        return {"status": "success", "message": "任务状态检查已触发"}
    except Exception as e:
        logger.error(f"Error triggering task check: {str(e)}")
        return {"status": "error", "message": f"任务状态检查失败: {str(e)}"} 