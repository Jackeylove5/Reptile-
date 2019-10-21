# 1.导包
import requests
# 2.准备url
url=''
# 3.发送请求获取响应
# 3.1第一种使用cookie的方法，使用请求头携带
# h={
#     'Cookie':''
# }
# response=requests.get(url,headers=h)
# 3.2使用cookies参数携带一个cookie字典
cookies_str=''
c={cookie_str.split('=',maxsplit=1)[0]:cookie_str.split('=',maxsplit=1)[1] for cookie_str in cookies_str.split('; ')}
response=requests.get(url,cookies=c)
# 4.打印获取数据
print(response.content.decode())