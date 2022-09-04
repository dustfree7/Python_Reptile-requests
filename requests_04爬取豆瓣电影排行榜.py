#! C:\Users\neo\Desktop\pyfiles\venv python
# -*- coding:utf-8 -*-
import requests
import json
if __name__ == "__main__":
    #指定url
    url = 'https://movie.douban.com/j/chart/top_list?'
    param = {
        'type': '11',
        'interval_id': '100:90',
        'action':'',
        'start': '0',    #从库中的第几部电影开始爬取
        'limit': '30',   #单次爬取的个数
    }
    headers = {
       'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'
   }
    response = requests.get(url=url,params=param,headers=headers)
    #获取响应数据  json()方法返回的是obj(需确认响应数据为json格式)
    list_data = response.json()
    #持久化存储
    fp = open('豆瓣剧情排行榜.json','w',encoding='utf-8')
    json.dump(list_data,fp=fp,ensure_ascii=False)

    print('成功结束！')




