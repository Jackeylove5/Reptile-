import requests

url='http://tieba.baidu.com/f?kw=%E4%B8%AD%E5%9B%BD&red_tag=i1241770478'
print(url)
# 解码
x_url=requests.utils.unquote(url)
print(x_url)      # http://tieba.baidu.com/f?kw=中国&red_tag=i1241770478

g_x_url='http://tieba.baidu.com/f?kw=中国&red_tag=i1241770478'
print(g_x_url)
# 编码
x_url=requests.utils.quote(g_x_url)
print(x_url) # http%3A//tieba.baidu.com/f%3Fkw%3D%E4%B8%AD%E5%9B%BD%26red_tag%3Di1241770478