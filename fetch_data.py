import requests
import os
import json

# 从环境变量中获取 Access Token
access_token = os.getenv('FB_ACCESS_TOKEN')
# 设置 API 端点和 Access Token
url = os.getenv('URL')
params = {
    'fields': 'business_discovery.username(yezyizhere){followers_count,username}',
    'access_token': access_token
}

# 发起 GET 请求
response = requests.get(url, params=params)

# 检查响应状态码
if response.status_code == 200:
    data = response.json()
    username = data.get("username", "未知用户名") 
    followers_count = data.get("followers_count", "未知粉丝数") 

# 将数据写入文件
    with open('output.txt', 'w') as file:
        file.write(f"{username},{followers_count}\n") 
        
else:
    print(f"请求失败，状态码: {response.status_code}")
