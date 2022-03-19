#!/usr/bin/python3
#-*- codeing = utf-8 -*-
#@Time : 1/10/2021 3:11 AM
#@Author : Liu
#@File : 4k.py
#@Software : PyCharm

#批量加引号：:(.*?):(.*?)'$1':'$2'

import requests
import os
from lxml import etree

def get_html():
    url = 'http://pic.netbian.com/4kmeinv/'
    params={}
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    response_txt = requests.get(url=url,params=params,headers=header).text
    return response_txt

def get_image(url):
    params={}
    header={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    response_txt = requests.get(url=url,params=params,headers=header).text

    img_tr = etree.HTML(response_txt, etree.HTMLParser(encoding='utf-8'))
    img = img_tr.xpath('//div[@class="photo-pic"]/a/img/@src')[0]
    img_url = 'http://pic.netbian.com' + img
    b_data = requests.get(url=img_url, params=params, headers=header).content
    return b_data,img_url


if __name__ == '__main__':

    if not os.path.exists('./4k高清'):
        os.mkdir('./4k高清')
    re_txt = get_html()
    tr = etree.HTML(re_txt, etree.HTMLParser(encoding='utf-8'))

    li_list = tr.xpath('//div[@class="wrap clearfix"]//ul[@class="clearfix"]/li')

    for li in li_list:
        image_href = li.xpath('./a/@href')[0]
        image_name = li.xpath('./a/img/@alt')[0] + '.jpg'
        image_name = image_name.encode('iso-8859-1').decode('gbk')

        image_url = 'http://pic.netbian.com' + image_href

        image_b_u = get_image(image_url)
        image_b = image_b_u[0]

        image_path = './4k高清/' + image_name
        with open(image_path,'wb') as fp:
            fp.write(image_b)
        print(image_name,'下载完成..:',image_b_u[1])
    print('结束...')





