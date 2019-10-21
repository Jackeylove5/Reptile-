import requests

# 1.准备代理字典，最多两组键(http/https)值对
# 值是IP：port
p={
    'http':'http://112.247.181.99:8060',
    "https":'222.197.182.108:3128'
}

url='https://httpbin.org/get'

response=requests.get(url,proxies=p)

print(response.content.decode())