# requests使用三步骤
# 1.导包
import requests
# 2.发送请求
# 2.1准备url
url='https://www.baidu.com'
# 2.2向url发送请求获取响应对象    发送什么请求.什么
response=requests.get(url)


# 1.text属性是获取文本信息，类型是字符串
# print(response.text)
# 2.encoding 获取猜测的编码格式    中国utf-8，gbk
# print(response.encoding)
# response.encoding='utf-8'
# print(response.encoding)
# print(type(response.text))

# 3.content 获取返回的二进制信息
# byte=response.content
# print(byte.decode('utf-8'))

# 4.url 获取响应的连接
# print(response.url)

# 5.headers 获取响应头
# print(response.headers)

# 6.status_code 获取响应状态码
print(response.status_code)

