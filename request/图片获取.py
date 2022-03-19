#!/usr/bin/python3
#-*- codeing = utf-8 -*-
#@Time : 1/9/2021 6:02 PM
#@Author : Liu
#@File : 图片获取.py
#@Software : PyCharm

import re
import requests
import os
import bs4


def get_net_page(page):
    url = 'https://www.qiushibaike.com/imgrank/page/'+str(page)+'/'
    param={}
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    image_msg = requests.get(url=url,params=param, headers= header).text

    return image_msg


def get_image(image_msg,rs):
    if not os.path.exists('./image'):
        os.mkdir('./image')

    image_list = re.findall(rs,image_msg,re.S)

    for image in image_list:
        image_url = 'https:' + image
        url = image_url
        param = {}
        header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
        image_b_file = requests.get(url=url, params=param, headers=header).content

        image_name = image.split('/')[-1]
        image_save_name = './image/' + image_name

        with open(image_save_name,'wb') as f:
            f.write(image_b_file)
        print(image_name,'保存完成...')


if __name__ == '__main__':

    n = int(input('>>'))
    rs = r'<div class="thumb">.*?img src="(.*?)" alt.*?</div>'

    for i in range(1,n+1):
        image_msg = get_net_page(i)
        get_image(image_msg,rs)




    print('结束...')








   # https: // pic.qiushibaike.com / system / pictures / 12396 / 123962991 / medium / 9NTIQSHLXIUL5U02.jpg




