import requests
# url='http://httpbin.org/post'
# # 发送post请求
# response=requests.post(url)
# print(response.text)

h={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
url='http://httpbin.org/post'

# p={
#     'wd':'python'
# }

# 请求体
d={
    'haha':'hehe',
    "哈哈":"呵呵"
}

# 发送post请求
# response= requests.post(url,headers=h,params=p)
response= requests.post(url,headers=h,data=d)
# print(response.text)
# 转换json的数据
print(response.json())
