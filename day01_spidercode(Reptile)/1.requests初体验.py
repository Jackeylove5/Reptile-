# requests使用三步骤
# 1.导包
import requests

# 2.发送请求
# 2.1准备url
url='https://www.baidu.com'
# 2.2向url发送请求获取响应对象    发送什么请求.什么
response=requests.get(url)

# 3.提取数据
print(response.text)