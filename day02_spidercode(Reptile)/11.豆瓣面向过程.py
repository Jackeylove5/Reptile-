import requests
import json
# 1.准备url
url='https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=200&page_start=0'
# url='https://movie.douban.com/tv/#!type=tv&tag=热门&sort=recommend&page_limit=20&page_start=0'
# 2.发送请求获取数据
response=requests.get(url)
print(response.json())
# 3.提取数据
data=response.json()
# print(data['subjects'])

list=data['subjects']
with open('douban.json','w',encoding='utf-8') as f :
    for l in list:
        dic={}
        dic['title']=l["title"]
        dic['rate']=l["rate"]
        dic['cover']=l['cover']
        json.dump(dic,f,ensure_ascii=False)
        f.write(',\n')
