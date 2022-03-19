#!/usr/bin/python3
# -*- codeing = utf-8 -*-
# @Time : 1/8/2021 3:36 PM
# @Author : Liu
# @File : 药监局.py
# @Software : PyCharm


import requests
import json

if __name__ == '__main__':
    print('开始...')
    kw = input('>>')

    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'

    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    ID_list = []
    for page in range(1,10):
        params = {'on': 'true',
                  'page': '1',
                  'pageSize': '15',
                  'productName': '',
                  'conditionType': '1',
                  'applyname': '',
                  'applysn': ''
                  }
        p_txt = requests.post(url=url, data=params, headers=header).json()
        for p_dict in p_txt['list']:
            ID_list.append(p_dict['ID'])

    p_list = []
    url2 = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id_s in ID_list:
        data = {'id': id_s}
        p_2_txt = requests.post(url=url2, data=data, headers=header).json()
        p_list.append(p_2_txt)

    txt = './' + kw + '药监局.json'
    with open(txt, 'w', encoding='utf-8') as f:
        json.dump(p_list, fp=f, ensure_ascii=False)

    print('结束...')








