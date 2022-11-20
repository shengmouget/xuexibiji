# coding: utf-8 
# @Time    : 2022/10/10 下午11:00
# 1.找到未加密的参数
# 2.想把法把参数进行加密（必需参考网易逻辑） params --> encText  encSecKey-->encSeckey
# 3.请求到网易 拿到评论信息
import requests
from Crypto.Cipher import AES
from base64 import b64encode
import json
url = 'https://music.163.com/weapi/comment/resource/comments/get?csrf_token='

# 请求方式post
data = {
    'csrf_token': "",
    'cursor': "-1",
    'offset': "0",
    'orderType': "1",
    'pageNo': "1",
    'pageSize': "20",
    'rid': "R_SO_4_1984488522",
    'threadId': "R_SO_4_1984488522"
}
# 处理加密过程
e = '010001'
f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff' \
    '68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee' \
    '341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c' \
    '3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52' \
    '741d546b8e289dc6935b3ece0462db0a22b8e7'
g = '0CoJUm6Qyw8W8jud'
i = 'GwQezTjpllWHqH5s'
def get_encSecKey():
    return "dacc068d1d82ea4de3129e4913a3727a737aca2d86c7aaf576d8323ca3eb748372e561a540af7dda2eb9a5bb207d932520e2eede54537f9f922491250f6871a8b435b8ed5bdf2d171a770ebffbeb3b69f6f83b110826d85bd23c13331880393174625b26f3907f0a4e7639ef6ac1520461b3b2791057fcc23a53cd0a2e0d5d0c"

def get_params(data):
    frist = enc_params(data,g)
    second = enc_params(frist,i)
    return second  #返回的params

def to_16(data): #把数据拉成16位
    pad = 16 - len(data)%16
    data+=chr(pad)*pad
    return data

def enc_params(data,key): #加密过程
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"),IV=iv.encode("utf-8"),mode=AES.MODE_CBC) #创造加密
    bs = aes.encrypt(data.encode("utf-8")) #加密  加密的长度必需是16的倍速
    return str(b64encode(bs),"utf-8")
"""
    function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)  #循环16次
            e = Math.random() * b.length, #随机数
            e = Math.floor(e),#取整
            c += b.charAt(e); #取字符串
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }
"""

resq = requests.post(url,data={
    "params":get_params(json.dumps(data)),
    "encSecKey":get_encSecKey()
})
dic = resq.json()
dic_content = dic['data']['hotComments']
for content in dic_content:
    print(content['content'])
