#!/usr/bin/python3
#-*- codeing = utf-8 -*-
#@Time : 1/8/2021 1:40 AM
#@Author : Liu
#@File : 3_obj.py
#@Software : PyCharm

import requests

if __name__=="__main__":
    print('开始...')
    url = 'https://www.baidu.com/s'
    kw = input('>>')
    params={'wd':kw}
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    response=requests.get(url=url, params=params, headers=headers)

    p_txt = response.text
    txt = './' + kw + '.html'

    with open(txt, 'w', encoding='utf-8') as f:
        f.write(p_txt)

    print('结束...')


