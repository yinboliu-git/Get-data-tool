#!/usr/bin/python3
#-*- codeing = utf-8 -*-
#@Time : 1/8/2021 2:21 PM
#@Author : Liu
#@File : 豆瓣电影.py
#@Software : PyCharm

import requests
import json

if __name__ == '__main__':
    print('开始...')
    kw = input('>>')

    url = 'https://movie.douban.com/j/chart/top_list'
    params={'type': '24',
            'interval_id' : '100:90',
            'action':'',
            'start': kw,
            'limit': '20',
            }
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    response = requests.get(url=url,params=params,headers=header)

    p_txt = response.text
    txt = './'+kw+'豆瓣.json'
    with open(txt, 'w', encoding= 'utf-8') as f:
        json.dump(p_txt,fp=f,ensure_ascii=False)

    print('结束...')

