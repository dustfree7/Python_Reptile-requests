#! C:\Users\neo\Desktop\pyfiles\venv python
# -*- coding:utf-8 -*-
#需求：爬取sogou.com首页
import requests
if __name__ == "__main__":
    #指定url
    url = 'https://www.sogou.com/'
    #发起请求        #get方法会返回一个响应对象
    response = requests.get(url=url)
    #获取响应数据     #.text返回字符串形式的响应数据
    page_text = response.text
    print(page_text)
    #持久化存储
    with open(r'C:\Users\neo\Desktop\pyfiles\sogou.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    print('爬取数据结束！')