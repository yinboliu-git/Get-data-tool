#!/usr/bin/python3
#-*- codeing = utf-8 -*-
#@Time : 1/11/2021 4:11 AM
#@Author : Liu
#@File : bilibibli.py
#@Software : PyCharm

import requests
import re  # 正则表达式
import pprint
import json
import subprocess


session = requests.session()

def __send_request(url_1,headers):
    response = session.get(url=url_1, headers=headers)
    return response


def get_url(html_data):
    """解析视频数据"""

    # 提取视频的标题
    title = re.findall('<span class="tit">(.*?)</span>', html_data)[0]
    # print(title)

    # 提取视频对应的json数据
    json_data = re.findall('<script>window\.__playinfo__=(.*?)</script>', html_data)[0]
    # print(json_data)  # json_data 字符串
    json_data = json.loads(json_data)
    str_json = pprint.pformat(json_data)
    with open('json.txt','w',encoding='utf-8') as fp:
        fp.write(str_json)

    # 提取音频的url地址
    audio_url = json_data['data']['dash']['audio'][0]['backupUrl'][0]

    # 提取视频画面的url地址
    video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]
    title = re.sub(r'[^\u4e00-\u9fa5]','', title)

    video_data = {'title':title,'a_url': audio_url,'v_url': video_url}
    print(video_data)

    return video_data


def save_data(video_data, headers, ):
    # 请求数据
    file_name = video_data['title']
    print('正在请求音频数据')
    audio_data = send_request(video_data['a_url'], headers=headers).content
    print('正在请求视频数据')
    video_data = send_request(video_data['v_url'], headers=headers).content
    with open(file_name + '.mp3', mode='wb') as f:
        f.write(audio_data)
        print('正在保存音频数据')
    with open(file_name + '.mp4', mode='wb') as f:
        f.write(video_data)
        print('正在保存视频数据')



def merge_data(video_data):
    """数据的合并"""
    video_name = video_data['title']
    print('视频合成开始:', video_data['title'])
    # ffmpeg -i video.mp4 -i audio.wav -c:v copy -c:a aac -strict experimental output.mp4
    COMMAND = f'ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -c:v copy -c:a aac -strict experimental output.mp4'
    subprocess.Popen(COMMAND, shell=True)
    print('视频合成结束:', video_data['title'])




def get_bz_video(url):

    headers = {'Referer': url,
               'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'}
    html_data = session.get(url=url, headers=headers).text
    video_data = get_url(html_data)
    save_data(video_data, headers)
    merge_data(video_data)

url= 'https://www.bilibili.com/video/BV17b411q7EV'

get_bz_video(url)