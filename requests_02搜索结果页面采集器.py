#! C:\Users\neo\Desktop\pyfiles\venv python
# -*- coding:utf-8 -*-
import requests
if __name__ == "__main__":
    #UA伪装：将对应的User-Agent封装到一个字典中。
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    #处理url携带的参数：封装到字典中
    kw = input('Enter a word:')
    param = {
        'query':kw
    }
    #对指定的url发起的请求携带了一些参数。
    response = requests.get(url=url,params=param,headers=headers)

    page_text = response.text
    fileName = kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功！')