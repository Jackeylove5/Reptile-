import requests
# url='https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=python&rsv_pq=900677b90002173e&rsv_t=3108cm4uE3OgBPnLVlFyfAsOSXY709xiPOZwZqS3lh%2FTWcT3xw6s0v01Ke4&rqlang=cn&rsv_enter=1&rsv_dl=tb&rsv_sug3=7&rsv_sug1=7&rsv_sug7=101&rsv_sug2=0&inputT=1745&rsv_sug4=2537'
# # response=requests.get(url)
# # print(response.content.decode())
#
# # 1.怎么通过get请求携带请求头
# # 1.1准备请求头
h={
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
# # 1.2携带请求头
# response=requests.get(url,headers=h)
# print(response.content.decode())

# 2.get请求怎么携带参数
# 2.1手动拼
url='https://www.baidu.com/s?={}'
s=input('请输入要搜索的关键字')
url=url.format(s)
response=requests.get(url,headers=h)
print(response.content.decode())
# 2.2使用params参数携带查询字符串参数
url='https://www.baidu.com/s'
p={
    'wd':'python'
}
response=requests.get(url,header=h)
print(response.content.decode())
