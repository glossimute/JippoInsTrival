import requests
import os
import json

# 从环境变量中获取 Access Token
access_token = os.getenv('FB_ACCESS_TOKEN')
# 设置 API 端点和 Access Token
url = 'https://graph.facebook.com/v20.0/17841407991309868'
params = {
    'fields': 'business_discovery.username(yezyizhere){followers_count,username}',
    'access_token': access_token
}

# 发起 GET 请求
response = requests.get(url, params=params)

# 检查响应状态码
if response.status_code == 200:
    data = response.json()
    print(data)
    data1 = json.loads(data)
    with open('output.txt', 'w') as file:
    file.write(data1["username"]+","+data1[followers_count]"\n")
    print("数据成功写入 output.txt 文件")
else:
    print(f"请求失败，状态码: {response.status_code}")
