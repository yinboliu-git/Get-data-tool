#!/usr/bin/python3
#-*- codeing = utf-8 -*-
#@Time : 1/10/2021 2:09 AM
#@Author : Liu
#@File : 二手房.py
#@Software : PyCharm

import requests
from lxml import etree

def get_html():
    url = 'https://bj.58.com/chaoyang/ershoufang/?PGTID=0d30000c-0000-1866-f3d9-82af01f8e3bb&ClickID=1'
    params={}
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    response_txt = requests.get(url=url,params=params,headers=header).text
    return response_txt


if __name__ == '__main__':
    html_text = get_html()
    #print(html_text)

    xp = '//body//div[@class="main-wrap"]//ul[@class="house-list-wrap"]/li'
    tr = etree.HTML(html_text, etree.HTMLParser(encoding='utf-8'))

    li_list = tr.xpath(xp)
    fp = open('./fan.txt','w', encoding='utf-8')
    print(li_list)

    for li in li_list:
        li_title = li.xpath('.//h2[@class="title"]/a/text()')[0]
        li_price = li.xpath('.//div[@class="price"]/p[@class="unit"]/text()')[0]
        li_msg = li_title + ':' + li_price + '\n'
        fp.write(li_msg)


    fp.close()
    print('结束...')




