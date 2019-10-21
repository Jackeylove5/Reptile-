import requests

class Spider:
    def __init__(self,name,start,end):
        # 实例化
        self.name=name
        self.start=start
        self.end=end
        self.headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
        self.url_parents='http://tieba.baidu.com/f?kw='+self.name+'&ie=utf-8&pn={}'

    # 获取url列表的方法
    def get_url_list(self):
        # 需要用到模板url和start以及end
        url_list=[]
        for i in range(self.start,self.end+1):
            url_list.append(self.url_parents.format((i-1)*50))
        return url_list

    # 获取数据的方法
    def get_data(self,url_list):
        # 遍历列表发送请求获取响应数据
        page=self.start
        for url in url_list:
            response=requests.get(url,headers=self.headers)
            data=response.content.decode()
            # 调用保存数据的方法
            self.save_data(data,page)
            page+=1

    # 保存数据的方法
    def save_data(self,data,page):
        with open(self.name+'_第{}页.html'.format(page),'w',encoding='utf-8') as f:
            f.write(data)

    def run(self):
        # run方法
        # 获取url列表
        url_list=self.get_url_list()
        # 遍历url_list方法请求
        self.get_data(url_list)

if __name__=='__main__':
    t=Spider('王源',1,3)
    t.run()