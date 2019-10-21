# 准备一个代理列表，列表的每一个元素就是一个代理的字典
import random

import requests

p_list=[
    {'http':'http://112.247.181.99:8060'},
    {'http':'http://139.196.78.83:80'},
    {'http':'http://101.4.136.34:81'},
    {'http':'223.111.131.100:8080'},
    {'http':'http://111.29.3.187:8080'},
    {'http':'http://111.29.3.195:80'},
    {'http':"39.137.69.8:8080"}]

url='http://httpbin.org/get'

for i in range(6):
    p= random.choice(p_list)
    try:
        print(requests.get(url, proxies=p,timeout=2).content.decode())
    except Exception as e:
        print('此代理{}不能使用'.format(p))


# 暗网  洋葱路由
