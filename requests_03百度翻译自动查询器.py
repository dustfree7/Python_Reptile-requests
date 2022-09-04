#! C:\Users\neo\Desktop\pyfiles\venv python
# -*- coding:utf-8 -*-
import requests
import json
if __name__ == "__main__":
    #指定url
    post_url = 'https://fanyi.baidu.com/sug'
    #UA伪装
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }
    #post请求参数处理
    word = input('Enter a word:')
    data = {
        'kw': word,
    }
    #发送post请求
    response = requests.post(url=post_url,data=data,headers=headers)
    #获取响应数据并处理    json()方法返回的是obj(需确认响应数据为json格式)
    dict_obj = response.json()
    #持久化存储
    fileName = word+'.json'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(dict_obj,fp=fp,ensure_ascii=False)

    print('成功结束！')
