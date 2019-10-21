# 1.导包
import requests

# 2.准备图片的url
url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1571293615785&di=a5499e622213590db67c33c57dcdb223&imgtype=0&src=http%3A%2F%2Fb-ssl.duitang.com%2Fuploads%2Fitem%2F201703%2F09%2F20170309134320_Lnxt8.png'

# 3.发送请求
response=requests.get(url)

# 4.获取数据进行保存
b=response.content

# 5.将二进制写入文件
with open('二叔.jpg','wb') as f:
    f.write(b)

