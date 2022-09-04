#! C:\Users\neo\Desktop\pyfiles\venv python
# -*- coding:utf-8 -*-
import requests
import json
if __name__ == "__main__":
    #指定url
    post_url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    #UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }
    #post请求参数处理
    word = input('Enter a China city name:')
    data = {
        'cname':'',
        'pid':'',
        'keyword': word,
        'pageIndex':'1',
        'pageSize': '10',
    }
    #请求发送
    response = requests.post(url=post_url,data=data,headers=headers)
    #获取响应数据
    page_text = response.text
    #持久化存储
    fileName = word+'肯德基位置查询.txt'
    fp = open(fileName,'w',encoding='utf-8')
    json.dump(page_text,fp=fp,ensure_ascii=False)
    print('成功结束！')

