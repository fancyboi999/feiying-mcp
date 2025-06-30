import requests
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

def test_direct_request():
    # 从环境变量获取API令牌
    api_token = os.getenv("FLYWORKS_API_TOKEN")
    if not api_token:
        print("错误: 未设置FLYWORKS_API_TOKEN环境变量")
        return
    
    # 直接使用文档中的示例代码
    url = "https://hfw-api.hifly.cc/api/v2/hifly/avatar/list"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    params = {
        "page": 1,
        "size": 10,
        "kind": 2  # 查询公共数字人
    }
    
    print(f"发送请求到: {url}")
    print(f"请求头: {headers}")
    print(f"参数: {params}")
    
    try:
        response = requests.get(url, headers=headers, params=params)
        print(f"状态码: {response.status_code}")
        print(f"响应内容: {response.text}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"解析后的JSON: {data}")
    except Exception as e:
        print(f"请求失败: {str(e)}")

if __name__ == "__main__":
    test_direct_request() 