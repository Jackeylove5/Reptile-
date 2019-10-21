# 将cookieJar转换为字典
import requests

response=requests.get('http://www.baidu.com')

cookirjar=response.cookies

dic=requests.utils.dict_from_cookiejar(cookirjar)
print(dic)

# 将字典转换为cookirjar
cookir=requests.utils.cookiejar_from_dict(dic)
print(cookir)