import requests,json
class Spider:
    # 实例化
    def __init__(self):
        # 准备url
        self.url='https://movie.douban.com/j/search_subjects?type=tv&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=200&page_start=0'

    # 获取数据的方法
    def get_data(self):
        # 发送请求
        response=requests.get(url=self.url)
        # 获取数据
        data=response.json()
        print(data)
        # 获取有用数据  字典
        list = data['subjects']
        # 遍历有用数据字典
        for l in list:
            dic = {}
            dic['title'] = l["title"]   # 名字
            dic['rate'] = l["rate"]     # 评分
            dic['cover'] = l['cover']    # 图片地址
            # 每遍历一次调用一次保存数据的方法
            self.save_data(dic)

    # 保存数据的方法
    def save_data(self,data_list):
        # 保存到json文件中，已追加的方式打开
        with open('me_douban.json','a',encoding='utf-8') as f:
            # json-->文件
            json.dump(data_list,f,ensure_ascii=False)
            # ，+换行
            f.write(',\n')

    # run方法
    def run(self):
        # 调用获取数据的方法
        list=self.get_data()
        # 调用保存数据的方法
        self.save_data(list)

if __name__=="__main__":
    douban=Spider()
    douban.run()