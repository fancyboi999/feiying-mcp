# API 文档

飞影数字人 MCP 服务器提供了多种工具，用于数字人克隆、声音克隆、视频创作等功能。本文档详细介绍了每个工具的功能、参数和返回值。

## 目录

- [数字人工具](#数字人工具)
- [声音工具](#声音工具)
- [视频工具](#视频工具)
- [音频工具](#音频工具)
- [上传工具](#上传工具)
- [查询工具](#查询工具)

## 数字人工具

### create_avatar_by_video

通过视频创建数字人。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| title | string | 是 | 数字人名称，不超过20个字 |
| video_url | string | 视频URL和文件路径二选一必填 | 视频URL地址，支持mp4、mov格式且使用h264编码，500MB以内，分辨率范围360p～4K，时长范围5秒～30分钟 |
| file_path | string | 视频URL和文件路径二选一必填 | 本地视频文件路径，系统会自动上传该文件 |
| user_id | string | 否 | 用户ID，用于关联数字人所有者，如不提供则使用默认用户 |

**返回值：**

```json
{
  "task_id": "任务ID",
  "status": "waiting",
  "message": "数字人克隆任务已提交，请稍后查询任务状态"
}
```

### create_avatar_by_image

通过图片创建数字人。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| title | string | 是 | 数字人名称，不超过20个字 |
| image_url | string | 图片URL和文件路径二选一必填 | 图片URL地址 |
| file_path | string | 图片URL和文件路径二选一必填 | 本地图片文件路径，系统会自动上传该文件 |
| model | integer | 否 | 模型类型，1:视频2.0，2:视频2.1，默认2 |
| user_id | string | 否 | 用户ID，用于关联数字人所有者，如不提供则使用默认用户 |

**返回值：**

```json
{
  "task_id": "任务ID",
  "status": "waiting",
  "message": "数字人克隆任务已提交，请稍后查询任务状态"
}
```

### query_avatar_task

查询数字人克隆任务状态。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| task_id | string | 是 | 任务ID |

**返回值：**

```json
{
  "task_id": "任务ID",
  "status": "success",  // waiting, processing, success, failed
  "avatar_id": "数字人ID",  // 仅在成功时返回
  "message": "任务状态信息"
}
```

### list_public_avatars

获取公共数字人列表。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| page | integer | 否 | 页码，默认1 |
| size | integer | 否 | 每页数量，默认20 |
| kind | integer | 否 | 数字人类型，1:私有，2:公共，默认2 |

**返回值：**

```json
{
  "total": 100,
  "page": 1,
  "size": 20,
  "total_pages": 5,
  "items": [
    {
      "id": "数字人ID",
      "title": "数字人名称",
      "preview_url": "预览图URL",
      "created_at": "创建时间"
    }
  ]
}
```

## 声音工具

### create_voice

创建声音克隆。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| title | string | 是 | 声音名称，不超过20个字 |
| audio_url | string | 音频URL和文件路径二选一必填 | 音频URL地址，支持mp3、wav、m4a格式，50MB以内，时长范围5秒～30分钟 |
| file_path | string | 音频URL和文件路径二选一必填 | 本地音频文件路径，系统会自动上传该文件 |
| user_id | string | 否 | 用户ID，用于关联声音所有者，如不提供则使用默认用户 |

**返回值：**

```json
{
  "task_id": "任务ID",
  "status": "waiting",
  "message": "声音克隆任务已提交，请稍后查询任务状态"
}
```

### query_voice_task

查询声音克隆任务状态。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| task_id | string | 是 | 任务ID |

**返回值：**

```json
{
  "task_id": "任务ID",
  "status": "success",  // waiting, processing, success, failed
  "voice_id": "声音ID",  // 仅在成功时返回
  "message": "任务状态信息"
}
```

### list_public_voices

获取公共声音列表。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| page | integer | 否 | 页码，默认1 |
| size | integer | 否 | 每页数量，默认20 |
| kind | integer | 否 | 声音类型，1:私有，2:公共，默认2 |

**返回值：**

```json
{
  "total": 100,
  "page": 1,
  "size": 20,
  "total_pages": 5,
  "items": [
    {
      "id": "声音ID",
      "title": "声音名称",
      "preview_url": "预览音频URL",
      "created_at": "创建时间"
    }
  ]
}
```

## 视频工具

### create_video_by_audio

通过音频创建视频（音频驱动视频创作）。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| avatar | string | 是 | 数字人ID，可以是公共数字人ID或自己克隆的数字人ID |
| file_id | string | 文件ID和音频URL二选一必填 | 上传的音频文件ID |
| audio_url | string | 文件ID和音频URL二选一必填 | 音频URL |
| title | string | 否 | 视频标题，如不提供则使用"未命名" |
| user_id | string | 否 | 用户ID，用于关联视频所有者，如不提供则使用默认用户 |

**返回值：**

```json
{
  "task_id": "任务ID",
  "status": "waiting",
  "message": "视频创作任务已提交，请稍后查询任务状态"
}
```

### create_video_by_tts

通过文本创建视频（文本驱动视频创作）。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| avatar | string | 是 | 数字人ID，可以是公共数字人ID或自己克隆的数字人ID |
| voice | string | 是 | 声音ID，可以是公共声音ID或自己克隆的声音ID |
| text | string | 是 | 文本内容，最多5000字 |
| title | string | 否 | 视频标题，如不提供则使用"未命名" |
| subtitle_enabled | boolean | 否 | 是否启用字幕，默认false |
| subtitle_font_size | integer | 否 | 字幕字体大小，默认40 |
| subtitle_font_color | string | 否 | 字幕颜色，默认"#FFFFFF" |
| subtitle_bg_color | string | 否 | 字幕背景色，默认"#000000" |
| subtitle_bg_opacity | number | 否 | 字幕背景透明度，0-1之间，默认0.5 |
| user_id | string | 否 | 用户ID，用于关联视频所有者，如不提供则使用默认用户 |

**返回值：**

```json
{
  "task_id": "任务ID",
  "status": "waiting",
  "message": "视频创作任务已提交，请稍后查询任务状态"
}
```

### query_video_task

查询视频创作任务状态。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| task_id | string | 是 | 任务ID |

**返回值：**

```json
{
  "task_id": "任务ID",
  "status": "success",  // waiting, processing, success, failed
  "video_url": "视频URL",  // 仅在成功时返回
  "duration": 60,  // 视频时长（秒），仅在成功时返回
  "message": "任务状态信息"
}
```

## 音频工具

### create_audio_by_tts

通过文本创建音频（文本转语音）。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| voice | string | 是 | 声音ID，可以是公共声音ID或自己克隆的声音ID |
| text | string | 是 | 文本内容，最多5000字 |
| title | string | 否 | 音频标题，如不提供则使用"未命名" |
| user_id | string | 否 | 用户ID，用于关联音频所有者，如不提供则使用默认用户 |

**返回值：**

```json
{
  "task_id": "任务ID",
  "status": "waiting",
  "message": "音频创作任务已提交，请稍后查询任务状态"
}
```

### query_audio_task

查询音频创作任务状态。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| task_id | string | 是 | 任务ID |

**返回值：**

```json
{
  "task_id": "任务ID",
  "status": "success",  // waiting, processing, success, failed
  "audio_url": "音频URL",  // 仅在成功时返回
  "duration": 60,  // 音频时长（秒），仅在成功时返回
  "message": "任务状态信息"
}
```

## 上传工具

### upload_file

上传文件。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| file_path | string | 是 | 本地文件路径 |
| file_type | string | 否 | 文件类型，可选值：image, video, audio，默认根据文件扩展名自动判断 |

**返回值：**

```json
{
  "file_id": "文件ID",
  "message": "文件上传成功"
}
```

## 查询工具

### query_private_avatars

查询用户的私人虚拟人列表。

**参数：**

| 参数名 | 类型 | 必填 | 说明 |
|-------|------|------|------|
| user_id | string | 是 | 用户ID |
| page | integer | 否 | 页码，默认1 |
| size | integer | 否 | 每页数量，默认10 |

**返回值：**

```json
{
  "total": 100,
  "page": 1,
  "size": 10,
  "total_pages": 10,
  "items": [
    {
      "id": "数据库ID",
      "avatar_id": "数字人ID",
      "title": "数字人名称",
      "created_at": "创建时间",
      "task_id": "关联任务ID"
    }
  ]
}
``` 