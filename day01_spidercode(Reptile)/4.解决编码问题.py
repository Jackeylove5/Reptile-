import requests

url='http://www.people.com.cn'
response= requests.get(url)

# 1.使用utf-8进行解码
print(response.content.decode())
# 2.使用gbk进行解码
print(response.content.decode('gbk'))
# 3.text
print(response.text)