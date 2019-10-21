import requests
import execjs

# 访问两个网页
# 第一个网页帮助区分单词类型(是中文还是英文)
# 第二个网站帮助翻译
# en英文 zh中文
# 1. 获取翻译类型的网址
while True:
    url = 'https://fanyi.baidu.com/langdetect'
    jsCode = """
        function a(r) {
            if (Array.isArray(r)) {
                for (var o = 0, t = Array(r.length); o < r.length; o++)
                    t[o] = r[o];
                return t
            }
            return Array.from(r)
        }
        function n(r, o) {
            for (var t = 0; t < o.length - 2; t += 3) {
                var a = o.charAt(t + 2);
                a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
                a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
                r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
            }
            return r
        }
        var i = null;
        function e(r) {
            var t = r.length;
            t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))

            var u = void 0, l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);

            u = null !== i ? i : (i = '320305.131321201' || "") || "";
            for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
                var A = r.charCodeAt(v);
                128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
                S[c++] = A >> 18 | 240,
                S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
                S[c++] = A >> 6 & 63 | 128),
                S[c++] = 63 & A | 128)
            }
            for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
                p += S[b],
                p = n(p, F);
            return p = n(p, D),
            p ^= s,
            0 > p && (p = (2147483647 & p) + 2147483648),
            p %= 1e6,
            p.toString() + "." + (p ^ m)
        }
    """
    word = input('请输入要翻译的单词:')
    sign = execjs.compile(jsCode).call("e", word)
    # 1.1伪装请求头
    h = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }
    # 1.2制作需要翻译的数据
    d = {
        'query': word
    }
    # 2. 发送POST请求获取数据
    response = requests.post(url, headers=h, data=d)
    # 需要使用json()方法将返回的数据转换成字典格式
    dict = response.json()
    lan = dict['lan']
    # 3.获取第二个网址
    url = 'https://fanyi.baidu.com/v2transapi'

    # 3.1制作数据
    d['from'] = lan
    d['to'] = 'zh' if lan == 'en' else 'en'  # True是返回值 if 条件 else False时的返回值
    d['transtype'] = 'translang'
    d['simple_means_flag'] = '3'
    d['sign'] = sign
    d['token'] = 'f468541b174ed0358587a074de1d8824'
    # 3.2伪装头部信息
    h['cookie'] = 'BAIDUID=44ABC9CB7C25E33A4951A335694ED0B8:FG=1; BIDUPSID=44ABC9CB7C25E33A4951A335694ED0B8; PSTM=1556239437; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1556614902,1556614925,1556616277,1557305334; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; H_PS_PSSID=1463_21088_29135_29237_28519_29098_28833_29220_26350_29440; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; PSINO=3; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1561516000,1561709933,1562219321,1562309626; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22de%22%2C%22text%22%3A%22%u5FB7%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1562310948; yjs_js_security_passport=9f1dfd194f2955a207757f199ed765ecaaa06a12_1562310949_js'

    # 4.发送POST请求
    response = requests.post(url, headers=h, data=d)
    print('翻译的结果为:', response.json()['trans_result']['data'][0]['dst'])