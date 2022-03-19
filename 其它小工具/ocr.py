# -*- coding: utf-8 -*-
from urllib import parse
import base64
from PIL import Image
import hashlib
import time
import requests
import os



APPID = "5ffac6f6"
API_KEY = "5b299ba1b4b8381041636071ebec5d74"


def getHeader(language, location):
    curTime = str(int(time.time()))
    param = "{\"language\":\""+language+"\",\"location\":\""+location+"\"}"
    paramBase64 = base64.b64encode(param.encode('utf-8'))

    m2 = hashlib.md5()
    str1 = API_KEY + curTime + str(paramBase64, 'utf-8')
    m2.update(str1.encode('utf-8'))
    checkSum = m2.hexdigest()

    header = {
        'X-CurTime': curTime,
        'X-Param': paramBase64,
        'X-Appid': APPID,
        'X-CheckSum': checkSum,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    }
    return header


def getBody(filepath):
    with open(filepath, 'rb') as f:
        imgfile = f.read()
    data = {'image': str(base64.b64encode(imgfile), 'utf-8')}
    return data
# 语种设置


def get_content(image_name,URL):
    # 是否返回文本位置信息
    language = 'en'
    location = "true"
    # 图片上传接口地址
    pic_f = image_name
    headers = getHeader(language, location)
    r_out = requests.post(URL, headers=headers, data=getBody(pic_f))
    r_re = eval(r_out.content)
    return r_re


def get_text_1(image_name,URL):
    r = get_content(image_name,URL)
    re_line_list = r['data']['block'][0]['line']
    str_list = []
    for re_line in re_line_list:
        re_list = re_line['word']
        for re in re_list:
            str_list.append(re['content'])
    return str_list


def get_text_2(image_name,URL):
    img = Image.open(image_name)
    img = img.convert('L')
    im_name = 'tmi_.png'
    img.save('tmi_.png', 'PNG')
    r = get_content(im_name, URL)
    re_line_list = r['data']["document"]['blocks'][0]['lines']

    str_list = []
    for re_line in re_line_list:
        str_list.append(re_line['text'])
    if os.path.exists(im_name):
        os.remove(im_name)

    return str_list


def get_text(image_name,URL_mode):#mode=1 手写；mode=2 高级语言印刷

    if URL_mode == 1:
        URL = "https://webapi.xfyun.cn/v1/service/v1/ocr/handwriting"
        str = get_text_1(image_name,URL)

    elif URL_mode == 2:
        URL = '	https://webapi.xfyun.cn/v1/service/v1/ocr/recognize_document'
        str = get_text_2(image_name, URL)
    return str
