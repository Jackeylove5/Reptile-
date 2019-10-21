# 1.导包
import requests
# 2.准备url列表
# 2.1准备url模板
h={
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'
}
t_name=input('请输入要爬取的贴吧名字')
url='http://tieba.baidu.com/f?kw='+t_name+'&ie=utf-8&pn={}'
print(url)
start=int(input('请输入起始页'))
end=int(input('请输入结束页'))
# 2.2准备url列表
url_list=[]
for i in range(start,end+1):
    url_list.append(url.format(i-1)*50)
print(url_list)

# 3.遍历url列表发送请求获取响应数据进行保存
for url in url_list:
    print(url)
    # 3.1发送请求
    response=requests.get(url,headers=h)
    print(response.content.decode())
    data=response.content.decode()
    with open('杨洋_第{}页.html'.format(start),'w',encoding='utf-8') as f:
        f.write(data)
    start+=1