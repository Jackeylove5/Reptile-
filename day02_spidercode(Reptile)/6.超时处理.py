import requests
url='http://www.facebook.com'
# 参数timeout，指定的值为数字单位为秒
try:
    response=requests.get(url,timeout=2)
    print(response.content.decode())
except Exception as e:
    print('此网站无法访问：{}'.format(url))