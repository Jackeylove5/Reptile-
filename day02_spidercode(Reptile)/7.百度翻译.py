import requests,execjs
while True:
    # 1.获取语种
    # 此url是用来获取翻译单词的语种
    url_lang = 'https://fanyi.baidu.com/langdetect'
    h = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    }
    word = input('请输入要翻译的词：')
    d = {
        "query": word
    }
    response1 = requests.post(url_lang, data=d, headers=h)
    data1 = response1.json()
    print(data1)
    lan = data1['lan']
    print(lan)

    # 生成sign
    with open('baidu.js', 'r') as f:
        js = f.read()
    sign = execjs.compile(js).call('e', word)
    print(sign)

    # 2.获取翻译
    # 只能被翻译的url
    url_trans = 'https://fanyi.baidu.com/v2transapi'
    d = {
        'from': 'zh',  # 从什么语种   上一次请求
        'to': 'en' if lan == 'zh' else 'zh',  # 翻译为的语种  用户输入
        'query': word,  # 要翻译的单词
        'transtype': 'translang',  # 固定数据
        'simple_means_flag': 3,  # 固定数据
        'sign': sign,
        'token': '063dc969a0fb07a6841dc6e4cbb0355d'  # 固定数据
    }
    response = requests.post(url_trans, data=d)
    print(response.json()['trans_result']['data'][0]['dst'])  # content-type: application/json



















