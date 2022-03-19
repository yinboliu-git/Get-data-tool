#!/usr/bin/python3
#-*- codeing = utf-8 -*-
#@Time : 1/11/2021 12:57 AM
#@Author : Liu
#@File : 视频3.py
#@Software : PyCharm

import requests
import re
from lxml import etree
import random
import math
import time
from multiprocessing.dummy import Pool
import os


# 第一步：获取首页的响应请求的html
def get_response_main(url_l):
    params = {}
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}
    response = requests.get(url=url_l, params=params, headers=headers)

    return response


# 第二步：（可选）获取ajax请求的html
def get_response_ajax(start):
    url = 'https://www.pearvideo.com/category_loading.jsp'
    params = {'reqType':'5',
              'categoryId':'130',
              'start':start,
              'mrd':'0.4655147181633341',
              'filterIds':' 1715554,1714415,1714668,1710634,1710806,1710605,1710483,1709803,1709230,1709104,1708751,1708633,1708387,1708303,1708038'}
    headers = {'Referer': 'https://www.pearvideo.com/category_130',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    response = requests.get(url=url, params=params, headers=headers)

    return response


# 第三步：通过html获得id与标题（名字）
def get_cID(response):
    response_text = response.text

    tree = etree.HTML(response_text, etree.HTMLParser(encoding='utf-8'))

    div_list = tree.xpath('//div[@class="vervideo-bd"]')
    video_list = []
    for div in div_list:
        video_id = div.xpath('./a/@href')[0]
        video_name = div.xpath('.//div[@class="vervideo-title"]/text()')
        id = re.findall('video_(.*)', video_id)[0]
        video_dict = {
            'name': video_name,
            'id': id
        }
        video_list.append(video_dict)
    return video_list

    #print(id_list)


# 第四步：获取video的链接
def get_videourl(cID_id):
    rd = format(math.modf(0.8793245822636901+random.random())[0], '.16f')
    url = 'https://www.pearvideo.com/videoStatus.jsp?contId={}&mrd={}'.format(cID_id, rd)
    params = {}

    headers = {'Cookie':'__secdyid=5c651bdd9056d29bca400d1a46360c41b7a2233eb949a86a021610294791; acw_tc=76b20f6916102947910938410e2b8102dd7c3a39ba770e8d36c338722926f5; JSESSIONID=B849A301F8B5A518DD3549C00728CAFD; PEAR_UUID=f657eee0-44a8-4934-bd08-14bb75c3eb71; _uab_collina=161029479009952359488367; UM_distinctid=176ed0c8d022b2-08500ebcc41333-333376b-144000-176ed0c8d037fd; CNZZDATA1260553744=176940513-1610291448-https%253A%252F%252Fwww.baidu.com%252F%7C1610291448; Hm_lvt_9707bc8d5f6bba210e7218b8496f076a=1610294791; p_h5_u=69C6910E-29D2-44D1-B3EE-803C9E34489F; Hm_lpvt_9707bc8d5f6bba210e7218b8496f076a=1610296111; SERVERID=ed8d5ad7d9b044d0dd5993c7c771ef48|1610296279|1610294791',
               'Referer':'https://www.pearvideo.com/video_{}'.format(cID_id),
               'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

    response = requests.get(url=url, params=params, headers=headers)

    res_text = response.json()
    video_url = res_text['videoInfo']['videos']['srcUrl']
    new_url = re.sub(r'\/\d{13}-', f'/cont-{cID_id}-', video_url)

    #print(new_url)
    return new_url


# 在最后一步：下载并保存视频
def downsave_video(url_dict):
    name = url_dict['name'] + '.mp4'
    stext = name+ '开始下载...'
    print(stext)
    video_name = './li_video/' + name
    response_b = requests.get(url=url_dict['url']).content
    if not os.path.exists('./li_video'):
        os.mkdir('./li_video')
    with open(video_name, 'wb') as fp:
        fp.write(response_b)

    etext = name+'下载结束'

    print(etext)



a = input('>>')
if a == '1':
    print('开始...')
    start_time = time.time()
    url = "https://www.pearvideo.com/category_130"
    res = get_response_main(url)
    video_list = get_cID(res)
    url_list = []
    for video in video_list:
        url_get = get_videourl(video['id'])
        v_name = re.sub(r'[^\u4e00-\u9fa5]','', video['name'][0])
        url_dict = {'url': url_get,
                    'name': v_name
                    }
        url_list.append(url_dict)
        time.sleep(random.random()/10)

    list_num = min(url_list.__len__(), 10)
    pool_video = Pool(list_num)
    pool_video.map_async(downsave_video, url_list)

    print('共有{}全部任务正在排队下载中....'.format(list_num))

    pool_video.close()
    pool_video.join()

    print('全部结束...')
    input('>>')


