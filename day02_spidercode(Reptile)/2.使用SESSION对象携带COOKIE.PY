# session对象就看成requests,带着cookie的requests
# session会自动携带cookie，先进行登陆的操作
# 准备登陆使用的url
import requests
# 生成session对象
session=requests.session()
# 准备登陆的url
url=''
session.headers={
    'user-agent':''
}
# 准备表单那数据
d={
    'email':'',
    'password':''
}
# 先发送登陆的请求
response=session.post(url,data=d)

# 向详情页发送请求
response=session.get('')

print(response.content.decode())












