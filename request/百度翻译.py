#!/usr/bin/python3
#-*- codeing = utf-8 -*-
#@Time : 1/8/2021 2:01 AM
#@Author : Liu
#@File : 百度翻译.py
#@Software : PyCharm

import requests
import json
if __name__ == '__main__':
    print('开始...')
    url = 'https://fanyi.baidu.com/sug'

    kw = input('>>')
    data = {'kw':kw}
    header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36' }
    response = requests.post(url=url, data=data, headers=header)

    p_txt = response.json()
    txt = './' + kw + '.json'
    with open(txt,'w',encoding='utf-8') as f:
        json.dump(p_txt, fp = f, ensure_ascii = False)

    print('结束...')


