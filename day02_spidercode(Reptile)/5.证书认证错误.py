import requests

url='http://www.numpy.org.cn'

response=requests.get(url,verify=False)
print(response.content.decode())