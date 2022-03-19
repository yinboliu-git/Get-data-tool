#!/usr/bin/python3
#-*- codeing = utf-8 -*-
#@Time : 1/8/2021 2:48 PM
#@Author : Liu
#@File : 肯德基.py
#@Software : PyCharm

import requests
import json

if __name__ == '__main__':
    print('开始...')

    kw = input('>>')
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?'
    param = {'op':'keyword',
             'cname': '',
             'pid':'',
             'keyword': '北京',
             'pageIndex': '1',
             'pageSize': '10'
             }

    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    response = requests.post(url=url, data=param, headers=header)

    p_txt = response.text
    txt_name = './' + kw + '.json'
    with open(txt_name,'w',encoding='utf-8') as f:
        json.dump(p_txt,fp=f,ensure_ascii=False)

    print('结束...')